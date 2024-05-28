from mysql.connector import Error
from abc import ABC, abstractmethod


class ABCTeacherDAO(ABC):

    @abstractmethod
    def insert(self, teacher):
        raise NotImplementedError()
   

    @abstractmethod
    def update(self, teacher_id, teacher):
        raise NotImplementedError()


    @abstractmethod
    def delete(self, teacher_id):
        raise NotImplementedError()
  

    @abstractmethod
    def get_one(self, teacher_id):
        raise NotImplementedError()
  


class TeacherImpl(ABCTeacherDAO):
    def __init__(self, connection):
        self.connection = connection

    def insert(self, teacher):
        cursor = self.connection.cursor()
        try:
            query = "INSERT INTO teachers (id, firstname, lastname) VALUES (%s , %s, %s)"
            cursor.execute(query, (teacher.id ,teacher.firstname , teacher.lastname))
            self.connection.commit()
            print(f"Inserted teacher: {teacher.lastname}")
        except Error as e:
            print(f"Error: {e}")
    


    def get_one(self, teacher_id):
        cursor = self.connection.cursor()
        try:
            query = "SELECT * FROM teachers WHERE id = %s"
            cursor.execute(query, (teacher_id,))
            return cursor.fetchone()
        except Error as e:
            print(f"Error: {e}")
            return None


    def update(self, teacher_id, teacher):
        cursor = self.connection.cursor()
        try:
            query = "UPDATE teachers SET firstname = %s,lastname = %s  WHERE id = %s"
            cursor.execute(query, (teacher.firstname,teacher.lastname, teacher_id))
            self.connection.commit()
            print(f"Updated teacher with id: {teacher_id}")
        except Error as e:
            print(f"Error: {e}")


    def delete(self, teacher_id):
        cursor = self.connection.cursor()
        try:
            query = "DELETE FROM teachers WHERE id = %s"
            cursor.execute(query, (teacher_id,))
            self.connection.commit()
            print(f"Deleted teacher with id: {teacher_id}")
        except Error as e:
            print(f"Error: {e}")
