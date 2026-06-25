# Student Report Card System
# A beginner Python project that calculates total marks,
# average, highest mark, lowest mark, and grade.
# Author: Sahana

name=input("Enter student name").title()
marks=[
    int(input("Enter marks for first subject")),
    int(input("Enter marks for second subject")),
    int(input("Enter marks for third subject")),
    int(input("Enter marks for four subject")),
    int(input("Enter marks for five subject"))
]

print("-------Student Report Card-------")
print("Name: ",name)
print("Marks:",marks)
total_marks=sum(marks)
print("Total_marks: ",total_marks)                   
average=(total_marks)/5
print("Average: ",average)
highest=max(marks)
print("highest marks: ",highest)
lowest=min(marks)
print("Lowest marks: ",min(marks))
Grade=""
if average>=90:
    Grade="A"
    print("Grade:A")
elif average>=75:
    Grade="B"
    print("Grade:B")
elif average>=60:
    Grade="C"
    print("Grade:C")
elif average>=35:
    Grade="D"
    print("Grade:D")
else:
    Grade="F"
    print("Grade:F")
new={"name":name,"marks":marks,"Total marks":total_marks,"Average":average,"Highest marks":highest,"Lowest marks":lowest,"Grade":Grade}
print(new)

