grades = [85, 92, 78, 65, 88, 91, 73, 89, 55, 94]
print("the total no of students is:",len(grades))
gradeA=0
gradeB=0
gradeC=0
below_grade=0
for i in grades:
    if i>=90:
        gradeA+=1
    elif i>=80:
        gradeB+=1
    elif i>=70:
        gradeC+=1
    else:
        below_grade+=1
print("The no of the students got grade A is:",gradeA)
print("The no of the students got grade B is:",gradeB)
print("The no of the students got grade C is:",gradeC)
print("The no of the students got below grade is:",below_grade)