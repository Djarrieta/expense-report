import sqlite3
import uuid
from datetime import datetime

class Repository:
    table_name:str="spends"
    connection:any
    cursor:any

    def __init__(self):
        self.connection = sqlite3.connect("db.dp")
        self.cursor=self.connection.cursor()

        self.cursor.execute(f'''
                        CREATE TABLE IF NOT EXISTS {self.table_name} (
                            spend_id INT PRIMARY KEY,
                            description TEXT,
                            amount NUMERIC,
                            created TEXT
                        );
                    ''')

    def create_one(self, amount:int, description:str):

        spend_id=uuid.uuid1().int
        created=datetime.now().strftime("%y-%m-%d %H:%M:%S")
        mutation=f'''
                    INSERT INTO {self.table_name} VALUES 
                    ({spend_id}, '{description}', {amount}, '{created}');
                '''

        self.cursor.execute(mutation)
        self.connection.commit()

    def delete_by_id(self, spend_id:int):
        mutation=f'''
                    DELETE FROM {self.table_name} 
                    WHERE spend_id= {spend_id}
                '''

        self.cursor.execute(mutation)
        self.connection.commit()

    def get_all(self):
        query=f'''SELECT * FROM {self.table_name};'''

        self.cursor.execute(query)
        response=self.cursor.fetchall()
        
        return response
