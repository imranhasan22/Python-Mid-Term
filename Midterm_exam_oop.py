class Star_Cinema:
    hall_list = []

    def entry_hall(self, hall_obj):
        self.hall_list.append(hall_obj)

class Hall:
    def __init__(self, rows, cols, hall_no):
        self._seats = {}
        self._show_list = []
        self.rows = rows
        self.cols = cols
        self.hall_no = hall_no
        

    def entry_show(self, id, movie_name, time):
        show_info = (id, movie_name, time)
        self._show_list.append(show_info)
        self._seats[id] = [[0]*self.cols for _ in range(self.rows)]

    def book_seats(self, show_id, row, col):
        valid_id = False
        for xd in self._show_list:
            if xd[0] == show_id:
                valid_id = True
                break

        if not valid_id:
            print( "Invalid Id: please select option 1 to view available Movie id: ")
            return
        if not (0 <= row < self.rows and 0 <= col < self.cols):
            print('Invalid Information. plz check your row/col')
            return
        show_seats = self._seats.get(show_id)
        if show_seats[row][col] == 1:
            print(f'Seat row ={row+1} & col ={col+1}) is booked already! Try another')
        else:
            show_seats[row][col] = 1
            print('wow!seat booked successfully.')

    def view_show_list(self):
        print("Available Shows :\n")
        print('Show ID :' +'  '+'show  Name :' +'   '+'Time')
        print('________|______________|___________')
        for show in self._show_list:
            print("ID:", show[0], "| Movie:", show[1], "| Time:", show[2])

    def view_available_seats(self, id):
        if id not in self._seats:
            print("Invalid show ID.")
            return
        print(f"Available seats for this id : {id}")
        for row in self._seats[id]:
           print("{" + " ".join(["O" if i == 0 else "1" for i in row]) + "}")



hall = Hall(rows=10, cols=10, hall_no=1)
hall.entry_show(258, "Theri", "7:00 PM")
hall.entry_show(776, "pori ", "9:00 AM")
hall.entry_show(101, "Jawan", "2:00 PM")
hall.entry_show(290, "KGF2 ", "4:00 PM")
cinema = Star_Cinema()
cinema.entry_hall(hall)


while True:
        print(f'\nMenu :')
        print("1. View show list")
        print("2. View available seats")
        print("3. Book seats")
        print("4. Exit")

        option = int(input("Enter option: "))

        if option == 1:
            hall.view_show_list()

        elif option == 2:
            show_id =int(input('Enter your movie id : ')) 
            hall.view_available_seats(show_id)
            
        elif option == 3:
            show_id=int(input('Write Movie ID : '))
            ticket = int(input('how many tickets do you want to buy : '))
            for _ in range(ticket):
                row=int(input('Enter row\'s number :\n'))
                col=int(input('Enter col\'s number :\n'))
                row=row-1
                col=col-1
                hall.book_seats(show_id,row,col)
            
        elif option == 4:
            print("Exit The Show!")
            break
        else:
            print("Invalid option.Try Again")