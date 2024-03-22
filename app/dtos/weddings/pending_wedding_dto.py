from dataclasses import dataclass
from pydantic import Field

from app.dtos.weddings.wedding_status import WeddingStatus


@dataclass
class PendingWeddingDto:
    status: WeddingStatus = Field(default=WeddingStatus.PENDING)
