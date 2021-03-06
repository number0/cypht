#!/usr/bin/python

from sys import exc_info
from traceback import print_exception

GREEN = '\033[92m'
RED = '\033[91m'
END = '\033[0m'

def test_runner(obj, tests):
    passed = 0
    print
    for name in tests:
        func = getattr(obj, name)
        try:
            func()
            print '%s %sPASSED%s' % (name, GREEN, END)
            passed += 1
        except Exception:
            print '%s %sFAILED%s' % (name, RED, END)
            exc_type, exc_value, exc_traceback = exc_info()
            print_exception(exc_type, exc_value, exc_traceback)
    print
    print '%s%s of %s PASSED%s' % (GREEN, passed, len(tests), END)
    if (len(tests) > passed):
        print '%s%s of %s FAILED%s' % (RED, (len(tests) - passed), len(tests), END)
    print
    obj.end()
