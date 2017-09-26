def valid_string(n):
    try:
        if (not (type(n) is str and n)):
            return False;
        return True
    except Exception:
        return False;

def valid_string_max_size(n, max_size):
    try:
        if (len(n) > max_size):
            return False;
        return True
    except Exception:
        return False;