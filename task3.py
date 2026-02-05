import re

def normalize_phone(phone_number: str):
    international_ukr_code = "+38"
    clean_pattern = r"[^\d+]"

    clean_phone_number = re.sub(clean_pattern, "", phone_number)

    if clean_phone_number.startswith(international_ukr_code):
        return clean_phone_number
    
    prefix = "+" if clean_phone_number.startswith("38") else international_ukr_code

    return prefix + clean_phone_number
    