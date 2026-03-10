"""Attendance tracking service."""

from datetime import datetime

from config import ATTENDANCE_FILE
from utils.file_handler import load_json, save_json
from utils.validators import get_valid_roll


def load_attendance() -> dict:
    return load_json(ATTENDANCE_FILE)


def save_attendance(attendance: dict) -> None:
    save_json(ATTENDANCE_FILE, attendance)


def mark_attendance(students: dict) -> None:
    """Mark attendance for students on a given date."""
    attendance = load_attendance()
    date = input(f"Enter date (YYYY-MM-DD) [default: {datetime.today().strftime('%Y-%m-%d')}]: ").strip()
    if not date:
        date = datetime.today().strftime("%Y-%m-%d")

    print(f"\nMarking attendance for {date}:")
    print("Enter 'P' for Present, 'A' for Absent\n")

    for roll, data in students.items():
        while True:
            status = input(f"  {data['name']} ({roll}): ").strip().upper()
            if status in ("P", "A"):
                if roll not in attendance:
                    attendance[roll] = {}
                attendance[roll][date] = status
                break
            print("  ⚠ Enter 'P' or 'A'")

    save_attendance(attendance)
    print("✅ Attendance recorded!\n")


def view_attendance(students: dict) -> None:
    """View attendance summary for all students."""
    attendance = load_attendance()

    if not attendance:
        print("📭 No attendance records found.\n")
        return

    print(f"\n{'Roll':<8} {'Name':<20} {'Present':<10} {'Absent':<10} {'Total':<8} {'%':<8}")
    print("─" * 65)

    for roll, dates in attendance.items():
        name = students.get(roll, {}).get("name", "Unknown")
        present = sum(1 for s in dates.values() if s == "P")
        absent = sum(1 for s in dates.values() if s == "A")
        total = present + absent
        pct = round((present / total) * 100, 1) if total else 0
        indicator = "✅" if pct >= 75 else "⚠️" if pct >= 50 else "❌"
        print(f"{roll:<8} {name:<20} {present:<10} {absent:<10} {total:<8} {pct}% {indicator}")
    print()


def view_student_attendance(students: dict) -> None:
    """View detailed attendance for a specific student."""
    attendance = load_attendance()
    roll = get_valid_roll()

    if roll not in attendance:
        print(f"📭 No attendance records for roll {roll}.\n")
        return

    name = students.get(roll, {}).get("name", "Unknown")
    dates = attendance[roll]

    print(f"\n  Attendance for {name} ({roll}):")
    print(f"  {'Date':<15} {'Status':<10}")
    print(f"  {'─' * 25}")
    for date, status in sorted(dates.items()):
        symbol = "✅ Present" if status == "P" else "❌ Absent"
        print(f"  {date:<15} {symbol}")

    present = sum(1 for s in dates.values() if s == "P")
    total = len(dates)
    print(f"\n  Summary: {present}/{total} days present ({round(present/total*100, 1) if total else 0}%)\n")
