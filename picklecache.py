#!/usr/bin/env python
# -*- coding: utf-8 -*-


import os, pickle

class PickleCache(object):

    def __init__(self, file_path='datastore.pkl', autosync=False):

        self.__file_path = file_path
        self.__data = {}
        self.autosync = autosync


    def __setitem__(self, key, value):

        self.__data[key] = value


    def __len__(self):

        return len(self.__data)


    def __getitem__(self, key):

        try:
            return self.__data[key]
        except LookupError as err:
            raise err


    def __delitem__(self, key):

        try:
            del self.__data[key]
        except LookupError as err:
            raise err
        
