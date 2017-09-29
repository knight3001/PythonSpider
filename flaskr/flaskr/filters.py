from flask import Flask

app = Flask(__name__) # create the application instance :)
app.config.from_object(__name__) # load config from this file , flaskr.py

@app.template_filter('reverse')
def reverse_filter(s):
    return s[::-1]

