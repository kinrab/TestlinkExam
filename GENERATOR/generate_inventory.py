
# Параметры для запуска: generate_inventory.py -n 3 -f data/inventory_data.json
#
#  n 3 - число групп которые нужно сгенерировать генератору
#  f data/invwntory_data.json - имя файла и папка в которой он находится

# Как запустить генератор из командной строки чтобы он нашел import:
#    python -m generator.generate_inventory

from DATA.data_inventory import *
import os.path
import jsonpickle
import getopt
import sys

########################################################################################################################
#  ОСНОВНОЙ КОД ЗАПУСКА:
########################################################################################################################

# Параметры по умолчанию устанавливаем на случай если не указаны они в командной строке:
# n число записей и f - имя файла
n = 7
f = "data/inventory_data.json" # Или f = r"data\groups7.json" но универсальнее обратный слэш использовать

# Берем параметры из командной строки
try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["numberofinventory","file"] )
except getopt.GetoptError as Err:
    getopt.usage()
    sys.exit(2)

# Если параметры есть, то читаем:
for o , a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a

# Теперь создается структура данных длинной n элементов:
test_data = [
             Inventory
             (
                 Inventory_Hostname= random_string("Name:", 20),
                 Inventory_IPaddress = generate_random_ip(),
                 Inventory_Owner ="testmanager",                                           # Этот элемент не буду менять.
                 Inventory_Purpose = random_string("Purpose:", 20),
                 Inventory_Hardware="Vegman R320",
                 Inventory_Notes= random_string("Notes:", 40)

             ) for _ in range(n)]

# Формируем имя файла и путь к нему для записи в него данных:
data_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)

# Открываем файл и пишем в него данные в формате JSON - а структура управления кодом "with" сама закроет файл
with open(data_file,"w") as data_f:
    jsonpickle.set_encoder_options("json", indent = 2)
    data_f.write( jsonpickle.encode(test_data))
