from flask import Flask


app = Flask(__name__)

app.config['SECRET_KEY'] = 'b26f6d49e9ea23f46c90a06c0219e287'

from simpleapp.routes import routes
