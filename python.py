class Store:
    def __init__(self, name):
        self.name = name
        self.productlist = []

    def add_product(self, product):
        self.productlist.append(product)
    
    def sell_product(self, id):
        self.productlist.pop(id)
        print(f'Product Sold! Product: {productlist.pop(id)}')







class Product:
    def __init__(self, name, price, category):
        self.name = name
        self.price = price
        self.category = category
    
    def update_price(self, percent_change, is_increased):
        if is_increased == True:
            self.price = (self.price * percent_change) + self.price
            return self
        else:
            self.price = self.price - (self.price * percent_change)
            return self
    def price_info(self):
        print(f'Product Name: {self.name} \n Price: {self.price} \n Category: {self.category}')

milk = Product('Milk', 4.99, 'Groceries')
eggs = Product('Eggs', 4.99, 'Groceries')
milk.price_info()
eggs.price_info()
matt = Store('Matt Mart')
matt.add_product('eggs')
