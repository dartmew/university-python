import re

def validate_car_id(car_id):
    pattern = r'^[АЕЁИКЛМНОРСТУХ]{1}\d{3}[АЕЁИКЛМНОРСТУХ]{2}\d{2,3}$'
    
    match = re.match(pattern, car_id)
    if match:
        number = car_id[:-2]
        region = car_id[-2:]
        return f"Номер {number} валиден. Регион: {region}."
    else:
        return "Номер не валиден."

print(validate_car_id(input("Введите номер машины: ")))
