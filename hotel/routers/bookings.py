from datetime import date

from fastapi import APIRouter
from hotel.db.db_interface import DBInterface
from hotel.db.models import DBBooking, DBRoom
from hotel.operations.bookings import (
    create_booking,
    delete_booking,
    read_all_bookings,
    read_booking,
    check_rooms_available,
)
from hotel.operations.models import BookingCreateData, BookingResult, RoomResult

router = APIRouter()


@router.get("/bookings")
def api_read_all_bookings() -> list[BookingResult]:
    booking_interface = DBInterface(DBBooking)
    return read_all_bookings(booking_interface)


@router.get("/booking/{booking_id}")
def api_read_booking(booking_id: int) -> BookingResult:
    booking_interface = DBInterface(DBBooking)
    return read_booking(booking_id, booking_interface)


@router.post("/booking")
def api_create_booking(data: BookingCreateData):
    room_interface = DBInterface(DBRoom)
    booking_interface = DBInterface(DBBooking)
    return create_booking(data, room_interface, booking_interface)


@router.delete("/booking/{booking_id}")
def api_delete_booking(booking_id: int) -> BookingResult:
    booking_interface = DBInterface(DBBooking)
    return delete_booking(booking_id, booking_interface)

@router.get("/booking/availability/{start_date}/{end_date}")
def api_check_rooms_available(start_date: date, end_date: date) -> list[RoomResult]:
    booking_interface = DBInterface(DBBooking)
    room_interface = DBInterface(DBRoom)
    return check_rooms_available(start_date, end_date, booking_interface, room_interface)
