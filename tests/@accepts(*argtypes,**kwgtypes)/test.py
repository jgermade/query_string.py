#!/usr/bin/env python
from datetime import date, datetime
from unittest import main, TestCase
from assert_is import *

class Test(TestCase):
    def test(self):
        is_date(date.today())

    @raises(AssertionError)
    def test_exception(self):
        is_date(None)

if __name__ == "__main__": # pragma: no cover
    main()