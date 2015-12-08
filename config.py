#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: jeremiah.marks
# @Date:   2015-12-08 10:27:17
# @Last Modified by:   jeremiah.marks
# @Last Modified time: 2015-12-08 10:34:45

import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'q^TAxJvQuUEj&JbMjpj6&!byXJk88RpqxUWNR8kD$BKc4X!sz*DZubTJ@fUj&$SkmzS0Edecsi*mcrBvvxGnLL1gh^cMcdit0iM8'


    @staticmethod
    def init_app(app):
        pass

class DevelopmentConfig(Config):
    DEBUG = True


config = {'default': DevelopmentConfig}
