from menu import Pizza, Burger, Drinks, Menu
from Restaurant import Restaurant
from User import Customer, Cheef, Server, Manager
from order import Order

def main():
    menu = Menu()
    pizza_1 = Pizza('Shutkhi Pizza', 600, 'large', ['shotkhi', 'onion'])
    menu.add_menu_item('pizza', pizza_1)
    pizza_2 = Pizza('Chicken Pizza', 400, 'large', ['chicken', 'onion', 'oil'])
    menu.add_menu_item('pizza', pizza_2)
    pizza_3 = Pizza('Beef Pizza', 500, 'large', ['beef', 'oil'])
    menu.add_menu_item('pizza', pizza_3)

    #add burger
    burger_1 = Burger('Naga Burger', 1000, 'Chichen', ['bread', 'chili'])   
    menu.add_menu_item('burger', burger_1) 
    burger_2 = Burger('beef Burger', 1000, 'Chichen', ['beef', 'chili']) 
    menu.add_menu_item('burger', burger_2) 

    #Add drinks
    coke = Drinks('Coke', 50, True)
    menu.add_menu_item('drinks', coke)
    coffee = Drinks("Mocha coffee", 200, False)
    menu.add_menu_item('drinks', coffee)

    #show Menu
    menu.show_menu()

    tasty_treat_restaurant = Restaurant("Testy Treat", 2000, menu)

    # add emoloyees
    manager = Manager('sakib manager',1234, 'sakin12@gmail.com', 'noakhali', 12000, 'Jan 1 2020', 'core')
    tasty_treat_restaurant.add_employee('manager', manager)

    cheef = Cheef('rustom Baburchi', 12324234, 'rostom@gmail.com', 'noakhali', 1200, 'jan 4 2002', 'cheef', 'polaw' )
    tasty_treat_restaurant.add_employee('cheef', cheef)

    server = Server('Chotu Server', 4554, 'chto@gmail.com', 'patiya', 200, 'Feb 1 2020', 'Server')
    tasty_treat_restaurant.add_employee('server', server)

    #show employee
    tasty_treat_restaurant.show_employee()

    #Customer 
    customer_1 = Customer('Sakib khan', 234, 'sakib@gmail.com', 'bonani', 100000)
    order_1 = Order(customer_1, [pizza_3, coffee])
    customer_1.pay_for_order(order_1)
    tasty_treat_restaurant.add_order(order_1)
    #Customer_1 paying for order_1
    tasty_treat_restaurant.receive_payment(order_1, 2000, customer_1)
    print("revenue and balance after first customer", tasty_treat_restaurant.revenue, tasty_treat_restaurant.balance)

    #Customer 
    customer_2 = Customer('rakib khan', 23456, 'rakib@gmail.com', 'bonani', 1000000)
    order_2= Order(customer_2, [pizza_2, coffee])
    customer_2.pay_for_order(order_2)
    tasty_treat_restaurant.add_order(order_2)
    #Customer_1 paying for order_1
    tasty_treat_restaurant.receive_payment(order_2, 3000, customer_2)
     
    print("revenue and balance after Second customer", tasty_treat_restaurant.revenue, tasty_treat_restaurant.balance)
 
    #pay rent
    tasty_treat_restaurant.pay_expense(tasty_treat_restaurant.rent, 'Rent')
    print("after rent ", tasty_treat_restaurant.revenue, tasty_treat_restaurant.balance, tasty_treat_restaurant.expense)


    tasty_treat_restaurant.pay_salary(cheef)
    print("after salary", tasty_treat_restaurant.revenue, tasty_treat_restaurant.balance, tasty_treat_restaurant.expense)

#call the main
# main()
# or
if __name__=='__main__':
    main()