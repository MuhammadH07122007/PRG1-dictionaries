student_grades = {
    "Elara": 85,
    "Kwame": 92,
    "Siobhan": 78,
    "Kai": 96
}

print(student_grades["Kwame"])
print(student_grades.get("Aisha", "Not found"))

result = student_grades["Elara"] = 45
print(result)

print(student_grades.get("Aisha", "Student is missing"))

student_grades["mhk"] = 39
print(student_grades.get("mhk", "Not found"))
