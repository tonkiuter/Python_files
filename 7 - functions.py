month_days = [0,31,28,31,30,31,30,31,31,30,31,30,31]

def hello_func(greeting, name= 'okaru'):
    print('{},{}'.format(greeting, name))

def student_info(*args, **kwargs):
    print(args)
    print(kwargs)


courses = ['Art', 'Science', 'History']

info = {'name': 'Alvaro', 'age': 23, }

student_info(*courses, **info)

#--------------------------------------------------------------------------------------



def is_leap(year):

    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0 )

def days_of_month(year, month):
    
    if not 1 <= month <=12:
        return 'Invalid Month'

    if month == 2 and is_leap(year):
        return 29

    return month_days[month]

print(days_of_month(2020, 2))