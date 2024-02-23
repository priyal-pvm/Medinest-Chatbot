import re
def get_str_from_apt_dict(apt_dict: dict):
    result = ", ".join([f"{int(value)} {key}" for key, value in apt_dict.items()])
    return result

def extract_session_id(session_str: str):
    match = re.search(r"/sessions/(.*?)/contexts/", session_str)
    if match:
        extracted_string = match.group(1)
        return extracted_string

    return ""