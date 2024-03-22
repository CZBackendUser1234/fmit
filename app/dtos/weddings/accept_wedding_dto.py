from dataclasses import dataclass
from uuid import UUID
from pydantic import Field

from app.dtos.weddings.wedding_status import WeddingStatus


@dataclass
class AcceptWeddingDto:
    m_name: str
    m_surname: str
    f_name: str
    f_surname: str
    digital_signature: UUID
    status: WeddingStatus = Field(default=WeddingStatus.ACCEPTED)
