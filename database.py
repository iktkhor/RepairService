import sqlite3

from models.employee import Employee
from models.feedback_py import Feedback
from models.order import Order
from models.client import Client
from models.component import Component
from models.work import Work


def connect_db():
    db_connection = None
    try:
        db_connection = sqlite3.connect('database.sqlite')
        print('Database connected')
    except sqlite3.Error as e:
        print(e)
    return db_connection


def entry_user(conn, login, password):
    client = select_client(conn, login, password)
    employee = select_employee(conn, login, password)
    if client:
        return 'Client'
    elif employee:
        return 'Employee'
    return None


def add_client(conn, client):
    c = conn.cursor()
    c.execute("INSERT INTO Client (client_name, client_login, client_password, "
              "client_phone, client_photo) VALUES (?,?,?,?,?)",
              (client.name, client.login, client.password, client.phone, client.photo,))
    conn.commit()


def add_employee(conn, employee):
    c = conn.cursor()
    c.execute("INSERT INTO Employee (employee_name, employee_login, employee_password, employee_phone, "
              "employee_experience, employee_role_id) VALUES (?,?,?,?,?,?)",
              (employee.name, employee.login, employee.password, employee.phone, employee.experience, employee.role_id,))
    conn.commit()


def add_order(conn, order):
    c = conn.cursor()
    c.execute("INSERT INTO Orders (order_status_id, client_id, device_id, order_description) "
              "VALUES (?,?,?,?)",
              (order.order_status_id, order.client_id, order.device_id, order.order_description,))
    conn.commit()


def add_component(conn, component):
    c = conn.cursor()
    c.execute("INSERT INTO Component (component_name, device_id, supplier_id, component_type_id, "
              "component_cost, component_quantity) VALUES (?,?,?,?,?,?)",
              (component.name, component.device_id, component.supplier_id, component.type_id, component.cost,
               component.quantity,))
    new_component_id = c.execute("SELECT component_id FROM Component WHERE component_name = ?",
                                 (component.name,)).fetchone()[0]
    print(new_component_id)
    if component.type_id == 1:
        c.execute("INSERT INTO ComponentsInWorks (work_id, component_id) VALUES (?,?)", (1, new_component_id),)
    elif component.type_id == 2:
        c.execute("INSERT INTO ComponentsInWorks (work_id, component_id) VALUES (?,?)", (2, new_component_id,))
    conn.commit()


def add_work_in_order(conn, work_id, order_id):
    c = conn.cursor()
    if not c.execute("SELECT * FROM WorksInOrders WHERE work_id = ? AND order_id = ?", (work_id, order_id,)).fetchone():
        try:
            c.execute("INSERT INTO WorksInOrders (work_id, order_id, is_done) VALUES (?,?,?)", (work_id, order_id, 0,))
            conn.commit()
            return True
        except Exception as e:
            print(e)
    else:
        return False


def add_request(conn, request_text, client_id):
    c = conn.cursor()
    c.execute("INSERT INTO Request (request_text, client_id) VALUES (?,?)", (request_text, client_id,))
    conn.commit()


def set_work_in_order_status(conn, work_id, order_id, is_done):
    c = conn.cursor()
    c.execute("UPDATE WorksInOrders SET is_done = ? WHERE work_id = ? AND order_id = ?",
              (is_done, work_id, order_id,))
    conn.commit()
    return True


def delete_work_in_order(conn, work_id, order_id):
    c = conn.cursor()
    c.execute("DELETE FROM WorksInOrders WHERE work_id = ? AND order_id = ?", (work_id, order_id,))
    conn.commit()


def delete_works_in_order(conn, order_id):
    c = conn.cursor()
    c.execute("DELETE FROM WorksInOrders WHERE order_id = ?", (order_id,))
    conn.commit()


def set_order_status(conn, order_id, order_status_id):
    c = conn.cursor()
    c.execute("UPDATE Orders SET order_status_id = ? WHERE order_id = ?",
              (order_status_id, order_id,))
    conn.commit()
    return True


def set_order_employee(conn, order_id, employee_id):
    c = conn.cursor()
    c.execute("UPDATE Orders SET employee_id = ? WHERE order_id = ?",
              (employee_id, order_id,))
    conn.commit()
    return True


def set_component_quantity(conn, component_id, new_quantity):
    c = conn.cursor()
    c.execute("UPDATE Component SET component_quantity = ? WHERE component_id = ?",
              (new_quantity, component_id,))
    conn.commit()
    return True


def select_client(conn, login, password):
    c = conn.cursor()
    c.execute("SELECT * FROM Client WHERE client_login = ? AND client_password = ?", (login, password))
    client = c.fetchone()
    return client


def select_client_name(conn, client_id):
    c = conn.cursor()
    c.execute("SELECT client_name FROM Client WHERE client_id = ?", (client_id,))
    client_name = c.fetchone()
    return client_name[0]


def select_clients(conn):
    c = conn.cursor()
    c.execute("SELECT * FROM Client")
    data = c.fetchall()
    clients = []
    if data:
        for cln in data:
            client = Client(client_id=(cln[0]), client_name=cln[1], client_login=cln[2], client_password=cln[3],
                            client_phone=cln[4], client_photo=cln[5])
            clients.append(client)
    return clients


def select_components(conn):
    c = conn.cursor()
    c.execute("SELECT * FROM Component")
    data = c.fetchall()
    components = []
    if data:
        for cmpn in data:
            component = Component(component_id=int(cmpn[0]), name=cmpn[1], device_id=int(cmpn[2]), supplier_id=int(cmpn[3]),
                                  type_id=int(cmpn[4]), cost=int(cmpn[5]), quantity=int(cmpn[6]))
            components.append(component)
    return components


def select_component_by_id(conn, component_id):
    c = conn.cursor()
    c.execute("SELECT * FROM Component WHERE component_id = ?", (component_id,))
    data = c.fetchone()
    component = None
    if data:
        component = Component(component_id=int(data[0]), name=data[1], device_id=int(data[2]), supplier_id=int(data[3]),
                              type_id=int(data[4]), cost=int(data[5]), quantity=int(data[6]))
    return component


def select_device_components(conn, device_id):
    c = conn.cursor()
    c.execute("SELECT * FROM Component WHERE device_id = ?", (device_id,))
    data = c.fetchall()
    components = []
    if data:
        for cmpn in data:
            component = Component(int(cmpn[0]), cmpn[1], cmpn[2], cmpn[3], cmpn[4], cmpn[5], int(cmpn[6]))
            components.append(component)
    return components


def select_device_id(conn, device_name):
    c = conn.cursor()
    c.execute("SELECT device_id FROM Device WHERE device_name = ?", (device_name,))
    device_id = c.fetchall()
    return device_id[0][0]


def select_device_name(conn, device_id):
    c = conn.cursor()
    c.execute("SELECT device_name FROM Device WHERE device_id = ?", (device_id,))
    device_name = c.fetchone()
    return device_name[0]


def select_client_by_id(conn, client_id):
    c = conn.cursor()
    c.execute("SELECT * FROM Client WHERE client_id = ?", (client_id,))
    data = c.fetchone()
    client = None
    if data:
        client = Client(client_id=(data[0]), client_name=data[1], client_login=data[2], client_password=data[3],
                        client_phone=data[4], client_photo=data[5])
    return client


def select_employee(conn, login, password):
    c = conn.cursor()
    c.execute("SELECT * FROM Employee WHERE employee_login = ? AND employee_password = ?", (login, password,))
    data = c.fetchone()
    employee = None
    if data:
        employee = Employee(emp_id=int(data[0]), emp_name=data[1], emp_login=data[2], emp_password=data[3],
                            emp_phone=data[4], emp_experience=int(data[5]), emp_role_id=int(data[6]))
    return employee


def select_employee_by_id(conn, employee_id):
    c = conn.cursor()
    c.execute("SELECT * FROM Employee WHERE employee_id = ?", (employee_id,))
    data = c.fetchone()
    employee = None
    if data:
        employee = Employee(emp_id=int(data[0]), emp_name=data[1], emp_login=data[2], emp_password=data[3],
                            emp_phone=data[4], emp_experience=int(data[5]), emp_role_id=int(data[6]))
    return employee


def select_employees(conn):
    c = conn.cursor()
    c.execute("SELECT * FROM Employee")
    data = c.fetchall()
    employees = []
    if data:
        for emp in data:
            employee = Employee(int(emp[0]), emp[1], emp[2], emp[3], emp[4], int(emp[5]), int(emp[6]))
            employees.append(employee)
    return employees


def select_work(conn, work_id):
    c = conn.cursor()
    c.execute("SELECT * FROM Work WHERE work_id = ?", (work_id,))
    data = c.fetchone()
    work = None
    if data:
        work = Work(work_id=(data[0]), work_name=data[1], work_description=data[2], work_cost=int(data[3]))
    return work


def select_works(conn):
    c = conn.cursor()
    c.execute("SELECT * FROM Work")
    data = c.fetchall()
    works = []
    if data:
        for wrk in data:
            work = Work(work_id=(wrk[0]), work_name=wrk[1], work_description=wrk[2], work_cost=int(wrk[3]))
            works.append(work)
    return works


def select_works_in_order(conn, order_id):
    c = conn.cursor()
    c.execute("SELECT * FROM WorksInOrders WHERE order_id = ?", (order_id,))
    data = c.fetchall()
    return data


def select_components_in_work(conn, work_id):
    c = conn.cursor()
    c.execute("SELECT * FROM ComponentsInWorks WHERE work_id = ?", (work_id,))
    data = c.fetchall()
    return data


def delete_employee(conn, employee_id):
    c = conn.cursor()
    c.execute("DELETE FROM Employee WHERE employee_id = ?", (employee_id,))
    conn.commit()


def delete_order(conn, order_id):
    c = conn.cursor()
    c.execute("DELETE FROM Orders WHERE order_id = ?", (order_id,))
    conn.commit()


def delete_component(conn, component_id):
    c = conn.cursor()
    c.execute("DELETE FROM Component WHERE component_id = ?", (component_id,))
    conn.commit()


def select_companies(conn):
    c = conn.cursor()
    c.execute("SELECT * FROM Company")
    companies = c.fetchall()
    return companies


def select_devices(conn):
    c = conn.cursor()
    c.execute("SELECT * FROM Device")
    devices = c.fetchall()
    return devices


def select_device_types(conn):
    c = conn.cursor()
    c.execute("SELECT * FROM Device_type")
    device_types = c.fetchall()
    return device_types


def select_feedbacks(conn):
    c = conn.cursor()
    c.execute("SELECT * FROM Feedback")
    feedbacks = c.fetchall()
    return feedbacks


def select_order(conn, order_id):
    c = conn.cursor()
    c.execute("SELECT * FROM Orders WHERE order_id = ?", (order_id,))
    data = c.fetchone()
    order = None
    if data:
        order = Order(order_id=(data[0]), order_status_id=int(data[1]), employee_id=int(data[2]),
                      client_id=int(data[3]), device_id=int(data[4]), order_description=data[5])
    return order


def select_orders(conn):
    c = conn.cursor()
    c.execute("SELECT * FROM Orders")
    data = c.fetchall()
    orders = []
    if data:
        for ord in data:
            order = Order(order_id=(ord[0]), order_status_id=int(ord[1]), employee_id=ord[2],
                          client_id=int(ord[3]), device_id=int(ord[4]), order_description=ord[5])
            orders.append(order)
    return orders


def select_employee_orders(conn, employee_id):
    c = conn.cursor()
    c.execute("SELECT * FROM Orders WHERE employee_id = ?", (employee_id,))
    data = c.fetchall()
    orders = []
    if data:
        for ord in data:
            if ord[1] in [2, 3]:
                order = Order(order_id=(ord[0]), order_status_id=int(ord[1]), employee_id=ord[2],
                              client_id=int(ord[3]), device_id=int(ord[4]), order_description=ord[5])
                orders.append(order)
    return orders


def select_order_statuses(conn):
    c = conn.cursor()
    c.execute("SELECT * FROM Order_status")
    order_statuses = c.fetchall()
    return order_statuses


def select_supplier_by_id(conn, supplier_id):
    c = conn.cursor()
    c.execute("SELECT * FROM Supplier WHERE supplier_id = ?", (supplier_id,))
    supplier = c.fetchall()
    return supplier[0]


def select_suppliers(conn):
    c = conn.cursor()
    c.execute("SELECT * FROM Supplier")
    suppliers = c.fetchall()
    return suppliers


def select_company_devices(conn, company_id):
    c = conn.cursor()
    c.execute("SELECT * FROM Device WHERE company_id = ?", (company_id,))
    devices = c.fetchall()
    return devices


def select_component_types(conn):
    c = conn.cursor()
    c.execute("SELECT * FROM Component_type")
    component_types = c.fetchall()
    return component_types


def select_component_type_name(conn, type_id):
    c = conn.cursor()
    c.execute("SELECT component_type_name FROM Component_type WHERE component_type_id = ?", (type_id,))
    type_name = c.fetchall()
    return type_name[0][0]


def create_tables(conn):
    create_table_client(conn)
    create_table_request(conn)
    create_table_employee_role(conn)
    create_table_employee(conn)
    create_table_feedback(conn)
    create_table_order_status(conn)
    create_table_device_type(conn)
    create_table_company(conn)
    create_table_device(conn)
    create_table_supplier(conn)
    create_table_component_type(conn)
    create_table_component(conn)
    create_table_order(conn)
    create_table_work(conn)


def create_table_client(conn):
    c = conn.cursor()
    c.execute("CREATE TABLE IF NOT EXISTS Client ("
              "id INTEGER PRIMARY KEY AUTOINCREMENT, "
              "client_name TEXT, "
              "client_login TEXT, "
              "client_password TEXT, "
              "client_phone TEXT, "
              "client_photo TEXT"
              ")")


def create_table_request(conn):
    c = conn.cursor()
    c.execute("CREATE TABLE IF NOT EXISTS Request ("
              "request_id INTEGER PRIMARY KEY AUTOINCREMENT, "
              "request_text TEXT, "
              "client_id INTEGER"
              ")")


def create_table_employee_role(conn):
    c = conn.cursor()
    c.execute("CREATE TABLE IF NOT EXISTS Employee_role ("
              "role_id INTEGER PRIMARY KEY AUTOINCREMENT, "
              "role_name TEXT, "
              "role_description TEXT"
              ")")


def create_table_employee(conn):
    c = conn.cursor()
    c.execute("CREATE TABLE IF NOT EXISTS Employee ("
              "employee_id INTEGER PRIMARY KEY AUTOINCREMENT, "
              "employee_name TEXT, "
              "employee_login TEXT, "
              "employee_password TEXT, "
              "employee_phone TEXT, "
              "employee_experience INTEGER, "
              "employee_role_id INTEGER"
              ")")


def create_table_feedback(conn):
    c = conn.cursor()
    c.execute("CREATE TABLE IF NOT EXISTS Feedback ("
              "feedback_id INTEGER PRIMARY KEY AUTOINCREMENT, "
              "order_id INTEGER, "
              "feedback_rating INTEGER, "
              "feedback_text TEXT, "
              "date TEXT"
              ")")


def create_table_order_status(conn):
    c = conn.cursor()
    c.execute("CREATE TABLE IF NOT EXISTS Order_status ("
              "order_status_id INTEGER PRIMARY KEY AUTOINCREMENT, "
              "order_status_name TEXT"
              ")")


def create_table_device_type(conn):
    c = conn.cursor()
    c.execute("CREATE TABLE IF NOT EXISTS Device_type ("
              "device_type_id INTEGER PRIMARY KEY AUTOINCREMENT, "
              "device_type_name TEXT"
              ")")


def create_table_company(conn):
    c = conn.cursor()
    c.execute("CREATE TABLE IF NOT EXISTS Company ("
              "company_id INTEGER PRIMARY KEY AUTOINCREMENT, "
              "company_name TEXT, "
              "company_country TEXT"
              ")")


def create_table_device(conn):
    c = conn.cursor()
    c.execute("CREATE TABLE IF NOT EXISTS Device ("
              "device_id INTEGER PRIMARY KEY AUTOINCREMENT, "
              "device_type_id INTEGER, "
              "device_name TEXT, "
              "company_id INTEGER"
              ")")


def create_table_order(conn):
    c = conn.cursor()
    c.execute("CREATE TABLE IF NOT EXISTS Orders ("
              "order_id INTEGER PRIMARY KEY AUTOINCREMENT, "
              "device_id INTEGER, "
              "client_id INTEGER, "
              "order_status_id INTEGER, "
              "order_description TEXT"
              ")")


def create_table_supplier(conn):
    c = conn.cursor()
    c.execute("CREATE TABLE IF NOT EXISTS Supplier ("
              "supplier_id INTEGER PRIMARY KEY AUTOINCREMENT, "
              "supplier_name TEXT, "
              "supplier_phone TEXT, "
              "supplier_website TEXT, "
              "supplier_address TEXT"
              ")")


def create_table_component_type(conn):
    c = conn.cursor()
    c.execute("CREATE TABLE IF NOT EXISTS Component_type ("
              "component_type_id INTEGER PRIMARY KEY AUTOINCREMENT, "
              "component_type_name TEXT"
              ")")


def create_table_component(conn):
    c = conn.cursor()
    c.execute("CREATE TABLE IF NOT EXISTS Component ("
              "component_id INTEGER PRIMARY KEY AUTOINCREMENT, "
              "component_name TEXT, "
              "device_id INTEGER, "
              "supplier_id INTEGER, "
              "component_type_id INTEGER, "
              "component_cost INTEGER"
              ")")


def create_table_work(conn):
    c = conn.cursor()
    c.execute("CREATE TABLE IF NOT EXISTS Work ("
              "work_id INTEGER PRIMARY KEY AUTOINCREMENT, "
              "order_id INTEGER, "
              "employee_id INTEGER"
              ")")

