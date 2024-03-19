from uuid import UUID, uuid4

from beanie import Document
from pydantic import Field

from app.dtos.weddings.wedding_status import WeddingStatus


class Wedding(Document):
    id: UUID = Field(default_factory=uuid4, alias="_id")
    m_name: str
    m_surname: str
    f_name: str
    f_surname: str
    digital_signature: UUID = Field(default_factory=uuid4)
    status: WeddingStatus
    decline_message: str

    class Settings:
        name = 'weddings'
