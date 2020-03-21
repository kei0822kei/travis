#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest

from module.add import add


class TestAdd(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(1, 2), 3)


if __name__ == '__main__':
    unittest.main()

