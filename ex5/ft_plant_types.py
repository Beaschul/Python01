#!/usr/bin/python3

class Plant:
    def __init__(self, name: str, height: float, days: int) -> None:
        self._name: str = name
        self._height: float = height
        self._days: int = days

    def show(self) -> None:
        print(f"{self._name}: {self._height} cm, {self._days} days old")

    def set_height(self, height: float) -> None:
        if height < 0.0:
            print(f"{self._name}: Error, height can't be negative")
            print("Height update rejected")
        else:
            self._height = height
            print(f"Height updated: {self._height:.0f}cm")

    def get_height(self) -> float:
        return self._height

    def set_age(self, days: int) -> None:
        if days < 0:
            print(f"{self._name}: Error, age can't be negative")
            print("Age update rejected")
        else:
            self._days = days
            print(f"Age updated: {days} days")

    def get_age(self) -> int:
        return self._days

    def grow(self, days: int) -> None:
        if days > 0:
            self._height += days * 2.1
            self._days += days


class Flower(Plant):
    def __init__(
        self, name: str, height: float, days: int, color: str
                ) -> None:
        super().__init__(name, height, days)
        self._color = color
        self._bloomed = False

    def show(self) -> None:
        super().show()
        print(f"Color: {self._color}")
        if self._bloomed:
            print(f"{self._name} is blooming beautifully!")
        else:
            print(f"{self._name} has not bloomed yet")

    def bloom(self) -> None:
        print(f"[asking the {self._name.lower()} to bloom]")
        self._bloomed = True


class Tree(Plant):
    def __init__(
        self, name: str, height: float, days: int, trunk_diameter: float
                ) -> None:
        super().__init__(name, height, days)
        self._trunk_diameter = trunk_diameter

    def show(self) -> None:
        super().show()
        print(f"Trunk diameter: {self._trunk_diameter:.1f}cm")

    def produce_shade(self) -> None:
        print(f"[asking the {self._name.lower()} to produce shade]")
        shade_len = self._height
        shade_wid = self._trunk_diameter
        print(f"Tree {self._name} now produces a shade of "
              f"{shade_len:.1f}cm long and {shade_wid:.1f}cm wide.")


class Vegetable(Plant):
    def __init__(
        self, name: str, height: float, days: int, harvest_season: str
                ) -> None:
        super().__init__(name, height, days)
        self._harvest_season = harvest_season
        self._nutritional_value = 0

    def show(self) -> None:
        super().show()
        print(f"Harvest season: {self._harvest_season}")
        print(f"Nutritional value: {self._nutritional_value}")

    def grow(self, days: int) -> None:
        if days > 0:
            super().grow(days)
            self._nutritional_value += days * 0.1
            self._nutritional_value = round(self._nutritional_value)


def ft_plant_types() -> None:
    print("=== Garden Plant Types ===")

    print("=== Flower")
    rose = Flower("Rose", 15.0, 10, "red")
    rose.show()
    rose.bloom()
    rose.show()
    print()

    print("=== Tree")
    oak = Tree("Oak", 200.0, 365, 5.0)
    oak.show()
    oak.produce_shade()
    print()

    print("=== Vegetable")
    tomato = Vegetable("Tomato", 5.0, 10, "April")
    tomato.show()
    print("[make tomato grow and age for 20 days]")
    tomato.grow(20)
    tomato.show()


if __name__ == "__main__":
    ft_plant_types()
