grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]  #список
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}    #множество
grades_m = []
for num in grades:
    s = sum(num)/len(num)
    grades_m.append(s)
print(grades_m)
students_sort = list(sorted(students))
print(students_sort)
list = dict(zip(grades_m,students_sort))
print(list)