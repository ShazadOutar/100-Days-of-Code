# Published Documentation is here: https://documenter.getpostman.com/view/26683183/2sAXxTaVYP

import random

from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Boolean, Select

app = Flask(__name__)


# CREATE DB
class Base(DeclarativeBase):
    pass


# Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)


# Cafe TABLE Configuration
class Cafe(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    map_url: Mapped[str] = mapped_column(String(500), nullable=False)
    img_url: Mapped[str] = mapped_column(String(500), nullable=False)
    location: Mapped[str] = mapped_column(String(250), nullable=False)
    seats: Mapped[str] = mapped_column(String(250), nullable=False)
    has_toilet: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_wifi: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_sockets: Mapped[bool] = mapped_column(Boolean, nullable=False)
    can_take_calls: Mapped[bool] = mapped_column(Boolean, nullable=False)
    coffee_price: Mapped[str] = mapped_column(String(250), nullable=True)

    def to_dict(self):
        dictionary = {}
        for column in self.__table__.columns:
            dictionary[column.name] = getattr(self, column.name)
        return dictionary


with app.app_context():
    db.create_all()


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/random")
def get_random_cafe():
    result = db.session.execute(db.select(Cafe))
    all_cafes = result.scalars().all()
    random_cafe = random.choice(all_cafes)
    # return f"{random_cafe.name}"
    return jsonify(cafe={
        "can_take_calls": random_cafe.can_take_calls,
        "coffee_price": random_cafe.coffee_price,
        "has_sockets": random_cafe.has_sockets,
        "has_toilet": random_cafe.has_toilet,
        "has_wifi": random_cafe.has_wifi,
        "id": random_cafe.id,
        "img_url": random_cafe.img_url,
        "location": random_cafe.location,
        "map_url": random_cafe.map_url,
        "name": random_cafe.name,
        "seats": random_cafe.seats
    })

@app.route("/all")
def get_all_cafes():
    result = db.session.execute(db.select(Cafe).order_by(Cafe.name))
    all_cafes = result.scalars().all()
    all_cafes_list = []
    for cafe in all_cafes:
        all_cafes_list.append(cafe.to_dict())
    # print(jsonify(cafe=all_cafes_list))
    return jsonify(cafes=all_cafes_list)

# HTTP GET - Read Record
@app.route("/search")
def search_area():
    query_location = request.args.get('Location')
    search_results = []
    with app.app_context():
        cafes = db.session.execute(db.select(Cafe).where(Cafe.location == query_location)).scalars().all()
        for cafe in cafes:
            search_results.append(cafe.to_dict())
    if search_results:
        return jsonify(cafes=search_results)
    else:
        return jsonify(error={
            "Not Found": "Sorry, no cafes found for that location"
        }), 404

# HTTP POST - Create Record
@app.route("/add", methods=["POST"])
def add_cafe():
    new_cafe = Cafe(
        name=request.form.get("name"),
        map_url=request.form.get("map_url"),
        img_url=request.form.get("img_url"),
        location=request.form.get("location"),
        has_sockets=bool(request.form.get("sockets")),
        has_toilet=bool(request.form.get("toilet")),
        has_wifi=bool(request.form.get("wifi")),
        can_take_calls=bool(request.form.get("calls")),
        seats=request.form.get("seats"),
        coffee_price=request.form.get("coffee_price"),
    )
    db.session.add(new_cafe)
    db.session.commit()
    return jsonify(response={"success": "Successfully added the new cafe."})


# HTTP PUT/PATCH - Update Record
@app.route("/update-price/<int:cafe_id>", methods=["PATCH"])
def update_price(cafe_id):
    new_price = request.args.get("new_price")
    cafe_to_update = db.session.get(Cafe, cafe_id)
    if cafe_to_update:
        cafe_to_update.coffee_price = new_price
        db.session.commit()
        # db.session.query(Cafe).where(id=cafe_id).update(coffee_price=new_price)
        return jsonify(response={"success": "Successfully updated the cafe price."})
    else:
        return jsonify(error={
            "Not Found": "Sorry, no cafes found for that location"
        }), 404


# HTTP DELETE - Delete Record
@app.route("/report-closed/<int:cafe_id>", methods=["DELETE"])
def delete_cafe(cafe_id):
    entered_key = request.args.get("api-key")
    if entered_key == "TopSecretAPIKey":
        cafe_to_be_deleted = db.session.get(Cafe, cafe_id)
        if cafe_to_be_deleted:
            db.session.delete(cafe_to_be_deleted)
            db.session.commit()
            return jsonify(response={
                "Success": "Cafe was deleted"
            }), 200
        else:
            return jsonify(error={
            "Not Found": "Sorry, no cafes found for that id"
        }), 404
    else:
        return jsonify(error={
            "Forbidden": "Sorry, wrong API key"
        }), 403

if __name__ == '__main__':
    app.run(debug=True)
