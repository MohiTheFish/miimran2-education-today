from app import db,ma

# Models
class Authors(db.Model):
    authorId = db.Column(db.Integer, primary_key=True)
    authorRank = db.Column(db.Integer)
    normalizedName = db.Column(db.String(256))
    displayName = db.Column(db.String(256))
    lastKnownAffiliationId = db.Column(db.Integer)
    createdDate = db.Column(db.DateTime)

class Papers(db.Model):
    paperId = db.Column(db.Integer, primary_key=True)
    docType = db.Column(db.String)
    originalTitle = db.Column(db.String(1024))
    paperYear = db.Column(db.Integer)
    paperDate = db.Column(db.DateTime)
    publisher = db.Column(db.String(1024))
    originalVenue = db.Column(db.String(1024))

class PaperAuthorAffiliations(db.Model):
    paperId = db.Column(db.Integer)
    authorId = db.Column(db.Integer)
    affiliationId = db.Column(db.Integer)

    id = db.Column(db.Integer, primary_key=True)
    # __tablename__ = 'paperauthoraffiliations'

class PaperReferences(db.Model):
    paperId = db.Column(db.Integer, primary_key=True)
    paperReferenceId = db.Column(db.Integer, primary_key=True)
    __tablename__ = 'paperreferences'


# Serialization Schemas

class AuthorsSchema(ma.Schema):
    class Meta:
        fields = ("authorId", "authorRank", "normalizedName", "displayName", "lastKnownAffiliationId", "createdDate")
authors_schema = AuthorsSchema(many=True)

class PapersSchema(ma.Schema):
    class Meta:
        fields = ("paperId", "docType", "originalTitle", "paperYear", "paperDate", "publisher", "originalVenue")
papers_schema = PapersSchema(many=True)

class PaperAuthorAffiliationsSchema(ma.Schema):
    class Meta:
        fields = ("paperId", "authorId", "affiliationId")
paperAuthorAffiliations_schema = PaperAuthorAffiliationsSchema(many=True)

class PaperReferencesSchema(ma.Schema):
    class Meta:
        fields = ("paperId", "paperReferenceId")
paperReferences_schema = PaperReferencesSchema(many=True)