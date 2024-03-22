from dataclasses import dataclass
from pydantic import Field

from app.dtos.weddings.wedding_status import WeddingStatus


@dataclass
class DeclineWeddingDto:
    decline_message: str
    status: WeddingStatus = Field(default=WeddingStatus.DECLINED)
