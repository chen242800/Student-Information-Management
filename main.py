# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

fileanme = "student.txt"
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

        student = {'Id': id, 'name': name, 'English': english, 'Python': python, 'java': java}
        student_list.append(student)

        answer = input(" Do you want add another student? y/n\n")
        if answer == 'y' or answer == 'Y':
            continue
        else:
            break

        save(student_list)

def save(lst):
    try:
        stu_txt = open(fileanme, 'a', encoding='utf-8')
    except:
        stu_txt = open(fileanme, 'w', encoding="utf-8")
    for item in lst:
        stu_txt.write(str(item)+'\n')
    stu_txt.close()

def search():
    pass


def delete():
    pass


def modify():
    pass


def sort():
    pass


def total():
    pass


def show():
    pass


# Press the green button in the gutter to run the script.

if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
