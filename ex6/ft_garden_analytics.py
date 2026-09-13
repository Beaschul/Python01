#!/usr/bin/env python3

class Plant:
    class _Stats:
        def __init__(self) -> None:
            self._grow_calls: int = 0
            self._age_calls: int = 0
            self._show_calls: int = 0

        def increment_grow(self) -> None:
            self._grow_calls += 1

        def increment_age(self) -> None:
            self._age_calls += 1

        def increment_show(self) -> None:
            self._show_calls += 1

        def display(self) -> str:
            return (f"Stats: {self._grow_calls} grow, "
                    f"{self._age_calls} age, {self._show_calls} show")

    def __init__(self, name: str, height: float, age: int,
                 growth_rate: float = 0.8) -> None:
        self._name: str = name
        self._height: float = height
        self._age: int = age
        self._growth_rate: float = growth_rate
        self._stats: Plant._Stats = Plant._Stats()

    def get_name(self) -> str:
        return self._name

    def get_height(self) -> float:
        return self._height

    def get_age(self) -> int:
        return self._age

    def set_height(self, height: float) -> None:
        if height < 0:
            print(f"{self._name}: Error, height can't be negative")
        else:
            self._height = height

    def set_age(self, age: int) -> None:
        if age < 0:
            print(f"{self._name}: Error, age can't be negative")
        else:
            self._age = age

    def grow(self) -> None:
        self._stats.increment_grow()
        self._height = round(self._height + self._growth_rate, 1)

    def age(self) -> None:
        self._stats.increment_age()
        self._age += 1

    def show(self) -> None:
        self._stats.increment_show()
        print(f"{self._name}: {self._height}cm, {self._age} days old")

    @staticmethod
    def check_age(age: int) -> bool:
        return age > 365

    @classmethod
    def anonymous(cls) -> "Plant":
        return cls("Unknown plant", 0.0, 0)


class Flower(Plant):
    def __init__(self, name: str, height: float, age: int,
                 color: str, growth_rate: float = 8.0) -> None:
        super().__init__(name, height, age, growth_rate)
        self._color: str = color
        self._bloomed: bool = False

    def bloom(self) -> None:
        self._bloomed = True

    def show(self) -> None:
        super().show()
        print(f"Color: {self._color}")
        if self._bloomed:
            print(f"{self._name} is blooming beautifully!")
        else:
            print(f"{self._name} has not bloomed yet")


class Tree(Plant):
    def __init__(self, name: str, height: float, age: int,
                trunk_diameter: float, growth_rate: float = 0.5) -> None:
        super().__init__(name, height, age, growth_rate)
        self._trunk_diameter: float = trunk_diameter
        self._shade_calls: int = 0

    def produce_shade(self) -> None:
        self._shade_calls += 1
        print(f"Tree {self._name} now produces a shade of "
              f"{self._height}cm long and {self._trunk_diameter}cm wide.")

    def show(self) -> None:
        super().show()
        print(f"Trunk diameter: {self._trunk_diameter}cm")

    def show_shades(self) -> None:
        print(f"{self._shade_calls} shade")
         


class Vegetable(Plant):
    def __init__(self, name: str, height: float, age: int,
                 harvest_season: str, growth_rate: float = 2.1) -> None:
        super().__init__(name, height, age, growth_rate)
        self._harvest_season: str = harvest_season
        self._nutritional_value: int = 0

    def grow(self) -> None:
        super().grow()
        self._nutritional_value += 1

    def age(self) -> None:
        super().age()
        self._nutritional_value += 1

    def show(self) -> None:
        super().show()
        print(f"Harvest season: {self._harvest_season}")
        print(f"Nutritional value: {self._nutritional_value}")


class Seed(Flower):
    def __init__(self, name: str, height: float, age: int,
                 color: str, growth_rate: float = 30.0) -> None:
        super().__init__(name, height, age, color, growth_rate)
        self._seeds: int = 0

    def bloom(self) -> None:
        super().bloom()
        self._seeds = 42

    def show(self) -> None:
        super().show()
        print(f"Seeds: {self._seeds}")


def show_statistics(plant: Plant) -> None:
    print(f"\n[statistics for {plant.get_name()}]")
    print(plant._stats.display())


if __name__ == "__main__":
    print("=== Garden statistics ===")
    print("=== Check year-old")
    print(f"Is 30 days more than a year? -> {Plant.check_age(30)}")
    print(f"Is 400 days more than a year? -> {Plant.check_age(400)}")

    print("\n=== Flower")
    rose = Flower("Rose", 15.0, 10, "red")
    rose.show()
    show_statistics(rose)

    print("\n[asking the rose to grow and bloom]")
    rose.grow()
    rose.bloom()
    rose.show()
    show_statistics(rose)

    print("\n=== Tree")
    oak = Tree("Oak", 200.0, 365, 5.0)
    oak.show()
    show_statistics(oak)
    oak.show_shades()

    print("\n[asking the oak to produce shade]")
    oak.produce_shade()
    show_statistics(oak)
    oak.show_shades()

    print("\n=== Seed")
    sunflower = Seed("Sunflower", 80.0, 45, "yellow")
    sunflower.show()
    show_statistics(sunflower)

    print("\n[make sunflower grow, age and bloom]")
    sunflower.grow()
    sunflower.age()
    sunflower.bloom()
    sunflower.show()
    show_statistics(sunflower)

    print("\n=== Anonymous")
    unknown = Plant.anonymous()
    unknown.show()
    show_statistics(unknown)