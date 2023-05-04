class Order:
    """Класс заказа"""

    def __init__(self, order_id, order_status_id, employee_id, client_id, device_id, order_description):
        self.order_id = order_id
        self.order_status_id = order_status_id
        self.employee_id = employee_id
        self.client_id = client_id
        self.device_id = device_id
        self.order_description = order_description
