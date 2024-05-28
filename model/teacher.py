class Teacher:
    def __init__(self,id=None, firstname=None, lastname=None):
        self._id = id
        self._firstname = firstname
        self._lastname = lastname

    def __str__(self):
        return f"{self._firstname} {self._lastname}"

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value

    @property
    def firstname(self):
        return self._firstname

    @firstname.setter
    def firstname(self, value):
        self._firstname = value

    @property
    def lastname(self):
        return self._lastname

    @lastname.setter
    def lastname(self, value):
        self._lastname = value