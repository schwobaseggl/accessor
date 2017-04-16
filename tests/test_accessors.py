# -*- coding: utf-8 -*-
from unittest.case import TestCase

from accessor.accessors import A
from tests.utils import AttributeContainer


class AccessorTest(TestCase):
    def setUp(self):
        self.attr_obj = AttributeContainer(
            dct={
                'key': [
                    1,
                    'abc',
                    AttributeContainer(a=1, b=2)
                ]
            },
            one=1,
            abc='abc',
            lst=[0, 1, 2]
        )
        self.key_obj = {
            'one': 1,
            'abc': 'abc',
            'lst': [0, 1, 2]
        }
        self.index_obj = [
            'abc',
            1,
        ]

    def tearDown(self):
        del self.attr_obj
        del self.key_obj
        del self.index_obj

    def test_single_attr_bit_exists(self):
        accessor = A('one')
        self.assertEqual(accessor.resolve(self.attr_obj), 1)

    def test_single_attr_bit_fails(self):
        accessor = A('fail')
        self.assertEqual(accessor.resolve(self.attr_obj), None)

    def test_single_key_bit_exists(self):
        accessor = A('one')
        self.assertEqual(accessor.resolve(self.key_obj), 1)

    def test_single_key_bit_fails(self):
        accessor = A('fail')
        self.assertEqual(accessor.resolve(self.key_obj), None)

    def test_single_index_bit_exists(self):
        accessor = A('1')
        self.assertEqual(accessor.resolve(self.index_obj), 1)

    def test_single_index_bit_fails(self):
        accessor = A('fail')
        self.assertEqual(accessor.resolve(self.index_obj), None)

    def test_nested_attr_bits_exists(self):
        accessor = A('dct.key.1.2')
        self.assertEqual(accessor.resolve(self.attr_obj), 'c')

    def test_nested_attr_bits_fails(self):
        accessor = A('lst.abc')
        self.assertEqual(accessor.resolve(self.attr_obj), None)

    def test_nested_key_bits_exists(self):
        accessor = A('lst.1')
        self.assertEqual(accessor.resolve(self.key_obj), 1)

    def test_nested_key_bits_fails(self):
        accessor = A('abc.abc')
        self.assertEqual(accessor.resolve(self.key_obj), None)

    def test_nested_index_bits_exists(self):
        accessor = A('0.__len__')
        self.assertEqual(accessor.resolve(self.index_obj), 3)

    def test_nested_index_bits_fails(self):
        accessor = A('1.__len__')
        self.assertEqual(accessor.resolve(self.index_obj), None)
