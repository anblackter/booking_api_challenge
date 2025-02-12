from hotel.db.models import DBCustomer, DBRoom, DBAddress

addresses = [
    DBAddress(
        street="Clinton",
        city="New York",
        zip_code=11122
    ),
    DBAddress(
        street="Avenue",
        city="Nevada",
        zip_code=30213
    ),
    DBAddress(
        street="Move",
        city="Boston",
        zip_code=2020
    ),
    DBAddress(
        street="13th",
        city="Miami",
        zip_code=5050
    ),
    DBAddress(
        street="Carlton",
        city="New York",
        zip_code=11150
    )
]

customers = [
    DBCustomer(
        first_name="John",
        last_name="Smith",
        email_address="email@email.com",
        marketing_emails=True,
        address_id=1,
    ),
    DBCustomer(
        first_name="Jane",
        last_name="Doe",
        email_address="jane@hotmail.com",
        marketing_emails=True,
        address_id=2,
    ),
    DBCustomer(
        first_name="Jack",
        last_name="Black",
        email_address="jack@black.com",
        marketing_emails=False,
        address_id=3,
    ),
    DBCustomer(
        first_name="Jill",
        last_name="White",
        email_address="jill@gmail.com",
        marketing_emails=False,
        address_id=4,
    ),
    DBCustomer(
        first_name="Arjan",
        last_name="Codes",
        email_address="hi@arjancodes.com",
        marketing_emails=True,
        address_id=5,
    ),
]

rooms = [
    DBRoom(number="101", size=10, price=150_00, amenities=["TV", "Mirror"]),
    DBRoom(number="102", size=10, price=150_00, amenities=["TV", "Desktop"]),
    DBRoom(number="103", size=20, price=250_00, amenities=["Pet Friendly", "Beach View"]),
    DBRoom(number="104", size=20, price=250_00, amenities=["Wifi", "Drinks"]),
    DBRoom(number="105", size=30, price=350_00, amenities=["Air Conditioner", "Lock Box"]),
]
