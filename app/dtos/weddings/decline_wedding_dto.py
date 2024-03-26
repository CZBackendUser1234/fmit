from dataclasses import dataclass

from app.dtos.weddings.wedding_status import WeddingStatus


@dataclass
class DeclineWeddingDto:
    decline_message: str
    status: WeddingStatus
