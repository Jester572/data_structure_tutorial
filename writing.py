class Queue:
    
    def __init__(self):
        self.queue = []
        
    def add_queue(self, value):
        self.queue.append(value)

    def exit_queue(self):
        print("Removed " + self.queue.pop(0) + " from queue")
        
    def is_empty(self):
        if self.queue == 0:
            return True
        
class main:
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
    
    