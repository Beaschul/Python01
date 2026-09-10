#!/usr/bin/python3

class Plant:
    def __init__(self, name: str, height: float, days: int) -> None:
        self._name: str = name   
        self._height: float = height
        self._days: int = days

        self.set_height(height)
        self.set_age(days)

    def show(self) -> None:
        print(f"{self._name}: {self._height:.1f}cm, " + f"{self._days} days old\n")

    def set_height(self, height: float) -> None:
        if height < 0.0:
            print(f"{self._days}: Error, height can't be negative")
            print("Height update rejected")
        else:
            self._height = height

    def get_height(self):
        return self._height

    def set_age(self, days):
        if days < 0:
            print(f"{self._days}: Error, age can't be negative")
            print("Height update rejected")
        else:
            self._days = days

    def get_age(self):
        return self._days



def ft_garden_security() -> None:
    print("=== Garden Security System ===")
    rose = Plant("Rose", 15, 10)
    print("Plant created:", end=" ")
    rose.show()

    rose.set_height(20)
    rose.set_age(2)
    print("\nCurrent state:")
    rose.show()

if __name__ == "__main__":
    ft_garden_security()