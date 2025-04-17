class Tea:
    def __init__(self, bev_type, temperature, steeping_time):
        self.type = bev_type
        self.temperature = temperature
        self.steeping_time = steeping_time
    
    def info(self):
        print(f"This is the brewing information for {self.type}. {self.type} is best brewed at {self.temperature}. The ideal steeping time is {self.steeping_time} minutes.")

    def serving_recommendation(self):
        print("Tea is best served with honey as sweetener.")

class Coffee:
    def __init__(self, bev_type, temperature, steeping_time):
        self.type = bev_type
        self.temperature = temperature
        self.steeping_time = steeping_time
    
    def info(self):
        print(f"This is the brewing information for {self.type}. {self.type} is best brewed at {self.temperature}. The ideal steeping time is {self.steeping_time} minutes.")

    def serving_recommendation(self):
        print("Coffee is best served with sugar and milk.")

Tea = Tea("Green tea", 70, 2)
Coffee = Coffee("French press coffee", 90, 3)

for beverage in (Tea, Coffee):
    beverage.info()
    beverage.serving_recommendation()