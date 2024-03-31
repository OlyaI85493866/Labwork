import csv

while True: #объявление цикла. В случае, если номер не будет найден, пользователю будет предлагаться повторно ввести ФИО
    with open('FIOandTelephone.csv', 'r', encoding="utf-8-sig") as r: #открытие файла
        text = csv.DictReader(r)
        n = input("Введите имя (введите команду stop, если хотите прекратить ввод): ")
        if n == 'stop':
            break
        found = False
        for row in text: #объявление цикла
            if row['FIO'] == n: #поиск данных
                print(f"Найден номер телефона: {row['Telephone']}")
                found = True
                break
        if not found:
            print("Номер телефона не найден. Пожалуйста, попробуйте снова.")
        else:
            break
