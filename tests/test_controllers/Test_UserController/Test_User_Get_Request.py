import json
from unittest import TestCase
from unittest.mock import patch, MagicMock
import nose
import src

class UserControllerTest(TestCase):
    response_user_list = [
        {
            "email": "b@testmail.com",
            "id": 1111,
            "account_key": None,
            "full_name": "B Sokhi",
            "key": "O",
            "metadata": "age 25, female, dr",
            "password": "hellofromtheotherside",
            "phone_number": "233-323-2332"
        },
        {
            "email": "a@testmail.com",
            "id": 99999,
            "account_key": None,
            "full_name": "B Vinod",
            "key": "O",
            "metadata": "age 60, female, phd",
            "password": "hellofromtheotherside",
            "phone_number": "345-3233-6554"
        }]

    @patch('src.infrastructure.UserDataAccess.UserDataAccess.get_user',
           MagicMock(return_value=response_user_list))
    def test_it_should_return_200_when_users_exist(self):
        try:
            response = src.test_client().get('/v1/users')

            expected_value = 200
            real_value = response.status_code
            nose.tools.assert_equal(expected_value, real_value, 'it should have returned {} but returned {} instead'.format(expected_value, real_value))

        except Exception as ex:
            print(ex)
            nose.tools.assert_false(True)

    @patch('src.infrastructure.UserDataAccess.UserDataAccess.get_user',
           MagicMock(return_value=response_user_list))
    def test_it_should_return_the_correct_number_of_users(self):
        try:
            response = src.test_client().get('/v1/users')
            response_list = json.loads(response.data.decode('utf8'))

            expected_value = len(self.response_user_list)
            real_value = len(response_list)

            nose.tools.assert_equal(expected_value, real_value,
                                    "/v1/users should have returned {} items, but it returned {}".format(
                                        expected_value, real_value))
        except Exception as ex:
            print(ex)
            nose.tools.assert_false(True)

    @patch('src.infrastructure.UserDataAccess.UserDataAccess.get_user',
           MagicMock(return_value=response_user_list))
    def test_it_should_return_the_correct_email(self):
        try:
            response = src.test_client().get('/v1/users')
            response_list = json.loads(response.data.decode('utf8'))
            expected_value = "b@testmail.com"
            real_value = response_list[0]['email']
            nose.tools.assert_equal(expected_value, real_value,
                                    "/v1/users should have returned {} for the first email, but it returned {}".format(
                                        expected_value, real_value))
        except Exception as ex:
            print(ex)
            nose.tools.assert_false(True)

    @patch('src.infrastructure.UserDataAccess.UserDataAccess.get_user',
           MagicMock(return_value=response_user_list))
    def test_it_should_return_the_correct_id(self):
        try:
            response = src.test_client().get('/v1/users')
            response_list = json.loads(response.data.decode('utf8'))
            expected_value = 1111
            real_value = response_list[0]['id']
            nose.tools.assert_equal(expected_value, real_value,
                                    "/v1/users should have returned {} for the first id, but it returned {}".format(
                                        expected_value, real_value))
        except Exception as ex:
            print(ex)
            nose.tools.assert_false(True)

    @patch('src.infrastructure.UserDataAccess.UserDataAccess.get_user',
           MagicMock(return_value=response_user_list))
    def test_it_should_return_none_account_key(self):
        try:
            response = src.test_client().get('/v1/users')
            response_list = json.loads(response.data.decode('utf8'))
            expected_value = None
            real_value = response_list[0]['account_key']
            nose.tools.assert_equal(expected_value, real_value,
                                    "/v1/users should have returned {} for the first account_key, but it returned {}".format(
                                        expected_value, real_value))
        except Exception as ex:
            print(ex)
            nose.tools.assert_false(True)

    @patch('src.infrastructure.UserDataAccess.UserDataAccess.get_user',
           MagicMock(return_value=response_user_list))
    def test_it_should_return_the_correct_fullname(self):
        try:
            response = src.test_client().get('/v1/users')
            response_list = json.loads(response.data.decode('utf8'))
            expected_value = 'B Sokhi'
            real_value = response_list[0]['full_name']
            nose.tools.assert_equal(expected_value, real_value,
                                    "/v1/users should have returned {} for the first account_key, but it returned {}".format(
                                        expected_value, real_value))
        except Exception as ex:
            print(ex)
            nose.tools.assert_false(True)

    @patch('src.infrastructure.UserDataAccess.UserDataAccess.get_user',
           MagicMock(return_value=response_user_list))
    def test_it_should_return_the_correct_key(self):
        try:
            response = src.test_client().get('/v1/users')
            response_list = json.loads(response.data.decode('utf8'))
            expected_value = 'O'
            real_value = response_list[0]['key']
            nose.tools.assert_equal(expected_value, real_value,
                                    "/v1/users should have returned {} for the first account_key, but it returned {}".format(
                                        expected_value, real_value))
        except Exception as ex:
            print(ex)
            nose.tools.assert_false(True)

    @patch('src.infrastructure.UserDataAccess.UserDataAccess.get_user',
           MagicMock(return_value=response_user_list))
    def test_it_should_return_the_correct_metadata(self):
        try:
            response = src.test_client().get('/v1/users')
            response_list = json.loads(response.data.decode('utf8'))
            expected_value = 'age 25, female, dr'
            real_value = response_list[0]['metadata']
            nose.tools.assert_equal(expected_value, real_value,
                                    "/v1/users should have returned {} for the first account_key, but it returned {}".format(
                                        expected_value, real_value))
        except Exception as ex:
            print(ex)
            nose.tools.assert_false(True)

    @patch('src.infrastructure.UserDataAccess.UserDataAccess.get_user',
           MagicMock(return_value=response_user_list))
    def test_it_should_return_the_correct_password(self):
        try:
            response = src.test_client().get('/v1/users')
            response_list = json.loads(response.data.decode('utf8'))
            expected_value = 'hellofromtheotherside'
            real_value = response_list[0]['password']
            nose.tools.assert_equal(expected_value, real_value,
                                    "/v1/users should have returned {} for the first account_key, but it returned {}".format(
                                        expected_value, real_value))
        except Exception as ex:
            print(ex)
            nose.tools.assert_false(True)

    @patch('src.infrastructure.UserDataAccess.UserDataAccess.get_user',
           MagicMock(return_value=response_user_list))
    def test_it_should_return_the_correct_phonenumber(self):
        try:
            response = src.test_client().get('/v1/users')
            response_list = json.loads(response.data.decode('utf8'))
            expected_value = '233-323-2332'
            real_value = response_list[0]['phone_number']
            nose.tools.assert_equal(expected_value, real_value,
                                    "/v1/users should have returned {} for the first account_key, but it returned {}".format(
                                        expected_value, real_value))
        except Exception as ex:
            print(ex)
            nose.tools.assert_false(True)