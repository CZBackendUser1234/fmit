from dataclasses import dataclass

from pydantic import Field, field_validator

from app.utils.constants import NAME_MIN_LEN, NAME_MAX_LEN, SURNAME_MIN_LEN, SURNAME_MAX_LEN
from app.utils.validators import person_name_validation, person_surname_validation


@dataclass
class CreateWeddingDto:
    m_name: str = Field(
        description="Name of the male person",
        examples=["Андрей", "Сергей", "Пётр"],
        min_length=NAME_MIN_LEN,
        max_length=NAME_MAX_LEN
    )
    m_surname: str = Field(
        description="Surname of the male person",
        examples=["Иванов", "Петров", "Васечкин"],
        min_length=SURNAME_MIN_LEN,
        max_length=SURNAME_MAX_LEN
    )
    f_name: str = Field(
        description="Name of the female person",
        examples=["Настя", "Алёна"],
        min_length=NAME_MIN_LEN,
        max_length=NAME_MAX_LEN
    )
    f_surname: str = Field(
        description="Surname of the female person",
        examples=["Иванова", "Петрова", "Васечкина"],
        min_length=SURNAME_MIN_LEN,
        max_length=SURNAME_MAX_LEN
    )

    @field_validator('m_name')
    @classmethod
    def person_m_name_validation(cls, name: str) -> str:
        return person_name_validation(name)

    @field_validator('f_name')
    @classmethod
    def person_f_name_validation(cls, name: str) -> str:
        return person_name_validation(name)

    @field_validator('m_surname')
    @classmethod
    def person_m_surname_validation(cls, surname: str) -> str:
        return person_surname_validation(surname)

    @field_validator('f_surname')
    @classmethod
    def person_f_surname_validation(cls, surname: str) -> str:
        return person_surname_validation(surname)
