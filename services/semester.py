"""Semester/term management service."""

from config import SUBJECTS
from models.student import calculate_grade, calculate_gpa, is_passed
from utils.validators import get_valid_roll, get_valid_marks
from services.student_service import save_students


def add_semester(students: dict) -> None:
    """Add a new semester for a student."""
    roll = get_valid_roll()
    if roll not in students:
        print(f"❌ No student found with roll number {roll}.\n")
        return

    data = students[roll]
    existing = list(data.get("semesters", {}).keys())
    print(f"  Existing semesters: {', '.join(existing)}")

    semester = input("  Enter new semester name (e.g., Sem-2): ").strip()
    if not semester:
        print("  ⚠ Semester name cannot be empty.\n")
        return
    if semester in existing:
        print(f"  ⚠ {semester} already exists for this student.\n")
        return

    print(f"  Enter marks for {data['name']} — {semester}:")
    marks = {}
    for subject in SUBJECTS:
        marks[subject] = get_valid_marks(subject)

    total = sum(marks.values())
    average = round(total / len(marks), 2)

    data["semesters"][semester] = {
        "marks": marks,
        "total": total,
        "average": average,
        "grade": calculate_grade(average),
        "gpa": calculate_gpa(marks),
        "passed": is_passed(marks),
    }
    data["current_semester"] = semester

    save_students(students)
    print(f"  ✅ {semester} added for {data['name']}!\n")


def view_semester_progress(students: dict) -> None:
    """View a student's progress across semesters."""
    roll = get_valid_roll()
    if roll not in students:
        print(f"❌ No student found with roll number {roll}.\n")
        return

    data = students[roll]
    semesters = data.get("semesters", {})

    if not semesters:
        print("  📭 No semester data.\n")
        return

    print(f"\n  📈 Semester Progress for {data['name']} ({roll}):")
    print(f"  {'Semester':<10} {'Average':<10} {'GPA':<8} {'Grade':<8} {'Status'}")
    print(f"  {'─' * 48}")

    prev_avg = None
    for sem_name, sem_data in semesters.items():
        trend = ""
        if prev_avg is not None:
            diff = sem_data["average"] - prev_avg
            trend = f" (↑{diff:+.1f})" if diff > 0 else f" (↓{diff:+.1f})" if diff < 0 else " (→)"
        status = "Pass" if sem_data["passed"] else "Fail"
        print(f"  {sem_name:<10} {sem_data['average']:<10} {sem_data['gpa']:<8} {sem_data['grade']:<8} {status}{trend}")
        prev_avg = sem_data["average"]
    print()
