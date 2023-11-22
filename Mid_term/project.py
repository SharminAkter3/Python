class Star_Cinema:
    __hall_list = []

    @classmethod
    def entry_hall(cls, hall):
        cls.__hall_list.append(hall)


class Hall(Star_Cinema):
    def __init__(self, rows, cols, hall_no) -> None:
        self.__seats = {}
        self.__show_list = []
        self.__rows = rows
        self.__cols = cols
        self.__hall_no = hall_no
        self.entry_hall(self)

    def entry_show(self, id, movie_name, time):
        show_all = (id, movie_name, time)
        self.__show_list.append(show_all)
        seats = [[0 for _ in range(self.__cols)] for _ in range(self.__rows)]
        self.__seats[id] = seats

    def book_seats(self, id, seats_book):
        if id in self.__seats:
            for row, col in seats_book:
                booking_seat = self.__seats[id]
                if 0 <= row < self.__rows and 0 <= col < self.__cols:
                    if booking_seat[row][col] == 0:
                        booking_seat[row][col] = 1
                        print("Seats booked successfully!")
                    else:
                        print(f"Seat ({row}, {col}) is already booked.")
                else:
                    print(f"Invalid seat: ({row}, {col})")
                    return
        else:
            print(f"Invalid show ID: {id}")

    def view_show_list(self):
        for id, movie_name, time in self.__show_list:
            print(f"SHOW ID: {id}, MOVIE NAME: {movie_name}, TIME: {time}")

    def view_available_seats(self, id):
        if id in self.__seats:
            print(f"AVAILABLE SEATS FOR SHOW : {id}")
            seats = self.__seats[id]
            for i in range(self.__rows):
                for j in range(self.__cols):
                    if seats[i][j] == 0:
                        print(f"SEAT: {i}, {j}")
            print("\nUpdate Seats matrix:")
            for i in range(self.__rows):
                for j in range(self.__cols):
                    print(seats[i][j], end=" ")
                print()
        else:
            print(f"SHOW WITH ID {id} NOT FOUND.")


first_View = Hall(7, 7, 111)
first_View.entry_show(id="101", movie_name="TAQDEER", time="06/10/2023  2.00PM")
first_View.entry_show(id="303", movie_name="ACTION", time="07/10/2023  1.00PM")

while True:
    print("\n OPTION: \n")
    print("-----------------------------------")
    print("1. VIEW ALL SHOW TODAY")
    print("2. VIEW AVAILABLE SEATS")
    print("3. BOOK TICKET")
    print("4. EXIT")
    print("------------------------------------")

    option = int(input("ENTER OPTION : "))
    if option == 1:
        first_View.view_show_list()

    elif option == 2:
        show_id = input("ENTER SHOW ID: ")
        first_View.view_available_seats(show_id)

    elif option == 3:
        show_id = input("ENTER SHOW ID: ")
        number_of_ticket = input("Number of Tickets: ")
        seats_to_book = [
            (int(input("ENTER SEAT ROW : ")), int(input("ENTER SEAT COLUMN : ")))
            for _ in range(int(number_of_ticket))
        ]
        first_View.book_seats(id=show_id, seats_book=seats_to_book)
        # print("Seats booked successfully!")

    elif option == 4:
        break
    else:
        print("Invalid option.")
        break
