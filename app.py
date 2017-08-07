from flask import Flask
from flask import send_from_directory
from flask import render_template

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
   # user = {'nickname': 'Jonathan'}
   # return render_template('index.html', title='Home', user=user)
   return render_template('index.html')


@app.route('/graphs/<path:path>')
def send_graph(path):
    return send_from_directory('graphs', path)

if __name__ == '__main__':
    app.run()


#from flask import Flask, render_template
#
#app = Flask(__name__)
#
#@app.route('/<string:page_name>/')
#def static_page(page_name):
#    return render_template('%s.html' % page_name)
#
#if __name__ == '__main__':
#    app.run()
#

# This one works

