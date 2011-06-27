#!/usr/bin/env python
import doctest
import unittest
import os
import sys
import glob
from should_dsl import should, should_not
from splinter.browser import Browser
from tests.fake_webapp import start_server, stop_server, EXAMPLE_APP

browser = Browser()

def test_suite():
    flags = doctest.NORMALIZE_WHITESPACE | doctest.ELLIPSIS
    if sys.version_info >= (3,):
        flags |= doctest.IGNORE_EXCEPTION_DETAIL
    doctests_path = os.path.join('tests')

    suite = unittest.TestSuite()

    for doctest_file in os.listdir(doctests_path):
        if doctest_file.endswith('.txt'):
            suite.addTest(doctest.DocFileSuite(os.path.join(doctests_path,
                                                            doctest_file),
                                               globs={'browser': browser,
                                                      'should': should,
                                                      'should_not': should_not},
                                               optionflags=flags))
    return suite


def setup():
    start_server()
    browser.visit(EXAMPLE_APP)

def teardown():
    browser.quit()
    stop_server()

if __name__ == '__main__':
    runner = unittest.TextTestRunner(verbosity=2)
    setup()
    result = runner.run(test_suite())
    teardown()
    sys.exit(int(bool(result.failures or result.errors)))
