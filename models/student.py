"""Student data model."""

from config import SUBJECTS, CREDITS, GRADE_MAP, PASS_MARK


def calculate_grade(average: float) -> str:
    """Return letter grade based on average marks."""
    if average >= 90:
        return "A+"
    elif average >= 80:
        return "A"
    elif average >= 70:
        return "B"
    elif average >= 60:
        return "C"
    elif average >= 50:
        return "D"
    return "F"


def calculate_gpa(marks: dict) -> float:
    """Calculate GPA on a 4.0 scale using credit-weighted average."""
    total_credits = 0
    weighted_sum = 0.0

    for subject, mark in marks.items():
        credit = CREDITS.get(subject, 3)
        grade = calculate_grade(mark)
        grade_point = GRADE_MAP.get(grade, 0.0)
        weighted_sum += grade_point * credit
        total_credits += credit

    return round(weighted_sum / total_credits, 2) if total_credits else 0.0


def is_passed(marks: dict) -> bool:
    """Check if student passed all subjects."""
    return all(mark >= PASS_MARK for mark in marks.values())


def create_student_record(name: str, marks: dict, semester: str = "Sem-1") -> dict:
    """Create a structured student record dictionary."""
    total = sum(marks.values())
    average = round(total / len(marks), 2)
    grade = calculate_grade(average)
    gpa = calculate_gpa(marks)

    return {
        "name": name,
        "semesters": {
            semester: {
                "marks": marks,
                "total": total,
                "average": average,
                "grade": grade,
                "gpa": gpa,
                "passed": is_passed(marks),
            }
        },
        "current_semester": semester,
    }
