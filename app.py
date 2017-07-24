from flask import Flask, render_template

app = Flask(__name__)

@app.route('/<string:page_name>/')
def static_page(page_name):
    return render_template('%s.html' % page_name)

if __name__ == '__main__':
    app.run()

#from flask import Flask
#app = Flask(__name__)
#
#@app.route('/')
#def hello():
#    return "Hello World!"
#
#if __name__ == '__main__':
#            app.run()
