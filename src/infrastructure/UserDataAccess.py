import mysql.connector
import os
from src.entities.User import User_Get_Response


class UserDataAccess:
    conf = {
        'user': os.environ["DB_USERNAME"],
        'password': os.environ["DB_PASSWORD"],
        'host': os.environ["DB_HOST"],
        'database': os.environ["DB_NAME"]
    }

    def get_user(self, filter=None):
        cursor = None
        conn = None
        return_value = []
        try:
            conn = mysql.connector.connect(**self.conf)
            cursor = conn.cursor()
            cursor.callproc("get_users", (filter, ))

            for result in cursor.stored_results():
                users = result.fetchall()
                for row in users:
                    return_value.append(User_Get_Response(row[1], row[2], row[3], row[4], row[5], row[6]))

            cursor.close()
            conn.commit()
            conn.close()

            return return_value

        except Exception as e:
            print("Error: ")
            print(e)

            if cursor:
                cursor.close()
            if conn:
                conn.close()
            return []



    def update_user(self, user):
        cursor = None
        conn = None
        try:
            conn = mysql.connector.connect(**self.conf)
            cursor = conn.cursor()
            cursor.callproc("update_user", (user.email, user.phone_number, user.full_name, user.password.hashed_password, user.password.password_salt, user.key, user.account_key, user.metadata) )

            for recordset in cursor.stored_results():
                for row in recordset:
                    p = row[0]
                    break;
            cursor.close()
            conn.commit()
            conn.close()
            return p

        except Exception as e:
            print("Error: ")
            print(e)
            if cursor:
                cursor.close()
            if conn:
                conn.close()
            return -1

    def connect_to_db(self):
        cursor = None
        conn = None
        try:
            conn = mysql.connector.connect(**self.conf)
            cursor = conn.cursor()

            cursor.close()
            conn.commit()
            conn.close()

            return True

        except Exception as e:
            print("Error: ")
            print(e)
            return False