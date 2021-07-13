from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, BooleanField, IntegerField, RadioField, SelectField, TextAreaField
from wtforms.validators import InputRequired, Email, Optional, URL, AnyOf

class AddPetForm(FlaskForm):

    pet_name = StringField("Pet Name", validators = [InputRequired(message = "Enter the pet's name")])
    species = SelectField("Species", 
        validators = [InputRequired(message = "What creature is it?")],
        choices = [('dog', 'Dog'), ('bunny','Bunny'), ('cat', 'Cat')])
    photo_url = StringField("Photo URL", validators = [Optional(), URL(message = "Hmm... It doesn't seem like a valid URL. You mind checking it and trying again?")])
    age = SelectField("Age", 
        validators = [Optional()],
        choices = [(num, num) for num in range(31)])
    notes = TextAreaField("Notes", validators = [InputRequired(message = "Hey! Tell us somethong about this pet!")])
