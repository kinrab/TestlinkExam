
from DATAMODEL.inventory_data_model import Inventory
import pymysql
import re

config = {
    'host': '127.0.0.1',
    'user': 'root',
    'password': '',
    'database': 'testlink',
    'charset': 'utf8mb4',
    'autocommit': True,                                # Важно: подтверждаем всё сразу
    'cursorclass': pymysql.cursors.DictCursor       # Данные в виде {'id': 1, 'name': '...'
}

class DbFixture:

    def __init__(self, host, name, user, password):
        self.host = host,
        self.name = name,
        self.user = user,
        self.password = password

        #self.connection = pymysql.connect(**config)


    def Get_inventory_list(self):

        list = []

        # 1. Сбрасываем состояние транзакции, чтобы увидеть свежие данные
        #self.connection.rollback()

        connection = pymysql.connect(**config)

        try:
            with connection.cursor() as cursor:

                # На всякий случай сбрасываем состояние
                connection.rollback()

                cursor.execute("select name, ipaddress, owner_id, content from inventory")

                rows = cursor.fetchall()

                for row in rows:

                    hostname = row['name']
                    ipaddress = row['ipaddress']
                    owner = row['owner_id']
                    content = row['content']

                    # СОдержимое поля content: Из него нужно извлечь Purpose Hardware Notes
                    # a: 3:{s: 5: "notes";s: 23:"Notes:uhVD0vLhaRtDcKsR2";7:"purpose";s: 20:"Purpose:fRbuiqc0Oejt"; s: 8:"hardware"; s: 11:"Vegman R320";}

                    notes = re.search(r'Notes:[^"]+', content).group()
                    purpose = re.search(r'Purpose:[^"]+', content).group()
                    hardware = re.search(r'Vegman R320', content).group()

                    if owner == 2:
                        ownername = 'testmanager'
                    else:
                        ownername = 'admin'

                    list.append(Inventory(Inventory_Hostname=hostname,
                                          Inventory_IPaddress=ipaddress,
                                          Inventory_Owner=ownername,
                                          Inventory_Purpose=purpose,
                                          Inventory_Hardware=hardware,
                                          Inventory_Notes=notes
                                          )
                                )

        finally:
            connection.commit()
            connection.close()

        return list

    def destroy(self):

        pass

        # self.connection.close()
        #pass #self.connection.close()


    def Get_count_of_inventory(self):

        list = []

        count = -1 # Будет означать ошибку

        # 1. Сбрасываем состояние транзакции, чтобы увидеть свежие данные
        #self.connection.rollback()

        connection = pymysql.connect(**config)

        try:
            with connection.cursor() as cursor:

                # На всякий случай сбрасываем состояние
                connection.rollback()

                cursor.execute("select COUNT(*) from inventory")

                rows = cursor.fetchall()

                count = rows[0]['COUNT(*)']

        finally:
            connection.commit()
            connection.close()

        # -1 - будем считать неопределенным ответом и ошибкой.

        return count

