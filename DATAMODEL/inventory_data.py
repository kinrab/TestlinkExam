
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
    #  Определение операции сравнения экземпляров класса (сравниваем все кроме Notes!)
    ####################################################################################################################

    def __eq__(self, other):

        return  (self.Inventory_Hostname == other.Inventory_Hostname) and (self.Inventory_IPaddress == other.Inventory_IPaddress) and (self.Inventory_Owner== other.Owner) \
                (self.Inventory_Purpose == other.Inventory_Purpose) and (self.Inventory_Hardware == other.Inventory_Hardware)

