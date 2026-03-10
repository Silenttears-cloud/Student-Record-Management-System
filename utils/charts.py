"""Matplotlib visualization utilities."""

from config import SUBJECTS


def plot_subject_averages(students: dict) -> None:
    """Bar chart of class-wide subject averages."""
    try:
        import matplotlib.pyplot as plt
    except ImportError:
        print("⚠ matplotlib not installed. Run: pip install matplotlib\n")
        return

    if not students:
        print("📭 No data to visualize.\n")
        return

    subject_totals = {s: 0.0 for s in SUBJECTS}
    count = 0

    for data in students.values():
        sem = data.get("current_semester", "Sem-1")
        sem_data = data.get("semesters", {}).get(sem)
        if sem_data:
            for s in SUBJECTS:
                subject_totals[s] += sem_data["marks"].get(s, 0)
            count += 1

    if count == 0:
        print("📭 No semester data found.\n")
        return

    avgs = [round(subject_totals[s] / count, 2) for s in SUBJECTS]
    colors = ["#4CAF50", "#2196F3", "#FF9800", "#9C27B0", "#F44336"]

    plt.figure(figsize=(10, 6))
    bars = plt.bar(SUBJECTS, avgs, color=colors, edgecolor="black", linewidth=0.5)
    for bar, avg in zip(bars, avgs):
        plt.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 1, str(avg),
                 ha="center", va="bottom", fontweight="bold")
    plt.title("📊 Subject-wise Class Averages", fontsize=16, fontweight="bold")
    plt.ylabel("Average Marks")
    plt.ylim(0, 110)
    plt.tight_layout()
    plt.show()


def plot_student_comparison(students: dict) -> None:
    """Bar chart comparing student averages."""
    try:
        import matplotlib.pyplot as plt
    except ImportError:
        print("⚠ matplotlib not installed. Run: pip install matplotlib\n")
        return

    if not students:
        print("📭 No data to visualize.\n")
        return

    names = []
    averages = []

    for data in students.values():
        sem = data.get("current_semester", "Sem-1")
        sem_data = data.get("semesters", {}).get(sem)
        if sem_data:
            names.append(data["name"][:15])
            averages.append(sem_data["average"])

    if not names:
        return

    colors = ["#4CAF50" if a >= 60 else "#FF9800" if a >= 40 else "#F44336" for a in averages]

    plt.figure(figsize=(max(8, len(names) * 1.2), 6))
    bars = plt.barh(names, averages, color=colors, edgecolor="black", linewidth=0.5)
    for bar, avg in zip(bars, averages):
        plt.text(bar.get_width() + 1, bar.get_y() + bar.get_height() / 2, str(avg),
                 va="center", fontweight="bold")
    plt.title("📊 Student Performance Comparison", fontsize=16, fontweight="bold")
    plt.xlabel("Average Marks")
    plt.xlim(0, 110)
    plt.tight_layout()
    plt.show()
