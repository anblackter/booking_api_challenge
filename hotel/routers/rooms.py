from fastapi import APIRouter
from hotel.db.db_interface import DBInterface
from hotel.db.models import DBBooking
from hotel.operations.models import RoomResult, RoomAvailable
from hotel.operations.rooms import read_all_rooms, read_room
from hotel.operations.bookings import check_room_availability

router = APIRouter()


@router.get("/rooms")
def api_read_all_rooms() -> list[RoomResult]:
    return read_all_rooms()


@router.get("/room/{room_id}")
def api_read_room(room_id: int) -> RoomResult:
    return read_room(room_id)

@router.get("/room/availability/{room_id}/{date_required}")
def api_check_room_availability(room_id: int, date_required: str) -> RoomAvailable:
    booking_interface = DBInterface(DBBooking)
    return check_room_availability(room_id, date_required, booking_interface)