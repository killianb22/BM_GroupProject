menu = 0
while menu != 5:
    print('1. View/Add Stock')
    print('2. View Shopping Basket')
    print('3. View Change Calculator')
    print('4. Item Packing Assisance')
    print('5. Exit')


    menu_str = input('Choose option (Enter option number)')
    menu = int(menu_str)


#View/Add Stock
    if menu == 1:
        stock_menu = 0
        while stock_menu != 3:
            print('1. View stock')
            print('2. Add Stock')
            print('3. Back to main menu')


            stock_menu_str = input('Choose an option')
            stock_menu = int(stock_menu_str)
            

#Shopping Basket & Calculations   
    elif menu == 2:
        sb_menu = 0
        while sb_menu != 4:
            print('1. Buy Luxury Item')
            print('2. Buy Essential Item')
            print('3. Buy Gift Card')
            print('4. Back to main menu')

            sb_menu_str = input('Choose an option')
            sb_menu = int(sb_menu_str)
        
       
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