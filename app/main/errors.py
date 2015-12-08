#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: jeremiah.marks
# @Date:   2015-12-08 11:19:44
# @Last Modified by:   jeremiah.marks
# @Last Modified time: 2015-12-08 11:20:31
from flask import render_template
from . import main


@main.app_errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@main.app_errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500
