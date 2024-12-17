import re

def remove_consecutive_duplicates(some_string):
    result = re.sub(r'\b(\w+)\s+\1\b', r'\1', some_string)
    return result

some_string = input("Введите последовательность слов: ")
print(remove_consecutive_duplicates(some_string))