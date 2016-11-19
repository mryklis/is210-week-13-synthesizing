#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""file caching module"""


import os
import pickle


class PickleCache(object):
    """file caching class"""

    def __init__(self, file_path='datastore.pkl', autosync=False):
        """class construct

        Args:
            file_path (str): file path to open
            autosync (bool): attribute

        Example:
        >>> cacher = PickleCache()
        >>> kprint cacher._PickleCache__file_path
        'datastore.pkl'
        >>> print cacher._PickleCache__file_object
        None
        >>> print cacher._PickleCache__data
        {}
        """

        self.__file_path = file_path
        self.__data = {}
        self.autosync = autosync

    def __setitem__(self, key, value):
        """method for storing values

        Args:
            key (Str): required argument
            value (str): required argument

        Example:
            >>> pcache = PickleCache()
            >>> pcache['test'] = 'hello'
            >>> print pcache._PickleCache__data['test']
            'hello'
            >>> len(pcache)
            1
        """

        self.__data[key] = value
        if self.autosync is True:
            self.flush()

    def __len__(self):
        """return length of dic

        Args:
            None

        Returns:
            len (int): length of object

        Example:
             >>> pcache = PickleCache()
             >>> pcache['test'] = 'hello'
             >>> print len(pcache)
             1
             >>> del pcache['test']
             >>> print len(pcache)
             0
        """

        return len(self.__data)

    def __getitem__(self, key):
        """return value from data

        Args:
            key (string): value in dic

        Returns:
             value from data

        Example:
             >>> pcache = PickleCache()
             >>> pcache['test'] = 'hello'
             >>> print pcache['test']
             'hello'
        """

        try:
            return self.__data[key]
        except LookupError as err:
            raise err

    def __delitem__(self, key):
        """delete item from dic

        ARgs:
            key (str): dic key

        Returns:
            None

        Example:
            >>> pcache = PickleCache()
            >>> pcache['test'] = 'hello'
            >>> print len(pcache)
            1
            >>> del pcache['test']
            >>> print len(pcache)
            0
        """

        try:
            del self.__data[key]
        except LookupError as err:
            raise err

        if self.autosync is True:
            self.flush()

    def load(self):
        """method to open file

        Args:
            None

        Returns:
             None

        Example:
             >>> import pickle
             >>> fh = open('datastore.pkl', 'w')
             >>> pickle.dump({'foo': 'bar'}, fh)
             >>> fh.close()
             >>> pcache = PickleCache('datastore.pkl')
             >>> print pcache['foo']
             'bar'

        """

        if os.path.exists(self.__file_path) \
           and os.path.getsize(self.__file_path) != 0:
            with open(self.__file_path, 'r') as dataf:
                self.__data = pickle.load(dataf)
        dataf.close()
        self.load()

    def flush(self):
        """clear data

        ARgs:
            None

        Returns:
            None

        Example:
            >>> pcache = PickleCache()
            >>> pcache['foo'] = 'bar'
            >>> pcache.flush()
            >>> fhandler = open(pcache._PickleCache__file_path, 'r')
            >>> data = pickle.load(fhandler)
            >>> print data
            {'foo': 'bar'}

        """

        with open(self.__file_path, 'w') as dataf:
            pickle.dump(self.__data, dataf)
        dataf.close()
