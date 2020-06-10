#!/usr/bin/python3
"""Test Module
    Cointains the test modules for base
"""
import unittest
import pep8
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase:
    """
    Contains test cases
    """
    def test_pep8_model(self):
        """
        pep8 test
        """
        pep = pep8.StyleGuide(quiet=True)
        p = pep.check_files(['models/base.py'])
        self.assertEqual(p.total_errors, 0, "fix pep8")

    def test_pep8_test(self):
        """
        pep8 test
        """
        pep = pep8.StyleGuide(quiet=True)
        p = pep.check_files(['tests/test_models/test_base.py'])
        self.assertEqual(p.total_errors, 0, "fix pep8")

    def test_0_id(self):
        """
        Check id method
        """
        Base._Base__nb_objects = 0
        b1 = Base()
        b2 = Base()
        b3 = Base()
        b4 = Base(12)
        b5 = Base()
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)
        self.assertEqual(b3.id, 3)
        self.assertEqual(b4.id, 12)
        self.assertEqual(b5.id, 4)

    def test_1_id(self):
        """
        After run set of ids
        """
        Base._Base__nb_objects = 0
        bas = Base()
        self.assertEqual(bas.id, 1)

    def test_2_id(self):
        """
        Random arguments passed to check
        """
        Base._Base__nb_objects = 0
        t1 = Base(22)
        self.assertEqual(t1.id, 22)
        t2 = Base(-33)
        self.assertEqual(t2.id, -33)
        t3 = Base()
        self.assertEqual(t3.id, 1)

    def test_3_set_nb(self):
        """
        nb_objects as private
        """
        b = Base(33)
        with self.assertRaises(AttributeError):
            print(b.nb_objects)
        with self.assertRaises(AttributeError):
            print(b.__nb_objects)
