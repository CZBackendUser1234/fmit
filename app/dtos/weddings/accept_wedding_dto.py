from dataclasses import dataclass
from uuid import UUID


@dataclass
class AcceptWeddingDto:
    m_name: str
    m_surname: str
    f_name: str
    f_surname: str
    digital_signature: UUID
