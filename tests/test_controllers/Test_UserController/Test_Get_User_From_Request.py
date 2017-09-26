import json
import os
from unittest import TestCase
from unittest.mock import patch, MagicMock
import nose
import app

class Test_UserController_Post_Request(TestCase):
    new_id = 999

    @patch('src.infrastructure.UserDataAccess.UserDataAccess.update_user',
           MagicMock(return_value=new_id))
    def test_it_should_return_201_when_user_is_successfully_created(self):
        try:
            if 'aws_region' in os.environ:
                os.environ.pop("aws_region")
            response = app.test_client().post('/v1/users',
              data=json.dumps(
                  {
                      "email": "jjj@testmail.com",
                      "phone_number": "233-323-2332",
                      "full_name": "B Sokhi",
                      "password": "hellofromtheotherside",
                      "metadata": "age 34, female, phd"
                  }
                ),
                content_type='application/json')

            expected_value = 201
            real_value = response.status_code
            nose.tools.assert_equal(expected_value, real_value, 'it should have returned {} but returned {} instead'.format(expected_value, real_value))

        except Exception as ex:
            print(ex)
            nose.tools.assert_false(True)

    @patch('src.infrastructure.UserDataAccess.UserDataAccess.update_user',
           MagicMock(return_value=new_id))
    def test_it_should_return_the_correct_email_when_user_is_successfully_created(self):
        try:
            if 'aws_region' in os.environ:
                os.environ.pop("aws_region")

            response = app.test_client().post('/v1/users',
                                              data=json.dumps(
                                                  {
                                                      "email": "jjj@testmail.com",
                                                      "phone_number": "233-323-2332",
                                                      "full_name": "B Sokhi",
                                                      "password": "hellofromtheotherside",
                                                      "metadata": "age 34, female, phd"
                                                  }
                                              ),
                                              content_type='application/json')

            response_obj = json.loads(response.data.decode('utf8'))
            expected_value = "jjj@testmail.com"
            real_value = response_obj['email']

            nose.tools.assert_equal(expected_value, real_value,
                                    'it should have returned {} but returned {} instead'.format(expected_value,
                                                                                                real_value))

        except Exception as ex:
            print(ex)
            nose.tools.assert_false(True)

    @patch('src.infrastructure.UserDataAccess.UserDataAccess.update_user',
           MagicMock(return_value=new_id))
    def test_it_should_return_the_correct_phonenumber_when_user_is_successfully_created(self):
        try:
            if 'aws_region' in os.environ:
                os.environ.pop("aws_region")
            response = app.test_client().post('/v1/users',
                                              data=json.dumps(
                                                  {
                                                      "email": "jjj@testmail.com",
                                                      "phone_number": "233-323-2332",
                                                      "full_name": "B Sokhi",
                                                      "password": "hellofromtheotherside",
                                                      "metadata": "age 34, female, phd"
                                                  }
                                              ),
                                              content_type='application/json')

            response_obj = json.loads(response.data.decode('utf8'))
            expected_value = "233-323-2332"
            real_value = response_obj['phone_number']

            nose.tools.assert_equal(expected_value, real_value,
                                    'it should have returned {} but returned {} instead'.format(expected_value,
                                                                                                real_value))

        except Exception as ex:
            print(ex)
            nose.tools.assert_false(True)

    @patch('src.infrastructure.UserDataAccess.UserDataAccess.update_user',
           MagicMock(return_value=new_id))
    def test_it_should_return_the_correct_fullname_when_user_is_successfully_created(self):
        try:
            if 'aws_region' in os.environ:
                os.environ.pop("aws_region")
            response = app.test_client().post('/v1/users',
                                              data=json.dumps(
                                                  {
                                                      "email": "jjj@testmail.com",
                                                      "phone_number": "233-323-2332",
                                                      "full_name": "B Sokhi",
                                                      "password": "hellofromtheotherside",
                                                      "metadata": "age 34, female, phd"
                                                  }
                                              ),
                                              content_type='application/json')

            response_obj = json.loads(response.data.decode('utf8'))
            expected_value = "B Sokhi"
            real_value = response_obj['full_name']

            nose.tools.assert_equal(expected_value, real_value,
                                    'it should have returned {} but returned {} instead'.format(expected_value,
                                                                                                real_value))

        except Exception as ex:
            print(ex)
            nose.tools.assert_false(True)

    @patch('src.infrastructure.UserDataAccess.UserDataAccess.update_user',
           MagicMock(return_value=new_id))
    def test_it_should_return_the_correct_metadata_when_user_is_successfully_created(self):
        try:
            if 'aws_region' in os.environ:
                os.environ.pop("aws_region")
            response = app.test_client().post('/v1/users',
                                              data=json.dumps(
                                                  {
                                                      "email": "jjj@testmail.com",
                                                      "phone_number": "233-323-2332",
                                                      "full_name": "B Sokhi",
                                                      "password": "hellofromtheotherside",
                                                      "metadata": "age 34, female, phd"
                                                  }
                                              ),
                                              content_type='application/json')

            response_obj = json.loads(response.data.decode('utf8'))
            expected_value = "age 34, female, phd"
            real_value = response_obj['metadata']

            nose.tools.assert_equal(expected_value, real_value,
                                    'it should have returned {} but returned {} instead'.format(expected_value,
                                                                                                real_value))

        except Exception as ex:
            print(ex)
            nose.tools.assert_false(True)

    @patch('src.infrastructure.UserDataAccess.UserDataAccess.update_user',
           MagicMock(return_value=new_id))
    def test_it_should_return_valid_string_for_key_when_user_is_successfully_created(self):
        try:
            if 'aws_region' in os.environ:
                os.environ.pop("aws_region")
            response = app.test_client().post('/v1/users',
                                              data=json.dumps(
                                                  {
                                                      "email": "jjj@testmail.com",
                                                      "phone_number": "233-323-2332",
                                                      "full_name": "B Sokhi",
                                                      "password": "hellofromtheotherside",
                                                      "metadata": "age 34, female, phd"
                                                  }
                                              ),
                                              content_type='application/json')

            response_obj = json.loads(response.data.decode('utf8'))
            real_value = response_obj['key']

            nose.tools.assert_true(type(real_value) is str,
                                    'type of the key field should have returned {} but returned {} instead'.format('str',
                                                                                                type(real_value)))

        except Exception as ex:
            print(ex)
            nose.tools.assert_false(True)

    @patch('src.infrastructure.UserDataAccess.UserDataAccess.update_user',
           MagicMock(return_value=new_id))
    def test_it_should_return_valid_int_for_id_when_user_is_successfully_created(self):
        try:
            if 'aws_region' in os.environ:
                os.environ.pop("aws_region")
            response = app.test_client().post('/v1/users',
                                              data=json.dumps(
                                                  {
                                                      "email": "jjj@testmail.com",
                                                      "phone_number": "233-323-2332",
                                                      "full_name": "B Sokhi",
                                                      "password": "hellofromtheotherside",
                                                      "metadata": "age 34, female, phd"
                                                  }
                                              ),
                                              content_type='application/json')

            response_obj = json.loads(response.data.decode('utf8'))

            expected_value = self.new_id
            real_value = response_obj['id']

            nose.tools.assert_equal(expected_value, real_value,
                                   'it should have returned {} but returned {} instead'.format(expected_value,
                                                                                                real_value))

        except Exception as ex:
            print(ex)
            nose.tools.assert_false(True)

    @patch('src.infrastructure.UserDataAccess.UserDataAccess.update_user',
           MagicMock(return_value=new_id))
    def test_it_should_return_valid_int_for_id_when_user_is_successfully_created(self):
        try:
            if 'aws_region' in os.environ:
                os.environ.pop("aws_region")
            response = app.test_client().post('/v1/users',
                                              data=json.dumps(
                                                  {
                                                      "email": "jjj@testmail.com",
                                                      "phone_number": "233-323-2332",
                                                      "full_name": "B Sokhi",
                                                      "password": "hellofromtheotherside",
                                                      "metadata": "age 34, female, phd"
                                                  }
                                              ),
                                              content_type='application/json')

            response_obj = json.loads(response.data.decode('utf8'))
            real_value = response_obj['id']

            nose.tools.assert_true(type(real_value) is int,
                                   'type of the key field should have returned {} but returned {} instead'.format('int',
                                                                                                                  type(
                                                                                                                      real_value)))

        except Exception as ex:
            print(ex)
            nose.tools.assert_false(True)