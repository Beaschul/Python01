#!/usr/bin/python3

class Plant:
    def __init__(self, name: str, height: float, days: int) -> None:
        self.name: str = name
        self.height: float = height
        self.days: int = days

    def show(self):
        print(
            f"Created: {self.name}: {self.height:.1f}cm, " +
            f"{self.days} days old"
        )

    def grow(self, growth_amount: float):
        self.height += growth_amount

    def age(self):
        self.days += 1


def ft_plant_factory() -> None:
    print("=== Plant Factory Output ===")
    rose = Plant("Rose", 25.0, 30)
    rose.show()
    oak = Plant("Oak", 200.0, 365)
    oak.show()
    cactus = Plant("Cactus", 5.0, 90)
    cactus.show()
    sunflower = Plant("Sunflower", 80.0, 45)
    sunflower.show()
    fern = Plant("Fern", 15.0, 120)
    fern.show()


if __name__ == "__main__":
    ft_plant_factory()
