from flask import Flask
from flask import send_from_directory

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello World!"


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

