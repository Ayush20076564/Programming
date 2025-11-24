
class Booking:
    def __init__(self, staff: int, customer: int, day: int, start: int, end: int, branch):
        
        # Validate day
        if not (1 <= day <= 5):
            raise ValueError("Day must be between 1 and 5 (Mon–Fri).")

        # Validate time range
        if not (9 <= start < end <= 17):
            raise ValueError("Meeting must be between 09:00 and 17:00.")

        # Validate duration
        if end - start < 1:
            raise ValueError("Meeting must last at least one hour.")

        self.staff = staff
        self.customer = customer
        self.day = day
        self.start = start
        self.end = end
        self.branch = branch

    def timeslots(self):
        """Return a list of (day, hour) that this meeting occupies."""
        return [(self.day, h) for h in range(self.start, self.end)]

    def __repr__(self):
        return f"<Booking staff={self.staff}, cust={self.customer}, day={self.day}, {self.start}-{self.end}>"


class Employee:
    allEmployees = []   # class-level list

    def __init__(self, id: int, name: str):
        self.id = id
        self.name = name

        # schedule[(day, hour)] = Booking or None
        self.schedule = {}
        for d in range(1, 6):      # Mon–Fri
            for h in range(9, 17):  # 9 to 16 (meeting ends by 17)
                self.schedule[(d, h)] = None

        Employee.allEmployees.append(self)


    def is_free(self, booking: Booking):
        for slot in booking.timeslots():
            if self.schedule[slot] is not None:
                return False
        return True

  
    def has_buffer_for_cross_branch(self, booking: Booking, home_branch):
        # If booking is in home branch → no buffer needed
        if booking.branch == home_branch:
            return True

        day = booking.day
        start = booking.start
        end = booking.end

        # must have 1 hour before
        if start > 9 and self.schedule[(day, start - 1)] is not None:
            return False

        # must have 1 hour after
        if end < 17 and self.schedule[(day, end)] is not None:
            return False

        return True

    def addBooking(self, booking: Booking, home_branch):
        # check free
        if not self.is_free(booking):
            return False

        # check buffer rule
        if not self.has_buffer_for_cross_branch(booking, home_branch):
            return False

        # add booking to schedule
        for slot in booking.timeslots():
            self.schedule[slot] = booking

        return True

    def __repr__(self):
        return f"<Employee {self.id}, {self.name}>"


class Branch:
    def __init__(self, address: str, numBooths: int):
        self.address = address
        self.employees = []
        # booths = {1:[],2:[],3:[]}
        self.booths = {b: [] for b in range(1, numBooths + 1)}

    def addEmployee(self, emp: Employee):
        self.employees.append(emp)


    def booth_free(self, booth_id, booking: Booking):
        for b in self.booths[booth_id]:
            if b.day == booking.day:
                # check time overlap
                if not (booking.end <= b.start or booking.start >= b.end):
                    return False
        return True

  
    def addBooking(self, booking: Booking):
        if booking.branch != self:
            raise ValueError("Booking branch mismatch.")

        # find employee
        emp = None
        for e in self.employees:
            if e.id == booking.staff:
                emp = e
                break

        if emp is None:
            raise ValueError("Employee not assigned to this branch.")

        # try add to employee schedule
        if not emp.addBooking(booking, home_branch=self):
            return False

        # assign booth
        for booth_id in self.booths:
            if self.booth_free(booth_id, booking):
                self.booths[booth_id].append(booking)
                return True

        # revert employee schedule if booth fail
        for slot in booking.timeslots():
            emp.schedule[slot] = None

        return False

    def __repr__(self):
        return f"<Branch {self.address}>"


#                  SAMPLE DATA + TESTS


print("\n==== Creating Branches ====")
dublin_main = Branch("Dublin City Centre", 3)
dublin_north = Branch("Dublin North", 2)

print(dublin_main)
print(dublin_north)

print("\n==== Creating Employees ====")
alice = Employee(1, "Alice")
bob = Employee(2, "Bob")
charlie = Employee(3, "Charlie")

print(alice)
print(bob)
print(charlie)

print("\n==== Assign Employees to Branches ====")
dublin_main.addEmployee(alice)
dublin_main.addEmployee(bob)
dublin_north.addEmployee(charlie)

print("Main branch employees:", dublin_main.employees)
print("North branch employees:", dublin_north.employees)


print("\n==== TEST 1: Valid Booking ====")
bk1 = Booking(1, 101, day=2, start=10, end=12, branch=dublin_main)
print("Booking 1 added:", dublin_main.addBooking(bk1))

print("\n==== TEST 2: Employee Time Conflict ====")
bk2 = Booking(1, 102, day=2, start=11, end=13, branch=dublin_main)
print("Booking 2 added:", dublin_main.addBooking(bk2))  # Should be False

print("\n==== TEST 3: Another Employee Valid ====")
bk3 = Booking(2, 103, day=2, start=11, end=12, branch=dublin_main)
print("Booking 3 added:", dublin_main.addBooking(bk3))  # True

print("\n==== TEST 4: Invalid Day ====")
try:
    Booking(1, 201, 6, 10, 11, dublin_main)
except ValueError as e:
    print("Error:", e)

print("\n==== TEST 5: Invalid Time ====")
try:
    Booking(1, 202, 2, 8, 10, dublin_main)
except ValueError as e:
    print("Error:", e)

# print("\n==== TEST 6: Cross-Branch Booking without buffer (should fail) ====")
# bk4 = Booking(1, 301, day=3, start=12, end=13, branch=dublin_north)
# print("Booking 4 added:", dublin_north.addBooking(bk4))

print("\n==== TEST 7: Valid Booking for North Branch Employee ====")
bk5 = Booking(3, 401, day=1, start=10, end=11, branch=dublin_north)
print("Booking 5 added:", dublin_north.addBooking(bk5))

print("\n==== FINAL BOOTH SCHEDULES ====")
print("Main branch booths:", dublin_main.booths)
print("North branch booths:", dublin_north.booths)

print("\n==== EMPLOYEE SCHEDULES CHECK ====")
print("Alice schedule:", {k:v for k,v in alice.schedule.items() if v})
print("Bob schedule:",   {k:v for k,v in bob.schedule.items() if v})
print("Charlie schedule:",{k:v for k,v in charlie.schedule.items() if v})
