#!/usr/bin/env python3
"""
Student Record Management System
A feature-rich CLI application for managing student records.
"""

import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from services.auth import login, change_password
from services.student_service import (
    load_students, save_students,
    add_student, view_all_students,
    search_by_roll, search_by_name,
    update_student, delete_student,
)
from services.attendance import mark_attendance, view_attendance, view_student_attendance
from services.analytics import show_performance_analysis
from services.semester import add_semester, view_semester_progress
from services.history import view_history, undo_last_delete
from utils.export import export_all_students_csv, export_attendance_csv
from utils.charts import plot_subject_averages, plot_student_comparison


MAIN_MENU = """
╔══════════════════════════════════════════════╗
║     📚 STUDENT RECORD MANAGEMENT SYSTEM      ║
╠══════════════════════════════════════════════╣
║                                              ║
║   1.  Add Student                            ║
║   2.  View All Students                      ║
║   3.  Search by Roll Number                  ║
║   4.  Search by Name                         ║
║   5.  Update Student                         ║
║   6.  Delete Student                         ║
║   7.  Performance Analysis                   ║
║   8.  Attendance Menu            ►           ║
║   9.  Semester Menu              ►           ║
║   10. Export to CSV              ►           ║
║   11. Visualizations (Charts)    ►           ║
║   12. View History / Undo                    ║
║   13. Change Password                        ║
║   14. Exit                                   ║
║                                              ║
╚══════════════════════════════════════════════╝"""

ATTENDANCE_MENU = """
  ┌──────────────────────────────┐
  │   📋 ATTENDANCE MENU         │
  ├──────────────────────────────┤
  │   1. Mark Attendance         │
  │   2. View All Attendance     │
  │   3. View Student Attendance │
  │   4. Export Attendance CSV   │
  │   5. Back                    │
  └──────────────────────────────┘"""

SEMESTER_MENU = """
  ┌──────────────────────────────┐
  │   📅 SEMESTER MENU           │
  ├──────────────────────────────┤
  │   1. Add New Semester        │
  │   2. View Semester Progress  │
  │   3. Back                    │
  └──────────────────────────────┘"""

EXPORT_MENU = """
  ┌──────────────────────────────┐
  │   📤 EXPORT MENU             │
  ├──────────────────────────────┤
  │   1. Export Students CSV     │
  │   2. Export Attendance CSV   │
  │   3. Back                    │
  └──────────────────────────────┘"""

CHART_MENU = """
  ┌──────────────────────────────┐
  │   📊 VISUALIZATION MENU      │
  ├──────────────────────────────┤
  │   1. Subject Averages Chart  │
  │   2. Student Comparison Chart│
  │   3. Back                    │
  └──────────────────────────────┘"""

HISTORY_MENU = """
  ┌──────────────────────────────┐
  │   📜 HISTORY MENU            │
  ├──────────────────────────────┤
  │   1. View Action History     │
  │   2. Undo Last Delete        │
  │   3. Back                    │
  └──────────────────────────────┘"""


def attendance_submenu(students: dict) -> None:
    while True:
        print(ATTENDANCE_MENU)
        choice = input("  Enter choice (1-5): ").strip()
        if choice == "1":
            mark_attendance(students)
        elif choice == "2":
            view_attendance(students)
        elif choice == "3":
            view_student_attendance(students)
        elif choice == "4":
            from services.attendance import load_attendance
            export_attendance_csv(students, load_attendance())
        elif choice == "5":
            break
        else:
            print("  ⚠ Invalid choice.\n")


def semester_submenu(students: dict) -> None:
    while True:
        print(SEMESTER_MENU)
        choice = input("  Enter choice (1-3): ").strip()
        if choice == "1":
            add_semester(students)
        elif choice == "2":
            view_semester_progress(students)
        elif choice == "3":
            break
        else:
            print("  ⚠ Invalid choice.\n")


def export_submenu(students: dict) -> None:
    while True:
        print(EXPORT_MENU)
        choice = input("  Enter choice (1-3): ").strip()
        if choice == "1":
            export_all_students_csv(students)
        elif choice == "2":
            from services.attendance import load_attendance
            export_attendance_csv(students, load_attendance())
        elif choice == "3":
            break
        else:
            print("  ⚠ Invalid choice.\n")


def chart_submenu(students: dict) -> None:
    while True:
        print(CHART_MENU)
        choice = input("  Enter choice (1-3): ").strip()
        if choice == "1":
            plot_subject_averages(students)
        elif choice == "2":
            plot_student_comparison(students)
        elif choice == "3":
            break
        else:
            print("  ⚠ Invalid choice.\n")


def history_submenu(students: dict) -> dict:
    while True:
        print(HISTORY_MENU)
        choice = input("  Enter choice (1-3): ").strip()
        if choice == "1":
            view_history()
        elif choice == "2":
            students = undo_last_delete(students)
            save_students(students)
        elif choice == "3":
            break
        else:
            print("  ⚠ Invalid choice.\n")
    return students


def main():
    """Main application entry point."""
    print("\n  Welcome to the Student Record Management System!")

    if not login():
        return

    students = load_students()

    while True:
        print(MAIN_MENU)
        choice = input("Enter your choice (1-14): ").strip()

        if choice == "1":
            add_student(students)
        elif choice == "2":
            view_all_students(students)
        elif choice == "3":
            search_by_roll(students)
        elif choice == "4":
            search_by_name(students)
        elif choice == "5":
            update_student(students)
        elif choice == "6":
            delete_student(students)
        elif choice == "7":
            show_performance_analysis(students)
        elif choice == "8":
            attendance_submenu(students)
        elif choice == "9":
            semester_submenu(students)
        elif choice == "10":
            export_submenu(students)
        elif choice == "11":
            chart_submenu(students)
        elif choice == "12":
            students = history_submenu(students)
        elif choice == "13":
            change_password()
        elif choice == "14":
            save_students(students)
            print("\n  👋 Goodbye! Have a great day!\n")
            break
        else:
            print("  ⚠ Invalid choice. Please try again.\n")


if __name__ == "__main__":
    main()
