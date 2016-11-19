#!/usr/bin/env python
# -*- coding: utf-8 -*-


import os, pickle

class PickleCache(object):

    def __init__(self, file_path='datastore.pkl', autosync=False):

        self.__file_path = file_path
        self.__data = {}
        self.autosync = autosync