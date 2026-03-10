"""Application configuration and constants."""

import os

# Directories
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")

# File paths
STUDENTS_FILE = os.path.join(DATA_DIR, "students.json")
ATTENDANCE_FILE = os.path.join(DATA_DIR, "attendance.json")
AUTH_FILE = os.path.join(DATA_DIR, "auth.json")
HISTORY_FILE = os.path.join(DATA_DIR, "history.json")
EXPORT_DIR = os.path.join(BASE_DIR, "exports")

# Academic config
SUBJECTS = ["Math", "Science", "English", "History", "Computer"]
CREDITS = {"Math": 4, "Science": 4, "English": 3, "History": 3, "Computer": 4}
PASS_MARK = 40

# GPA scale (4.0)
GRADE_MAP = {
    "A+": 4.0, "A": 3.7, "B": 3.0, "C": 2.0, "D": 1.0, "F": 0.0,
}

# Ensure directories exist
os.makedirs(DATA_DIR, exist_ok=True)
os.makedirs(EXPORT_DIR, exist_ok=True)
