#!/usr/bin/python

# this module is capable to edit every rule file for modules
# Catalin Brezeanu - 22.12.2017

import os
import datetime
import time
import sys
import tempfile

module = sys.argv[1]
operation = sys.argv[2]
ip_s = sys.argv[3]
ip_d = sys.argv[4]
port = sys.argv[5]

def modifyRulesFile(module, operation):
    print('File to modify is: rules.'module'.')
    

class modifyRulesFile(object):

    def __init__(self, fname):
        self.__write_dict = {}
        self.__filename = fname
        with open(fname, 'rb') as fp:
            for line in fp:
                self.__tempfile.write(line)
        self.__tempfile.seek(0)

    def write(self, s, line_number = 'END'):
        if line_number != 'END' and not isinstance(line_number, (int, float)):
            raise FileModifierError("Line number %s is not a valid number" % line_number)
        try:
            self.__write_dict[line_number].append(s)
        except KeyError:
            self.__write_dict[line_number] = [s]

    def writeline(self, s, line_number = 'END'):
        self.write('%s\n' % s, line_number)

    def writelines(self, s, line_number = 'END'):
        for ln in s:
            self.writeline(s, line_number)

    def __popline(self, index, fp):
        try:
            ilines = self.__write_dict.pop(index)
            for line in ilines:
                fp.write(line)
        except KeyError:
            pass

    def close(self):
        self.__exit__(None, None, None)

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        with open(self.__filename,'w') as fp:
            for index, line in enumerate(self.__tempfile.readlines()):
                self.__popline(index, fp)
                fp.write(line)
            for index in sorted(self.__write_dict):
                for line in self.__write_dict[index]:
                    fp.write(line)
        self.__tempfile.close()



