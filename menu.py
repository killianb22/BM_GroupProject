all_essential_stock = {}
all_gift_stock = {}
all_luxury_stock = {}
shoppingbasket = {}

class user(object):
    def __init__(self):
        self.userId = ''
        self.items = ''

    def set_userID(self, new_userID):
        self.userId = new_userID

    def get_userID(self):
        return self.userId

    def set_item(self, new_item):
        self.item = new_item

    def get_item(self):
        return self.item

    def display(self):
        print(f'userId: {self.userId}')
        print(f'item: {self.item}')

menu = 0
while menu != 5:
    print('1. View/Add Stock')
    print('2. View Shopping Basket')
    print('3. View Change Calculator')
    print('4. Item Packing Assisance')
    print('5. Exit')
    print()

    menu_str = input('Choose option (Enter option number): ')
    print()
    menu = int(menu_str)

#View/Add Stock
    if menu == 1:
        stock_menu = 0
        while stock_menu != 3:
            print('1. View stock')
            print('2. Add Stock')
            print('3. Back to main menu')
            print()

            stock_menu_str = input('Choose an option: ')
            stock_menu = int(stock_menu_str)
            
            if stock_menu == 1:
                stock_type = 0
                while stock_type != 4:
                    print('1. View essential stock')
                    print('2. View luxury stock')
                    print('3. View gift stock')
                    print('4. Exit')
                    print()

                    stock_type_str = int(input('Choose an option (1-4): '))
                    print()
                    stock_type = stock_type_str

                    if stock_type == 1:
                        print(f'Essential Stock and its expiry dates: {all_essential_stock}')
                        print()
                        delete_essential = input('Would you like to delete an essential item? (Yes or No): ')
                        if delete_essential == 'Yes':
                            which_essential = input('Which item would you like to delete?: ')
                            if which_essential in all_essential_stock:
                                del all_essential_stock[which_essential]
                                print(f'{which_essential} has successfully been deleted!')
                                print(f'Here is the remaining stock: {all_essential_stock}')
                            else:
                                print('Sorry, that item is not in stock')


                    elif stock_type == 2:
                        print(f'Luxury Stock and its expiry dates: {all_luxury_stock}')
                        print()
                        delete_luxury = input('Would you like to delete an luxury item? (Yes or No): ')
                        if delete_luxury == 'Yes':
                            which_luxury = input('Which item would you like to delete?: ')
                            if which_luxury in all_luxury_stock:
                                del all_luxury_stock[which_luxury]
                                print(f'{which_luxury} has successfully been deleted!')
                                print(f'Here is the remaining stock: {all_luxury_stock}')
                            else:
                                print('Sorry, that item is not in stock')
                            
                    
                    elif stock_type == 3:
                        print(f'Gift Stock and its expiry dates: {all_gift_stock}')
                        print()
                        delete_gift = input('Would you like to delete an gift item? (Yes or No): ')
                        if delete_gift == 'Yes':
                            which_gift = input('Which item would you like to delete?: ')
                            if which_gift in all_gift_stock:
                                del all_gift_stock[which_gift]
                                print(f'{which_gift} has successfully been deleted')
                                print(f'Here is the remaining stock: {all_gift_stock}')
                            else:
                                print('Sorry, that item is not in stock')

            if stock_menu == 2:
                userId = input('Enter your id number: ')
                item_type = input('Is the item you are adding essential, luxury or gift?: ')


                if item_type == 'essential':
                    ess_item_name = input('What is the item?: ')
                    ess_expiry_date = input('Whats the expiry date?: ')
                    print()
                    all_essential_stock[ess_item_name] = ess_expiry_date
                    print(f'The item was successfully added: {all_essential_stock}')
                    print()

                elif item_type == 'luxury':
                    lux_item_name = input('What is the item?: ')
                    lux_expiry_date = input('Whats the expiry date?: ')
                    print()
                    all_luxury_stock[lux_item_name] = lux_expiry_date
                    print(f'The item was successfully added: {all_luxury_stock}')
                    print()

                elif item_type == 'gift':
                    gift_item_name = input('What is the item?: ')
                    gift_expiry_date = input('Whats the expiry date?: ')
                    print()
                    all_gift_stock[gift_item_name] = gift_expiry_date
                    print(f'The item was successfully added: {all_gift_stock}')
                    print()
                
                users = []
                # Create a new User object and set the specific
                #user = user()
                #user.set_userID(userId)
                #user.set_item(item)
       
                # Add new user to the list of all users
                #users.append(user)

#Shopping Basket & Calculations   
    elif menu == 2:
        sb_menu = 0
        while sb_menu != 5:
            print('1. Buy Luxury Item')
            print('2. Buy Essential Item')
            print('3. Buy Gift Card')
            print('4. Shopping Basket')
            print('5. Back to main menu')
            print()

            sb_menu_str = input('Choose an option (1-4): ')
            print()
            sb_menu = int(sb_menu_str)

            if sb_menu == 1:
                price_lux = 50
                print(f'These are the Luxury Items available: {all_luxury_stock}')
                print('Each Luxury item costs €50')
                print()

                users_lux_item = input('Which product would you like to purchase? ')
                if users_lux_item in all_luxury_stock:
                    shoppingbasket[users_lux_item] = price_lux
                    print(f'Items currently in basket: {shoppingbasket}')
                    print()
                else:
                    print(f'Sorry, {users_lux_item} is not in stock')


            if sb_menu == 2:
                price_ess = 30
                print(f'These are the Essential Items available: {all_essential_stock}')
                print('Each Essential item costs €30 ')
                print()

                users_ess_item = input('Which product would you like to purchase? ')
                if users_ess_item in all_essential_stock:
                    shoppingbasket[users_ess_item] = price_ess
                    print(f'Items currently in basket: {shoppingbasket}')
                    print()
                else:
                    print(f'Sorry, {users_ess_item} is not in stock')

            if sb_menu == 3:
                price_gift = 20
                print(f'These are the Gift Items available: {all_gift_stock}')    
                print('Each Gift item costs €20')   
                print()

                users_gift_item = input('Which product would you like to purchase? ')
                if users_gift_item in all_gift_stock:
                    shoppingbasket[users_gift_item] = price_gift
                    print(f'Items currently in basket: {shoppingbasket}')
                    print()
                else:
                    print(f'Sorry, {users_gift_item} is not in stock')     

            if sb_menu == 4:
                print(shoppingbasket)

#Change Calculator
    elif menu == 3:
        change = int(input('Enter total value of shopping basket'))

        cc_menu = 0
        while cc_menu != 3:
            print('1. Calculate')
            print('2. Clear all controls')
            print('3. Back to main menu')

            cc_menu_str = input('Choose an option')
            cc_menu = int(cc_menu_str)
        

#Item Packing
    elif menu == 4: 
        ip_menu = 0
        while ip_menu != 2:
            print('1. Enter box dimensions')
            print('2. Back to main menu')

            ip_menu_str = input('Choose an option')
            ip_menu = int(ip_menu_str)
    
    elif menu == 5:
        print('Thanks for shopping, have a nice day!')
