class Client:
    """Класс заказа"""

    def __init__(self, client_id, client_name, client_login, client_password, client_phone, client_photo):
        self.id = client_id
        self.name = client_name
        self.login = client_login
        self.password = client_password
        self.phone = client_phone
        self.photo = client_photo
