grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
average_grades = [sum(grades[0])/len(grades[0]), sum(grades[1])/len(grades[1]), sum(grades[2])/len(grades[2]), sum(grades[3])/len(grades[3]), sum(grades[4])/len(grades[4])]

students = sorted (students)

# 1-й способ
dict1 = dict(zip(students, average_grades))
print(dict1)

# 2-й способ
dict2 = {}
for i in range(len(average_grades)):
   dict2[students[i]]=average_grades[i]
print(dict2)

