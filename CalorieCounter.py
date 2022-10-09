class Calories:

    caloric_limit = int(input("Enter Your Daily Caloric Target: "))
    name = input("Name: ")
    calories = float(input("Number of calories: "))
    servings = input("Serving size: ")
    serving_amount = float(input("Number of servings: "))

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
