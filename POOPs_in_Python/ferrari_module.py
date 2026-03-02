class Ferrari:
    brand_name = "Ferrari"
    num_of_cars = 0
    def __init__(self, model, year, color, for_sale):
        self.model = model
        self.year = year
        self.color = color
        self.for_sale = for_sale
        Ferrari.num_of_cars += 1

    def drive(self):
        print(f"You drive the {self.color} color {self.brand_name} {self.model}")

    def repair(self):
        print(f"Your {self.color} color {self.brand_name} {self.model} need repair service.")

    def describe(self):
        print(f"You have a {self.brand_name} {self.model} of {self.color} made in {self.year} which is curently not for {self.for_sale}")


    @classmethod
    def total_collection(cls):
        return f"I have {cls.num_of_cars} {cls.brand_name} super cars."