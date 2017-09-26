from src.controllers.helpers.Validation import valid_string_max_size, valid_string

def validate_user_request(data):
    errors = []

    phone_number = data.get('phone_number')
    if (not valid_string(phone_number)):
        errors.append('phone_number has to be a string')
    elif (not valid_string_max_size(phone_number, 20)):
        errors.append('phone_number has to be less than 20 characters')

    email = data.get('email')
    if (not valid_string(email)):
        errors.append('email has to be a string')
    elif (not valid_string_max_size(email, 200)):
        errors.append('email has to be less than 200 characters')

    full_name = data.get('full_name')
    if (not valid_string(full_name)):
        errors.append('full_name has to be a string')
    elif (not valid_string_max_size(full_name, 200)):
        errors.append('full_name has to be less than 200 characters')

    password = data.get('password')
    if (not valid_string(password)):
        errors.append('password has to be a string')
    elif (not valid_string_max_size(password, 100)):
        errors.append('password has to be less than 100 characters')

    metadata = data.get('metadata')
    if (not valid_string(metadata)):
        errors.append('metadata has to be a string')
    elif (not valid_string_max_size(metadata, 2000)):
        errors.append('metadata has to be less than 2000 characters')

    return errors