#!/usr/bin/env python3

# Создаем пустой словарь для хранения данных
data_dict = {}

# Открываем исходный файл для чтения
with open("CalemMsg_ru.properties", "r") as input_file:
    # Открываем целевой файл для записи
    with open("CalemMsg.properties.out", "w") as output_file:
        # Читаем каждую строку из исходного файла и записываем её в целевой файл
        for line in input_file:
            strline = line.strip()
            if len(strline) > 0:
                if strline[0] == '#':
                    output_file.write(line)
                else:
                    index = strline.find('=')
                    # Выводим индекс первого вхождения '='
                    if (index > 0):
                        if len(strline) > (index + 1):
                            value = strline[(index+1):].strip()
                        else:
                            value = ""
                        # Добавляем ключ и значение в словарь
                        key = strline[:(index)].strip()
                        data_dict[key] = value
                        outline = "{key}={value};\n"
                        output_file.write(outline.format(key = key, value = value))
            else:
                output_file.write('\n')


# Выводим преобразованный в словарь файл
# print(data_dict)