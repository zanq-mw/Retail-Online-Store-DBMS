import cx_Oracle
from queries import *
from config import *

class DatabaseCmds:
    # Creates the tables
    def create_tables(self, cursor, connection):
        try:
            for query in create_tables_qs:
                cursor.execute(query)
                connection.commit()
            print("All tables have been created")
        except Exception as e:
            print(e)

    # Drops the tables 
    def drop_tables(self, cursor, connection):
        try:
            for query in drop_tables_qs:
                cursor.execute(query)
                connection.commit()
            print("All tables have been dropped")
        except Exception as e:
            print(e)

    # Populates tables with example data               
    def populate_tables(self, cursor, connection):
        try:
            for query in populate_tables_qs:
                cursor.execute(query)
                connection.commit()
            print("All tables have been populated")
        except Exception as e:
            print(e)
 
    # Query all results from within a table, takes user input for which table        
    def query_tables(self, cursor, table):
        try:
            query = f"SELECT * FROM {table}"
            cursor.execute(query)
            records = cursor.fetchall()

            if len(records) == 0:
                print(f"{table} is empty")

            for record in records:
                temp = ''
                for col in record:
                    temp += f'{col}\t'
                print(temp)

        except Exception as e:
            print(e)
    
    # Query a specific index from a table, user enters the table name, then the primary key/ID of the index they want to view
    def query_spec_row(self, cursor, table):
        try:
            columns = self.getColumns(table.upper(), cursor)
            
            if table == 'PURCHASEITEM': 
                pk1Value = input(f"Enter the purchaseId value for {table} row you want to see: ")
                pk2Value = input(f"Enter the productVariantId value for {table} row you want to see: ")
            
                query = f"""SELECT * FROM {table}
                            WHERE purchaseId = {pk1Value} AND productVariantId = {pk2Value}"""
                cursor.execute(query)
            else:
                PK = columns[0][0]
                pkValue = input(f"Enter the {PK} value for {table} row you want to see: ")
                query = f"""SELECT * FROM {table}
                            WHERE {PK} = {pkValue}"""
                cursor.execute(query)

            records = cursor.fetchall()

            for record in records:
                temp = ''
                for col in record:
                    temp += f'{col}\t'
                print(temp)

        except Exception as e:
            print(e)

    # Add a row to a specified table
    def add_row(self, cursor, table):
        try:
            columns = self.getColumns(table.upper(), cursor)
            cols = ''

            for column in columns:
                cols += column[0] + ', '

            values = input(f"Enter values seperated by commas for {cols[:-2]}: ").replace('"', "'")
            query = f"""INSERT INTO {table} VALUES ({values})"""
            cursor.execute(query)
            print("Row added")
        except Exception as e:
            print(e)

    # Update the values for a specified row in a specified table
    def update_row(self, cursor, table):
        try:
            columns = self.getColumns(table.upper(), cursor)

            if table == 'PURCHASEITEM': 
                pk1Value = input(f"Enter the purchaseId value for {table} row you want to update: ")
                pk2Value = input(f"Enter the productVariantId value for {table} row you want to update: ")
                quantity = input(f"Enter the new quantity value: ")
                query = f"""UPDATE PurchaseItem
                            SET quantity = {quantity}
                            WHERE purchaseId = {pk1Value} AND productVariantId = {pk2Value}"""
                cursor.execute(query)
            else:
                PK = columns[0][0]
                pkValue = input(f"Enter the {PK} value for {table} row you want to update: ")
                
                for i in range(1, len(columns)):
                    value = input(f"Enter value for {columns[i][0]}: ")
                    query = f"""UPDATE {table}
                                SET {columns[i][0]} = {value}
                                WHERE {PK}={pkValue}"""
                    cursor.execute(query)

            print("Row updated")

        except Exception as e:
            print(e)

    # Delete a specified row from a specified table, user inputs which table and index to delete
    def delete_row(self, cursor, table):
        try:
            columns = self.getColumns(table.upper(), cursor)

            if table == 'PURCHASEITEM': 
                pk1Value = input(f"Enter the purchaseId value for {table} row you want to delete: ")
                pk2Value = input(f"Enter the productVariantId value for {table} row you want to delete: ")
            
                query = f"""DELETE PurchaseItem
                            WHERE purchaseId = {pk1Value} AND productVariantId = {pk2Value}"""
                cursor.execute(query)
            else:
                PK = columns[0][0]
                pkValue = input(f"Enter the {PK} value for {table} row you want to delete: ")
                query = f"""DELETE FROM {table}
                            WHERE {PK} = {pkValue}"""
                cursor.execute(query)

            print("Row deleted")

        except Exception as e:
            print(e)

    # Get column names of a given table
    def getColumns(self, table, cursor):
        columns_q = f"""SELECT column_name
                FROM USER_TAB_COLUMNS
                WHERE table_name = '{table}'"""
        cursor.execute(columns_q)
        
        return cursor.fetchall()
        
# Connects to Oracle DB
def connectToDB():
    cx_Oracle.init_oracle_client(lib_dir=lib_dir)
    dsn = cx_Oracle.makedsn(host=host, port=port, sid=sid)
    connection = cx_Oracle.connect(user=user, password=password, dsn=dsn)
    cursor = connection.cursor()

    print("You're connected")
    return (connection, cursor)
    
# Main application
def startApp():
    printCommands()
    connection, cursor = connectToDB()
    quit = False
    DB = DatabaseCmds()

    while not quit:
        cmdline = input("> ").split()
        command = cmdline[0].lower()

        if command == 'c':
            DB.create_tables(cursor, connection)
        if command == 'd':
            DB.drop_tables(cursor, connection)
        if command == 'p':
             DB.populate_tables(cursor, connection)
        if command == 'q':
            if len(cmdline) == 1:
                print("Missing {table} parameter. Please try again")
            else:
                DB.query_tables(cursor, cmdline[1])
        if command == 'qspec':
            if len(cmdline) == 1:
                print("Missing {table} parameter. Please try again")
            else:
                DB.query_spec_row(cursor, cmdline[1].upper())
        if command == 'add':
            if len(cmdline) == 1:
                print("Missing {table} parameter. Please try again")
            else:
                DB.add_row(cursor, cmdline[1])
        if command == 'upd':
            if len(cmdline) == 1:
                print("Missing {table} parameter. Please try again")
            else:
                DB.update_row(cursor, cmdline[1].upper())
        if command == 'del':
            if len(cmdline) == 1:
                print("Missing {table} parameter. Please try again")
            else:
                DB.delete_row(cursor, cmdline[1].upper())
        if command == 'quit':
            quit = True
            print("Goodbye!")
            cursor.close()
            connection.close()

def printCommands():
    print('c = Create all tables')
    print('d = Delete all tables')
    print('p = Populate all tables')
    print('q {table} = Query all entires of a table')
    print('qspec {table} = Query specific row from a table')
    print('add {table} = Add row to a table')
    print('upd {table} = Update a row in a table')
    print('del {table} = Delete row from a table')
    print('quit = Quit application')

if __name__ == "__main__":
    startApp()
