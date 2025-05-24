class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"Ресторан: {self.restaurant_name}")
        print(f"Тип кухни: {self.cuisine_type}\n")


restaurant1 = Restaurant("Токио Сити", "японская")
restaurant2 = Restaurant("Теремок", "русская")
restaurant3 = Restaurant("боне капоне", "итальянская")

restaurant1.describe_restaurant()
restaurant2.describe_restaurant()
restaurant3.describe_restaurant()