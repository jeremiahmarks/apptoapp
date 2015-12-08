#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: jeremiah.marks
# @Date:   2015-12-08 10:27:32
# @Last Modified by:   jeremiah.marks
# @Last Modified time: 2015-12-08 10:31:37

import os

from app import create_app
from flask.ext.script import Manager, Shell

app = create_app('default')
manager = Manager(app)

def make_shell_context():
    return dict(app=app)

manager.add_command('shell', Shell(make_context=make_shell_context))

if __name__ == '__main__':
    manager.run()
