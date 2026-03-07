def audit_log(func):
    def wrapper(*args, **kwargs):
        print("Authorization Started")
        result = func(*args, **kwargs)
        print("Authorization Completed")
        return result
    return wrapper

def compute_access_level(control_num, favorite_artist):
    # Formula: access_level = CONTROL_NUM * 3 + len(FAVORITE_ARTIST)
    return (control_num * 3) + len(favorite_artist)

@audit_log
def validate_access(access_level, control_num):
    # Formula: threshold = CONTROL_NUM * 5
    threshold = control_num * 5
    return "ACCESS GRANTED" if access_level >= threshold else "ACCESS DENIED"