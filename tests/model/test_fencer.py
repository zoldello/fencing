#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `model/fencing` package."""
from model.fencer import Fencer

#from __future__ import absolute_import
#import unittest

#import imp

#foo = imp.load_source('Fencer', 'fencing/model/fencer.py')


class TestFencing(unittest.TestCase):
    """Model/Fencing. unit test"""

    def test___init___ensure_initialization_work(self):
        target = { "last_name": "jackson123", 'first_name': 'michael', 'club': 'blood on the dance floor', 'skill_level': 'A18'}

        fencer = Fencer(target)

        #self.assertEqual(fencer.last_name, target.last_name, 'Fencer model should properly set last name')


if __name__ == '__main__':
    unittest.main()
