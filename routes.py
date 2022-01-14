from sqlalchemy import or_, select, func
from sqlalchemy.sql import text
from flask import current_app,jsonify,request,send_from_directory
from app import create_app,db
from models import Authors,authors_schema, PaperAuthorAffiliations, paperAuthorAffiliations_schema, PaperReferences, paperReferences_schema

# Create an application instance
app = create_app()

# Define a route to fetch the avaialable articles

@app.route("/author/<name>/citations", methods=["GET"], strict_slashes=False)
def citations(name):

	author = Authors.query.filter(or_(Authors.authorId == name, Authors.displayName == name))
	results = authors_schema.dump(author)
	if len(results) == 0:
		return {"data": [], "error": "No author found"}, 404
	if len(results) > 1:
		return jsonify({"data": results, "error": "Many authors found."}), 400
	
	authorId = results[0]['authorId']
	authorName = results[0]['displayName']
	sqlQuery = text("""
	SELECT paperreferences.PaperReferenceId, count(paperreferences.PaperReferenceId) as count_PaperReferenceId
	FROM paperreferences JOIN paperauthoraffiliations on paperreferences.paperId = paperauthoraffiliations.paperId
	WHERE paperauthoraffiliations.AuthorId = :authorId
	GROUP BY paperreferences.PaperReferenceId
	ORDER BY count(paperreferences.PaperReferenceId);
	""")
	with db.engine.connect() as conn:
		res = conn.execute(sqlQuery, {"authorId":authorId})
		results = res.fetchall()
		results = [{"paperId":x[0], "count": x[1]} for x in results]
	
	return jsonify({
		"data": {
			"name": authorName,
			"id": authorId,
			"mostReferenced": results
		}
	}), 200

@app.route("/author", methods=["GET"], strict_slashes=False)
def authors():
	authors_query = Authors.query.with_entities(Authors.displayName, Authors.authorId)
	results = authors_schema.dump(authors_query)

	return jsonify({"data": results }), 200

if __name__ == "__main__":
	app.run(debug=True)