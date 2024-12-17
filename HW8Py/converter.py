import csv

def load_csv(file_path):
    # Загружаем данные из CSV-файла:
    with open(file_path, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        return list(reader)

def parse_customer_data(data):
    # Парсим данные о покупателе и формируем текстовое описание:
    descriptions = []
    for entry in data:
        description = format_description(entry)
        description = ' '.join(description.split())
        descriptions.append(description)
    return descriptions

def format_description(entry):
    # формируем текстовое описание на основе атрибутов покупателя:
    full_name = entry.get('name', 'Неизвестно')
    gender = entry.get('sex', 'Неизвестно')
    age = entry.get('age', 'Неизвестно')
    amount_spent = entry.get('bill', 'Неизвестно')
    device = entry.get('device_type', 'Неизвестно')
    browser = entry.get('browser', 'Неизвестно')
    region = entry.get('region', 'Неизвестно')

    return (f"Пользователь {full_name} {format_gender(gender)} пола, {age} лет совершил{get_suffix(gender)} "
            f"покупку на {amount_spent} у.е. с {format_browser_type(device)} браузера {browser}."
            f"{format_region(region)}")

def format_gender(sex):
    #форматируем пол пользователя для описания
    if sex == 'female':
        return 'женского'
    elif sex == 'male':
        return 'мужского'
    else:
        return 'Неправильный пол!'

def get_suffix(sex):
    #определяем суффикс для глагола в описании
    if sex == 'женского':
        return 'а'
    else:
        return ''
    
def format_browser_type(device):
    #форматируем тип браузера для описания
    if device == 'mobile' or device == 'tablet':
        return 'мобильного'
    elif device == 'laptop' or device == 'desktop':
        return 'десктопного'
    else:
        return ''
def format_region(region):
    #определяем есть ли данные о регионе. Если есть, то отображаем текстовую информацию.
    if region == '-':
        return ''
    else:
        return f' Регион, из которого совершалась покупка: {region}.'

def save_to_txt(descriptions, output_file):
    # сохраняем описания в TXT-файл:
    with open(output_file, mode='w', encoding='utf-8') as file:
        for description in descriptions:
            file.write(description + '\n')

def main(input_csv, output_txt):
    # основная функция программы:
    customer_data = load_csv(input_csv)
    descriptions = parse_customer_data(customer_data)
    save_to_txt(descriptions, output_txt)

if __name__ == "__main__":
    input_csv_file = "/home/dartmew/Documents/Projects/Univer/Python/HW8Py/web_clients_correct.csv"
    output_txt_file = "HW8Py/customer_descriptions.txt"
    main(input_csv_file, output_txt_file)