from src.controllers.helpers.Validation import valid_string, valid_string_max_size
import nose
from unittest import TestCase

class TestValidation_valid_string(TestCase):

    def test_with_valid_string(self):
        s = 'hello'
        is_valid = valid_string(s)

        nose.tools.assert_true(is_valid, '{} is a valid string but valid_string returned {}'.format(s, is_valid))

    def test_with_invalid_string(self):
        s = 9
        is_valid = valid_string(s)

        nose.tools.assert_false(is_valid, '{} is a valid string but valid_string returned {}'.format(s, is_valid))

    def test_with_none_value(self):
        s = None
        is_valid = valid_string(s)

        nose.tools.assert_false(is_valid, '{} is a valid string but valid_string returned {}'.format(s, is_valid))

class TestValidation_valid_string_max_size(TestCase):
    def test_with_correct_size(self):
        s = 'hello'
        max_size = 10
        is_valid = valid_string_max_size(s, max_size)
        nose.tools.assert_true(is_valid, 'valid_string_max_size should return True for string: {} when max size is: {}'.format(s, max_size))

    def test_with_long_string(self):
        s = 'hello'
        max_size = 2
        is_valid = valid_string_max_size(s, max_size)
        nose.tools.assert_false(is_valid, 'valid_string_max_size should return True for string: {} when max size is: {}'.format(s, max_size))

    def test_with_None_value(self):
        s = None
        max_size = 2
        is_valid = valid_string_max_size(s, max_size)
        nose.tools.assert_false(is_valid, 'valid_string_max_size should return True for string: {} when max size is: {}'.format(s, max_size))


    def test_with_integer(self):
        s = 3
        max_size = 2
        is_valid = valid_string_max_size(s, max_size)
        nose.tools.assert_false(is_valid, 'valid_string_max_size should return True for string: {} when max size is: {}'.format(s, max_size))
