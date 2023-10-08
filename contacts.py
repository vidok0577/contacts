# Читаем адресную книгу в формате CSV в список contacts_list:
import csv
import re
from pprint import pprint

with open("phonebook_raw.csv", encoding='utf8') as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)


# 1. Выполните пункты 1-3 задания.
# Ваш код

lst = []
lst.append(contacts_list[0])

for contact in contacts_list[1:]:
    fio = (' '.join(contact[:3])).split() + ['']

    current_person = fio[:3] + contact[3:7]
    pattern = r"(\+7|8)\s*\(?(\d{3})\)?[\s-]?(\d{3})[\s-]?(\d{2})[\s-]?(\d{2})\s*\(?[а-я\.]*[\s\)]?(\d*)\)?"
    repl = r'+7(\2)\3-\4-\5 доб.\6' if 'доб' in current_person[5] else r'+7(\2)\3-\4-\5'
    current_person[5] = re.sub(pattern, repl, current_person[5])

    for index, item in enumerate(lst):

        if fio[0] in item and fio[1] in item:
            for i in range(3, 7):
                if current_person[i]:
                    lst[index][i] = current_person[i]
            break
    else:
        lst.append(current_person)


# 2. Сохраните получившиеся данные в другой файл.
# Код для записи файла в формате CSV:
with open("phonebook.csv", "w") as f:
    datawriter = csv.writer(f, delimiter=",")

    # Вместо contacts_list подставьте свой список:
    datawriter.writerows(lst)
