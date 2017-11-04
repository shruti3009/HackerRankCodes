"""
Given the names and grades for each student in a Physics class of  students,
store them in a nested list and print the name(s) of any student(s) having the second lowest grade.

Note: If there are multiple students with the same grade, order their names alphabetically
and print each name on a new line.

Input Format

The first line contains an integer,n, the number of students.
The  subsequent lines describe each student over  lines; the first line contains a
student's name, and the second line contains their grade.

Output Format
Print the name(s) of any student(s) having the second lowest grade in Physics;
if there are multiple students,order their names alphabetically and print each one on a new line.
"""
students = [] #empty list
for _ in range(int(raw_input())): #user input of number of students
    students.append([raw_input(), float(raw_input())]) # for each student, input name and score
#print students

marks = [marks for name, marks in students]  #using list comprehension.
#parsing marks from the students (netsed-list) to another list which will be called marks.
marks_list = set(marks) #set func will see all the unique values in the list: marks
#and will be stored in marks_list.
#print marks_list
second_lowest = sorted(marks_list)[1] #the marks_list is sorted using sorted func.
#print second_lowest

print('\n'.join(sorted(name for name, marks in students if marks == second_lowest)))# this step is printing the names of student
in alphabetical order, who got same second lowest marks.
