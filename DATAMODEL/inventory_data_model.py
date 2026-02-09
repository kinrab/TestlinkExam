from ipaddress import ip_address

########################################################################################################################################################################################
# Класс для хранения сущности Inventory - тестовых стендов для тестирования
########################################################################################################################################################################################

class Inventory:

    ####################################################################################################################
    # Конструктор класса Inventory
    ####################################################################################################################

    def __init__(self, Inventory_Hostname = None, Inventory_IPaddress = None, Inventory_Owner = None,
                       Inventory_Purpose = None,Inventory_Hardware = None, Inventory_Notes = None):

        self.Inventory_Hostname = Inventory_Hostname
        self.Inventory_IPaddress = Inventory_IPaddress
        self.Inventory_Owner = Inventory_Owner
        self.Inventory_Purpose = Inventory_Purpose
        self.Inventory_Hardware = Inventory_Hardware
        self.Inventory_Notes = Inventory_Notes

    ####################################################################################################################
    #  Метод для вывода на печать всех свойств элемента класса Inventory
    ####################################################################################################################

    def __repr__(self):

        return "%s:%s:%s:%s:%s:%s" % ( self.Inventory_Hostname, self.Inventory_IPaddress, self.Inventory_Owner, self.Inventory_Purpose, self.Inventory_Hardware, self.Inventory_Notes )

    ####################################################################################################################
    #  Определение операции сравнения экземпляров класса (сравниваем все)
    ####################################################################################################################

    def __eq__(self, other):
        if not isinstance(other, Inventory):
            return False
        return (self.Inventory_Hostname == other.Inventory_Hostname and
                self.Inventory_IPaddress == other.Inventory_IPaddress and
                self.Inventory_Owner == other.Inventory_Owner and
                self.Inventory_Purpose == other.Inventory_Purpose and
                self.Inventory_Hardware == other.Inventory_Hardware)

    ####################################################################################################################
    #  Определение операции для сортировки
    ####################################################################################################################

    def __lt__(self, other):

        # Превращаем строки в объекты IP для корректного сравнения
        self_ip = ip_address(self.Inventory_IPaddress)
        other_ip = ip_address(other.Inventory_IPaddress)

        if self.Inventory_Hostname != other.Inventory_Hostname:
            return self.Inventory_Hostname < other.Inventory_Hostname

        return self_ip < other_ip
