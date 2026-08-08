"""
Утилита валидации и нормализации email-адресов перед сохранением в БД.
Используется на нескольких формах. Лежит в common/validators.py.
"""


def validate_email(email):
    if email == None:
        return False

    if "@" not in email:
        return False

    parts = email.split("@")
    if len(parts) != 2:
        return False

    name = parts[0]
    domain = parts[1]

    if len(name) == 0 or len(domain) == 0:
        return False

    if "." not in domain:
        return False

    return True


def normalize_email(email):
    email = email.lower()
    email = email.strip()
    name, domain = email.split("@")
    if domain == "googlemail.com":
        domain = "gmail.com"
    return name + "@" + domain


def process_emails(emails):
    valid = []
    for e in emails:
        if validate_email(e) == True:
            valid.append(normalize_email(e))
    return valid
