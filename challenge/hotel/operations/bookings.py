from hotel.operations.interface import DataInterface
from hotel.operations.models import BookingCreateData, BookingResult, RoomAvailable, RoomResult
from datetime import datetime, date, timedelta


def read_all_bookings(booking_interface: DataInterface) -> list[BookingResult]:
    bookings = booking_interface.read_all()
    return [BookingResult(**b) for b in bookings]


def read_booking(booking_id: int, booking_interface: DataInterface) -> BookingResult:
    booking = booking_interface.read_by_id(booking_id)
    return BookingResult(**booking)


def create_booking(
    data: BookingCreateData,
    room_interface: DataInterface,
    booking_interface: DataInterface,
) -> BookingResult:
    # retrieve the room
    available_rooms = check_rooms_available(data.from_date, data.to_date, booking_interface, room_interface)
    room = available_rooms[0]

    days = (data.to_date - data.from_date).days
    if days <= 0:
        raise ValueError("Invalid dates")

    booking_dict = data.dict()
    booking_dict["room_id"] = room.id
    booking_dict["price"] = room.price * days

    booking = booking_interface.create(booking_dict)
    return BookingResult(**booking)


def delete_booking(booking_id: int, booking_interface: DataInterface) -> BookingResult:
    booking = booking_interface.delete(booking_id)
    return BookingResult(**booking)


def check_room_availability(
    room_id: int,
    date_required: str,
    booking_interface: DataInterface,
) -> bool:
    bookings = read_all_bookings(booking_interface)
    busy_dates = []
    for booking in bookings:
        if room_id != booking.room_id:
            continue
        busy_dates.extend(_get_date_range(booking.from_date, booking.to_date))

    return RoomAvailable(available=not date_required in busy_dates)


def check_rooms_available(
    start_date: date,
    end_date: date,
    booking_interface: DataInterface,
    room_interface: DataInterface,
) -> list[RoomResult]:
    available_rooms = []
    desired_dates = _get_date_range(start_date, end_date)
    bookings = read_all_bookings(booking_interface)
    booked_room_ids = list(set(booking.room_id for booking in bookings))
    rooms = [RoomResult(**r) for r in room_interface.read_all()]
    available_rooms.extend([room for room in rooms if room.id not in booked_room_ids])

    for booking in bookings:
        busy_dates = _get_date_range(booking.from_date, booking.to_date)
        if any([desired_date in busy_dates for desired_date in desired_dates]):
            continue
        available_rooms.append(RoomResult(**room_interface.read_by_id(booking.room_id)))

    return available_rooms



def _get_date_range(from_date: date, to_date: date) -> list[str]:
    delta = to_date - from_date
    return [(from_date + timedelta(days=i)).strftime("%Y-%m-%d") for i in range(delta.days + 1)]

