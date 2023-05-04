class Component:
    """Класс компонента"""

    def __init__(self, component_id, name, device_id, supplier_id, type_id, cost, quantity):
        self.component_id = component_id
        self.name = name
        self.device_id = device_id
        self.supplier_id = supplier_id
        self.type_id = type_id
        self.cost = cost
        self.quantity = quantity
