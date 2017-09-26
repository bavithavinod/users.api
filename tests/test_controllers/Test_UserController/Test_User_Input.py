from unittest import TestCase
import nose
from src.controllers.User import _get_user_from_request

class TestUserInput(TestCase):

    def test_get_email_from_request(self):
        request = {
            "email": "b2@testmail.com"
        }

        user = _get_user_from_request(request)

        nose.tools.assert_equal("b2@testmail.com", user.email)
        nose.tools.assert_equal(None, user.full_name)
        nose.tools.assert_equal(None, user.password)
        nose.tools.assert_equal(None, user.metadata)
        nose.tools.assert_equal(None, user.phone_number)


    def test_get_fullname_from_request(self):
        request = {
            "full_name": "bs"
        }

        user = _get_user_from_request(request)
        nose.tools.assert_equal(None, user.email)
        nose.tools.assert_equal("bs", user.full_name)
        nose.tools.assert_equal(None, user.password)
        nose.tools.assert_equal(None, user.metadata)
        nose.tools.assert_equal(None, user.phone_number)

    def test_get_phonenumber_from_request(self):
        request = {
            "phone_number": "233-323-2332"
        }

        user = _get_user_from_request(request)
        nose.tools.assert_equal(None, user.email)
        nose.tools.assert_equal(None, user.full_name)
        nose.tools.assert_equal(None, user.password)
        nose.tools.assert_equal(None, user.metadata)
        nose.tools.assert_equal("233-323-2332", user.phone_number)


    def test_get_password_from_request(self):
        request = {
            "password": "hellofromtheotherside"
        }

        user = _get_user_from_request(request)

        nose.tools.assert_equal(None, user.email)
        nose.tools.assert_equal(None, user.full_name)
        nose.tools.assert_equal("hellofromtheotherside", user.password)
        nose.tools.assert_equal(None, user.metadata)
        nose.tools.assert_equal(None, user.phone_number)


    def test_get_metadata_from_request(self):
        request = {
            "metadata": "age 34, female, phd"
        }

        user = _get_user_from_request(request)

        nose.tools.assert_equal(None, user.email)
        nose.tools.assert_equal(None, user.full_name)
        nose.tools.assert_equal(None, user.password)
        nose.tools.assert_equal("age 34, female, phd", user.metadata)
        nose.tools.assert_equal(None, user.phone_number)