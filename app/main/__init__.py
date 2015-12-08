#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: jeremiah.marks
# @Date:   2015-12-08 11:19:38
# @Last Modified by:   jeremiah.marks
# @Last Modified time: 2015-12-08 11:20:18
from flask import Blueprint

main = Blueprint('main', __name__)

from . import views, errors
