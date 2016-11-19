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
        if self.autosync is True:
            self.flush()


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

        if self.autosync is True:
            self.flush()
            

    def load(self):

        if os.path.exists(self.__file_path) \
           and os.path.getsize(self.__file_path) != 0:
            with open(self.__file_path, 'r') as dataf:
                self.__data = pickle.load(dataf)
        dataf.close()
        self.load()


    def flush(self):

        with open(self.__file_path, 'w') as dataf:
            pickle.dump(self.__data, dataf)
        dataf.close()
