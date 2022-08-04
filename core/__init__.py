from flask import Flask
from config import DevelopmentConfig
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired
# from flask_mail import Mail, Message

app = Flask(__name__)

# app.config['MYSQL_HOST'] = 'localhost'
# app.config['MYSQL_USER'] = 'root'
# app.config['MYSQL_PASSWORD'] = ''
# app.config['MYSQL_DB'] = 'lcf_database'
#
# mysql = MySQL(app)

# Creating a connection cursor
# cursor = mysql.connection.cursor()
#
# # Executing SQL Statements
# cursor.execute(''' CREATE TABLE table_name(field1, field2...) ''')
# cursor.execute(''' INSERT INTO table_name VALUES(v1,v2...) ''')
# cursor.execute(''' DELETE FROM table_name WHERE condition ''')
#
# # Saving the Actions performed on the DB
# mysql.connection.commit()
#
# # Closing the cursor
# cursor.close()


# def insert_data():


# mail = Mail(app)
app.config.from_object(DevelopmentConfig)
# app.config['MAIL_SERVER'] = 'localhost'
# app.config['MAIL_PORT'] = '25'
# app.config['MAIL_USE_SSL'] = True
# app.config['MAIL_USERNAME'] = "litewo4052@tonaeto.com"
# app.config['SECRET_KEY'] = 'N*ZuFKc+RCD,WcFlNr-Q#s^Jf`%8D-'


# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.sqlite3'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# db = SQLAlchemy(app)

# def send_contact_form(result):
#     msg = Message("Hello",
#                   sender="from@example.com",
#                   recipients=["litewo4052@tonaeto.com"])
#
#     msg.body = """
#     Name: {}
#     Email: {}
#     Message: {}
#     """.format(result["name"], result["email"], result["message"])
#
#     mail.send(msg)

# class MetDataTable(db.Model):
#      id = db.Column(db.Integer, primary_key = True)
#      month = db.Column(db.String(100), primary_key = False)
#      total_precipation= db.Column(db.Integer, primary_key = False)
#      mean_air_temp= db.Column(db.Integer, primary_key = False)
#      mean_rel_humidity= db.Column(db.Integer, primary_key = False)
#      mean_pan_evaporation= db.Column(db.Integer, primary_key = False)
#      mean_daytime_cloud= db.Column(db.Integer, primary_key = False)
#      total_sunshining= db.Column(db.Integer, primary_key = False)
#      year= db.Column(db.Integer, primary_key = False)


class ContactForm(FlaskForm):
    name = StringField('Please Enter Your Full Name', validators=[DataRequired()])
    email = StringField('Please Enter Your Email', validators=[DataRequired()])
    message = TextAreaField('Enter Your Message', validators=[DataRequired()])
    submit = SubmitField('Submit')


from core import routes
