from applications.salary import calculate_salary
from applications.db.people import get_employee
from datetime import datetime

print(datetime.date(datetime.now()))

if __name__ == '__main__':
    calculate_salary()
    get_employee()