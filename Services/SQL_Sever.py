class SQLSever:
    class_name = "SQL_Sever"
    class_variable = 1

    def __init__(self, IP, connection, cursor):
        self.IP = IP
        self.connection = connection
        self.cursor = cursor

    def instane_method(self):
        print('This returns something specific to the instance of the class')

    def class_metho(cls):
        print('This returns something that applies to the whole class')

    def static_method():
        print('This returns something that always returns specific output')
    
    def init_server(self, sqlite3):
        self.connection = sqlite3.connect('password_database.db')
        self.cursor = self.connection.cursor()


def main():
    a = 0

if __name__ == "__main__":
    main()
    print(
        "this main only runs if this file is ran, not if another program executes it: SQL_Sever"
    )