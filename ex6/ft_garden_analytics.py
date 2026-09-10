#!/usr/bin/python3

class Plant:
    class Stats:
        def __init__(self) -> None:
            self._grow_calls = 0
            self._age_calls = 0
            self._show_calls = 0

        def increment_grow(self) -> None:
            self._grow_calls += 1
        
        def increment_age(self) -> None:
            self._age_calls += 1

        def increment_show(self) -> None:
            self._show_calls += 1
        
        def display(self) -> None:
            print(f"Stats: {self._grow_calls} grow, {self._age_calls} "
                  f"age, {self._show_calls} show")

    def __init__(self, name: str, height: float, days: int) -> None:
        self._name: str = name
        self._height: float = height
        self._days: int = days
        self._stats: Plant.Stats = Plant.Stats()

    def get_name(self) -> str:
        return self._name

    def get_height(self) -> int:
        return self._height

    def get_age(self) -> int:
        return self._days 

    def set_height(self, height: float) -> None:
        if height < 0:
            print(f"{self._name}: Error, height can't be negative")
        else:
            self._height = height

    def set_age(self, age: int) -> None:
        if age < 0:
            print(f"{self._name}: Error, age can't be negative")
        else:
            self._days = age

    def grow(self) -> None:
        self._stats.increment_grow()
        self._height = round(self._height + 0.8, 1)

    def age(self) -> None:
        self._stats.increment_age()
        self._days += 1

    def show(self) -> None: PAREI AQUI

    @staticmethod
    def is_older_than_a_year(days: int) -> bool:
        return days > 365


    @classmethod
    def anonymous(cls) -> "Plant":
        return cls("Unknown plant", 0.0, 0)

    def show(self) -> None:
        self._stats.inc_show()
        print(f"{self._name}: {self._height:.1f}cm, {self._days} days old")

    def set_height(self, height: float) -> None:
        if height < 0.0:
            print(f"{self._name}: Error, height can't be negative")
            print("Height update rejected")
        else:
            self._height = height
            print(f"Height updated: {height:.0f}cm")

    def get_height(self) -> float:
        return self._height

    def set_age(self, days: int) -> None:
        self._stats.inc_age()
        if days < 0:
            print(f"{self._name}: Error, age can't be negative")
            print("Age update rejected")
        else:
            self._days = days

    def get_age(self) -> int:
        return self._days

    def grow(self, days: int) -> None:
        self._stats.inc_grow()
        if days > 0:
            self._height += days * 2.1
            self._days += days

    def get_stats(self) -> "Plant.Stats":
        return self._stats


class Flower(Plant):
    def __init__(self, name: str, height: float, days: int, color: str) -> None:
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
        self._bloomed = True


class Tree(Plant):
    def __init__(self, name: str, height: float, days: int, trunk_diameter: float) -> None:
        super().__init__(name, height, days)
        self._trunk_diameter = trunk_diameter

    def show(self) -> None:
        super().show()
        print(f"Trunk diameter: {self._trunk_diameter:.1f}cm")

    def produce_shade(self) -> None:
        self._stats.inc_shade()
        print(f"[asking the {self._name.lower()} to produce shade]")
        print(f"Tree {self._name} now produces a shade of "
            f"{self._height:.1f}cm long and {self._trunk_diameter:.1f}cm "
            f"wide.")


class Vegetable(Plant):
    def __init__(self, name: str, height: float, days: int, harvest_season: str) -> None:
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


class Seed(Flower):
    def __init__(self, name: str, height: float, days: int, color: str, seeds: int = 0) -> None:
        super().__init__(name, height, days, color)
        self._seeds = seeds

    def show(self) -> None:
        super().show() 
        print(f"Seeds: {self._seeds}")

    def bloom(self) -> None:
        super().bloom()
        if self._seeds == 0:
            self._seeds = 42  


def display_statistics(plant: Plant) -> None:
    print(f"[statistics for {plant._name}]")
    plant.get_stats().display()
    if isinstance(plant, Tree):
        print(f"{plant.get_stats().get_shade()} shade")


def ft_garden_analytics() -> None:
    print("=== Garden statistics ===")

    print("=== Check year-old")
    print(f"Is 30 days more than a year? -> {Plant.is_older_than_a_year(30)}")
    print(f"Is 400 days more than a year? -> {Plant.is_older_than_a_year(400)}")

    print("\n=== Flower")
    rose = Flower("Rose", 15.0, 10, "red")
    rose.show()
    display_statistics(rose)
    print("[asking the rose to grow and bloom]")
    rose.grow(4) 
    rose.bloom()
    rose.show()
    display_statistics(rose)

    print("\n=== Tree")
    oak = Tree("Oak", 200.0, 365, 5.0)
    oak.show()
    display_statistics(oak)
    oak.produce_shade()
    display_statistics(oak)

    print("\n=== Seed")
    sunflower = Seed("Sunflower", 80.0, 45, "yellow")
    sunflower.show()
    print("[make sunflower grow, age and bloom]")
    sunflower.grow(14)
    sunflower.set_age(65)
    sunflower.bloom()
    sunflower.show()
    display_statistics(sunflower)

    print("\n=== Anonymous")
    unknown = Plant.anonymous()
    unknown.show()
    display_statistics(unknown)


if __name__ == "__main__":
    ft_garden_analytics()