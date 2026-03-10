"""Input validation utilities."""


def get_valid_marks(subject: str) -> float:
    """Prompt until a valid mark (0-100) is entered."""
    while True:
        try:
            mark = float(input(f"  Enter {subject} marks (0-100): "))
            if 0 <= mark <= 100:
                return mark
            print("  ⚠ Marks must be between 0 and 100.")
        except ValueError:
            print("  ⚠ Please enter a valid number.")


def get_valid_roll() -> str:
    """Prompt until a non-empty roll number is entered."""
    while True:
        roll = input("Enter Roll Number: ").strip()
        if roll:
            return roll
        print("⚠ Roll number cannot be empty.")


def get_valid_name() -> str:
    """Prompt until a non-empty name is entered."""
    while True:
        name = input("Enter Student Name: ").strip()
        if name:
            return name
        print("⚠ Name cannot be empty.")


def get_valid_choice(prompt: str, valid: list[str]) -> str:
    """Prompt until one of the valid choices is entered."""
    while True:
        choice = input(prompt).strip()
        if choice in valid:
            return choice
        print(f"⚠ Please enter one of: {', '.join(valid)}")
