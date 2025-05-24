class Restaurant:
    def __init__(self, restaurant_name, cuisine_type, initial_rating=0):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.rating = initial_rating  #атрибут рейтинг

    def describe_restaurant(self):
        print(f"Ресторан: {self.restaurant_name}")
        print(f"Тип кухни: {self.cuisine_type}")
        print(f"Рейтинг: {self.rating}\n")

    def update_rating(self, new_rating):
        self.rating = new_rating
        print(f"Рейтинг ресторана '{self.restaurant_name}' обновлен: {self.rating}")


restaurant = Restaurant("Кимчи ту гоу", "корейская", 4.5)

restaurant.describe_restaurant()

restaurant.update_rating(4.8)
restaurant.describe_restaurant()