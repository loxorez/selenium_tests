import pymysql.cursors


class OxwallDB(object):
    def __init__(self):
        self.connection = pymysql.connect(host='localhost',
                                          user='root',
                                          password='mysql',
                                          db='oxwall4',
                                          charset='utf8mb4',
                                          cursorclass=pymysql.cursors.DictCursor)

    def close(self):
        self.connection.close()

    def get_users(self):
        with self.connection.cursor() as cursor:
            # Read a single record
            sql = "SELECT `id`, `username`, `password` FROM `ow_base_user`"
            cursor.execute(sql)
            result = cursor.fetchone()
            self.connection.commit()
        return result

    def create_users(self):
        with self.connection.cursor() as cursor:
            # Create a single record
            sql = f"""INSERT `ow_base_user` (`username`, `email`, `password`, `joinIp`)
                    VALUES ("tester", "tester324234@gmail.com", "3e532967bc4ef8f1777f77bef0e657e145f40915a8425931d2954e5a2f9ef225", "12322143123")
                    """
            cursor.execute(sql)
        self.connection.commit()

    def delete_users(self):
        with self.connection.cursor() as cursor:
            # Delete a single record
            sql = f"""DELETE FROM `ow_base_user` 
                    WHERE `ow_base_user`.`username` = "tester"
                    """
            cursor.execute(sql)
        self.connection.commit()

