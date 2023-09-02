from student import Student

student = Student("шvan Ivanov56", "subjects.csv")
student.add_score("Математика", 47)
student.add_test_result("Математика", 45)
print(student.average_test_score("Математика"))
print(student.average_score())