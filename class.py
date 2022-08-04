class Car(object):
    def __init__(self,model, color, company, speed_limit):
        self.color = color
        self.model = model
        self.company = company
        self.speed_limit = speed_limit
    
    def start(self):
        print("car started")
    
    def stop(self):
        print("car stopped")
    
    def accelerating(self):
        print("accelerating...")
    
    def change_gear(self, gear_type):
        print("Gear Changed")

Koenigsegg = Car("Agera","red","Koenigsegg",250)
print(Koenigsegg.start())
print(Koenigsegg.accelerating())
print(Koenigsegg.stop())
print(Koenigsegg.color)