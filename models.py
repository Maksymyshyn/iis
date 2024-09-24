class Product:
    def __init__(self, name, description, price, category, stock, manufacturer):
        self.name = name
        self.description = description
        self.price = price
        self.category = category
        self.stock = stock
        self.manufacturer = manufacturer

    def __repr__(self):
        return f"Product(Name: {self.name}, Price: {self.price}, Stock: {self.stock})"

# Фрейм "Клієнт"
class Client:
    def __init__(self, name, email, phone, purchase_history=[], preferences=[]):
        self.name = name
        self.email = email
        self.phone = phone
        self.purchase_history = purchase_history
        self.preferences = preferences

    def __repr__(self):
        return f"Client(Name: {self.name}, Email: {self.email})"

# Фрейм "Замовлення"
class Order:
    def __init__(self, order_id, client, product_list, status="Pending"):
        self.order_id = order_id
        self.client = client
        self.product_list = product_list
        self.status = status
        self.total_amount = sum(product.price for product in product_list)
        self.order_date = None

    def place_order(self, order_date):
        self.order_date = order_date
        self.status = "Confirmed"

    def __repr__(self):
        return f"Order(ID: {self.order_id}, Client: {self.client.name}, Status: {self.status}, Total: {self.total_amount})"

# Фрейм "Онлайн-консультант"
class OnlineConsultant:
    def __init__(self, name, availability=True, specialization="", contact_details=""):
        self.name = name
        self.availability = availability
        self.specialization = specialization
        self.contact_details = contact_details

    def __repr__(self):
        return f"Consultant(Name: {self.name}, Available: {self.availability})"

# Фрейм "Каталог"
class Catalog:
    def __init__(self):
        self.products = []
        self.categories = set()

    def add_product(self, product):
        self.products.append(product)
        self.categories.add(product.category)

    def search(self, keyword):
        return [product for product in self.products if keyword.lower() in product.name.lower()]

    def filter_by_category(self, category):
        return [product for product in self.products if product.category == category]

    def __repr__(self):
        return f"Catalog(Products: {len(self.products)}, Categories: {len(self.categories)})"

# Створення об'єктів на основі фреймів
# Додамо продукти
product1 = Product("Цемент М500", "Високоякісний цемент", 100, "Будівельні матеріали", 50, "Ферозіт")
product2 = Product("Штукатурка", "Фасадна штукатурка", 200, "Будівельні матеріали", 30, "Ферозіт")
product3 = Product("Ґрунтовка", "Ґрунтовка для стін", 50, "Будівельні матеріали", 100, "Ферозіт")

# Додамо клієнтів
client1 = Client("Іван Іванов", "ivanov@example.com", "+380123456789")
client2 = Client("Олена Петрова", "petrova@example.com", "+380987654321")

# Створимо каталог і додамо продукти
catalog = Catalog()
catalog.add_product(product1)
catalog.add_product(product2)
catalog.add_product(product3)

# Додамо замовлення
order1 = Order(order_id="001", client=client1, product_list=[product1, product3])
order1.place_order(order_date="2024-09-25")

# Додамо онлайн-консультанта
consultant = OnlineConsultant(name="Анна Консультант", availability=True, specialization="Будівельні матеріали", contact_details="anna@example.com")

# Виведення інформації про об'єкти
print(catalog)              # Інформація про каталог
print(catalog.search("Цем"))  # Пошук продуктів по ключовому слову
print(order1)               # Інформація про замовлення
print(consultant)           # Інформація про онлайн-консультанта
