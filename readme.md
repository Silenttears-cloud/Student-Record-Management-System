```
     ____  _             _            _     __  __                                                   _   
    / ___|| |_ _   _  __| | ___ _ __ | |_  |  \/  | __ _ _ __   __ _  __ _  ___ _ __ ___   ___ _ __ | |_ 
    \___ \| __| | | |/ _` |/ _ \ '_ \| __| | |\/| |/ _` | '_ \ / _` |/ _` |/ _ \ '_ ` _ \ / _ \ '_ \| __|
     ___) | |_| |_| | (_| |  __/ | | | |_  | |  | | (_| | | | | (_| | (_| |  __/ | | | | |  __/ | | | |_ 
    |____/ \__|\__,_|\__,_|\___|_| |_|\__| |_|  |_|\__,_|_| |_|\__,_|\__, |\___|_| |_| |_|\___|_| |_|\__|
                                                                      |___/                               
     ____            _                 
    / ___| _   _ ___| |_ ___ _ __ ___ 
    \___ \| | | / __| __/ _ \ '_ ` _ \
     ___) | |_| \__ \ ||  __/ | | | | |
    |____/ \__, |___/\__\___|_| |_| |_|
           |___/                        
```

<div align="center">

# 📚 Student Record Management System

### A Feature-Rich Python CLI Application

```
╔═══════════════════════════════════════════════════════════════╗
║                                                               ║
║   Manage student records, track attendance, analyze grades,   ║
║   visualize performance — all from your terminal!             ║
║                                                               ║
╚═══════════════════════════════════════════════════════════════╝
```

![Python](https://img.shields.io/badge/Python-3.8+-blue?style=for-the-badge&logo=python&logoColor=white)
![CLI](https://img.shields.io/badge/Interface-CLI-green?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Active-brightgreen?style=for-the-badge)

</div>

---

## 📖 Table of Contents

- [Introduction](#-introduction)
- [Features](#-features-at-a-glance)
- [Project Structure](#-project-structure)
- [Setup & Installation Guide](#-setup--installation-guide)
- [How to Run](#-how-to-run)
- [User Manual](#-user-manual--complete-guide)
- [Screenshots](#-what-it-looks-like)
- [FAQ](#-frequently-asked-questions)
- [Contributing](#-contributing)

---

## 🌟 Introduction

```
┌─────────────────────────────────────────────────────────────────┐
│                                                                 │
│   Welcome to the Student Record Management System!              │
│                                                                 │
│   This program is designed for teachers, school admins, and     │
│   students who want a simple, powerful, and offline tool to     │
│   manage academic records right from the command line.           │
│                                                                 │
│   No internet needed. No complex setup. Just Python.            │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

**What does this program do?**

This is a **command-line application** built in Python that helps you:

- ✅ **Add, view, update, and delete** student records
- ✅ **Track attendance** on a daily basis
- ✅ **Calculate grades and GPA** automatically (4.0 scale)
- ✅ **Analyze class performance** with rankings and statistics
- ✅ **Manage multiple semesters** and track progress over time
- ✅ **Export data to CSV** files for use in Excel/Google Sheets
- ✅ **Visualize data** with bar charts using matplotlib
- ✅ **Undo accidental deletions** with action history
- ✅ **Secure access** with password-protected admin login

All data is stored locally in **JSON files** — no database setup required!

---

## ⚡ Features at a Glance

```
╔══════════════════════════════════════════════════════════════════╗
║                                                                  ║
║  ┌──────────────┐  ┌──────────────┐  ┌──────────────────────┐   ║
║  │  📝 CRUD     │  │  📊 CHARTS   │  │  📋 ATTENDANCE       │   ║
║  │  Operations  │  │  & Graphs    │  │  Tracking            │   ║
║  └──────────────┘  └──────────────┘  └──────────────────────┘   ║
║                                                                  ║
║  ┌──────────────┐  ┌──────────────┐  ┌──────────────────────┐   ║
║  │  🎓 GPA      │  │  📤 CSV      │  │  🔐 ADMIN            │   ║
║  │  Calculator  │  │  Export      │  │  Login System         │   ║
║  └──────────────┘  └──────────────┘  └──────────────────────┘   ║
║                                                                  ║
║  ┌──────────────┐  ┌──────────────┐  ┌──────────────────────┐   ║
║  │  📅 SEMESTER │  │  🏆 RANKINGS │  │  ↩️  UNDO / HISTORY   │   ║
║  │  Management  │  │  & Analysis  │  │  Support              │   ║
║  └──────────────┘  └──────────────┘  └──────────────────────┘   ║
║                                                                  ║
╚══════════════════════════════════════════════════════════════════╝
```

| Feature | Description |
|---------|-------------|
| **Add Student** | Add new students with marks for 5 subjects |
| **View All Students** | See all records in a formatted table |
| **Search by Roll/Name** | Find students instantly |
| **Update Records** | Modify marks for any student |
| **Delete Records** | Remove students (with undo support!) |
| **Attendance Tracking** | Mark daily Present/Absent for each student |
| **GPA Calculation** | Credit-weighted GPA on a 4.0 scale |
| **Grade System** | Automatic letter grades (A+ to F) |
| **Semester Support** | Track marks across multiple semesters |
| **Performance Analysis** | Class averages, subject toppers, pass/fail stats |
| **CSV Export** | Export student data & attendance to CSV |
| **Bar Charts** | Visualize performance with matplotlib |
| **Action History** | View log of all actions performed |
| **Undo Delete** | Restore the last deleted student |
| **Password Protection** | SHA-256 hashed admin credentials |
| **Change Password** | Update admin password from settings |

---

## 📁 Project Structure

```
student-management/
│
├── 📄 main.py                  # 🚀 Entry point — run this file!
├── 📄 config.py                # ⚙️  Settings, subjects, file paths
├── 📄 requirements.txt         # 📦 Python dependencies
├── 📄 README.md                # 📖 You are here!
│
├── 📂 models/
│   ├── __init__.py
│   └── student.py              # 🎓 Student data model, GPA, grades
│
├── 📂 services/
│   ├── __init__.py
│   ├── auth.py                 # 🔐 Login & password management
│   ├── student_service.py      # 📝 CRUD operations
│   ├── attendance.py           # 📋 Attendance tracking
│   ├── analytics.py            # 📊 Performance analysis
│   ├── history.py              # 📜 Action history & undo
│   └── semester.py             # 📅 Semester management
│
├── 📂 utils/
│   ├── __init__.py
│   ├── validators.py           # ✅ Input validation
│   ├── file_handler.py         # 💾 JSON file read/write
│   ├── export.py               # 📤 CSV export
│   └── charts.py               # 📈 Matplotlib visualizations
│
└── 📂 data/                    # 🗄️  Auto-created at runtime
    ├── students.json            # Student records
    ├── attendance.json          # Attendance data
    ├── auth.json                # Login credentials (hashed)
    └── history.json             # Action log
```

---

## 🛠 Setup & Installation Guide

### For Complete Beginners — Step by Step! 🐣

> **Don't worry if you've never used Python before. Follow each step carefully and you'll be running the program in minutes!**

---

### Step 1: Install Python 🐍

```
┌─────────────────────────────────────────────────────┐
│  Check if Python is already installed:              │
│                                                     │
│  Open your terminal/command prompt and type:        │
│                                                     │
│    python --version                                 │
│                                                     │
│  You should see something like: Python 3.x.x       │
│  If not, download Python from:                      │
│  👉 https://www.python.org/downloads/               │
│                                                     │
│  ⚠️  IMPORTANT: During installation, check the box  │
│  that says "Add Python to PATH"                     │
└─────────────────────────────────────────────────────┘
```

1. Go to [python.org/downloads](https://www.python.org/downloads/)
2. Download the latest Python version (3.8 or higher)
3. Run the installer
4. **✅ CHECK** the box that says **"Add Python to PATH"** (very important!)
5. Click "Install Now"
6. After installation, verify by opening a terminal and typing:
   ```bash
   python --version
   ```

---

### Step 2: Install VS Code 💻

1. Go to [code.visualstudio.com](https://code.visualstudio.com/)
2. Download and install VS Code for your operating system
3. Open VS Code
4. Install the **Python extension**:
   - Click the Extensions icon on the left sidebar (or press `Ctrl+Shift+X`)
   - Search for **"Python"** by Microsoft
   - Click **Install**

---

### Step 3: Download This Project 📥

**Option A — Using Git (Recommended):**
```bash
git clone <your-repo-url>
```

**Option B — Download ZIP:**
1. Click the green **"Code"** button on GitHub
2. Select **"Download ZIP"**
3. Extract the ZIP file to a folder on your computer

---

### Step 4: Open the Project in VS Code 📂

```
┌────────────────────────────────────────────────────────────┐
│                                                            │
│   1. Open VS Code                                          │
│   2. Click  File → Open Folder                             │
│   3. Navigate to the "student-management" folder           │
│   4. Click "Select Folder"                                 │
│                                                            │
│   You should now see all the project files in the          │
│   left sidebar (Explorer panel)                            │
│                                                            │
└────────────────────────────────────────────────────────────┘
```

---

### Step 5: Open the Terminal in VS Code 🖥️

- Press `` Ctrl + ` `` (backtick key, usually below Escape)
- Or go to **Terminal → New Terminal** from the menu bar
- A terminal panel will appear at the bottom of VS Code

---

### Step 6: Navigate to the Project Folder 📍

If your terminal isn't already in the `student-management` folder, type:

```bash
cd student-management
```

> **💡 Tip:** You can check your current location by typing `pwd` (Mac/Linux) or `cd` (Windows)

---

### Step 7: Install Dependencies 📦

Type this command in the terminal:

```bash
pip install -r requirements.txt
```

This installs **matplotlib** (needed for charts). You should see a success message.

> **⚠️ If `pip` doesn't work**, try:
> ```bash
> pip3 install -r requirements.txt
> ```
> or:
> ```bash
> python -m pip install -r requirements.txt
> ```

---

## 🚀 How to Run

```
╔══════════════════════════════════════════════════════════════╗
║                                                              ║
║   Make sure you're in the student-management folder, then:   ║
║                                                              ║
║   $ python main.py                                           ║
║                                                              ║
║   If that doesn't work, try:                                 ║
║                                                              ║
║   $ python3 main.py                                          ║
║                                                              ║
╚══════════════════════════════════════════════════════════════╝
```

```bash
cd student-management
python main.py
```

You'll see the login screen. Use the default credentials:

```
┌──────────────────────────────┐
│   🔐 Default Login           │
│                              │
│   Username:  admin           │
│   Password:  admin123        │
│                              │
│   (You can change this       │
│    later from the menu)      │
└──────────────────────────────┘
```

---

## 📘 User Manual — Complete Guide

### 🔐 1. Logging In

When you start the program, you'll see a login prompt:

```
╔══════════════════════════════════════╗
║         🔐 ADMIN LOGIN               ║
╚══════════════════════════════════════╝
  Username: admin
  Password: admin123
```

- You get **3 attempts** to enter the correct credentials
- The password is stored as a **SHA-256 hash** (secure!)
- After successful login, you'll see the main menu

---

### 📋 2. Main Menu

After logging in, you'll see this menu:

```
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
╚══════════════════════════════════════════════╝
```

Simply type the number of your choice and press **Enter**.

---

### ➕ 3. Adding a Student (Option 1)

```
Step-by-step:
─────────────────────────────────────────────
1. Choose option "1" from the main menu
2. Enter a unique Roll Number (e.g., 101)
3. Enter the student's name (e.g., John Doe)
4. Enter semester (e.g., Sem-1) or press Enter for default
5. Enter marks for each subject (0-100):
   • Math
   • Science  
   • English
   • History
   • Computer
6. The student is saved automatically! ✅
─────────────────────────────────────────────
```

**Example:**
```
Enter Roll Number: 101
Enter Student Name: Rahul Sharma
Enter Semester (e.g., Sem-1): Sem-1
Enter marks for each subject:
  Math (0-100): 85
  Science (0-100): 92
  English (0-100): 78
  History (0-100): 88
  Computer (0-100): 95
✅ Student 'Rahul Sharma' added successfully!
```

> **💡 The system automatically calculates:** Total, Average, Grade, GPA, and Pass/Fail status!

---

### 👀 4. Viewing All Students (Option 2)

Displays a beautiful formatted table with all student records:

```
Roll     Name               Sem     Math     Science  English  History  Computer Total   Avg     GPA    Grade  Status
──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
101      Rahul Sharma        Sem-1   85       92       78       88       95       438     87.6    3.7    A      ✅ Pass
102      Priya Singh         Sem-1   72       68       81       75       70       366     73.2    3.0    B      ✅ Pass
```

---

### 🔍 5. Searching for Students (Options 3 & 4)

**Search by Roll Number (Option 3):**
- Enter the exact roll number
- Shows complete details including all semesters

**Search by Name (Option 4):**
- Enter a partial name (e.g., "rah" will find "Rahul")
- Case-insensitive search
- Shows all matching results

---

### ✏️ 6. Updating a Student (Option 5)

```
Step-by-step:
─────────────────────────────────────────────
1. Choose option "5"
2. Enter the roll number of the student
3. Re-enter marks for all 5 subjects
4. The record updates automatically!
─────────────────────────────────────────────
```

> **💡 The old marks are saved in the history log, so you can track changes!**

---

### 🗑️ 7. Deleting a Student (Option 6)

```
Step-by-step:
─────────────────────────────────────────────
1. Choose option "6"
2. Enter the roll number
3. Confirm deletion by typing "y"
4. Student is removed (but can be restored!)
─────────────────────────────────────────────
```

> **💡 Don't worry!** If you accidentally delete a student, use **Option 12 → Undo Last Delete** to restore them!

---

### 📊 8. Performance Analysis (Option 7)

This powerful feature shows you:

```
┌─────────────────────────────────────────┐
│  📊 PERFORMANCE ANALYSIS                │
├─────────────────────────────────────────┤
│                                         │
│  • Class Average across all subjects    │
│  • Subject-wise Average breakdown       │
│  • 🏆 Subject Toppers (highest scorer   │
│    in each subject)                     │
│  • 📋 Student Rankings (by average)     │
│  • ✅ Pass / ❌ Fail Summary             │
│                                         │
└─────────────────────────────────────────┘
```

---

### 📋 9. Attendance Menu (Option 8)

```
  ┌──────────────────────────────┐
  │   📋 ATTENDANCE MENU         │
  ├──────────────────────────────┤
  │   1. Mark Attendance         │  → Mark Present/Absent for a student
  │   2. View All Attendance     │  → See attendance % for all students
  │   3. View Student Attendance │  → Detailed attendance for one student
  │   4. Export Attendance CSV   │  → Save attendance data to CSV file
  │   5. Back                    │
  └──────────────────────────────┘
```

**How to mark attendance:**
1. Enter the student's roll number
2. Enter the date (e.g., `2025-01-15`) or press Enter for today
3. Type `P` for Present or `A` for Absent

**Attendance percentage is calculated automatically!**

---

### 📅 10. Semester Menu (Option 9)

```
  ┌──────────────────────────────┐
  │   📅 SEMESTER MENU           │
  ├──────────────────────────────┤
  │   1. Add New Semester        │  → Add marks for a new term
  │   2. View Semester Progress  │  → See progress across semesters
  │   3. Back                    │
  └──────────────────────────────┘
```

**Adding a new semester:**
1. Enter the student's roll number
2. Enter the semester name (e.g., `Sem-2`)
3. Enter marks for all 5 subjects
4. The student's record now tracks multiple semesters!

**Viewing progress shows trends:**
```
  Sem-1 → Avg: 87.6 | GPA: 3.70 | Grade: A
  Sem-2 → Avg: 91.2 | GPA: 3.85 | Grade: A+  ↑ Improved!
```

---

### 📤 11. Export to CSV (Option 10)

```
  ┌──────────────────────────────┐
  │   📤 EXPORT MENU             │
  ├──────────────────────────────┤
  │   1. Export Students CSV     │  → All student data
  │   2. Export Attendance CSV   │  → Attendance records
  │   3. Back                    │
  └──────────────────────────────┘
```

- CSV files are saved in the `exports/` folder
- Files are **timestamped** (e.g., `students_20250115_143022.csv`)
- Open them in **Excel**, **Google Sheets**, or any spreadsheet app!

---

### 📈 12. Visualizations / Charts (Option 11)

```
  ┌──────────────────────────────┐
  │   📊 VISUALIZATION MENU      │
  ├──────────────────────────────┤
  │   1. Subject Averages Chart  │  → Bar chart of average marks per subject
  │   2. Student Comparison Chart│  → Compare averages of all students
  │   3. Back                    │
  └──────────────────────────────┘
```

> **📊 Charts pop up in a new window using matplotlib!**
> You need a graphical display for charts to work (won't work in SSH-only terminals).

---

### 📜 13. History & Undo (Option 12)

```
  ┌──────────────────────────────┐
  │   📜 HISTORY MENU            │
  ├──────────────────────────────┤
  │   1. View Action History     │  → See log of all ADD/UPDATE/DELETE actions
  │   2. Undo Last Delete        │  → Restore the most recently deleted student
  │   3. Back                    │
  └──────────────────────────────┘
```

**Every action is logged with:**
- Action type (ADD / UPDATE / DELETE)
- Description (who was affected)
- Timestamp (when it happened)

---

### 🔑 14. Change Password (Option 13)

```
Step-by-step:
─────────────────────────────────────────────
1. Choose option "13"
2. Enter your current password
3. Enter a new password (minimum 4 characters)
4. Confirm the new password
5. Password updated! 🔒
─────────────────────────────────────────────
```

> **🔒 Passwords are stored as SHA-256 hashes — never in plain text!**

---

### 🚪 15. Exit (Option 14)

- Saves all data automatically
- Displays a goodbye message
- Safely closes the program

---

## 🎓 Grading System

```
┌─────────────────────────────────────────────┐
│        📊 GRADING SCALE                     │
├──────────┬──────────┬───────────────────────┤
│  Marks   │  Grade   │  Grade Points (GPA)   │
├──────────┼──────────┼───────────────────────┤
│  90-100  │   A+     │       4.0             │
│  80-89   │   A      │       3.7             │
│  70-79   │   B      │       3.0             │
│  60-69   │   C      │       2.0             │
│  50-59   │   D      │       1.0             │
│   0-49   │   F      │       0.0             │
├──────────┴──────────┴───────────────────────┤
│  Pass Mark: 40 in EACH subject              │
│  GPA: Credit-weighted on 4.0 scale          │
└─────────────────────────────────────────────┘
```

**Subject Credits:**
| Subject | Credits |
|---------|---------|
| Math | 4 |
| Science | 4 |
| English | 3 |
| History | 3 |
| Computer | 4 |

---

## 🖼️ What It Looks Like

**Login Screen:**
```
  Welcome to the Student Record Management System!

╔══════════════════════════════════════╗
║         🔐 ADMIN LOGIN               ║
╚══════════════════════════════════════╝
  Username: admin
  Password: ********
  ✅ Login successful!
```

**Student Table:**
```
Roll     Name               Sem     Math     Science  English  History  Computer Total   Avg     GPA    Grade  Status
──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
101      Rahul Sharma        Sem-1   85       92       78       88       95       438     87.6    3.7    A      ✅ Pass
102      Priya Singh         Sem-1   45       38       81       75       70       309     61.8    2.0    C      ❌ Fail
103      Amit Patel          Sem-1   92       95       88       91       97       463     92.6    4.0    A+     ✅ Pass
```

---

## ❓ Frequently Asked Questions

<details>
<summary><b>Q: Where is my data stored?</b></summary>

All data is stored in JSON files inside the `data/` folder, which is automatically created when you first run the program. Files include:
- `students.json` — All student records
- `attendance.json` — Attendance data
- `auth.json` — Login credentials (hashed)
- `history.json` — Action log
</details>

<details>
<summary><b>Q: I forgot my password. What do I do?</b></summary>

Delete the `data/auth.json` file. The next time you run the program, it will reset to the default credentials (`admin` / `admin123`).
</details>

<details>
<summary><b>Q: Can I add more subjects?</b></summary>

Yes! Open `config.py` and modify the `SUBJECTS` list and `CREDITS` dictionary:
```python
SUBJECTS = ["Math", "Science", "English", "History", "Computer", "Art"]
CREDITS = {"Math": 4, "Science": 4, "English": 3, "History": 3, "Computer": 4, "Art": 2}
```
</details>

<details>
<summary><b>Q: Charts are not showing up!</b></summary>

Charts require a graphical display. If you're using SSH or a headless server, matplotlib won't be able to display charts. Use a local machine with a display, or modify `charts.py` to save charts as image files instead.
</details>

<details>
<summary><b>Q: Can I change the pass mark?</b></summary>

Yes! Open `config.py` and change:
```python
PASS_MARK = 40  # Change this to whatever you want
```
</details>

<details>
<summary><b>Q: How do I back up my data?</b></summary>

Simply copy the entire `data/` folder to a safe location. To restore, paste it back.
</details>

---

## 🤝 Contributing

```
╔═══════════════════════════════════════════════════╗
║                                                   ║
║   Contributions are welcome! 🎉                   ║
║                                                   ║
║   1. Fork the repository                          ║
║   2. Create a new branch                          ║
║   3. Make your changes                            ║
║   4. Submit a pull request                        ║
║                                                   ║
╚═══════════════════════════════════════════════════╝
```

**Ideas for contributions:**
- 🌐 Add a web-based GUI
- 📧 Email report generation
- 🗃️ SQLite database support
- 📱 Mobile-friendly interface
- 🌍 Multi-language support

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

---

<div align="center">

```
╔═══════════════════════════════════════════════════════════╗
║                                                           ║
║   ⭐ If you found this helpful, give it a star! ⭐        ║
║                                                           ║
║   Made with ❤️ and Python 🐍                              ║
║                                                           ║
╚═══════════════════════════════════════════════════════════╝
```

**Happy Coding! 🚀**

</div>
