class Queue:
    
    def __init__(self):
        self.queue = []
        
    def add_queue(self, value):
        self.queue.append(value)

    def exit_queue(self):
        value = self.queue[0]
        del self.queue[0]
        return value
    
    def is_empty(self):
        if self.queue == 0:
            return True
        
class DriveThrough:
    # Creates queue
    drive_through = Queue()
    
    drive_through.add_queue("Car 1")
    drive_through.add_queue("Car 2")
    drive_through.add_queue("Car 3")
    drive_through.exit_queue()
    drive_through.add_queue("Car 4")
    # Print queue
    
    print("\nRemaining cars in queue")
    for i in drive_through.queue:
        print(i)
    
    
class CircularQueue:
    
    class Kid:
        
        def __init__(self, name, turns):
            self.name = name
            self.turns = turns
    
    def __init__(self):
        self.kids = Queue()
        
    def add_kid(self, name, turns):
        
        kid = CircularQueue.Kid(name,turns)
        self.kids.add_queue(kid)

    def slide_down(self):
        if self.kids.is_empty():
            print("nobody is in line")
        else:
            kid = self.kids.exit_queue()
            
            if kid.turns > 0:
                kid.turns -= 1
                self.kids.add_queue(kid)
                print(kid.name + " went to back of the line")
        
class Slide:
    line = CircularQueue()
    line.add_kid("joe",5)
    line.add_kid("suzan",3)
    line.add_kid("james",4)
    line.slide_down()
    line.slide_down()
    line.slide_down()
    line.slide_down()
    for i in line.kids.queue:
        print(f"Turns left: {i.name}-{i.turns}" )
        
        
class Johnsons:
    
    class cars:
        def __init__(self, liscence, priority):
            self.liscence = liscence
            self.priority = priority
            
    def __init__(self):
        self.cars_line = Queue()
        
    def add_car(self, liscence, priority):
        car = Johnsons.cars(liscence,priority)
        self.cars_line.add_queue(car)
        
    def washed(self):
        # checks to make sure the queue is not empty
        if len(self.cars_line.queue) == 0:  
            print("The queue is empty.")
            return None
        # Finds the index of the item with the highest priority to remove
        high_pri_index = 0
        for index in range(0, len(self.cars_line.queue)):
            if self.cars_line.queue[index].priority > self.cars_line.queue[high_pri_index].priority:
                high_pri_index = index
        # Removes and return the item with the highest priority
        value = self.cars_line.queue[high_pri_index].liscence
        del self.cars_line.queue[high_pri_index]
        print(value)
        return value
    
print("Test 1")
carWashQueue = Johnsons()
print("\nWashed order\n")
carWashQueue.add_car("Car1",1)
carWashQueue.add_car("Car2",0)
carWashQueue.add_car("Car3",0)
carWashQueue.add_car("Car4",1)
carWashQueue.add_car("Car5",0)
carWashQueue.add_car("Car6",0)

while len(carWashQueue.cars_line.queue) > 0:
    carWashQueue.washed()