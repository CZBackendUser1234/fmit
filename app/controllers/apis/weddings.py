from fastapi import APIRouter, Depends, Path

from app.dtos.weddings.create_wedding_dto import CreateWeddingDto
from app.models.schemas.wedding import Wedding
from app.services.wedding_service import WeddingService
from app.utils.constants import UUID_REGEX_PATTERN

router = APIRouter()


@router.post(path='/create', description="Create a new wedding.", response_model=str)
async def create_wedding(
        create_wedding_dto: CreateWeddingDto,
        wedding_service: WeddingService = Depends()
):
    try:
        return await wedding_service.create_wedding(create_wedding_dto)
    except Exception as e:
        raise ValueError(f"Error during creating wedding for male with name: {create_wedding_dto.m_name} "
                         f"and female with name: {create_wedding_dto.f_name}. Error msg: {str(e)}")


@router.get(path="/wedding/{wedding_id}", description="Get the wedding by id.")
async def get_wedding_by_id(
        wedding_id: str = Path(
            description="ID of the wedding",
            examples=[
                "123e4567-e89b-12d3-a456-426655440000",
                "c73bcdcc-2669-4bf6-81d3-e4ae73fb11fd",
                "C73BCDCC-2669-4Bf6-81d3-E4AE73FB11FD"
            ],
            pattern=UUID_REGEX_PATTERN
        ),
        wedding_service: WeddingService = Depends()
):
    try:
        return await wedding_service.get_wedding_by_id(wedding_id)
    except Exception as e:
        raise ValueError(f"Error during get wedding by id: {wedding_id}. "
                         f"Error msg: {str(e)}")


@router.get(path="/weddings", description="Get all weddings.", response_model=list[Wedding])
async def get_all_weddings(
        wedding_service: WeddingService = Depends()
):
    try:
        return await wedding_service.get_all_weddings()
    except Exception as e:
        raise ValueError(f"Error during getting all weddings. "
                         f"Error msg: {str(e)}")
