"""
author   :   cyberwr3nch
date     :   19th March 2021
platform :   hackerrank.com
"""
if __name__ == '__main__':
    students = []                                 # initializing an empty list to accomodate users inputs
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([name, score])
    
    sorted_students = sorted(students, key=lambda x:x[1])
    second_lowest = sorted(set(x[1]for x in sorted_students))[1]
    dn = sorted([x[0] for x in students if x[1] == second_lowest ])
    print('\n'.join(dn))

# sorted based on score
# sorted_students = sorted(students, key=lambda x: x[1])       
# [['Tina', 37.2], ['Harry', 37.21], ['Berry', 37.21], ['Harsh', 39], ['Akriti', 41]]
# sorts the list in ascending order based on key which is the second element of the lists (marks)

########## ONE LINER ##########
# print(sorted_students[1])                                     # ['Harry', 37.21]
# print(sorted_students[1][1])                                  # 37.21

# second_lowest = [x[1] for x in sorted_students]                         - [37.2, 37.21, 37.21, 39, 41]
# second_lowest = set([x[1] for x in sorted_students])                    - {41, 37.21, 37.2, 39}
# second_lowest = sorted(set([x[1] for x in sorted_students]))            - [37.2, 37.21, 39, 41]
# second_lowest = sorted(set(x[1] for x in sorted_students))[1]             # 37.21
# print(second_lowest)

# dn = [student for student in students]                                      - [['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], ['Akriti', 41], ['Harsh', 39]]
# dn = [student for student in students if student[1] == second_lowest ]         - [['Harry', 37.21], ['Berry', 37.21]]
# dn = [student[0] for student in students if student[1] == second_lowest]       - ['Harry', 'Berry']
# dn = sorted([student[0] for student in students if student[1] == second_lowest])
# print(dn)                                                    # ['Berry', 'Harry']

# required output:
# print("-"*15)
# print("\n".join(dn))
# print("-"*15)
# Berry
# Harry
########## ONE LINER ##########

"""
Input Example:
input:
5
Harry
37.21
Berry
37.21
Tina
37.2
Akriti
41
Harsh
39
"""