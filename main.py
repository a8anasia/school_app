from DAO.teacher_dao import TeacherImpl
from Service.teacher_service import TeacherService
from model.teacher import Teacher
from connection_db import create_connection



def main():
    conn = create_connection('localhost', 'root', '12345', 'schoolapp5db','3306')

    if conn:
        teacher_dao = TeacherImpl(conn)
        teacher_service = TeacherService(teacher_dao)

        #insert teacher
        teacher1 = Teacher( 1, firstname="Alice",lastname="M.")
        teacher_service.add_teacher(teacher1)
        print(f"Inserted teacher with id: {teacher1.id}" , teacher1, )

        #get teacher
        get_teacher1 = teacher_service.get_teacher(1)
        print("Get Teacher ", get_teacher1)

        #update teacher
        up_teacher = Teacher(firstname="Bob", lastname="P.")
        teacher_service.update_teacher(teacher1.id, up_teacher)
        print( "Updated teacher: ", up_teacher)

        #teacher delete
        deleted_teacher = teacher_service.remove_teacher(1)



if __name__ == '__main__':
    main()

