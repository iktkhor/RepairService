from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QMessageBox, QListWidgetItem
from pymongo.mongo_client import MongoClient
import sys
import database as db

from views.ui_entrywindow import Ui_EntryWindow
from views.ui_client_menu import Ui_ClientMenu
from views.ui_feedback import Ui_Feedback
from views.ui_employee_menu import Ui_Employee_menu
from views.ui_add_employee import Ui_Add_employee
from views.ui_add_order import Ui_Add_order
from views.ui_employee_view import Ui_Employee_view
from views.ui_add_component import Ui_Add_component
from views.ui_component_view import Ui_Component_view
from views.ui_supplier_info import Ui_Supplier_info
from views.ui_order import Ui_Order_view
from views.ui_work_menu import Ui_Work_menu
from views.ui_component_in_work import Ui_ComponentInWork
from views.ui_work_in_order import Ui_WorkInOrder
from views.ui_avaible_components import Ui_Avaible_components

from models.employee import Employee
from models.client import Client
from models.order import Order
from models.component import Component

conn = db.connect_db()
uri = "mongodb+srv://ikthor:S3AdQikPDxvtP2GY@cluster0.zxomsvv.mongodb.net/?retryWrites=true&w=majority"
mongo_client = MongoClient(uri)
mongo_db = mongo_client['ServiceApp']
doctors_coll = mongo_db['suppliers']


class AvaibleComponents(QWidget):
    def __init__(self, components):
        super(AvaibleComponents, self).__init__()
        self.components = components
        self.ui = Ui_Avaible_components()
        self.ui.setupUi(self)
        self.setup_components()

    def setup_components(self):
        self.ui.list_avaible_components.clear()
        for component in self.components:
            print(component.name)
            component_widget = ComponentInWork(component)
            component_widget.ui.component_type.setText('Тип компонента: Экран')
            component_widget.ui.component_name.setText(f'Название компонента: {component.name}')
            component_widget.ui.component_cost.setText(f'Цена: {component.cost}')
            component_widget.ui.component_quantity.setText(f'Остаток: {component.quantity}')
            item = QListWidgetItem()
            item.setSizeHint(component_widget.sizeHint())
            self.ui.list_avaible_components.addItem(item)
            self.ui.list_avaible_components.setItemWidget(item, component_widget)


class WorkInOrderView(QWidget):
    def __init__(self, work_id, order_id):
        super(WorkInOrderView, self).__init__()
        self.work_id = work_id
        self.order_id = order_id
        self.ui = Ui_WorkInOrder()
        self.ui.setupUi(self)
        self.ui.complete_work_in_order.clicked.connect(self.complete_work)
        self.ui.show_components.clicked.connect(self.show_components)
        self.ui.delete_work_in_order.clicked.connect(self.delete_work)

    def complete_work(self):
        try:
            db.set_work_in_order_status(conn, self.work_id, self.order_id, 1)
        except Exception as e:
            print(e)

    def show_components(self):
        components_in_work = db.select_components_in_work(conn, self.work_id)
        order = db.select_order(conn, self.order_id)
        device_name = db.select_device_name(conn, order.device_id)
        components = []
        for comp in components_in_work:
            component = db.select_component_by_id(conn, comp[2])
            if component.device_id == order.device_id:
                components.append(component)
        self.avaible_components = AvaibleComponents(components)
        self.avaible_components.ui.device.setText(f'Телефон: {device_name}')
        self.avaible_components.show()

    def delete_work(self):
        db.delete_work_in_order(conn, self.work_id, self.order_id)


class ComponentInWork(QWidget):
    def __init__(self, component):
        super(ComponentInWork, self).__init__()
        self.component = component
        self.ui = Ui_ComponentInWork()
        self.ui.setupUi(self)
        self.ui.show_supplier.clicked.connect(self.show_supplier)

    def show_supplier(self):
        self.supplier_widget = SupplierInfo()
        sup_info = db.select_supplier_by_id(conn, self.component.supplier_id)
        self.supplier_widget.ui.supplier_name.setText(f'Название: {sup_info[1]}')
        self.supplier_widget.ui.supplier_phone.setText(f'Телефон: {sup_info[2]}')
        self.supplier_widget.ui.supplier_website.setText(f'Вебсайт: {sup_info[3]}')
        self.supplier_widget.ui.supplier_address.setText(f'Адрес: {sup_info[4]}')
        self.supplier_widget.show()


class WorkMenu(QWidget):
    def __init__(self):
        super(WorkMenu, self).__init__()
        self.ui = Ui_Work_menu()
        self.ui.setupUi(self)
        self.employee_id = EmployeeMenu.employee_id
        self.works = db.select_works(conn)
        self.clients = db.select_clients(conn)
        self.companies = db.select_companies(conn)
        self.devices = db.select_devices(conn)
        self.device_types = db.select_device_types(conn)
        self.orders = db.select_orders(conn)
        self.order_statuses = db.select_order_statuses(conn)
        self.employee_orders = db.select_employee_orders(conn, self.employee_id)
        self.setup_orders_list()
        self.setup_works_list()
        self.ui.refresh_list.clicked.connect(self.setup_orders_list)
        self.ui.wait_work.clicked.connect(self.wait_work)
        self.ui.finish_work.clicked.connect(self.finish_work)
        self.ui.cancel_work.clicked.connect(self.cancel_work)
        self.ui.reject_work.clicked.connect(self.reject_work)
        self.ui.employee_orders.currentIndexChanged.connect(self.setup_works_in_order)
        self.ui.add_work.clicked.connect(self.add_work)

    def wait_work(self):
        current_order = self.employee_orders[self.ui.employee_orders.currentIndex()]
        db.set_order_status(conn, current_order.order_id, 3)

    def finish_work(self):
        current_order = self.employee_orders[self.ui.employee_orders.currentIndex()]
        db.set_order_status(conn, current_order.order_id, 4)
        self.setup_orders_list()

    def cancel_work(self):
        current_order = self.employee_orders[self.ui.employee_orders.currentIndex()]
        db.set_order_status(conn, current_order.order_id, 5)
        self.setup_orders_list()

    def reject_work(self):
        current_order = self.employee_orders[self.ui.employee_orders.currentIndex()]
        db.set_order_status(conn, current_order.order_id, 6)
        self.setup_orders_list()

    def add_work(self):
        work_id = self.works[self.ui.works.currentIndex()].work_id
        order_id = self.employee_orders[self.ui.employee_orders.currentIndex()].order_id
        db.add_work_in_order(conn, work_id, order_id)
        self.setup_works_in_order()

    def setup_orders_list(self):
        self.ui.active_orders.clear()
        self.orders = db.select_orders(conn)
        for order in self.orders:
            if order.order_status_id == 1:
                order_widget = OrderView(order)
                order_widget.ui.pushButton.setText('Приступить к работе')
                order_widget.ui.pushButton.clicked.connect(order_widget.set_worker)
                item = QListWidgetItem()
                item.setSizeHint(order_widget.sizeHint())
                self.ui.active_orders.addItem(item)
                self.ui.active_orders.setItemWidget(item, order_widget)
        self.setup_employee_orders_list()
        self.setup_works_in_order()

    def setup_works_list(self):
        self.ui.works.clear()
        for work in self.works:
            self.ui.works.addItem(work.work_name)

    def setup_employee_orders_list(self):
        self.ui.employee_orders.clear()
        self.employee_orders = db.select_employee_orders(conn, self.employee_id)
        if self.employee_orders:
            for order in self.employee_orders:
                if order.order_status_id in [2, 3]:
                    order_client = db.select_client_by_id(conn, order.client_id)
                    device_name = db.select_device_name(conn, order.device_id)
                    self.ui.employee_orders.addItem(f'{device_name}, {order_client.name}')

    def setup_works_in_order(self):
        self.ui.works_in_order.clear()
        self.ui.client_info.clear()
        self.ui.order_status.clear()
        if self.employee_orders:
            current_order = self.employee_orders[self.ui.employee_orders.currentIndex()]
            order_client = db.select_client_by_id(conn, current_order.client_id)
            order_status = self.order_statuses[current_order.order_status_id - 1]
            self.ui.client_info.setText(f'Имя: {order_client.name}, телефон: {order_client.phone}')
            self.ui.order_status.setText(f'Статус: {order_status[1]}')
            self.ui.works_in_order.clear()
            for work_order in db.select_works_in_order(conn, current_order.order_id):
                work_id = work_order[0]
                work = db.select_work(conn, work_id)
                print(f'work_id {work.work_id}, {current_order.order_id}')
                work_widget = WorkInOrderView(work_id, current_order.order_id)
                if work_order[2] == 1:
                    work_widget.ui.complete_work_in_order.setEnabled(False)
                work_widget.ui.work_name.setText(f'Работа: {work.work_name}')
                work_widget.ui.work_description.setText(f'Описание: {work.work_description}')
                work_widget.ui.work_cost.setText(f'Стоимость: {work.work_cost} ₽')
                item = QListWidgetItem()
                item.setSizeHint(work_widget.sizeHint())
                self.ui.works_in_order.addItem(item)
                self.ui.works_in_order.setItemWidget(item, work_widget)


class OrderView(QWidget):
    def __init__(self, order):
        super(OrderView, self).__init__()
        self.order = order
        self.order_statuses = db.select_order_statuses(conn)
        self.clients = db.select_clients(conn)
        self.ui = Ui_Order_view()
        self.ui.setupUi(self)
        self.setup_order()

    def setup_order(self):
        client = db.select_client_by_id(conn, self.order.client_id)
        self.ui.client.setText(f'Клиент: {client.name}, {client.phone}')
        self.ui.device.setText(f'Устройство: {db.select_device_name(conn, self.order.device_id)}')
        self.ui.order_status.setText(f'Статус: {self.order_statuses[self.order.order_status_id - 1][1]}')
        self.ui.order_description.setText(f'Описание: {self.order.order_description}')

    def delete_order(self):
        db.delete_works_in_order(conn, self.order.order_id)
        db.delete_order(conn, self.order.order_id)

    def set_worker(self):
        db.set_order_employee(conn, self.order.order_id, EmployeeMenu.employee_id)
        db.set_order_status(conn, self.order.order_id, 2)


class SupplierInfo(QWidget):
    def __init__(self):
        super(SupplierInfo, self).__init__()
        self.ui = Ui_Supplier_info()
        self.ui.setupUi(self)


class ComponentView(QWidget):
    def __init__(self, component):
        super(ComponentView, self).__init__()
        self.component = component
        self.ui = Ui_Component_view()
        self.ui.setupUi(self)
        self.ui.setup_component(component)
        self.ui.show_supplier.clicked.connect(self.show_supplier)
        self.ui.delete_component.clicked.connect(self.delete_component)
        self.ui.increase_components.clicked.connect(self.increase_component)
        self.ui.decrease_components.clicked.connect(self.decrease_component)

    def show_supplier(self):
        self.supplier_widget = SupplierInfo()
        sup_info = db.select_supplier_by_id(conn, self.component.supplier_id)
        self.supplier_widget.ui.supplier_name.setText(f'Название: {sup_info[1]}')
        self.supplier_widget.ui.supplier_phone.setText(f'Телефон: {sup_info[2]}')
        self.supplier_widget.ui.supplier_website.setText(f'Вебсайт: {sup_info[3]}')
        self.supplier_widget.ui.supplier_address.setText(f'Адрес: {sup_info[4]}')
        self.supplier_widget.show()

    def delete_component(self):
        db.delete_component(conn, self.component.component_id)

    def increase_component(self):
        current_quantity = int(self.component.quantity)
        new_quantity = current_quantity + 1
        db.set_component_quantity(conn, self.component.component_id, new_quantity)
        self.component.quantity = new_quantity

    def decrease_component(self):
        current_quantity = int(self.component.quantity)
        if current_quantity <= 0:
            error = QMessageBox()
            error.setWindowTitle('Ошибка')
            error.setText('Недостаточно компонентов на складе')
            error.setIcon(QMessageBox.Warning)
            error.exec_()
        else:
            new_quantity = current_quantity - 1
            db.set_component_quantity(conn, self.component.component_id, new_quantity)
            self.component.quantity = new_quantity


class AddComponent(QWidget):
    def __init__(self):
        super(AddComponent, self).__init__()
        self.component_types = db.select_component_types(conn)
        self.companies = db.select_companies(conn)
        self.devices = db.select_devices(conn)
        self.suppliers = db.select_suppliers(conn)
        self.components = db.select_components(conn)
        self.ui = Ui_Add_component()
        self.ui.setupUi(self)
        self.setup_component_types()
        self.setup_companies()
        self.setup_devices()
        self.setup_suppliers()
        self.setup_components_list()
        self.ui.device_company.currentIndexChanged.connect(self.setup_devices)
        self.ui.add_component.clicked.connect(self.add_component)
        self.ui.list_component_type.currentIndexChanged.connect(self.setup_components_list)
        self.ui.refresh_list.clicked.connect(self.setup_components_list)

    def setup_component_types(self):
        self.ui.component_type.clear()
        self.ui.list_component_type.clear()
        for component_type in self.component_types:
            self.ui.component_type.addItem(component_type[1])
            self.ui.list_component_type.addItem(component_type[1])

    def setup_companies(self):
        for company in self.companies:
            self.ui.device_company.addItem(company[1])

    def setup_devices(self):
        self.ui.device_name.clear()
        current_company = self.companies[self.ui.device_company.currentIndex()]
        current_company_id = int(current_company[0])
        for device in self.devices:
            if device[3] == current_company_id:
                self.ui.device_name.addItem(device[2])

    def setup_suppliers(self):
        for supplier in self.suppliers:
            self.ui.component_supplier.addItem(supplier[1])

    def setup_components_list(self):
        self.ui.list_components.clear()
        self.components = db.select_components(conn)
        for component in self.components:
            if component.type_id == (self.ui.list_component_type.currentIndex() + 1):
                component_widget = ComponentView(component)
                component_widget.ui.component_type.setText(f'Тип компонента: {db.select_component_type_name(conn, component.type_id)}')
                component_widget.ui.component_device.setText(f'Устройство: {db.select_device_name(conn, component.device_id)}')
                item = QListWidgetItem()
                item.setSizeHint(component_widget.sizeHint())
                self.ui.list_components.addItem(item)
                self.ui.list_components.setItemWidget(item, component_widget)

    def add_component(self):
        device_id = db.select_device_id(conn, self.ui.device_name.currentText())
        supplier_id = self.suppliers[self.ui.component_supplier.currentIndex()][0]
        component_type_id = self.component_types[self.ui.component_type.currentIndex()][0]
        try:
            new_component = Component(0, self.ui.component_name.text(), device_id, int(supplier_id), component_type_id,
                                      int(self.ui.component_cost.text()), self.ui.component_quantity.value())
            db.add_component(conn, new_component)
            self.setup_components_list()
        except Exception as e:
            print(e)

    def clear_ui(self):
        pass


class EmployeeView(QWidget):
    def __init__(self, employee):
        super(EmployeeView, self).__init__()
        self.employee = employee
        self.ui = Ui_Employee_view()
        self.ui.setupUi(self, employee)
        self.ui.change_data.clicked.connect(self.change_data)
        self.ui.delete_employee.clicked.connect(self.delete_employee)

    def change_data(self):
        print(self.ui.employee_name.text())

    def delete_employee(self):
        db.delete_employee(conn, self.employee.id)


class AddEmployee(QWidget):
    def __init__(self):
        super(AddEmployee, self).__init__()
        self.employees = db.select_employees(conn)
        self.ui = Ui_Add_employee()
        self.ui.setupUi(self)
        self.ui.add_employee.clicked.connect(self.add_employee)
        self.ui.refresh_list.clicked.connect(self.setup_employee_list)
        self.setup_employee_list()

    def setup_employee_list(self):
        self.employees = db.select_employees(conn)
        self.ui.list_employes.clear()
        for employee in self.employees:
            employee_widget = EmployeeView(employee)
            item = QListWidgetItem()
            item.setSizeHint(employee_widget.sizeHint())
            self.ui.list_employes.addItem(item)
            self.ui.list_employes.setItemWidget(item, employee_widget)

    def add_employee(self):
        name = self.ui.employee_name.text()
        login = self.ui.employee_login.text()
        password = self.ui.employee_password.text()
        phone = self.ui.employee_phone.text()
        exp = self.ui.employee_experience.value()
        role_id = self.ui.employee_role.currentIndex() + 2
        new_employee = Employee(0, name, login, password, phone, exp, role_id)
        db.add_employee(conn, new_employee)
        self.ui.clear_ui()


class AddOrder(QWidget):
    def __init__(self):
        super(AddOrder, self).__init__()
        self.clients = db.select_clients(conn)
        self.companies = db.select_companies(conn)
        self.devices = db.select_devices(conn)
        self.device_types = db.select_device_types(conn)
        self.orders = db.select_orders(conn)
        self.order_statuses = db.select_order_statuses(conn)
        self.ui = Ui_Add_order()
        self.ui.setupUi(self)
        self.setup_device_types()
        self.setup_companies()
        self.setup_devices()
        self.setup_clients()
        self.setup_order_statuses()
        self.setup_orders()
        self.ui.device_company.currentIndexChanged.connect(self.setup_devices)
        self.ui.device_type.currentIndexChanged.connect(self.setup_devices)
        self.ui.order_status.currentIndexChanged.connect(self.setup_orders)
        self.ui.add_order.clicked.connect(self.add_order)
        self.ui.refresh_list.clicked.connect(self.setup_orders)

    def add_order(self):
        device_id = db.select_device_id(conn, self.ui.device_model.currentText())
        client_id = self.clients[self.ui.client_list.currentIndex()].id
        new_order = Order(order_id=None, order_status_id=1, employee_id=None, client_id=client_id,
                          device_id=device_id, order_description=self.ui.order_description.toPlainText())
        db.add_order(conn, new_order)
        self.ui.clear_ui()

    def setup_order_statuses(self):
        self.ui.order_status.clear()
        for order_status in self.order_statuses:
            self.ui.order_status.addItem(order_status[1])

    def setup_orders(self):
        self.ui.list_orders.clear()
        self.orders = db.select_orders(conn)
        for order in self.orders:
            if (order.order_status_id - 1) == self.ui.order_status.currentIndex():
                order_widget = OrderView(order)
                order_widget.ui.pushButton.setText('Удалить заказ')
                order_widget.ui.pushButton.clicked.connect(order_widget.delete_order)
                item = QListWidgetItem()
                item.setSizeHint(order_widget.sizeHint())
                self.ui.list_orders.addItem(item)
                self.ui.list_orders.setItemWidget(item, order_widget)

    def setup_device_types(self):
        self.ui.device_type.clear()
        self.ui.device_type.addItem('Все')
        for device_type in self.device_types:
            self.ui.device_type.addItem(device_type[1])

    def setup_companies(self):
        self.ui.device_company.clear()
        for company in self.companies:
            self.ui.device_company.addItem(company[1])

    def setup_devices(self):
        self.ui.device_model.clear()
        current_company = self.companies[self.ui.device_company.currentIndex()]
        current_company_id = int(current_company[0])
        for device in self.devices:
            if device[3] == current_company_id:
                if self.ui.device_type.currentIndex() != 0:
                    if device[1] == self.device_types[self.ui.device_type.currentIndex() - 1][0]:
                        self.ui.device_model.addItem(device[2])
                else:
                    self.ui.device_model.addItem(device[2])

    def setup_clients(self):
        self.ui.client_list.clear()
        for client in self.clients:
            self.ui.client_list.addItem(f'Логин: {client.login}, Имя: {client.name}')


class EmployeeMenu(QWidget):
    employee_id = 0

    def __init__(self, employee_id):
        super(EmployeeMenu, self).__init__()
        EmployeeMenu.employee_id = employee_id
        self.ui = Ui_Employee_menu()
        self.ui.setupUi(self)
        self.setWindowTitle('Меню работника')
        self.setup_menu_tabs()

    def setup_menu_tabs(self):
        _translate = QtCore.QCoreApplication.translate
        print('Creating AddOrder class')
        self.tab_add_order = AddOrder()
        self.tab_add_order.setObjectName("AddOrder")
        print('Creating AddEmployee class')
        self.tab_add_employee = AddEmployee()
        self.tab_add_employee.setObjectName("AddEmployee")
        print('Creating AddComponent class')
        self.tab_add_component = AddComponent()
        self.tab_add_component.setObjectName("AddComponent")
        print('Creating WorkMenu class')
        self.tab_work_menu = WorkMenu()
        self.tab_work_menu.setObjectName("WorkerMenu")
        current_employee = db.select_employee_by_id(conn, EmployeeMenu.employee_id)
        print(current_employee.id)
        if current_employee.role_id == 1:
            print('Admin')
            self.ui.tabWidget.addTab(self.tab_add_order, "")
            self.ui.tabWidget.setTabText(self.ui.tabWidget.indexOf(self.tab_add_order),
                                         _translate("Employee_menu", "Добавить заказ"))
            self.ui.tabWidget.addTab(self.tab_add_employee, "")
            self.ui.tabWidget.setTabText(self.ui.tabWidget.indexOf(self.tab_add_employee),
                                         _translate("Employee_menu", "Добавить работника"))
            self.ui.tabWidget.addTab(self.tab_add_component, "")
            self.ui.tabWidget.setTabText(self.ui.tabWidget.indexOf(self.tab_add_component),
                                         _translate("Employee_menu", "Добавить компонент"))
        elif current_employee.role_id == 2:
            print('Manager')
            self.ui.tabWidget.addTab(self.tab_add_order, "")
            self.ui.tabWidget.setTabText(self.ui.tabWidget.indexOf(self.tab_add_order),
                                         _translate("Employee_menu", "Добавить заказ"))
        elif current_employee.role_id == 3:
            print('Worker')
            self.ui.tabWidget.addTab(self.tab_work_menu, "")
            self.ui.tabWidget.setTabText(self.ui.tabWidget.indexOf(self.tab_work_menu),
                                         _translate("Employee_menu", "Выполнение заказов"))
            self.ui.tabWidget.addTab(self.tab_add_component, "")
            self.ui.tabWidget.setTabText(self.ui.tabWidget.indexOf(self.tab_add_component),
                                         _translate("Employee_menu", "Добавить компонент"))


class Feedback(QWidget):
    def __init__(self):
        super(Feedback, self).__init__()
        self.ui = Ui_Feedback()
        self.ui.setupUi(self)


class ClientMenu(QWidget):
    def __init__(self, client_id):
        super(ClientMenu, self).__init__()
        self.client_id = client_id
        self.companies = db.select_companies(conn)
        self.devices = db.select_devices(conn)
        self.feedbacks = db.select_feedbacks(conn)
        self.ui = Ui_ClientMenu()
        self.ui.setupUi(self)
        self.setWindowTitle('Меню клиента')
        self.ui.tabWidget.setCurrentIndex(0)
        self.setup_companies()
        self.setup_devices()
        self.setup_feedbacks()
        self.ui.send_request.clicked.connect(self.send_request)
        self.ui.add_feedback.clicked.connect(self.add_feedback)
        self.ui.companies_box.currentIndexChanged.connect(self.setup_devices)

    def send_request(self):
        try:
            text = (self.ui.companies_box.currentText() + ' ' + self.ui.models_box.currentText() + '\n' +
                    self.ui.break_description.toPlainText())
            db.add_request(conn, text, self.client_id)
            self.ui.break_description.clear()
        except Exception as e:
            print(e)
        print(text)

    def add_feedback(self):
        self.setup_feedbacks()
        self.ui.feedback_text.clear()

    def setup_companies(self):
        for company in self.companies:
            self.ui.companies_box.addItem(company[1])

    def setup_devices(self):
        self.ui.models_box.clear()
        current_company = self.companies[self.ui.companies_box.currentIndex()]
        current_company_id = int(current_company[0])
        for device in self.devices:
            if device[3] == current_company_id:
                self.ui.models_box.addItem(device[2])

    def setup_feedbacks(self):
        self.ui.feedback_list.clear()
        self.feedbacks = db.select_feedbacks(conn)
        for feedback in self.feedbacks:
            try:
                order = db.select_order(conn, feedback[1])
                client_info = db.select_client_by_id(conn, order.client_id)
                feedback_widget = Feedback()
                feedback_widget.ui.feedback_text.setText(feedback[3])
                feedback_widget.ui.feedback_value_label.setText(f'Оценка: {feedback[2]}/10')
                feedback_widget.ui.client_name_label.setText(client_info.name)
                feedback_widget.ui.photo.setPixmap(QtGui.QPixmap("../../PycharmProjects/ServiceApp/photos/" +
                                                                 client_info.photo))
                item = QListWidgetItem()
                item.setSizeHint(feedback_widget.sizeHint())
                self.ui.feedback_list.addItem(item)
                self.ui.feedback_list.setItemWidget(item, feedback_widget)
            except Exception as e:
                print(e)


class Login(QMainWindow):
    def __init__(self):
        super(Login, self).__init__()
        self.ui = Ui_EntryWindow()
        self.ui.setupUi(self)
        self.ui.stackedWidget.setCurrentIndex(0)
        self.ui.reg.clicked.connect(self.on_reg_clicked)
        self.ui.back.clicked.connect(self.on_back_clicked)
        self.ui.end_reg.clicked.connect(self.on_end_reg_clicked)
        self.ui.entry.clicked.connect(self.on_entry_clicked)
        self.setWindowTitle('Вход')

    def open_client_window(self):
        try:
            current_client = db.select_client(conn, self.ui.login.text(), self.ui.password.text())
            self.client_menu = ClientMenu(current_client[0])
            self.client_menu.show()
        except Exception as e:
            print(e)

    def open_employee_window(self):
        try:
            current_employee = db.select_employee(conn, self.ui.login.text(), self.ui.password.text())
            self.employee_menu = EmployeeMenu(current_employee.id)
            self.employee_menu.show()
        except Exception as e:
            print(e)

    def on_reg_clicked(self):
        self.ui.stackedWidget.setCurrentIndex(1)

    def on_back_clicked(self):
        self.ui.stackedWidget.setCurrentIndex(0)

    def on_entry_clicked(self):
        try:
            entry = db.entry_user(conn, self.ui.login.text(), self.ui.password.text())
        except Exception as e:
            print(e)
        if entry:
            if entry == 'Client':
                self.open_client_window()
            elif entry == 'Employee':
                self.open_employee_window()
            self.close()
        else:
            error = QMessageBox()
            error.setWindowTitle('Ошибка')
            error.setText('Вы ввели неправильные данные')
            error.setIcon(QMessageBox.Warning)
            error.exec_()

    def on_end_reg_clicked(self):
        client_name = self.ui.new_name.text()
        client_login = self.ui.new_login.text()
        client_password = self.ui.new_password.text()
        client_phone = self.ui.new_phone.text()

        if client_name == '' or client_login == '' or client_password == '' or client_phone == '':
            error = QMessageBox()
            error.setWindowTitle('Ошибка')
            error.setText('Вы не заполнили все поля')
            error.setIcon(QMessageBox.Warning)
            error.exec_()
        else:
            try:
                new_client = Client(0, client_name, client_login, client_password, client_phone, 'default.jpg')
                db.add_client(conn, new_client)
                info = QMessageBox()
                info.setWindowTitle('Уведомление')
                info.setText('Аккаунт зарегистрирован')
                info.setIcon(QMessageBox.Information)
                info.exec_()
                self.clear_ui()
            except Exception as e:
                print(e)

    def clear_ui(self):
        self.ui.new_name.clear()
        self.ui.new_login.clear()
        self.ui.new_password.clear()
        self.ui.new_phone.clear()


if __name__ == '__main__':
    # db.create_tables(conn)
    app = QApplication(sys.argv)
    win = Login()
    win.show()
    sys.exit(app.exec_())
