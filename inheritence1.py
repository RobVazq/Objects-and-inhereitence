class item:
    def __init__(self, description, price, quantity):
        self.description = description
        self.price = price
        self.quantity = quantity
            

    def display(self):
        return print('Item:{} Price:${} Quantity:{}'.format(self.description, self.price, self.quantity))

class perishable(item):
    def __init__(self, description, price, quantity, sellby, wt):
        super().__init__(description, price, quantity)
        self.sellby = sellby
        self.wt = wt

    def display_p(self):
        return print( 'Item:{} Price:${} Quantity:{} Sellby: {} Weight {}'.format ( self.description, self.price, self.quantity , self.sellby, self.wt))

class electronics(item):
    def __init__(self, description, price, quantity, warranty, power):
        super().__init__(description, price, quantity)
        self.warranty = warranty
        self.power = power
    def display_e(self):
        return print( 'Item:{} Price:${} Quantity:{} Warranty:{} Power:{}'.format(self.description, self.price, self.quantity, self.warranty, self.power))

class Movies(item):
    def __init__(self, description, price, quantity, director, release_year, rating):
        super().__init__(description, price, quantity)
        self.director = director
        self.release_year = release_year
        self.rating = rating


    def display_m(self):
        return print('Item:{} Price:${} Quantity:{}, Director:{} Release Year:{} Rating:{}'.format(self.description, self.price, self.quantity, self.director, self.release_year, self.rating))

a = perishable( 'tomatoes', '1.50', 1.00, 'march 2025', '22oz')
a.display_p()
b = perishable('cheddar cheese', '3.50', '1.00', 'march 2022', '16oz')
b.display_p()
print('')
c = electronics('charger', '8.00', '1.00', '90 days', 'wall_power')
c.display_e()
d = electronics('gameboy', '125.00', '1.00', '2 years', 'AA')
d.display_e() 
print('')
e = Movies('A movie', '14.00', '1.00', 'Roberto Vazquez', '2019', 'R')
e.display_m()
f = Movies('A PG13 movie', '19.99', '1.00', 'Roberto Vazquez', '2021', 'PG13')
f.display_m()
