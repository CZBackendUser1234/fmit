import re

from pydantic import ValidationError

from app.utils.constants import NAME_MAX_LEN, NAME_MIN_LEN, SURNAME_MIN_LEN, SURNAME_MAX_LEN


def person_name_validation(name: str):
    if name is None or name.strip() == "":
        raise ValidationError("Person name must be not empty!")
    if len(name) < NAME_MIN_LEN or len(name) > NAME_MAX_LEN:
        raise ValueError(f"Person name should be between {NAME_MIN_LEN}-{NAME_MAX_LEN} char.")
    if len(re.findall(r'\d', name)) > 0:
        raise ValueError("Person name shouldn't have digits.")
    if not re.match("^[\u0400-\u04FF]*$", name):
        raise ValueError("Person name should have valid characters.")


def person_surname_validation(surname: str):
    if surname is None or surname.strip() == "":
        raise ValidationError("Person surname must be not empty!")
    if len(surname) < SURNAME_MIN_LEN or len(surname) > SURNAME_MAX_LEN:
        raise ValueError(f"Person surname should be between {NAME_MIN_LEN}-{NAME_MAX_LEN} char.")
    if len(re.findall(r'\d', surname)) > 0:
        raise ValueError("Person surname shouldn't have digits.")
    if not re.match("^[\u0400-\u04FF]*$", surname):
        raise ValueError("Person surname should have valid characters.")

