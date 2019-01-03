#!/usr/bin/python
# -*- coding:utf-8; tab-width:4; mode:python -*-

from flask import Flask, make_response, jsonify
from flask_sqlalchemy import SQLAlchemy


# Por defecto el root es $PREFIX/var/myapp-instance
app=Flask(__name__, instance_relative_config=False)
app.config.from_pyfile('../instance/development.cfg')

db = SQLAlchemy(app)

from myapp.tweet_routes import bp_tweets

app.register_blueprint(bp_tweets, url_prefix="/tweets")

db.init_app(app)
with app.app_context():
    db.create_all()

# Este podría ir en otro Blueprint
@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not Found'}), 404)


