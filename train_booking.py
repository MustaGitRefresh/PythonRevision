class Seat:
    def __init__(self, seat_number, is_booked=False):
        self.seat_number = seat_number
        self.is_booked = is_booked

    def __str__(self):
        return f"Seat Number: {self.seat_number}"

    def __repr__(self):
        return f"Seat(seat_number={self.seat_number}, is_booked={self.is_booked})"

    @property
    def is_booked(self):
        return self._is_booked

    @is_booked.setter
    def is_booked(self, value):
        if isinstance(value, bool):
            self._is_booked = value
        else:
            raise ValueError("is_booked must be a boolean value.")


class Train:
    def __init__(self, train_number, seats):
        self.train_number = train_number
        self.seats = seats

    def __str__(self):
        return f"Train Number: {self.train_number}"

    def __repr__(self):
        return f"Train(train_number={self.train_number}, seats={self.seats})"

    def book_seat(self, seat_number):
        for seat in self.seats:
            if seat.seat_number == seat_number:
                if seat.is_booked:
                    print(f"Seat {seat_number} is already booked.")
                else:
                    seat.is_booked = True
                    print(f"Seat {seat_number} booked successfully.")
                return
        print(f"Invalid seat number {seat_number}.")


class BookingApp:
    def __init__(self, trains):
        self.trains = trains

    def __str__(self):
        return "Railway Seat Booking App"

    def __repr__(self):
        return "BookingApp(trains={})".format(self.trains)

    def display_available_seats(self):
        for train in self.trains:
            print(f"{train}:")
            available_seats = [seat for seat in train.seats if not seat.is_booked]
            if available_seats:
                for seat in available_seats:
                    print(seat)
            else:
                print("No available seats.")

# Usage Example
seat1 = Seat("A1")
seat2 = Seat("A2")
seat3 = Seat("A3", is_booked=True)

train1 = Train("T123", [seat1, seat2, seat3])
train2 = Train("T456", [Seat("B1"), Seat("B2")])

booking_app = BookingApp([train1, train2])
booking_app.display_available_seats()
print()

train1.book_seat("A1")
booking_app.display_available_seats()
print()

train1.book_seat("A1")
train1.book_seat("A2")
train1.book_seat("A3")
booking_app.display_available_seats()
