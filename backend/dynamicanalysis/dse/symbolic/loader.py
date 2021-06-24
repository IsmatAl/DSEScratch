# Copyright: copyright.txt

import inspect
import logging
import re
import os
import sys
from .invocation import FunctionInvocation
from .symbolic_types import SymbolicInteger, getSymbolic

# The built-in definition of len wraps the return value in an int() constructor, destroying any symbolic types.
# By redefining len here we can preserve symbolic integer types.
import builtins
builtins.len = (lambda x: x.__len__())


class Loader:
    def __init__(self, filename, entry):
        self._fileName = os.path.basename(filename)
        self._fileName = self._fileName[:-3]
        if (entry == ""):
            self._entryPoint = self._fileName
        else:
            self._entryPoint = entry
        self._resetCallback(True)

    def getFile(self):
        return self._fileName

    def getEntry(self):
        return self._entryPoint

    def createInvocation(self):
        inv = FunctionInvocation(self._execute, self._resetCallback)
        func = self.app.__dict__[self._entryPoint]
        argspec = inspect.getargspec(func)
        # check to see if user specified initial values of arguments
        if "concrete_args" in func.__dict__:
            for (f, v) in func.concrete_args.items():
                if not f in argspec.args:
                    # print("Error in @concrete: " + self._entryPoint +
                    #       " has no argument named " + f)
                    raise ImportError("Error in @concrete: " + self._entryPoint +
                                      " has no argument named " + f)
                else:
                    Loader._initializeArgumentConcrete(inv, f, v)
        if "symbolic_args" in func.__dict__:
            for (f, v) in func.symbolic_args.items():
                if not f in argspec.args:
                    # print("Error (@symbolic): " + self._entryPoint +
                    #       " has no argument named " + f)
                    raise ImportError("Error (@symbolic): " + self._entryPoint +
                                      " has no argument named " + f)
                elif f in inv.getNames():
                    # print("Argument " + f +
                    #       " defined in both @concrete and @symbolic")
                    raise ImportError("Argument " + f +
                                      " defined in both @concrete and @symbolic")
                else:
                    s = getSymbolic(v)
                    if (s == None):
                        # print("Error at argument " + f + " of entry point " + self._entryPoint +
                        #       " : no corresponding symbolic type found for type " + str(type(v)))
                        raise ImportError("Error at argument " + f + " of entry point " + self._entryPoint +
                                          " : no corresponding symbolic type found for type " + str(type(v)))
                    Loader._initializeArgumentSymbolic(inv, f, v, s)
        for a in argspec.args:
            if not a in inv.getNames():
                Loader._initializeArgumentSymbolic(inv, a, 0, SymbolicInteger)
        return inv

    # need these here (rather than inline above) to correctly capture values in lambda
    def _initializeArgumentConcrete(inv, f, val):
        inv.addArgumentConstructor(f, val, lambda n, v: val)

    def _initializeArgumentSymbolic(inv, f, val, st):
        inv.addArgumentConstructor(f, val, lambda n, v: st(n, v))

    # -- private

    def _resetCallback(self, firstpass=False):
        self.app = None
        if firstpass and self._fileName in sys.modules:
            print("There already is a module loaded named " + self._fileName)
            raise ImportError(
                "There already is a module loaded named " + self._fileName)
        try:
            if (not firstpass and self._fileName in sys.modules):
                del(sys.modules[self._fileName])
            self.app = __import__(self._fileName)
            if not self._entryPoint in self.app.__dict__ or not callable(self.app.__dict__[self._entryPoint]):
                print("File " + self._fileName +
                      ".py doesn't contain a function named " + self._entryPoint)
                raise ImportError("File " + self._fileName +
                                  ".py doesn't contain a function named " + self._entryPoint)
        except Exception as arg:
            print("Couldn't import " + self._fileName)
            print(arg)
            raise ImportError("Couldn't import " + self._fileName)

    def _execute(self, **args):
        return self.app.__dict__[self._entryPoint](**args)


def loaderFactory(filename, entry):
    if not os.path.isfile(filename) or not re.search(".py$", filename):
        print(filename)
        return None
    try:
        dir = os.path.dirname(filename)
        sys.path = [dir] + sys.path
        ret = Loader(filename, entry)
        return ret
    except ImportError as e:
        sys.path = sys.path[1:]
        raise e
