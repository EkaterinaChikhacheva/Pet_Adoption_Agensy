from flask import Flask, request, render_template,  redirect, flash, session
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, Pet
from forms import AddPetForm


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///adopt'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = "oh_so_secret"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
debug = DebugToolbarExtension(app)


connect_db(app)

@app.route('/')
def home_pg():
    """Home page"""
    pets = Pet.query.all()
    return render_template('home_pg.html', pets=pets)

@app.route('/add', methods = ["GET", "POST"])
def add_form():
    """Form for adding a pet, handeling POST request from that form"""

    form = AddPetForm()

    if form.validate_on_submit():
        name = form.pet_name.data
        species = form.species.data
        photo_url = form.photo_url.data
        age = form.age.data
        notes = form.notes.data

        new_pet = Pet(
            name = name, 
            species = species, 
            photo_url = photo_url, 
            age = age,
            notes = notes)
        db.session.add(new_pet)
        db.session.commit()

        flash(f"{name} {species} was added to the shelter!")
        return redirect("/")

    else:
        return render_template(
            "add_pet.html", form=form)


@app.route('/<int:pet_id>', methods = ["GET", "POST"])
def display_edit_pet(pet_id):
    pet = Pet.query.get(pet_id)
    return render_template('pet_details_edit.html', pet = pet)