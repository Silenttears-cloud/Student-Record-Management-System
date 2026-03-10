"""Performance analysis and statistics."""

from config import SUBJECTS, PASS_MARK


def show_performance_analysis(students: dict) -> None:
    """Comprehensive performance analysis."""
    if not students:
        print("📭 No records to analyze.\n")
        return

    records = []
    for roll, data in students.items():
        sem = data.get("current_semester", "Sem-1")
        sem_data = data.get("semesters", {}).get(sem)
        if sem_data:
            records.append((roll, data["name"], sem_data))

    if not records:
        print("📭 No semester data found.\n")
        return

    averages = [r[2]["average"] for r in records]
    class_avg = round(sum(averages) / len(averages), 2)

    print(f"\n{'═' * 55}")
    print(f"  📊 PERFORMANCE ANALYSIS")
    print(f"{'═' * 55}")
    print(f"  Total Students : {len(records)}")
    print(f"  Class Average  : {class_avg}")

    print(f"\n  Subject-wise Analysis:")
    print(f"  {'Subject':<12} {'Average':<10} {'Highest':<10} {'Topper'}")
    print(f"  {'─' * 50}")
    for subject in SUBJECTS:
        marks_list = [(r[1], r[2]["marks"].get(subject, 0)) for r in records]
        avg = round(sum(m for _, m in marks_list) / len(marks_list), 2)
        topper = max(marks_list, key=lambda x: x[1])
        print(f"  {subject:<12} {avg:<10} {topper[1]:<10} {topper[0]}")

    ranked = sorted(records, key=lambda x: x[2]["average"], reverse=True)
    print(f"\n  🏆 Student Rankings:")
    print(f"  {'Rank':<6} {'Name':<20} {'Avg':<8} {'GPA':<6} {'Grade':<6} {'Status'}")
    print(f"  {'─' * 55}")
    for rank, (roll, name, sem_data) in enumerate(ranked, 1):
        status = "Pass" if sem_data["passed"] else "Fail"
        print(f"  {rank:<6} {name:<20} {sem_data['average']:<8} {sem_data['gpa']:<6} {sem_data['grade']:<6} {status}")

    passed = sum(1 for r in records if r[2]["passed"])
    failed = len(records) - passed
    print(f"\n  📋 Pass/Fail Summary:")
    print(f"    Passed: {passed} ({round(passed/len(records)*100, 1)}%)")
    print(f"    Failed: {failed} ({round(failed/len(records)*100, 1)}%)")

    if failed > 0:
        print(f"\n  ❌ Failed Students:")
        for roll, name, sem_data in records:
            if not sem_data["passed"]:
                failed_subjects = [s for s, m in sem_data["marks"].items() if m < PASS_MARK]
                print(f"    {name} — Failed in: {', '.join(failed_subjects)}")

    print(f"\n  🥇 Topper  : {ranked[0][1]} (Avg: {ranked[0][2]['average']}, GPA: {ranked[0][2]['gpa']})")
    print(f"  📉 Lowest  : {ranked[-1][1]} (Avg: {ranked[-1][2]['average']}, GPA: {ranked[-1][2]['gpa']})")
    print(f"{'═' * 55}\n")
