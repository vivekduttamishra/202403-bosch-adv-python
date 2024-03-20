import random

class Employee:
    def __init__(self, name, salary, isPermanent=True):
        self._name = name
        self._salary = salary
        self._id=None
        self._organization=None
        self._isPermanent=isPermanent

    def __str__(self):
        if self:
            return f'{self._organization} Employee#{self._id} {"*" if self._isPermanent else "x"} Name={self._name} Salary={self._salary}'
        else:
            return f' Unemployeed {self._name}'
        
    def __bool__(self):
        return self._id!=None  and self._organization!=None and isinstance(self._organization,Organization)
   
   
class Organization:
    def __init__(self,name):
        self._name=name
        self._last_id=0
        self._employees=[]

    def __str__(self):
        return self._name
    
    def add_employee(self, employee):
        if not isinstance(employee,Employee):
            raise ValueError(f"{type(employee).__name__} not an Employee")
        else:
            self._last_id+=1
            employee._id=self._last_id
            employee._organization=self
            self._employees.append(employee)
            return employee

    def __iter__(self):
        return Organization.EmployeeIterator(self._employees)

    class EmployeeIterator:
        def __init__(self,employees):
            self._employees=employees
            #always start before first. you reach first on next call
            self._current=-1

        def __next__(self):
            
            while True:
                self._current+=1
                if self._current>=len(self._employees):
                    raise StopIteration()
                #if self._employees[self._current]._isPermanent:
                return self._employees[self._current]
                


def get_organization(name, emp_count):
    org=Organization(name)
    for i in range(emp_count):
        salary=random.randint(20,50)*1000
        isPermanent= random.randint(0,100)<70
        org.add_employee(Employee(f'Employee{i}', salary, isPermanent))
    return org