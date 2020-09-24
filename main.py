# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import os

import string
filename = "student.txt"


def menu():
    print("--------Student Information Management System--------")
    print("-----------------Function Menu-----------------------")
    print("\t\t\t1. insert new student")
    print("\t\t\t2. search a student")
    print("\t\t\t3. delete a student")
    print("\t\t\t4. edit a student")
    print("\t\t\t5. reorder")
    print("\t\t\t6. total student number")
    print("\t\t\t7. show all student")
    print("\t\t\t0. exit")
    print("------------------------end---------------------------")


def main():
    while True:
        menu()
        choice = int(input('Please enter the number: '))
        if choice in [0, 1, 2, 3, 4, 5, 6, 7]:
            if choice == 0:
                answer = input(" Are you sure to exit the system? y/n")
                if answer == 'y' or answer == 'Y':
                    print("Thank you!")
                    break
                else:
                    continue
            elif choice == 1:
                insert()  #
            elif choice == 2:
                search()  #
            elif choice == 3:
                delete()  #
            elif choice == 4:
                modify()  #
            elif choice == 5:
                sort()  #
            elif choice == 6:
                total()  #
            elif choice == 7:
                show()  #


def insert():
    student_list = []
    while True:
        id = input("Please input ID: ")
        if not id:
            break
        name = input("Please input name: ")
        if not name:
            break
        try:
            english = input("Please input English grade: ")
            python = input("Please input Python grade: ")
            java = input("Please input Java grade: ")
        except:
            print("Please input decimal number")
            continue

        student = {'Id': id, 'name': name, 'English': english, 'Python': python, 'Java': java}
        student_list.append(student)

        answer = input(" Do you want add another student? y/n\n")
        if answer == 'y' or answer == 'Y':
            continue
        else:
            break
    save(student_list)
    print("Input student information successfully")


def save(lst):
    try:
        stu_txt = open(filename, 'a', encoding='utf-8')
    except:
        stu_txt = open(filename, 'w', encoding="utf-8")
    for item in lst:
        stu_txt.write(str(item) + '\n')
    stu_txt.close()


def search():
    student_query=[]
    while True:
        Id = ''
        name = ''
        if os.path.exists(filename):
            mode = input('search by Id(1) or name(2)? ')
            if mode == '1':
                Id = input('Please input student Id:')
            elif mode == '2':
                name = input('Please input student name:')
            else:
                print('Your input is not right, please input again')
                search()
            with open(filename, 'r', encoding='utf-8') as rfile:
                student = rfile.readlines()
                for item in student:
                    d = dict(eval(item))
                    if Id != '':
                        if d['Id'] == Id:
                            student_query.append(d)
                    elif name != '':
                        if d['name'] == name:
                            student_query.append(d)

            show_student(student_query)
            student_query.clear()
            answer = input(" Do you want search another student? y/n\n")
            if answer == 'y' or answer == 'Y':
                continue
            else:
                break
        else:
            print(" There is no student information.")
            return


def show_student(lst):
    if len(lst) == 0:
        print('There is no this student')
        return
    format_title = '{:^6}\t{:^12}\t{:^8}\t{:^10}\t{:^10}'
    print(format_title.format('Id', "name", 'English','Python','Java'))
    format_data = '{:^6}\t{:^12}\t{:^8}\t{:^10}\t{:^10}'
    for item in lst:
        print(format_data.format(item.get('Id'),
                                  item.get('name'),
                                  item.get('English'),
                                  item.get('Python'),
                                  item.get('Java')))

def delete():
    while True:
        student_id = input("Please input id: ")
        if student_id != '':
            if os.path.exists(filename):  # if file exist
                with open(filename, 'r', encoding='utf-8') as file:
                    student_old = file.readlines()
            else:  # if not
                student_old = []
            flag = False  # False is delete unsuccessfully
            if student_old:
                with open(filename, 'w', encoding='utf-8') as wfile:
                    d = {}
                    for item in student_old:
                        d = dict(eval(item))  # translate String into dict
                        if d['Id'] != student_id:
                            wfile.write(str(d) + '\n')
                        else:
                            flag = True

                    if flag:
                        print('Delete successfully')
                    else:
                        print(f"Do not find the student who's id is {student_id}")
            else:
                print("There is no student in database")
                break
            show()  # show all student information
            answer = input("Do you need to delete a student? y/n\n")
            if answer == 'y' or answer == 'Y':
                continue
            else:
                break


def modify():
    show()
    if os.path.exists(filename):
        with open(filename,'r',encoding='utf-8') as rfile:
            student_old = rfile.readlines()
    else:
        return
    student_id = input("Please input student Id:")
    with open(filename,'w',encoding='utf-8') as wfile:
        for item in student_old:
            d = dict(eval(item))
            if d['Id'] == student_id:
                print(" Find the student, now start modifying")
                while True:
                    try:
                        d['name'] = input('Please input name:')
                        d['English'] = input("Please input English grade: ")
                        d['Python'] = input("Please input Python grade: ")
                        d['Java'] = input("Please input Java grade: ")
                    except:
                        print('wrong input, please input again')
                    else:
                        break

                wfile.write(str(d)+'\n')
                print('modefy successfully')
            else:
                wfile.write(str(d)+'\n')
        answer = input("Do you need to modify another student information? y/n\n")
        if answer == 'y' or answer == 'Y':
            modify()


def sort():
    student_list = []
    if os.path.exists(filename):
        with open(filename, 'r', encoding='utf-8') as rfile:
            students = rfile.readlines()

        for item in students:
            student_list.append(dict(eval(item)))
        if student_list:
            print('Please choose sorting method:\n')
            print('\t\t\t1. by Id')
            print('\t\t\t2. by name')
            print('\t\t\t3. by English Grade')
            sort_way = input()
            asc_or_desc = input('ascend(1) or descend(2)?\n')
            if asc_or_desc=='1':
                asc_or_desc == False
            elif asc_or_desc=='2':
                asc_or_desc == True
            else:
                print('Sorry, your input is wrong, please input again')
                sort()
            if sort_way == '1':
                student_list.sort(key=lambda x: int(x['Id']), reverse=asc_or_desc)
            elif sort_way == '2':
                student_list.sort(key=lambda x: int(x['name']), reverse=asc_or_desc)
            elif sort_way == '3':
                student_list.sort(key=lambda x: int(x['English']), reverse=asc_or_desc)
            else:
                print('Sorry, your input is wrong, please input again')
                sort()

    else:
        print("There is no student in database")

    show_student(student_list)

def total():
    if os.path.exists(filename):
        with open(filename,'r',encoding='utf-8') as rfile:
            students = rfile.readlines()
            if students:
                print(f" There are {len(students)} students in database")
            else:
                print("There is no student in database")
    else:
        print("There is no student in database")

def show():
    student_list = []
    if os.path.exists(filename):
        with open(filename,'r',encoding='utf-8') as rfile:
            students = rfile.readlines()
            for item in students:
                student_list.append(eval(item))
            if student_list:
                # print(student_list)
                show_student(student_list)
            else:
                print("There is no student in database")
    else:
        print("There is no student in database")


# Press the green button in the gutter to run the script.

if __name__ == '__main__':
    main()

