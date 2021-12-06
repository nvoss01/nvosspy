# nvosspy
My python programs
README 
Thank you for checking out my Pizza class! View it here on GitHub: https://github.com/nvoss01/nvosspy
Class Documentation:
This is my Pizza Class. It allows you to construct a custom pizza with your desired crust and toppings.
The pizzas you make are malleable and can change to your will. You can streamline the process to create a specialty pizza
from a series of well known pizzas. You can even add two pizzas together, combining their crust and toppings. The most important
part of the program is adding olives to the pizza, so of course there is a method dedicated to doing just that.

Method Descriptions:
The self.__crust, self.__toppings and self.olives are my class variables. The first two denoted with underscores are private varaibles
The pizza1, pizza2, pizza3 and newpizza variables are normal data variables that are objects of the Pizza class
These objects can have their class variables altered and reassigned
The get_crust, get_toppings and get_olives methods take in self argument and return the private class variable self.__crust and self.__toppings respectively
get_olives returns self.olvies, which is not a private variable
The set_crust and set_toppings methods take in self and a string argument and set the crust and toppings based on the methods' argument input
The add_olives method takes in slef and an integer argument, and recursively adds that number of olives to the pizza desired
The specialty method takes in a string and automatically constructs a popular pizza from a select few of the most famous pizza types
The add_pizza method takes in self and a pizza object and combines the two of them, crust, toppings and all
Finally, the __str__ method is used for string concatenation and takes in self and returns an f string formatted in a readable way for the user
-------------------------------------------------------------------------------------------------------------------------------------------------------------
Demo Program Notes:

In the demo program(in the main) I test the methods of my Pizza class.
I start by creating a new object from the Pizza class, with a stuffed crust, topped with pepperoni and garlic
Then I create a second Pizza object


To run my demo program just open my python file in a code read/write program such as visual studio code
or navigate to its download location on your PC through the command prompt. In the command prompt type: py ownclass.py to run the program
In VSC or another program, press the run button, or ctrl f5.

For the specialty method in my Pizza class or you could say at my resturaunt, the popular pizzas I have implemented or serve are:
"hawaiian" "meat lovers" "four cheese" "vegetarian" and "margherita"
The types of crusts we have are "thin" "thick" "stuffed" and "normal"

Thank you for checking out my Pizza class! View it here on GitHub: https://github.com/nvoss01/nvosspy
