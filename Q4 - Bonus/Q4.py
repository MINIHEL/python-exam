def find_top_student(students, scores):
    if not students or not scores:
        print("No students or scores provided.")
        return

    studentScores = dict(zip(students, scores))
    topStudent = max(studentScores, key=studentScores.get)
    topScore = studentScores[topStudent]
    averageScore = sum(scores) / len(scores)

    print(f"Student with the highest score: {topStudent}, Score: {topScore}")
    print(f"Average score: {averageScore:.2f}")

students = ["Alice", "Bob", "Charlie", "David"]
scores = [85, 92, 78, 90]
find_top_student(students, scores)