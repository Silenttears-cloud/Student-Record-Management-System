"""Student CRUD operations."""

from config import SUBJECTS, STUDENTS_FILE
from models.student import create_student_record, calculate_grade, calculate_gpa, is_passed
from utils.file_handler import load_json, save_json
from utils.validators import get_valid_marks, get_valid_roll, get_valid_name
from services.history import log_action


def load_students() -> dict:
    return load_json(STUDENTS_FILE)


def save_students(students: dict) -> None:
    save_json(STUDENTS_FILE, students)


def add_student(students: dict) -> None:
    """Add a new student record."""
    roll = get_valid_roll()
    if roll in students:
        print(f"⚠ Student with roll number {roll} already exists.\n")
        return

    name = get_valid_name()
    semester = input("Enter Semester (e.g., Sem-1): ").strip() or "Sem-1"

    marks = {}
    print("Enter marks for each subject:")
    for subject in SUBJECTS:
        marks[subject] = get_valid_marks(subject)

    students[roll] = create_student_record(name, marks, semester)
    save_students(students)
    log_action("ADD", f"Added student {name} (Roll: {roll})", {"roll": roll, "data": students[roll]})
    print(f"✅ Student '{name}' added successfully!\n")


def view_all_students(students: dict) -> None:
    """Display all student records in a table."""
    if not students:
        print("📭 No student records found.\n")
        return

    print(f"\n{'Roll':<8} {'Name':<18} {'Sem':<7} ", end="")
    for s in SUBJECTS:
        print(f"{s:<9}", end="")
    print(f"{'Total':<7} {'Avg':<7} {'GPA':<6} {'Grade':<6} {'Status'}")
    print("─" * 110)

    for roll, data in students.items():
        sem = data.get("current_semester", "Sem-1")
        sem_data = data.get("semesters", {}).get(sem, {})
        if not sem_data:
            continue
        marks = sem_data.get("marks", {})
        status = "✅ Pass" if sem_data.get("passed") else "❌ Fail"
        print(f"{roll:<8} {data['name']:<18} {sem:<7} ", end="")
        for s in SUBJECTS:
            print(f"{marks.get(s, '-'):<9}", end="")
        print(f"{sem_data['total']:<7} {sem_data['average']:<7} {sem_data['gpa']:<6} {sem_data['grade']:<6} {status}")
    print()


def search_by_roll(students: dict) -> None:
    """Search for a student by roll number."""
    roll = get_valid_roll()
    if roll not in students:
        print(f"❌ No student found with roll number {roll}.\n")
        return
    _display_student(roll, students[roll])


def search_by_name(students: dict) -> None:
    """Search students by partial name match."""
    query = input("Enter name to search: ").strip().lower()
    if not query:
        print("⚠ Search query cannot be empty.\n")
        return

    results = {r: d for r, d in students.items() if query in d["name"].lower()}
    if not results:
        print(f"❌ No students found matching '{query}'.\n")
        return

    print(f"\n  Found {len(results)} result(s):")
    for roll, data in results.items():
        sem = data.get("current_semester", "Sem-1")
        avg = data.get("semesters", {}).get(sem, {}).get("average", "N/A")
        print(f"    Roll: {roll} | Name: {data['name']} | Avg: {avg}")
    print()


def update_student(students: dict) -> None:
    """Update marks for an existing student."""
    roll = get_valid_roll()
    if roll not in students:
        print(f"❌ No student found with roll number {roll}.\n")
        return

    data = students[roll]
    sem = data.get("current_semester", "Sem-1")

    print(f"Updating marks for {data['name']} ({sem}):")
    marks = {}
    for subject in SUBJECTS:
        marks[subject] = get_valid_marks(subject)

    total = sum(marks.values())
    average = round(total / len(marks), 2)

    old_data = data["semesters"][sem].copy()
    data["semesters"][sem] = {
        "marks": marks,
        "total": total,
        "average": average,
        "grade": calculate_grade(average),
        "gpa": calculate_gpa(marks),
        "passed": is_passed(marks),
    }

    save_students(students)
    log_action("UPDATE", f"Updated {data['name']} (Roll: {roll})", {"roll": roll, "old": old_data})
    print("✅ Student record updated!\n")


def delete_student(students: dict) -> None:
    """Delete a student record."""
    roll = get_valid_roll()
    if roll not in students:
        print(f"❌ No student found with roll number {roll}.\n")
        return

    name = students[roll]["name"]
    confirm = input(f"Delete '{name}' (roll {roll})? (y/n): ").lower()
    if confirm == "y":
        deleted = students.pop(roll)
        save_students(students)
        log_action("DELETE", f"Deleted {name} (Roll: {roll})", {"roll": roll, "data": deleted})
        print(f"🗑 Student '{name}' deleted.\n")
    else:
        print("Cancelled.\n")


def _display_student(roll: str, data: dict) -> None:
    """Pretty-print a single student record."""
    print(f"\n{'═' * 45}")
    print(f"  Name     : {data['name']}")
    print(f"  Roll     : {roll}")

    for sem_name, sem_data in data.get("semesters", {}).items():
        print(f"\n  ── {sem_name} ──")
        for subject, mark in sem_data["marks"].items():
            status = "✓" if mark >= 40 else "✗"
            print(f"    {subject:<12}: {mark:>6}  {status}")
        print(f"    {'Total':<12}: {sem_data['total']:>6}")
        print(f"    {'Average':<12}: {sem_data['average']:>6}")
        print(f"    {'GPA':<12}: {sem_data['gpa']:>6}")
        print(f"    {'Grade':<12}: {sem_data['grade']:>6}")
        print(f"    {'Status':<12}: {'✅ Passed' if sem_data['passed'] else '❌ Failed'}")

    print(f"{'═' * 45}\n")
