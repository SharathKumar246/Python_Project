"""
2.Write a Python script that analyzes a text file containing student grades and generates a comprehensive report. (7 marks)
Input CSV Format:
csv
StudentID,Name,Math,Physics,Chemistry,Biology
S001,Alice Johnson,85,90,88,92
S002,Bob Smith,78,82,75,80
S003,Carol White,92,88,95,90
S004,David Brown,70,68,72,75
Requirements:
•	Read the CSV file
•	Create a class Student to store each student's information
•	Calculate individual student averages
•	Generate a report showing: 
o	Total number of students
o	Class average for each subject
o	Overall class average
o	Top 3 students by overall average
o	Students who scored above 90 in any subject
o	Subject-wise highest and lowest scores
•	Handle file not found exceptions
•	Write formatted output to a text file
"""


#!/usr/bin/python3

class Student:
    def __init__(self, sid, name, m, p, c, b):
        self.sid = sid
        self.name = name
        self.m = int(m)
        self.p = int(p)
        self.c = int(c)
        self.b = int(b)

    def avg(self):
        return (self.m + self.p + self.c + self.b) / 4


def main():
    students = []

    try:
        with open("students.csv", "r") as f:
            next(f)   # skip header
            for line in f:
                row = line.strip().split(",")
                #print(row, len(row))
        students.append(Student(*row))

    except FileNotFoundError:
        print("File not found")
        return

    total = len(students)

    # Subject averages
    math_avg = sum(s.m for s in students) / total
    phy_avg = sum(s.p for s in students) / total
    chem_avg = sum(s.c for s in students) / total
    bio_avg = sum(s.b for s in students) / total

    overall_avg = (math_avg + phy_avg + chem_avg + bio_avg) / 4

    students.sort(key=lambda x: x.avg(), reverse=True)
    top3 = students[:3]

    with open("report.txt", "w") as r:
        r.write(f"Total Students: {total}\n")
        r.write(f"Overall Class Average: {overall_avg}\n\n")

        r.write("Top 3 Students:\n")
        for s in top3:
            r.write(f"{s.name} - {s.avg()}\n")

        r.write("\nAbove 90 in any subject:\n")
        for s in students:
            if s.m>90 or s.p>90 or s.c>90 or s.b>90:
                r.write(s.name + "\n")

        r.write("\nHighest & Lowest Scores:\n")
        r.write(f"Math: {max(s.m for s in students)} | {min(s.m for s in students)}\n")
        r.write(f"Physics: {max(s.p for s in students)} | {min(s.p for s in students)}\n")
        r.write(f"Chemistry: {max(s.c for s in students)} | {min(s.c for s in students)}\n")
        r.write(f"Biology: {max(s.b for s in students)} | {min(s.b for s in students)}\n")

    print("Report Generated")


main()


