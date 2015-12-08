#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: jeremiah.marks
# @Date:   2015-12-08 11:19:57
# @Last Modified by:   jeremiah.marks
# @Last Modified time: 2015-12-08 11:42:03

from flask import render_template, session, redirect, url_for, current_app
from . import main
from .forms import sourceDestinationApps
from .. import ISServer, contactMigrator

@main.route('/', methods=['GET', 'POST'])
def index():
    form = sourceDestinationApps()
    if form.validate_on_submit():
        app1 = ISServer.ISServer(form.appname1.data, form.apikey1.data)
        app2 = ISServer.ISServer(form.appname2.data, form.apikey2.data)
        contactMigrator.migrateContacts(source=app1, dest=app2)
        return redirect(url_for('.index'))
    return render_template('index.html',form=form)
