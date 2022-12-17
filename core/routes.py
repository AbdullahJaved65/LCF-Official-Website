import warnings

import pandas as pd
import plotly.io as pio
from flask import render_template, \
    send_file, request, redirect
from flask_mysqldb import MySQL

from core import ContactForm, app

# from keras.models import load_model

warnings.filterwarnings('ignore')
# from plotly import Figure
pio.renderers.default = 'browser'

# loading  data
# data = pd.read_csv('C:/LCF Official Website/core/ml_notebooks/pred.csv',
#                    parse_dates=['Date'], index_col='Date')

# model1 = load_model('C:/LCF Official Website/core/ml_notebooks/model2.h5')

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'lcf_database'

mysql = MySQL(app)


@app.route('/', methods=("POST", "GET"))
def home():
    form = ContactForm()
    # result = {}
    # result['name'] = request.form["name"]
    # result['email'] = request.form["email"]
    # result['message'] = request.form["message"]
    # # res = pd.DataFrame({'name': name, 'email': email, 'message': message}, index=[0])
    # # res.to_csv('./contactusMessage.csv')
    # send_contact_form(result)
    # return redirect("/")
    if request.method == 'POST':
        name = request.form["name"]
        email = request.form["email"]
        message = request.form["message"]
        res = pd.DataFrame({'name': name, 'email': email,
                            'message': message}, index=[0])
        res.to_csv('./contactusMessage.csv')
        return redirect("/")
    else:
        return render_template("index.html", form=form, dict=dict)


@app.route('/about.html')
def about():
    return render_template('about.html')


@app.route('/contact.html', methods=["GET", "POST"])
def contact():
    form = ContactForm()
    if request.method == 'POST':
        name = request.form["name"]
        email = request.form["email"]
        message = request.form["message"]
        res = pd.DataFrame({'name': name, 'email': email,
                            'message': message}, index=[0])
        res.to_csv('./contactusMessage.csv')

        return redirect("contact.html")
    else:
        return render_template('contact.html', form=form)


@app.route('/event.html')
def event():
    return render_template('event.html')


@app.route('/gallery.html')
def gallery():
    return render_template('gallery.html')


@app.route('/team.html')
def team():
    return render_template('team.html')


@app.route('/download.html')
def upload_form():
    return render_template('download.html')


@app.route('/download')
def download_file():
    """html2pdf.pdf"""
    # path = "info.xlsx"
    # path = "simple.docx"
    # path = "sample.txt"
    return send_file("C:/LCF Official Website/templates/download.html", as_attachment=True)


@app.route('/db_page.html')
def db_page():
    return render_template('db_page.html')


@app.route('/database_search_page/<name>', methods=['GET'])
def search_page(name):
    cur = mysql.connection.cursor()

    cur.execute("SELECT `COLUMN_NAME` "
                "FROM `INFORMATION_SCHEMA`.`COLUMNS` "
                "WHERE `TABLE_SCHEMA`='lcf_database' AND `TABLE_NAME`='" + name + "';")

    column = cur.fetchall()
    length = len(column)

    cur.execute("SELECT * from " + name + "")
    # cur.execute("SELECT * from bot")
    result = cur.fetchall()

    return render_template('database_search_page.html', col=column, len=length, data=result, )