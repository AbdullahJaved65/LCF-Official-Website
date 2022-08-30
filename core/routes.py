import warnings
import numpy as np
import pandas as pd
import plotly.express as px
import plotly.io as pio
import matplotlib.pyplot as plt
import chart_studio
from chart_studio import tools as tls
import chart_studio.plotly as py
from flask import render_template, \
    send_file, request, redirect
from flask_mysqldb import MySQL
# import matplotlib.pyplot as plt
# from matplotlib import pyplot
from keras.models import load_model
from dash import Dash, html, Input, Output, callback, no_update
from base64 import b64encode

from core import ContactForm, app

warnings.filterwarnings('ignore')
# from plotly import Figure
pio.renderers.default = 'browser'

# loading  data
data = pd.read_csv('C:/LCF Official Website/core/ml_notebooks/pred.csv',
                   parse_dates=['Date'], index_col='Date')

model1 = load_model('C:/LCF Official Website/core/ml_notebooks/model2.h5')

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'lcf_database'

mysql = MySQL(app)

username = "abdullahjaved65"
api_key = "YYmQ4ilIrDcNVOvuIBEm"
tls.tools.set_credentials_file(username=username, api_key=api_key)


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


@app.route('/plot.png')
def create_figure(model, batch_size, data):
    test_predictions = []
    X = data.tail(12)
    Y = X.to_numpy()
    Y = Y.reshape(1, len(X), 1)
    for i in range(batch_size):
        # get the prediction value for the first batch
        current_pred = model1.predict(Y)[0]
        # append the prediction into the array
        test_predictions.append(current_pred)
        # use the prediction to update the batch and remove the first value
        Y = np.append(Y[:, 1:, :], [[current_pred]], axis=1)

        def inner_func(X):
            new = X
            new = pd.Index(pd.date_range(
                start=X.index[-1], periods=batch_size, freq="M")).strftime('%Y-%m')
            new.index = pd.to_datetime(new)
            return new

    df1 = pd.DataFrame(test_predictions,
                       index=inner_func(X),
                       columns=['waterlevel'])
    # dict =  {
    #         '2020-12':  1563.970215,
    #         '2021-01':  1563.332886,
    #         '2021-02':  1562.796753,
    #         '2021-03':  1562.158813,
    #         '2021-04':  1561.437256,
    #         '2021-05':  1560.755127,
    #         '2021-06':  1560.239258,
    #         '2021-07':  1559.708862,
    #         '2021-08':  1559.225464,
    #         '2021-09':  1558.695923,
    #         '2021-10':  1558.057007,
    #         '2021-11':  1557.595093
    # }
    # print(dict)
    return df1


def plot_png(data):
    pio.renderers = 'firefox'
    fig = px.line(df, y='waterlevel',   width=1920, height=1080,
                  title='Predicted Groundwater level of Kuchlak for the year 2021', labels=dict(index="Date"))
    
    fig.update_xaxes(rangeslider_visible=True)
    # fig.write_html("C:/LCF Official Website/file.html")
    return pio.show(fig)
    # data.plot()
   
batch_size = 12
df = create_figure(model1, batch_size, data)
graph_var = plot_png(df)
py.plot(graph_var, filename='groundwater level', auto_open=True)
# plt.savefig('fig.png')



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

        # cur = mysql.connection.cursor()
        # cur.execute("INSERT INTO user(name) VALUES(%s)",
        #             ["Ahsan"])
        #
        # # commit to db
        # mysql.connection.commit()
        #
        # # close connection
        # cur.close()
        return redirect("contact.html")
    else:
        return render_template('contact.html', form=form)


@app.route('/event.html')
def event():
    return render_template('event.html')
    # news_articles = get_latest_news()
    # return render_template('event.html', news_articles=news_articles)


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
    path = "html2pdf.pdf"
    # path = "info.xlsx"
    # path = "simple.docx"
    # path = "sample.txt"
    return send_file("C:/LCF Official Website/core/templates/download.html", as_attachment=True)


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
