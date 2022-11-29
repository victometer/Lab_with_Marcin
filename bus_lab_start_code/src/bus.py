class Bus:
    def __init__(self, route_num, dest):
        self.route_number = route_num
        self.destination = dest
        self.passengers = []

    def drive (self):
        return 'Brum brum'
    
    def passenger_count (self):
        return len(self.passengers)

    def pick_up (self, person):
        self.passengers.append(person)

    def drop_off (self, person):
        self.passengers.remove(person)

    def empty (self):
        self.passengers.clear()

    def pick_up_from_stop (self, bus_stop):
        for person in bus_stop.queue:
            self.passengers.append(person)
        bus_stop.clear()
        
    


