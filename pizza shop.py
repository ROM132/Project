import time


class Pizza_Shop:
    pizza_option = {
        "small pizza": ["small pizza", 11],
        "medium pizza": ["medium pizza", 16],
        "large pizza": ["large pizza", 21],
    }

    pizza_extras = {
        "olives": ["olives", 4],
        "tuna": ["tuna", 3],
        "corn": ["corn", 5],
    }
    print("Welcome to our pizza shop!\n"
          "##########################")

    def __init__(self, pizza=None, money=0, qus=None):
        self.pizza = pizza
        self.money = money
        self.qus = qus

    def money_handler(self):
        self.money = input("How much dollar you brought with you today?: ")
        time.sleep(2)
        if self.money.isdigit():
            self.money = int(self.money)
            p.before_buy_pizza()
        else:
            print("Pls enter a number next time!")
            p.money_handler()

    def before_buy_pizza(self):
        print(f"oh i see you brought with you {self.money} dollar today")
        time.sleep(2)
        print("What you like to buy? ")
        p.print_pizza()

    def print_pizza(self):
        my_keys = ""
        for key in self.pizza_option:
            my_keys += key + ", "
        print(my_keys)
        p.buy_pizza()

    def buy_pizza(self):
        self.qus = input(": ")
        key = self.qus
        val = self.pizza_option.get(key)
        if val is None:
            print(f"You choose not available item")
            p.buy_pizza()
        else:
            price = self.pizza_option[key][1]
            if self.qus == self.pizza_option[self.qus][0]:
                print(f"Ok the {self.qus} cost {self.pizza_option[key][1]} dollar")
                while True:
                    self.qus = input("are you sure you want to buy it? (y/n):  ").lower()
                    if self.qus == "y" and self.money >= price:
                        time.sleep(1)
                        self.pizza = self.pizza_option[key][1]
                        self.money = self.money - price
                        p.print_extras()
                    elif self.qus == "n":
                        print("Ok good bey!")
                        exit()
                    elif self.qus == "y" and self.money < price:
                        print("You dont have enough money try to buy other pizza!")
                        p.before_buy_pizza()
                    else:
                        print("Invalid input try again!")
            else:
                print("That not one of our option pls try again!")
                p.buy_pizza()

    def add_extras(self):
        self.qus = input(": ")
        key = self.qus
        val = self.pizza_extras.get(key)
        if val is None:
            print(f"You choose not available item")
            p.add_extras()
        else:
            extra = self.pizza_extras[key][0]
            extra_cost = self.pizza_extras[key][1]
            if self.qus == self.pizza_extras[key][0]:
                while True:
                    print(f"Ok the {extra} cost {extra_cost} dollar are you sure?")
                    self.qus = input("(yes/no): ")
                    if self.qus == "yes" and self.money > extra_cost:
                        print("Ok wait a second while we add it!")
                        time.sleep(3)
                        print(f"Ok we add the {extra} to your pizza")
                        print("Enjoy!\nGood bey!")
                        exit()
                    elif self.qus == "no":
                        print("Ok pick something else!")
                        p.print_extras()
                    elif self.qus == "yes" and self.money < extra_cost:
                        print("You dont have enough money!")
                        time.sleep(2)
                        p.print_extras()
                    else:
                        print("Invalid input try again!")

            elif self.qus == "none":
                print(f"Ok you got the {self.pizza} good bey and enjoy!")
                exit()
            else:
                print("Invalid input try again!")
                p.add_extras()

    def print_extras(self):
        print("What you want to add to the pizza?")
        my_keys_ = ""
        for key_ in self.pizza_extras:
            my_keys_ += key_ + ", "
        print(my_keys_ + "or none")
        p.add_extras()


p = Pizza_Shop()
p.money_handler()