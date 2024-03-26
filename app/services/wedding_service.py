from uuid import UUID

from app.dtos.weddings.accept_wedding_dto import AcceptWeddingDto
from app.dtos.weddings.create_wedding_dto import CreateWeddingDto
from app.dtos.weddings.decline_wedding_dto import DeclineWeddingDto
from app.dtos.weddings.pending_wedding_dto import PendingWeddingDto
from app.dtos.weddings.wedding_status import WeddingStatus
from app.models.schemas import Wedding


class WeddingService:

    @classmethod
    async def create_wedding(
            cls,
            create_wedding_dto: CreateWeddingDto
    ):
        try:
            wedding: Wedding = Wedding(
                m_name=create_wedding_dto.m_name,
                m_surname=create_wedding_dto.m_surname,
                f_name=create_wedding_dto.f_name,
                f_surname=create_wedding_dto.f_surname,
                status=WeddingStatus.PENDING,
                decline_message=""
            )

            wedding_saved: Wedding = await wedding.insert()

            return str(wedding_saved.id)
        except Exception as e:
            raise ValueError(f"Error during saving wedding for male with name: {create_wedding_dto.m_name} "
                             f"and female with name: {create_wedding_dto.f_name}. Error msg: {str(e)}")

    @classmethod
    async def get_wedding_by_id(
            cls,
            wedding_id: str
    ):
        try:
            wedding_by_id = await Wedding.find_one(Wedding.id == UUID(wedding_id))

            if wedding_by_id.status == WeddingStatus.PENDING:
                return PendingWeddingDto(
                    status=WeddingStatus.PENDING
                )
            elif wedding_by_id.status == WeddingStatus.ACCEPTED:
                return AcceptWeddingDto(
                    m_name=wedding_by_id.m_name,
                    m_surname=wedding_by_id.m_surname,
                    f_name=wedding_by_id.f_name,
                    f_surname=wedding_by_id.f_surname,
                    digital_signature=wedding_by_id.digital_signature,
                    status=WeddingStatus.ACCEPTED
                )
            elif wedding_by_id.status == WeddingStatus.DECLINED:
                return DeclineWeddingDto(
                    decline_message=wedding_by_id.decline_message,
                    status=WeddingStatus.DECLINED
                )
            else:
                raise ValueError(f"Status: {wedding_by_id.status} does not supported!")

        except Exception as e:
            raise ValueError(f"Error during getting wedding with id: {wedding_id}. Error msg: {str(e)}")

    @classmethod
    async def get_all_weddings(cls):
        try:
            return await Wedding.find_all().to_list()
        except Exception as e:
            raise ValueError(f"Error during getting all weddings. "
                             f"Error msg: {str(e)}")