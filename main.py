from core import app

if __name__ == '__main__':
    app.run(debug=True)

# import io
# # Pandas and Matplotlib
# import matplotlib
# import matplotlib.pyplot as plt
# import pandas as pd
# import requests
# from core import app
# from .utils import get_latest_news
# from flask import Flask, \
#     render_template, \
#     Response
# from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
#
# matplotlib.use('Agg')
#
# url = "http://covidtracking.com/api/states/daily.csv"
# s = requests.get(url).content
#
# df = pd.read_csv(io.StringIO(s.decode('utf-8')))
#
# df['date'] = pd.to_datetime(df['date'], format='%Y%m%d')
#
# df.drop(['dateChecked'], axis=1, inplace=True)
#
# df['state'] = df['state'].apply(str)
#
# df.fillna(value=-1, inplace=True)
#
# app = Flask(__name__)
#
#
# @app.route('/', methods=("POST", "GET"))
# def home():
#     return render_template('index.html')
#
#
# @app.route('/plot.png')
# def plot_png():
#     fig = create_figure()
#     output = io.BytesIO()
#     # FigureCanvas(fig).print_png(output)
#     FigureCanvas(plt.gcf()).print_png(output)
#     return Response(output.getvalue(), mimetype='image/png')
#
#
# def create_figure(var='positiveIncrease', state='NY'):
#     # assert type(var) == str, "Expected string as the variable name"
#     # assert type(state) == str, "Expected string as the state name"
#     # y = df[df['state'] == state][var]
#     # x = df[df['state'] == state]['date']
#     # fig = Figure()
#     # axis = fig.add_subplot(1, 1, 1)
#     # xs = range(100)
#     # ys = [random.randint(1, 50) for x in xs]
#     # axis.plot(xs, ys)
#     # return fig
#     """
#     Plots a bar chart of the given variable over the date range
#     """
#     assert type(var) == str, "Expected string as the variable name"
#     assert type(state) == str, "Expected string as the state name"
#
#     y = df[df['state'] == state][var]
#     x = df[df['state'] == state]['date']
#     plt.figure(figsize=(14, 7))
#     plt.title("Plot of \"{}\" for {}".format(var, state), fontsize=18)
#     plt.bar(x=x, height=y, edgecolor='k', color='orange')
#     plt.grid(True)
#     plt.xticks(fontsize=14, rotation=45)
#     plt.yticks(fontsize=14)
#     plt.savefig('foo.png', bbox_inches='tight')
#     plt.show()
#
#
# @app.route('/about.html')
# def about():
#     return render_template('about.html')
#
#
# @app.route('/contact.html')
# def contact():
#     return render_template('contact.html')
#
#
# @app.route('/event.html')
# def event():
#     return render_template('event.html')
#
#
# def news_headlines():
#     news_articles = get_latest_news()
#     return render_template("events.html", news_articles=news_articles)
#
#
# @app.route('/gallery.html')
# def gallery():
#     return render_template('gallery.html')
#
#
# if __name__ == "__main__":
#     app.run()
