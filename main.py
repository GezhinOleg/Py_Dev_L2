'''
Ваша задача: починить адресную книгу, используя регулярные выражения.
Структура данных будет всегда:
`lastname,firstname,surname,organization,position,phone,email`
Предполагается, что телефон и e-mail у человека может быть только один.
Необходимо:
1. поместить Фамилию, Имя и Отчество человека в поля lastname, firstname и surname соответственно. В записной книжке изначально может быть Ф + ИО, ФИО, а может быть сразу правильно: Ф+И+О;
2. привести все телефоны в формат +7(999)999-99-99. Если есть добавочный номер, формат будет такой: +7(999)999-99-99 доб.9999;
3. объединить все дублирующиеся записи о человеке в одну.
'''

from pprint import pprint
# читаем адресную книгу в формате CSV в список contacts_list
import csv
import re



def create_new_name_lst(contacts_list):
    contacts = []
    contacts2 = []

    contacts_set = set()
    for contact in contacts_list:
        name =' '.join(contact[0:3]).split(' ')[:3]
        contacts.append(name + contact[3:])

    for i in contacts:
        for j in contacts:
            if i[0] == j[0] and i[1] == j[1] and i is not j:
                if i[2] is '':
                    i[2] = j[2]
                if i[3] is '':
                    i[3] = j[3]
                if i[4] is '':
                    i[4] = j[4]
                if i[5] is '':
                    i[5] = j[5]
                if i[6] is '':
                    i[6] = j[6]
        contacts2.append(i)
    for i in contacts2:
        if i[0] not in contacts3:
            contacts3[i[0]] = i
    # print(contacts3)
    return contacts3



def make_phone_num():
    for phone in contacts3.values():
        pattern = r'(.*)[Д|д]об\.?\s*(\d+)'
        result = re.findall(pattern, phone[5])
        ext_no = None
        if len(result):
            ext_no = result[0][-1]
        pattern = r'[\+7|8]+[\s\-\(\)]*(\d*)[\s\-\(\)]*(\d*)[\s\-\(\)]*(\d*)[\s\-\(\)]*(\d*)'
        result = re.findall(pattern, phone[5])
        phone_no = '+7' + ''.join(result[0])
        if ext_no:
            phone_no += f' доб.{ext_no}'
        phone_no = phone_no[:2] + '(' + phone_no[2:5] + ')' + phone_no[5:8] + '-' + phone_no[8:10] + '-' + phone_no[10:]
        phone[5] = phone_no
    return contacts3

if __name__ == '__main__':
    with open("phonebook_raw.csv", encoding='utf-8') as f:
      rows = csv.reader(f, delimiter=",")
      contacts_list = list(rows)

    contacts3 = {}
    titles = contacts_list.pop(0)
    phones_name = create_new_name_lst(contacts_list)
    make_phone_num()

    finish_list = []
    finish_list.append(titles)
    for _ in contacts3.values():
        finish_list.append(_)
    print(finish_list)

    with open("phonebook.csv", "w", encoding='utf-8', newline='') as f:
      datawriter = csv.writer(f, delimiter=',')
      # Вместо contacts_list подставьте свой список
      datawriter.writerows(finish_list)
