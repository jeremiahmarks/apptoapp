#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: jeremiah.marks
# @Date:   2015-12-08 11:35:51
# @Last Modified by:   jeremiah.marks
# @Last Modified time: 2015-12-08 13:39:35


############################################################
##
##  This class exists mainly to accept two ISServer objects
##  and use those to move contacts between applications.
##
############################################################

def migrateContacts(source, dest):
    allsourcecons =source.getallrecords('Contact')
    for eachcon in allsourcecons:
        thiscon = {}
        for eachkey in eachcon:
            if eachkey != "Id" and eachcon[eachkey]:
                thiscon[eachkey] = eachcon[eachkey]
        dest.createnewrecord('Contact', thiscon)
