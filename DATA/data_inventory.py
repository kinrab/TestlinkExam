from DATAMODEL.inventory_data_model import Inventory
import random
import string

n = 3 # Генерируем три элемента для test_data

constant_data =\
[
            Inventory(Inventory_Hostname="Test1",  Inventory_IPaddress="192.168.1.100", Inventory_Owner="testmanager", Inventory_Purpose="Purpose #1", Inventory_Hardware="Vegman R320",  Inventory_Notes="Cтенд №1"),
            Inventory(Inventory_Hostname="Test2",  Inventory_IPaddress="192.168.1.101", Inventory_Owner="testmanager", Inventory_Purpose="Purpose #2", Inventory_Hardware="Vegman R320",  Inventory_Notes="Cтенд №2"),
            Inventory(Inventory_Hostname="Test3",  Inventory_IPaddress="192.168.1.102", Inventory_Owner="testmanager", Inventory_Purpose="Purpose #3", Inventory_Hardware="Vegman R320",  Inventory_Notes="Cтенд №3"),
            Inventory(Inventory_Hostname="Test4",  Inventory_IPaddress="192.168.1.103", Inventory_Owner="testmanager", Inventory_Purpose="Purpose #4", Inventory_Hardware="Vegman R320",  Inventory_Notes="Cтенд №4"),
            Inventory(Inventory_Hostname="Test5",  Inventory_IPaddress="192.168.1.104", Inventory_Owner="testmanager", Inventory_Purpose="Purpose #5", Inventory_Hardware="Vegman R320",  Inventory_Notes="Cтенд №5"),
            Inventory(Inventory_Hostname="Test6",  Inventory_IPaddress="192.168.1.105", Inventory_Owner="testmanager", Inventory_Purpose="Purpose #6", Inventory_Hardware="Vegman R320",  Inventory_Notes="Cтенд №6"),
            Inventory(Inventory_Hostname="Test7",  Inventory_IPaddress="192.168.1.106", Inventory_Owner="testmanager", Inventory_Purpose="Purpose #7", Inventory_Hardware="Vegman R320",  Inventory_Notes="Cтенд №7"),
            Inventory(Inventory_Hostname="Test8",  Inventory_IPaddress="192.168.1.107", Inventory_Owner="testmanager", Inventory_Purpose="Purpose #8", Inventory_Hardware="Vegman R320",  Inventory_Notes="Cтенд №8"),
            Inventory(Inventory_Hostname="Test9",  Inventory_IPaddress="192.168.1.108", Inventory_Owner="testmanager", Inventory_Purpose="Purpose #9", Inventory_Hardware="Vegman R320",  Inventory_Notes="Cтенд №9"),
            Inventory(Inventory_Hostname="Test10", Inventory_IPaddress="192.168.1.109", Inventory_Owner="testmanager",Inventory_Purpose="Purpose #10", Inventory_Hardware="Vegman R320",  Inventory_Notes="Cтенд №10")
]

########################################################################################################################
# Функция генерирует случайные строик с заданным в переменной prefix префиксом и длинной не более maxlen
########################################################################################################################
def random_string (prefix, maxlen):

    symbols_list =  string.ascii_letters + string.digits
    return prefix + "".join( [ random.choice(symbols_list) for i in range(random.randrange(10, maxlen)) ] )

########################################################################################################################
# Функция генерирует случайное число от 1 до 254
########################################################################################################################

def random_digit(min_val=1, max_val=254):

    return str(random.randint(min_val, max_val))

########################################################################################################################
# Функция Генерирует случайный IPv4 адрес, соединяя 4 случайных числа точками.  Используем random_string
########################################################################################################################

def generate_random_ip():

    return ".".join([random_digit() for _ in range(4)])

# Вариант 1: генеируем данные для теста модификации элементов
test_data_a = [
             Inventory
             (
                 Inventory_Hostname= random_string("Name:", 20),
                 Inventory_IPaddress = generate_random_ip(),
                 Inventory_Owner ="testmanager",                                           # Этот элемент не буду менять.
                 Inventory_Purpose = random_string("Purpose:", 20),
                 Inventory_Hardware="Vegman R320",
                 Inventory_Notes= random_string("Notes:", 40)

             ) for _ in range(n)]



# Вариант 2: с перебором комбинаторным
# test_data = [
#                    Group(group_name = name, group_header = footer, group_footer = header)
#                    for name in ["", random_string("name",10)]
#                    for header in ["", random_string("header",20)]
#                    for footer in ["", random_string("footer",20)]
# ]

