"""CSV export utilities."""

import csv
import os
from datetime import datetime

from config import SUBJECTS, EXPORT_DIR


def export_all_students_csv(students: dict) -> str | None:
    """Export all student records to a CSV file. Returns filepath."""
    if not students:
        print("📭 No records to export.\n")
        return None

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filepath = os.path.join(EXPORT_DIR, f"students_{timestamp}.csv")

    with open(filepath, "w", newline="") as f:
        writer = csv.writer(f)
        header = ["Roll", "Name", "Semester"] + SUBJECTS + ["Total", "Average", "Grade", "GPA", "Passed"]
        writer.writerow(header)

        for roll, data in students.items():
            for sem_name, sem_data in data.get("semesters", {}).items():
                row = [roll, data["name"], sem_name]
                row += [sem_data["marks"].get(s, "") for s in SUBJECTS]
                row += [sem_data["total"], sem_data["average"], sem_data["grade"], sem_data["gpa"], sem_data["passed"]]
                writer.writerow(row)

    print(f"✅ Exported to: {filepath}\n")
    return filepath


def export_attendance_csv(students: dict, attendance: dict) -> str | None:
    """Export attendance records to CSV."""
    if not attendance:
        print("📭 No attendance records to export.\n")
        return None

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filepath = os.path.join(EXPORT_DIR, f"attendance_{timestamp}.csv")

    with open(filepath, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Roll", "Name", "Date", "Status"])

        for roll, dates in attendance.items():
            name = students.get(roll, {}).get("name", "Unknown")
            for date, status in dates.items():
                writer.writerow([roll, name, date, status])

    print(f"✅ Attendance exported to: {filepath}\n")
    return filepath
