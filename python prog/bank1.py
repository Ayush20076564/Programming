class Booking:
    def __init__(self, staff:int, customer:int, day:int, start:int, end:int, branch):
        if not (1 <= day <= 5):
            raise ValueError("Day must be between 1 (Mon) and 5 (Fri)")
        if not (9 <= start < end <= 17):
            raise ValueError("Meetings must be between 09:00 and 17:00.")
        if not (end - start >= 1):
            raise ValueError("Meeting must be at least 1 hour long.")
        self.staff = staff
        self.customer = customer
        self.day = day
        self.start = start
        self.end = end
        self.branch = branch

    def timeslots(self):
        return [(self.day, hour) for hour in range(self.start, self.end)]

    def __repr__(self):
        return f"<Booking staff={self.staff} customer={self.customer} day={self.day} {self.start}-{self.end}>"


class Employee:
    allEmployees = []

    def __init__(self, id:int, name:str):
        self.id = id
        self.name = name
        self.schedule = {}
        for d in range(1, 6):
            for h in range(9, 17):
                self.schedule[(d, h)] = None
        Employee.allEmployees.append(self)

    def is_free(self, booking: Booking):
        for slot in booking.timeslots():
            if self.schedule[slot] is not None:
                return False
        return True

    def has_buffer_for_cross_branch(self, booking: Booking, employee_home_branch):
        if booking.branch == employee_home_branch:
            return True
        day = booking.day
        start = booking.start
        end = booking.end
        if start > 9 and self.schedule[(day, start - 1)] is not None:
            return False
        if end < 17 and self.schedule[(day, end)] is not None:
            return False
        return True

    def addBooking(self, booking: Booking, employee_home_branch):
        if not self.is_free(booking):
            raise ValueError("Employee is not free for this booking.")
        if not self.has_buffer_for_cross_branch(booking, employee_home_branch):
            raise ValueError("Cross-branch booking violates buffer rule.")
        for slot in booking.timeslots():
            self.schedule[slot] = booking
        return True

    def __repr__(self):
        return f"<Employee id={self.id} name={self.name}>"


class Branch:
    def __init__(self, address:str, numBooths:int):
        self.address = address
        self.employees = []
        self.booths = {b: [] for b in range(1, numBooths + 1)}

    def add_employee(self, employee:Employee):
        self.employees.append(employee)

    def booth_free(self, booth_id:int, booking:Booking):
        for b in self.booths[booth_id]:
            if b.day == booking.day:
                if not (booking.end <= b.start or booking.start >= b.end):
                    return False
        return True

    def addBooking(self, booking:Booking):
        if booking.branch != self:
            raise ValueError("Booking branch mismatch.")
        emp = None
        for e in self.employees:
            if e.id == booking.staff:
                emp = e
                break
        if emp is None:
            raise ValueError("Employee not assigned to this branch.")
        emp.addBooking(booking, employee_home_branch=self)
        for booth_id in self.booths:
            if self.booth_free(booth_id, booking):
                self.booths[booth_id].append(booking)
                return True
        for slot in booking.timeslots():
            emp.schedule[slot] = None
        return False

    def __repr__(self):
        return f"<Branch address={self.address}>"


print("\n==== Creating Branches ====")
dublin_main = Branch("Dublin City Centre", 2)
dublin_north = Branch("Dublin North", 2)

print("\n==== Creating Employees ====")
emp1 = Employee(101, "Alice")
emp2 = Employee(102, "Bob")
emp3 = Employee(201, "Charlie")

dublin_main.add_employee(emp1)
dublin_main.add_employee(emp2)
dublin_north.add_employee(emp3)

print("\n==== TEST 1: Valid Booking ====")
bk1 = Booking(101, 301, day=2, start=10, end=11, branch=dublin_main)
print("Booking 1 added:", dublin_main.addBooking(bk1))

print("\n==== TEST 2: Employee Time Conflict ====")
bk2 = Booking(101, 302, day=2, start=10, end=11, branch=dublin_main)
try:
    print("Booking 2 added:", dublin_main.addBooking(bk2))
except ValueError as e:
    print("Error:", e)

print("\n==== TEST 3: Cross-Branch OK ====")
bk3 = Booking(101, 303, day=2, start=13, end=14, branch=dublin_north)
try:
    print("Booking 3 added:", dublin_north.addBooking(bk3))
except ValueError as e:
    print("Error:", e)

print("\n==== TEST 4: Cross-Branch FAIL ====")
bk4 = Booking(101, 304, day=2, start=11, end=12, branch=dublin_north)
try:
    print("Booking 4 added:", dublin_north.addBooking(bk4))
except ValueError as e:
    print("Error:", e)

print("\n==== TEST 5: Employee not in Branch ====")
bk5 = Booking(999, 305, day=3, start=10, end=11, branch=dublin_main)
try:
    print("Booking 5 added:", dublin_main.addBooking(bk5))
except ValueError as e:
    print("Error:", e)

print("\n==== TEST 6: Invalid Day ====")
try:
    bk6 = Booking(101, 306, day=6, start=10, end=11, branch=dublin_main)
except ValueError as e:
    print("Error:", e)

print("\n==== TEST 7: Valid Booking North Branch ====")
bk7 = Booking(201, 307, day=1, start=10, end=11, branch=dublin_north)
print("Booking 7 added:", dublin_north.addBooking(bk7))

print("\n===== FINAL BOOTHS =====")
print("Main:", dublin_main.booths)
print("North:", dublin_north.booths)
