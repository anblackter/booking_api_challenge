# Installing and running the hotel reservation API example

To make running the case study easy, you can install poetry to handle the dependencies. You can install poetry by running:

```bash
pip install poetry
```

Then, you can install the dependencies by running:

```bash
poetry install
```

To start the API server, run the following command:

```bash
poetry run uvicorn main:app --reload
```

# Challenge
Below you find a few challenges to further build on the hotel room booking case study. Feel free to post your solution in the student community on Discord. Good luck!

## More fields
Currently, customers, rooms and bookings are relatively simple objects. Add a few fields to them and verify that you can read and update them via the API. Here are a few examples of fields you could add:

- Customer address information
- A boolean indicating whether a customer wants to receive marketing emails
- A list of amenities (represented by string values) in a room
- A boolean indicating whether a booking can be cancelled or not 

## Check room availability
Create an API endpoint for checking whether a room is available. The endpoint should receive a room id and a date and that returns whether the room with the id is available at that date. Extend the various layers in the application as needed to achieve this.

## Check room availability (advanced)
Create an API endpoint that retrieves the rooms that are available within a given date range. The endpoint should receive a start date and end date and then return a list of rooms that are available within the date range. Only include rooms that are fully available within the date range.

## Check availability when booking a room (advanced)
When a customer books a room, extend the operation to validate whether the room is actually available. If you want to go all in here, you can even change the create_booking endpoint to not receive a room number, but simply pick the first available room depending on availability.