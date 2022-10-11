class Food:

    caloric_limit = int(input("Enter Your Daily Caloric Target: "))
    food_name = input("Name of meal: ")
    food_calories = float(input("Number of calories: "))
    food_servings = input("Serving size: ")
    food_serving_amount = float(input("Number of servings: "))

    def __init__(
        self,
        meal_name: str,
        caloric_value: int,
        serving_size: int,
        number_of_servings: int,
    ) -> None:
        self.meal_name = meal_name
        self.caloric_value = caloric_value
        self.serving_size = serving_size
        self.number_of_servings = number_of_servings

    def addMeal(self):
        self.caloric_limit -= self.caloric_value
        print(self.caloric_limit)
