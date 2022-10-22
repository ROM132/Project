class Shop:
    password = "1234"
    product = {
        "1001": ["keyboard", 100, 180, False],
        "1002": ["mouse", 100, 180, False],
        "1003": ["phone", 100, 180, False],
    }

    def __init__(self, password=password, money=0, ok=False):
        self.ok = ok
        self.money = money
        self.password = password

    def Login(self):
        user_choice = input("Login Admin/Login User  [Type A to Login in Admin/ Type U to login in the User]: ").lower()
        if user_choice == "a":
            s.Admin_check()
        elif user_choice == "u":
            s.User()
        else:
            print("Invalid input try again!")
            s.Login()

    def Admin(self):
        print("welcome back Rom!")
        print("What you want to do today?")
        while True:
            s.Menu()
            qus = input("What you want to do?: ")
            if qus == "1":
                for key in self.product:
                    print(key, ' : ', self.product[key])
            elif qus == "2":
                while True:
                    id_ = input("Enter the id: ")
                    product_name = input("Enter product name: ")
                    product_quantity = input("Enter product quantity: ")
                    product_price = input("Enter product price: ")
                    if product_price.isdigit() and product_price.isdigit() or product_price.isdigit() or product_quantity.isdigit():
                        product_price = int(product_price)
                        product_quantity = int(product_quantity)
                    else:
                        print("Pls enter a number next time in the quantity and the price!")

                    for item in self.product:
                        if self.product[item][0] == product_name and item == id_:
                            print("You already have this id and this name try again!")
                            break
                        elif self.product[item][0] == product_name:
                            print("You already have this product name try again!")
                            break
                        elif item == id_:
                            print("You already have this id try again!")
                            break

                    add_product = f"{id_}: [{product_name}, {product_price}]"
                    self.product[id_] = [product_name, product_quantity, product_price]
                    break

            elif qus == "3":
                remove_id = input("Enter the id you want to delete: ")
                for key, value in list(self.product.items()):
                    if key == remove_id:
                        print(f"id {remove_id} removed succeeded")
                        del self.product[key]
                        s.Admin()
                print("The id do not found!")

            elif qus == "4":
                my_available = 0
                for key in self.product:
                    my_available += int(self.product[key][1])
                print(my_available)
            elif qus == "5":
                my_available = 0
                for key in self.product:
                    my_available += int(self.product[key][2]) * int(self.product[key][1])
                print(my_available)
            elif qus == "6":
                print("Logout succeeded")
                s.Login()
            else:
                print("Invalid input try again!")
                continue

    def User(self):
        while True:
            s.user()
            qus = input("What you want to do?: ")
            if qus == "1":
                for key in self.product:
                    print(key, ' : ', self.product[key])
            elif qus == "2":
                while True:
                    qus = input("Enter the id you want to buy: ")
                    key = qus
                    val = self.product.get(key)
                    if val is None:
                        print(f"You choose not available item")
                        break
                    else:
                        if self.money > self.product[key][2]:
                            self.product[key][1] = self.product[key][1] - 1
                            self.product[key][3] = True
                            print("You place the order!")
                            break
                        else:
                            print("You dont have enough money!")
                            break

            elif qus == "3":
                while True:
                    qus = input("Enter the id you want to cancel: ")
                    key = qus
                    val = self.product.get(key)
                    if val is None:
                        print(f"You choose not available item")
                        continue
                    else:
                        if self.product[key][3]:
                            self.product[key][1] = self.product[key][1] + 1
                            print("You cancel the order!")
                            break
                        else:
                            print("You dont order this!")
                            break

            elif qus == "4":
                if self.ok:
                    print("You can't take more money!")
                    s.User()
                else:
                    pass
                while True:
                    print(f"You currency money is {self.money}")
                    self.money = input("Enter how much money you like to have (0-1000): ")
                    if self.money.isdigit():
                        self.money = int(self.money)
                        if self.money <= 1000:
                            print("Your money update!")
                            self.ok = True
                            break
                        else:
                            print("Pls pick a number under 1000!")
                            self.money = 0
                            break
                    else:
                        print("Pls pick a number! next time!")
                        continue

            elif qus == "5":
                print("Logout succeeded")
                s.Login()
            else:
                print("Invalid input! try again")
                continue

    def Admin_check(self):
        try_password = 3
        while True:
            password = input("Enter the password: ")
            if password == self.password:
                s.Admin()
            else:
                try_password -= 1
                if try_password == 0:
                    print("You ran out of attempt! you are blocked!")
                    exit()
                else:
                    pass
                print(f"Incorrect password! {try_password} more attempt left!")
                continue

    def Menu(self):
        print("====================")
        print("1. Display Product")
        print("2. Add Product")
        print("3. Remove Product")
        print("4. All Product available")
        print("5. Total Income")
        print("6. Logout")
        print("====================")

    def user(self):
        print("====================")
        print("1. Display Product")
        print("2. Place order")
        print("3. Cancel order")
        print("4. Add money")
        print("5. Logout")
        print("====================")


s = Shop()
s.Login()
