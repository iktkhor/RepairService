class Employee:
    """Класс работника"""

    def __init__(self, emp_id, emp_name, emp_login, emp_password, emp_phone, emp_experience, emp_role_id):
        self.id = emp_id
        self.name = emp_name
        self.login = emp_login
        self.password = emp_password
        self.phone = emp_phone
        self.experience = emp_experience
        self.role_id = emp_role_id
