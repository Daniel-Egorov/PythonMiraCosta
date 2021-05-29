"""
{
    "File": "finalProject3.py",
    "Author": "Daniel Egorov",
    "Date": "05/22/21",
    "Desc": [
        "employee system for mira costa"
    ],
    "Algorithm": [
        "use classes to create employees",
        "save all employee information in a json file",
        "allow the user to choose what they would like to do with the employees",
        "and run the respective functions to complete the action theyd like"
    ]
}

"""
import json


class Employee:
    def __init__(self, firstname, lastname, empID, classes):
        self.firstname = firstname
        self.lastname = lastname
        self.empID = empID
        self.classes = classes

    def getName(self):
        return f'{self.firstname} {self.lastname}'

class PartEmployee(Employee):
    def __init__(self, firstname, lastname, empID, classes):
        super().__init__(firstname, lastname, empID, classes)
        self.empType = 'part time'

    def getPaycheck(self):
        return len(classes) * 1000

class HourlyEmployee(Employee):
    def __init__(self, firstname, lastname, empID, classes, hourlyWage, monthlyHours):
        super().__init__(firstname, lastname, empID, classes)
        self.hourlyWage = hourlyWage
        self.monthlyHours = monthlyHours
        self.empType = 'hourly'

    def getPaycheck(self):
        return self.hourlyWage * self.monthlyHours

class FullEmployee(Employee):
    def __init__(self, firstname, lastname, empID, classes, monthlyWage):
        super().__init__(firstname, lastname, empID, classes)
        self.monthlyWage = float(monthlyWage)
        self.empType = 'full time'

    def getPaycheck(self):
        return self.monthlyWage

def dictToEmp(empID):
    with open('employees.json') as file:
        data = json.load(file)
    temp = data[empID]

    if temp['empType'] == 'hourly':
        employee = HourlyEmployee(temp['firstname'], temp['lastname'], temp['empID'], temp['classes'], temp['hourWage'], temp['monthlyHours'])
    elif temp['empType'] == 'part time':
        employee = PartEmployee(temp['firstname'], temp['lastname'], temp['empID'], temp['classes'])
    elif temp['empType'] == 'full time':
        employee = FullEmployee(temp['firstname'], temp['lastname'], temp['empID'], temp['classes'], temp['monthWage'])

    return employee


def add():
    with open('employees.json') as file:
        data = json.load(file)

    print('Adding new employee')
    firstname = input('First Name: ')
    lastname = input('Last Name: ')
    empID = input('ID: ')
    empType = input('Type (full time, part time, hourly): ')
    classes = []
    classinput = input('Classes (press enter after each class, type DONE when done):\n')
    while not classinput.upper() == 'DONE':
        classes.append(classinput.lower().capitalize())
        classinput = input()

    if empType.lower() == 'hourly':
        hourWage = float(input('Hourly Wage: '))
        monthlyHours = float(input('Hours per Month: '))
        employee = HourlyEmployee(firstname, lastname, empID, classes, hourWage, monthlyHours)

        data[empID] = {
                'firstname': firstname,
                'lastname': lastname,
                'empID': empID,
                'empType': 'hourly',
                'classes': classes,
                'hourWage': hourWage,
                'monthlyHours': monthlyHours,
                'paycheck': employee.getPaycheck()
            }

    elif empType.lower() == 'full time':
        monthWage = float(input('Monthly Salary: '))
        employee = FullEmployee(firstname, lastname, empID, classes, monthWage)

        data[empID] = {
                'firstname': firstname,
                'lastname': lastname,
                'empID': empID,
                'empType': 'full time',
                'classes': classes,
                'monthWage': monthWage,
                'paycheck': employee.getPaycheck()
            }

    elif empType.lower() == 'part time':
        employee = PartEmployee(firstname, lastname, empID, classes)
        data[empID] = {
                'firstname', firstname,
                'lastname', lastname,
                'empID', empID,
                'empType', 'part',
                'classes', classes,
                'paycheck', employee.getPaycheck()
            }

    decide = input('would you like to save this employee to the database?\n')
    if decide.lower() == 'yes':
        with open('employees.json', 'w') as file:
            json.dump(data, file, indent = 4)
    else:
        return


def remove():
    with open('employees.json') as file:
        data = json.load(file)
    empID = input('What is the ID of the employee?\n')
    employee = dictToEmp(empID)

    decide = input(f'You are about to remove {employee.getName()}, are you sure?\n')
    if decide.lower() == 'yes':
        del data[empID]
        with open('employees.json', 'w') as file:
            json.dump(data, file, indent = 4)
        print(f'{employee.getName()} was removed')
        return
    else:
        print('Employee wasnt removed')
        return


def edit():
    with open('employees.json') as file:
        data = json.load(file)

    tempID = input('What is the ID of the employee?\n')
    employee = dictToEmp(tempID)
    print('Type the new information if needed, press enter to leave unchanged')
    firstname = input(f'firstname: {employee.firstname} ')
    lastname = input(f'lastname: {employee.lastname} ')
    empID = input(f'ID: {employee.empID} ')
    empType = input(f'Type: {employee.empType} ')
    classes = input(f'Classes: {",".join(employee.classes)} ')

    if firstname == '':
        firstname = employee.firstname
    if lastname == '':
        lastname = employee.lastname
    if empID == '':
        empID = employee.empID
    if empType == '':
        empType = employee.empType
    if classes == '':
        classes = employee.classes
    elif classes != '':
        classes = classes.split(',')

    del data[tempID]
    if empType == 'hourly':
        if employee.empType != 'hourly':
            hourWage = float(input(f'Hourly Wage: 0 '))
            monthlyHours = float(input(f'Monthly Hours: 0 '))
        else:
            hourWage = float(input(f'Hourly Wage: {employee.hourWage} '))
            monthlyHours = float(input(f'Monthly Hours: {employee.monthlyHours} '))
        employee = HourlyEmployee(firstname, lastname, empID, classes, hourWage, monthlyHours)
        data[empID] = {
            'firstname': firstname,
            'lastname': lastname,
            'empID': empID,
            'empType': empType,
            'classes': classes,
            'hourWage': hourWage,
            'monthlyHours': monthlyHours,
            'paycheck': employee.getPaycheck()
        }

    elif empType == 'full time':
        if employee.empType != 'full time':
            monthlyWage = float(input(f'Monthly Wage: 0 '))
        else:
            monthlyWage = float(input(f'Monthly Wage: {employee.monthlyWage} '))

        employee = FullEmployee(firstname, lastname, empID, classes, monthlyWage)
        data[empID] = {
            'firstname': firstname,
            'lastname': lastname,
            'empID': empID,
            'empType': empType,
            'classes': classes,
            'monthWage': monthlyWage,
            'paycheck': employee.getPaycheck()
        }

    elif empType == 'part time':
        employee = PartEmployee(firstname, lastname, empID, classes)
        data[empID] = {
            'firstname': firstname,
            'lastname': lastname,
            'empID': empID,
            'empType': empType,
            'classes': classes,
            'paycheck': employee.getPaycheck()
        }

    decide = input('would you like to save these changes?\n')
    if decide.lower() == 'yes':
        with open('employees.json', 'w') as file:
            json.dump(data, file, indent = 4)


def view():
    with open('employees.json') as file:
        data = json.load(file)

    for empID in data.keys():
        employee = dictToEmp(empID)
        print(f'{employee.getName()}:')
        print(f'    ID: {employee.empID}')
        print(f'    Type: {employee.empType}')
        print(f'    Paycheck: {employee.getPaycheck()}')

def main():
    with open('employees.json') as file:
        data = json.load(file)

    print('Welcome to the employee database!')

    action = input('Would you like to add, remove, edit, or view employees?\n(type QUIT to exit)\n')

    while not action.lower() == 'quit':
        if action.lower() == 'add':
            add()
        elif action.lower() == 'remove':
            remove()
        elif action.lower() == 'edit':
            edit()
        elif action.lower() == 'view':
            view()
        action = input('Would you like to add, remove, edit, or view employees?\n(type QUIT to exit)\n')

main()