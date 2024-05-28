from DAO.teacher_dao import TeacherImpl
from model.teacher import Teacher

class TeacherService:
    def __init__(self, teacher_dao):
        self.teacher_dao = teacher_dao

    def add_teacher(self, teacher):
        self.teacher_dao.insert(teacher)

    def get_teacher(self, teacher_id):
        return self.teacher_dao.get_one(teacher_id)

    def update_teacher(self, teacher_id, teacher):
        self.teacher_dao.update(teacher_id, teacher)

    def remove_teacher(self, teacher_id):
        self.teacher_dao.delete(teacher_id)
