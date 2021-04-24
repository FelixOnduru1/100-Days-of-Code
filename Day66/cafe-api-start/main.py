from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
from random import choice

app = Flask(__name__)

##Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


##Cafe TABLE Configuration
class Cafe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    map_url = db.Column(db.String(500), nullable=False)
    img_url = db.Column(db.String(500), nullable=False)
    location = db.Column(db.String(250), nullable=False)
    seats = db.Column(db.String(250), nullable=False)
    has_toilet = db.Column(db.Boolean, nullable=False)
    has_wifi = db.Column(db.Boolean, nullable=False)
    has_sockets = db.Column(db.Boolean, nullable=False)
    can_take_calls = db.Column(db.Boolean, nullable=False)
    coffee_price = db.Column(db.String(250), nullable=True)

    def to_dict(self):
        # Method 1.
        dictionary = {}
        # Loop through each column in the data record
        for column in self.__table__.columns:
            # Create a new dictionary entry;
            # where the key is the name of the column
            # and the value is the value of the column
            dictionary[column.name] = getattr(self, column.name)
        return dictionary

        # Method 2. Altenatively use Dictionary Comprehension to do the same thing.
        # return {column.name: getattr(self, column.name) for column in self.__table__.columns}


@app.route("/")
def home():
    return render_template("index.html")


@app.route('/random')
def get_random_cafe():
    all_cafes = db.session.query(Cafe).all()
    random_cafe = choice(all_cafes)
    # Method 1
    # return jsonify(cafe={
    #     # Omit the id from the response
    #     # "id": random_cafe.id,
    #     "name": random_cafe.name,
    #     "map_url": random_cafe.map_url,
    #     "img_url": random_cafe.img_url,
    #     "location": random_cafe.location,
    #     #Put some properties in a sub-category
    #     "amenities": {
    #       "seats": random_cafe.seats,
    #       "has_toilet": random_cafe.has_toilet,
    #       "has_wifi": random_cafe.has_wifi,
    #       "has_sockets": random_cafe.has_sockets,
    #       "can_take_calls": random_cafe.can_take_calls,
    #       "coffee_price": random_cafe.coffee_price,
    #     }
    # })
    return jsonify(cafe=random_cafe.to_dict())


@app.route('/all')
def get_all_cafes():

    all_cafes = db.session.query(Cafe).all()
    cafes_list = [cafe.to_dict() for cafe in all_cafes]

    return jsonify(cafes=cafes_list)


@app.route('/search')
def get_cafe_at_location():
    query_location = request.args.get('loc')
    searched_cafes = Cafe.query.filter_by(location=query_location).all()
    searched_cafes_list = [searched_cafe.to_dict() for searched_cafe in searched_cafes]
    if len(searched_cafes_list) != 0:

        return jsonify(cafes=searched_cafes_list)
    else:
        return jsonify(error={"Not Found": "Sorry we don't have a cafe in that location"})


@app.route('/add', methods=['POST'])
def add():
    api_key = request.args.get("api-key")
    if api_key == "TopSecretApiKey":
        new_cafe = Cafe(
            name=request.form.get('name'),
            map_url=request.form.get("map_url"),
            img_url=request.form.get("img_url"),
            location=request.form.get("location"),
            seats=request.form.get("seats"),
            has_toilet=bool(int(request.form.get("has_toilet"))),
            has_wifi=bool(int(request.form.get("has_wifi"))),
            has_sockets=bool(int(request.form.get("has_wifi"))),
            can_take_calls=bool(int(request.form.get("can_take_calls"))),
            coffee_price=request.form.get("coffee_price"),
            )
        db.session.add(new_cafe)
        db.session.commit()

        return jsonify(response={"success": "Successfully added a new cafe."}), 200
    else:
        return jsonify(error={"Forbidden": "You do not have the right credentials to perform this request."
                                           " Make sure you have the right api-key."}), 403


@app.route('/update-price/<int:cafe_id>', methods=['PATCH'])
def update_price(cafe_id):
    cafe_to_update = Cafe.query.get(cafe_id)
    if cafe_to_update:
        cafe_to_update.coffee_price = int(request.args.get('new_price'))

        db.session.commit()

        return jsonify(response={"Success": "Successfully updated the coffee price."}), 202
    else:
        return jsonify(error={"Not Found": "No hotel was found with that id."}), 404


@app.route('/report-closed/<int:cafe_id>', methods=['DELETE'])
def report_closed(cafe_id):
    cafe_to_delete = Cafe.query.get(cafe_id)
    api_key = request.args.get("api-key")

    if api_key == "TopSecretApiKey":
        if cafe_to_delete:
            db.session.delete(cafe_to_delete)
            db.session.commit()

            return jsonify(response={"Success": "The cafe was deleted successfully from the database."}), 200
        else:
            return jsonify(error={"Not Found": "No cafe was found with that id."}), 404
    else:
        return jsonify(error={"Forbidden": "You do not have the right credentials to perform this request."
                                           " Make sure you have the right api-key."}), 403


if __name__ == '__main__':
    app.run(debug=True)
