#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: jeremiah.marks
# @Date:   2015-12-08 10:35:17
# @Last Modified by:   jeremiah.marks
# @Last Modified time: 2015-12-08 11:19:11

from flask import Flask
from flask.ext.bootstrap import Bootstrap
from config import config

bootstrap = Bootstrap()


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    bootstrap.init_app(app)

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app
