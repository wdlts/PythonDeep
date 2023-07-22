import time

def validate_date():
    date = input('Date (dd.mm.yyyy): ')
    try:
        valid_date = time.strptime(date, '%d.%m.%Y')
        print("Date is OK!")
    except ValueError:
        print('Invalid date!')

validate_date()

