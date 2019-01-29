import employeeClass


def main():

    print("---------------------------------------------------------")
    E1 = employeeClass.Employee('name', 'id', 'department', 'title')
    E1.set_NAME('Susan Meyers')
    E1.set_ID('47899')
    E1.dept('Accounting')
    E1.titleSet('Vice President')
    print(E1)
    print("---------------------------------------------------------")
    E2 = employeeClass.Employee('name', 'id', 'department', 'title')
    E2.set_NAME('Mark Jones')
    E2.set_ID('39119')
    E2.dept('IT')
    E2.titleSet('Programmer')
    print(E2)
    print("---------------------------------------------------------")
    E3 = employeeClass.Employee('name', 'id', 'department', 'title')
    E3.set_NAME('Joy Rogersr')
    E3.set_ID('81774')
    E3.dept('Manufacturing')
    E3.titleSet('Engineer')
    print(E3)
    print("---------------------------------------------------------")

main()
