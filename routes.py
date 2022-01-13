from flask import current_app,jsonify,request
from app import create_app,db
from models import City,cities_schema

# Create an application instance
app = create_app()

# Define a route to fetch the avaialable articles

@app.route("/cities", methods=["GET"], strict_slashes=False)
def articles():

	cities = City.query.all()
	results = cities_schema.dump(cities)

	return jsonify(results)


if __name__ == "__main__":
	app.run(debug=True)