#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: jeremiah.marks
# @Date:   2015-12-08 11:19:50
# @Last Modified by:   jeremiah.marks
# @Last Modified time: 2015-12-08 11:23:12

from flask.ext.wtf import Form
from wtforms import StringField, SubmitField
from wtforms.validators import Required

class sourceDestinationApps(Form):
    appname1 = StringField("Source Applicaiton", validators=[Required()])
    apikey1 = StringField("Source API key", validators=[Required()])
    appname2 = StringField("Dest Applicaiton", validators=[Required()])
    apikey2 = StringField("Source API key", validators=[Required()])
    submit = SubmitField("Move Contacts")
