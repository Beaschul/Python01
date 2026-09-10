#!/usr/bin/python3

def ft_garden_intro(plant: str, height: int, age: int) -> None:
    print("=== Welcome to My Garden ===\n")
    print(f"Plant: {plant}")
    print(f"Height: {height}cm")
    print(f"Age: {age} days\n")
    print("=== End of Program ===\n")


if __name__ == "__main__":
    ft_garden_intro("Rose", 25, 30)
