#!/usr/bin/python3

from checker.abstract import AbstractChecker
import flag

import os
import os.path

import yaml

class LocalChecker(AbstractChecker):
    def __init__(self, tick, team, service, ip):
        AbstractChecker.__init__(self, tick, team, service, ip)
        self._starttime = 0
        self._backend = '/tmp'

    def store_yaml(self, ident, yaml):
        filename = os.path.join(self._backend, "%s.yaml" % ident)
        try:
            with open(filename, "w") as handle:
                return yaml.dump(yaml, handle)
        except FileNotFoundError:
            return None

    def store_blob(self, ident, blob):
        filename = os.path.join(self._backend, "%s.blob" % ident)
        try:
            with open(filename, "wb") as handle:
                return handle.write(blob)
        except FileNotFoundError:
            return None

    def retrieve_yaml(self, ident):
        filename = os.path.join(self._backend, "%s.yaml" % ident)
        try:
            with open(filename, "r") as handle:
                return yaml.load(handle)
        except FileNotFoundError:
            return None

    def retrieve_blob(self, ident):
        filename = os.path.join(self._backend, "%s.blob" % ident)
        try:
            with open(filename, "rb") as handle:
                return handle.read()
        except FileNotFoundError:
            return None

    def get_flag(self, tick, payload=None):
        generatedflag = flag.generate(self._team, self._service, payload,
                                      self._starttime + self._tickduration * tick)
        return generatedflag

    def set_backend(self, backend):
        self._backend = backend

    def set_starttime(self, starttime):
        self._starttime = starttime
