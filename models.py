from app import db,ma

class City(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(35),nullable=False)
    countryCode = db.Column(db.String(3), nullable=False)
    district = db.Column(db.String(3), nullable=False)
    population = db.Column(db.Integer, nullable=False)


    def __repr__(self):
        return "<City %r>" % self.title

# Generate marshmallow Schemas from your models
class CitySchema(ma.Schema):
    class Meta:
        # Fields to expose
        fields = ("id","name", "countryCode", "district", "population")


city_schema = CitySchema()
cities_schema = CitySchema(many=True)