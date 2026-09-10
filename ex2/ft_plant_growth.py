#!/usr/bin/python3

class Plant:
    def __init__(self, name: str, height: float, days: int) -> None:
        self.name: str = name
        self.height: float = height
        self.days: int = days

    def show(self):
        print(f"{self.name}: {self.height:.1f}cm, {self.days} days old")

    def grow(self, growth_amount: float):
        self.height += growth_amount

    def age(self):
        self.days += 1



def ft_plant_growth():
    print("=== Garden Plant Growth ===")
    rose = Plant("Rose", 25.0, 30)
    rose.show()
    total_growth = 0
    for day in range(1, 8):
        rose.grow(0.8)
        rose.age()
        print(f"=== Day {day} ===")
        rose.show()
        total_growth += 0.8
    print(f"Growth this week: {total_growth:.1f}cm")


if __name__ == "__main__":
    ft_plant_growth()
