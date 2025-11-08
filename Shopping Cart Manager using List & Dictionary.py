import time 
print("Welcome to Shopping Card Manager\n")

card = {}

while True:

    options = ["add item", "remove item", "view card", "exist"]

    for count, lst in enumerate(options,1):
        print("\n{}.{}".format(count, lst))

    print("\nEnter you choice for next move")
    choice = int(input("press the option (1,2,3,4) :"))

    if choice >= 5 and choice >=0:
       print("choose the correct option")
       time.sleep(2)

    else:
              
        if choice == 1:
           added_item = input("\nenter the items:")
    
           if added_item in card:
             card[added_item] += 1
           else:
             card[added_item] = 1
            #print("successfully added")
    
        if choice == 2:
           remove_item = input("\nenter the items to remove form you card:")
           card[remove_item] -= 1
           if card[remove_item] == 0:
            card.pop(remove_item) 
            print("successfully remove")
    
        if choice == 3:
           print(card)
           time.sleep(2)
    
        if choice == 4:
            print("Thank you for using Shopping Cart Manager!")
            break
    
