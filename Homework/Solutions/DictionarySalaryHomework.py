employees =[
    {
        "name":"Tim Storer",
        "position" : "Lecturer",
        "hourlyRate" : 11 , 
        "hoursWorked" : 16

    },
    {
        "name" : "Harry Smith",
        "position" : "Shop Assistant",
        "hourlyRate" : 6, 
        "hoursWorked"  : 35

    },
    {
        "name" : "Sarah Jackson",
        "position" : "Senior Lecturer",
        "hourlyRate" : 15, 
        "hoursWorked" : 20

    },
    {
        "name" : "Kate Lewis",
        "position" : "Reception",
        "hourlyRate" : 8, 
        "hoursWorked" : 40

    },
    {
        "name" : "Julie Parker",
        "position" : "Cleaner",
        "hourlyRate" : 6, 
        "hoursWorked" : 40 

    }
]

#print a full list of our employees and their positons
#write a function to find the amount each employee is owed in wages.
#Kate Lewis is getting a  pay rise- increase her salary to 9 pound an hour.
#A new employee, Simon McDonald, is joining as a lecturer. His hourly rate will be 10 pounds an hour, and he works 24 hours a week. Please add him to the list.
#Harry Smith is leaving the school - remove him from the list.

#Keep in mind that lists stay ordered, but dictionaries do not.

def salaryCalculator():
    salaries = {}
    for employee in employees:
        salaries[employee["name"]] = (str)(employee["hourlyRate"] * employee["hoursWorked"])
    return salaries

def employeeList():
    for employee in employees:
        print ("Employeee: " + employee["name"])
        print ("Position: " + employee["position"])
    print("\n")

def salaryChange(employeeName, newSalary):
    for employee in employees:
        if employee["name"] == employeeName:
            employee["salary"] = newSalary
            print(employee["name"] +"'s new salary is: £" + (str)(employee["salary"]))

def addEmployee(name, positon, hourlyRate, hoursWorked):
    newEmployes = {"name": name, "position": positon, "hourlyRate": hourlyRate, "hoursWorked": hoursWorked}
    employees.append(newEmployes)

def removeEmployee(name):
    for employee in employees:
        if employee["name"] == name:
            employees.remove(employee)
    print (employees)
