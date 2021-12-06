# Nathanael Voss CSE20
# Assignment 10.1 Your Own Class
# Pizza Class!

class Pizza(): # this is my class pizza
    # this is the constructor
    def __init__(self, crust, toppings): 
        self.__crust = crust #private data variable
        self.__toppings = toppings #private data variable
        self.olives = 0
        
    #get methods
    def get_crust(self):
        return self.__crust
    
    def get_toppings(self):
        return self.__toppings
    
    def get_olives(self):
        return self.olives
    
    #set methods
    def set_crust(self, crust):
        self.__crust = crust
        
    def set_toppings(self, toppings):
        self.__toppings = toppings
        
    # Other methods
    def add_olives(self, int): #method that recursively permanently adds an exact number of olives to the pizza
        if int == 0: return 
        self.olives += 1
        self.add_olives(int-1)
    #specialty pizzas can be automatically generated using the specialty method
    def specialty(pizza_type): 
        pizzaspecial = Pizza(crust = '', toppings = '')
        if pizza_type == 'hawaiian':
            pizzaspecial.set_crust('normal')
            pizzaspecial.set_toppings(('pineapple', 'Canadian Bacon'))
        if pizza_type == 'meat lovers':
            pizzaspecial.set_crust('thick')
            pizzaspecial.set_toppings(('pepperoni', 'sausage', 'bacon', 'salami'))
        if pizza_type == 'four cheese':
            pizzaspecial.set_crust('stuffed')
            pizzaspecial.set_toppings(('mozzerella', 'gorgonzola', 'parmesan', 'ricotta'))
        if pizza_type == 'vegetarian':
            pizzaspecial.set_crust('thin')
            pizzaspecial.set_toppings(('mushrooms', 'spinach', 'bellpepper', 'red onion'))
            pizzaspecial.add_olives(37)
        return pizzaspecial
    #this method combines two pizzas, their crusts and toppings, then returns the resulting frankenpizza
    def add_pizza(self, pizza): 
        frankenpizza = Pizza(crust = '', toppings = '')
        # combining crusts of both pizzas
        if self.__crust == 'thick' or pizza.__crust == 'thick':
            frankenpizza.__crust = 'thick'
        if self.__crust == 'stuffed' or pizza.__crust == 'stuffed':
            frankenpizza.__crust = 'stuffed'
        if self.__crust == 'thin' or pizza.__crust == 'thin':
            frankenpizza.__crust = 'thin'
        if (self.__crust == 'thick' and pizza.__crust == 'thin') or (self.__crust == 'thin' and pizza.__crust == 'thick'):
            frankenpizza.__crust = 'normal'
        
        #combining ingredients/toppings of both pizzas
        frankenpizza.__toppings = tuple(self.__toppings + pizza.__toppings)
        return frankenpizza
    #string method that prints your pizza in a user friendly readable way
    def __str__(self):
        return f'----------------------------------------\nYour Pizza:\nPizza Crust: {self.__crust}\nPizza Toppings: {self.__toppings}\nNumber of olives: {self.olives}'
       
       
def main():
    pizza1 = Pizza('stuffed', ('pepperoni', 'garlic')) #generates a new pizza object of the Pizza class
    pizza2 = Pizza('', ('pepper', 'sausage')) #generates another new pizza object of the Pizza class and it is missing a crust
    pizza2.set_crust('thick') #sets the crust of the second pizza object to thick
    pizza3 = Pizza.specialty('vegetarian') #generates a specialty vegetarian pizza using the specialty method
    print(pizza3)
    newpizza = pizza1.add_pizza(pizza2) #uses the add_pizza method to combind pizza1 and pizza 2 and assign it to a newpizza variable
    newpizza.add_olives(10) #recursively adds olives to the newpizza 
    print(newpizza)
    print(newpizza.get_crust())
    print(pizza2.get_toppings())
    
if __name__ == "__main__":
    main()