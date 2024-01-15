#Chong Weng Thim
#TP068621

#mainpage
def main():
    print(("-")*150)
    print("Welcome to FRESHCO main page!\n\nSection1:Login\nSection2:New User Registration\nSection3:Search Groceries Item\nSection4:Exit")
    section=input("Please select the section you want to go through [1/2/3/4]:")

    #call login function
    if section=="1":
        login()

    #call registration function
    elif section=="2":
        registration()
     
    #call search function        
    elif section=="3":
        search()
        main()
          
    #call exit function
    elif section=="4":
        exit()

    #avoid program stop running when invalid input
    else:
        print("Invalid.... please enter again")
        main()

    return section

#--------------------------------------------------------------------------------------------------------------------------------------------------------------
#user and admin login
def login():
    
    #open file to read
    userfile=open("freshco_user.txt","r")
    userinfo=userfile.read()
    
    #open file to read
    adminfile=open("freshco_admin.txt","r")
    admininfo=adminfile.read()
    
    while True:
        username=input("Enter your username:")
        password=input("Enter your password:")
        if username and password in userinfo:
            userpage()
        elif username and password in admininfo:
            adminpage()
            break

        #avoid program stop running if wrong input is entered
        else:
            print("Wrong username/password, Reenter!!")
            continue
    
    
def userpage():
    print(("-")*150)
    print("Welcome to FRESHCO user page!")
    print("1.View groceries\n2.Search groceries\n3.Place order\n4.View order/Make payment\n5.Personal information\n6.mainpage")
    choice=input("Please select the section you want to go through [1/2/3/4/5/6]:")
    #call view function
    if choice=="1":
        view()
        userpage()
        
    #call search function
    elif choice=="2":
        search()
        userpage()

    #call order function    
    elif choice=="3":
        order()

    #call view order function    
    elif choice=="4":
        view_order()
        userpage()
        
    #call view personal info function
    elif choice=="5":    
        personal_info()
        userpage()

    #call mainpage function
    elif choice=="6":
        main()

    #avoid program stop running if wrong input is entered
    else:
        print("Invalid, please select again!")
        userpage()
     

    return choice    

def adminpage():
    print(("-")*150)
    print("Welcome to FRESHCO admin page!")
    print("1.View groceries\n2.Search groceries\n3.Update groceries\n4.Add item\n5.Remove item\n6.View all customer order\n7.View specific customer order\n8.mainpage")
    choice=input("Please select the section you want to go through [1/2/3/4/5/6/7/8]:")
    
    #call view function
    if choice=="1":
        view()
        adminpage()
    #call search function
    elif choice=="2":
        search()
        adminpage()
    #call update item function
    elif choice=="3":
        update()
        adminpage()
    #call add item function
    elif choice=="4":
        add()
        adminpage()
    #call remove item function
    elif choice=="5":
        remove()
        adminpage()
    #call view customer order function
    elif choice=="6":
        view_all_order()
        adminpage()
    #call view_specific_function
    elif choice=="7":
        view_specific_order()
        adminpage()
    #call main function
    elif choice=="8":
        main()
    #avoid program stop running if wrong input is entered
    else:
        print("Invalid, please select again!")
        adminpage()
        
    return choice
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#new user registration
def registration():
    userfile=open("freshco_user.txt","r")
    userinfo=userfile.read()
    
    while True:
        print(("-")*150+"\nSection2:New User Registration")
        new_username=input("\nEnter your full name:")
        #avoid same people register again
        if new_username in userinfo:
            print("This name is registered, please try again")
            continue
        else:
            break
        
    new_gender=input("\nEnter your gender(m/f):")
    new_address=input("\nEnter your address:")
    new_email=input("\nEnter your email:")
        
    while True:
        new_contact=input("\nEnter your contact:")
        #program will not stop running when input is not number
        try:
            new_contact==int(new_contact)
        except:
            print("Invalid, please enter CONTACT NUMBER again")
            continue
        break
    
    while True:
        new_DOB=input("\nEnter your Date of Birth(DD/MM/YYYY):")
        #program will not stop running when input is wrong
        if len(new_DOB)==10:
            break
        else:
            print("Invalid, please enter DATE OF BIRTH again")
            continue
        
    while True:
        new_userID=input("\nEnter your user ID:")
        #avoid same ID used by different user
        if new_userID in userinfo:
            print("This username is used, please try another")
            continue
        else:
            break
        
    while True:
        new_pw=input("\nCreate password(at least 8 digit):")
        if len(new_pw)<8:
            print("Your password must be at least 8 digit")
            continue
        new_pw1=input("\nConfirm password:")
        #avoid program stop running when confirm password does not match
        if new_pw!=new_pw1:
            print("Password is not matched! Please input the same password!")
            continue
        else:
            break
    
        
    #new user information    
    userinfo=(new_username + "\t" + new_gender + "\t" + new_address + "\t" + new_email + "\t" + new_contact + "\t" + new_DOB + "\t" + new_userID + "\t" + new_pw)
    
    #open user text file to add new information
    userfile=open("freshco_user.txt","a")
    userfile.write(userinfo)
    userfile.close()

    print("Register sucessfully!, you can now proceed to login")
    main()
#---------------------------------------------------------------------------------------------------------------------------------------------------------------
#function to search item
def search():
    while True:
        print(("-")*150+"\nSearch item")
        searchfile=open("freshco_groceries.txt","r")   
        search=input("\nType id or name you want to search:")

        #capitalise 1st letter
        for line in searchfile:
            line=line.rstrip()
            if not search.title() in line:
                continue
            print("ID,Type,Product,Price,Details")
            print(line)
        searchfile.close()

        #Ask user if they want to search again
        option = input("\nDo you want to search more items?(yes/no):")
        if option == "yes":
            continue
        elif option == "no":
            break

        
#function to view item
def view():
    print(("-")*150+"\nView item")
    file=open("freshco_groceries.txt","r")
    for line in file:
        line=line.rstrip()
        print(line)
    file.close()
    
                    
                    
    
    
    
#function to add item
def add():
    print(("-")*150+"\nAdd new item")
    new_id=input("Enter new id:")
    new_category=input("Enter new category:")
    new_product=input("Enter new product:")
    new_price=input("Enter new price(RMX):")
    new_details=input("Enter new details:")

    #open file to add new item information
    file=open("freshco_groceries.txt","a")
    new_info=(new_id + "," + new_category + "," + new_product + "," + new_price + "," + new_details )
    file.write(new_info)
    file.close()

    print("Added successfully!")
    
#function to remove item
def remove():
    while True:
        print(("-")*150+"\nRemove item")
        remove_file=open("freshco_groceries.txt","r")
        remove=input("\nEnter the id of grocery that you want to remove:")
        
        for line in remove_file:
            line=line.rstrip()
            if not remove in line:
                continue
            print(line)
            
        select=input("\nDo you want to remove this item(yes/no)?")

        #print all things again except "remove"
        if select=="yes":
            
            delete_file=open("freshco_groceries.txt","r")
            lines=delete_file.readlines()
            delete_file.close()
            delete_file=open("freshco_groceries.txt","w")
            for i in lines:
                if not i.strip(",").startswith(remove):
                    delete_file.write(i)
            delete_file.close()
            print("Remove seccessfully")

        elif select=="no":
            break

        more=input("Do you want to remove more item(yes/no)?:")
        if more=="yes":
            continue
        elif more=="no":
            break
        remove_file.close()





#function to see personal information
def personal_info():
    print(("-")*150+"\nPersonal Information")
    personal_info=input("\nEnter your fullname/user ID to see your personal information:")
    file=open("freshco_user.txt","r")
    for line in file:
        line=line.rstrip()
        if not personal_info in line:
            continue
        print("Name\t\tGender\taddress\temail\t\tDOB\t\tuserID\tpassword")
        print(line)
    file.close()


#function to add order
def order():
    print(("-")*150 + "\nPlace your order")
    view()
    product_id=input("\nEnter the product id you want to add to your cart:")
    if product_id=="01":
        apple()
        
    elif product_id=="02":
        orange()
        userpage()
    elif product_id=="03":
        bacon()
        userpage()
    elif product_id=="04":
        bacon()
        userpage()
    elif product_id=="05":
        twisties()
        userpage()
    elif product_id=="06":
        lays()
        userpage()
    elif product_id=="07":
        softener()
        userpage()
    elif product_id=="08":
        detergent()
        userpage()
    elif product_id=="09":
        vitagen()
        userpage()
    elif product_id=="10":
        sprite()
        userpage()
    else:
        print("Invalid, please enter again")
        order()

#function to view cart and make payment
def view_order():
    while True:
        print(("-")*150+"\nView cart")
        viewfile=open("freshco_cart.txt","r")   
        view_name=input("\nType your fullname to view cart:")
        
        count=0   
        for line in viewfile:
            line=line.rstrip()
            if not view_name in line:
                continue
            count+=1
            print("Name\t\tID\tProduct\tAmount\t\tTotal.price")
            print(line)
            split=line.split("\t")
            print("\nYour grand total is:"+split[4])
        viewfile.close()

        #program will not stop if wrong input 
        if count == 0:      
            print("Invalid")
            view_order()    

        choose = input("\nDo you want to add more items into your cart?(yes/no):")
        if choose == "yes":
            order()
            
        elif choose == "no":
            checkout=input("\nDo you want to make payment now?(yes/no):")
            if checkout=="yes":
                break
            
            elif checkout=="no":
                userpage()
            
    while True:       
            card=input("\nEnter your credit card number(16digit):")
            if len(card)==16:
                break
            else:
                print("Invalid credit card number!Try again!")
                continue
        
                

    while True: 
        pin=input("\nEnter your 6-digit pin:")
        if len(pin)==6:
            delete_file=open("freshco_cart.txt","r")
            #convert to lists
            lines=delete_file.readlines()
            delete_file.close()
            delete_file=open("freshco_cart.txt","w")
            for i in lines:
                #rewrite the whole file except starts with the user's full name
                if not i.strip(",").startswith(view_name):
                     
                    delete_file.write(i)
            delete_file.close()
            print("\n---Payment processing---")
            print("---Payment successful!---")
            print("---Going back to userpage---")
            userpage()
    

        else:
             
            print("Invalid 6-digit pin! Try again!")
            continue

#function to view specific customer's cart
def view_specific_order():
     while True:
        print(("-")*150+"\nView specific customer cart")
        viewfile=open("freshco_cart.txt","r")   
        view_name=input("\nType customer fullname to view cart:")
        
        #print line starts with (view_name)
        for line in viewfile:
            line=line.rstrip()
            if not view_name in line:
                continue
            print("Name\t\tID\tProduct\tAmount\t\tTotal.price")
            print(line)
        viewfile.close()
        
        viewmore=input("\nDo you want to view more customer cart?(yes/no):")
        if viewmore=="yes":
            continue
        elif viewmore=="no":
            break

#function to view all customers' cart
def view_all_order():
    print(("-")*150+"\nView all customer cart")
    view_all=open("freshco_cart.txt","r")
    for line in view_all:
        line=line.rstrip()
        print(line)
    view_all.close()

    
#function to update item
def update():
    print(("-")*150+"\nUpdate item")
    file=open("freshco_groceries.txt","r")
    edit_groceries=file.readlines()
        
    stuff=0
    #first line will be shown as[1],2nd line will be shown as [2] .....
    for i in edit_groceries:
        print("[",(stuff+1),"]",i.strip())
        stuff+=1

    try:      
        stuff_number=input("\nEnter the number of line that you wish to edit:")
        if 0<int(stuff_number)<=int(stuff):
            #the 1st is = 0th in list
            number_selected=edit_groceries[int(stuff_number)-1].split(",")

            info=0
            #first line will be shown as[1],2nd line will be shown as [2] .....
            for stuff_info in number_selected:
                print("[",(info+1),"]",stuff_info)
                info+=1
            info_number=input("\nEnter the number of info you wish to edit:")
            if 0<int(info_number)<=int(info):
                new_edit=input("\nEnter new info:")

                if new_edit != number_selected[int(info_number)-1]:
                    if info_number==5:
                        new_line="\n"
                        number_selected[int(info_number)-1]=new_edit+new_line+new_line
                        updated_record=",".join(number_selected)
                        edit_groceries[int(stuff_number)-1]=updated_record
                        with open("freshco_groceries.txt","w") as file:
                            file.writelines(edit_groceries)
                        file.close()
                        print("\nRecord updated!")
                    elif info_number != 5:
                        new=""
                        number_selected[int(info_number)-1]=new_edit+new
                        updated_record=",".join(number_selected)
                        edit_groceries[int(stuff_number)-1]=updated_record
                        with open("freshco_groceries.txt","w") as file:
                            file.writelines(edit_groceries)
                        file.close()
                        print("\nRecord updated!")
          
            else:
                print("Invalid input!")
                
        else:
            print("Invalid input!")
            
    except:
        print("Invalid input!")

   


    
    
  


#------------------------------------------------------------------------------------------------------------------------------
#function to add into cart text file
def apple():
    while True:
        name_apple=input("Enter your fullname:")
        quantity_apple=input("Enter how many packs of apples you want to add into your cart:")
    
        price_apple=int(quantity_apple)*9
        price_apple=str(price_apple)
        cart_apple=(name_apple + "\t" + "01" + "\t" + "Apple" + "\t" + quantity_apple+"pack(s)" + "\t" + "RM"+price_apple)
        #add into file
        applefile=open("freshco_cart.txt","a")
        applefile.write(cart_apple)
        applefile.close()
        print("Added to your cart")
        ask=input("\nDo you want to add more item(yes/no)?:")
        if ask=="yes":
            order()
            
        elif ask=="no":
            userpage()
            break

def orange():
    while True:
        name_orange=input("Enter your fullname:")
        quantity_orange=input("Enter how many packs of oranges you want to add into your cart:")
    
    
        price_orange=int(quantity_orange)*9
        price_orange=str(price_orange)
        cart_orange=(name_orange + "\t" + "02" + "\t" + "orange" + "\t" + quantity_orange+"pack(s)" + "\t" + "RM" + price_orange)
        #add into file
        orangefile=open("freshco_cart.txt","a")
        orangefile.write(cart_orange)
        orangefile.close()
        print("Added to your cart")
        ask=input("\nDo you want to add more item(yes/no)?:")
        if ask=="yes":
            order()
            
        elif ask=="no":
            userpage()
            break
def egg():
    while True:
        name_egg=input("Enter your fullname:")
        quantity_egg=input("Enter how many packs of eggs you want to add into your cart:")
    
    
        price_egg=int(quantity_egg)*8
        price_egg=str(price_egg)
        cart_egg=(name_egg + "\t" + "03" + "\t" + "Egg" + "\t" + quantity_egg+"pack(s)" + "\t" + "RM"+price_egg)
        #add into file
        eggfile=open("freshco_cart.txt","a")
        eggfile.write(cart_egg)
        eggfile.close()
        print("Added to your cart")
        ask=input("\nDo you want to add more item(yes/no)?:")
        if ask=="yes":
            order()
            
        elif ask=="no":
            userpage()
            break
def bacon():
    while True:
        name_bacon=input("Enter your fullname:")
        quantity_bacon=input("Enter how many packs of bacons you want to add into your cart:")
    
    
        price_bacon=int(quantity_bacon)*9
        price_bacon=str(price_bacon)
        cart_bacon=(name_bacon + "\t" + "04" + "\t" + "Bacon" + "\t" + quantity_bacon+"pack(s)" + "\t" + "RM"+price_bacon)
        #add into file
        baconfile=open("freshco_cart.txt","a")
        baconfile.write(cart_bacon)
        baconfile.close()
        print("Added to your cart")
        ask=input("\nDo you want to add more item(yes/no)?:")
        if ask=="yes":
            order()
            
        elif ask=="no":
            userpage()
            break
def twisties():
    while True:
        name_twisties=input("Enter your fullname:")
        quantity_twisties=input("Enter how many packs of twisties you want to add into your cart:")
    
    
        price_twisties=int(quantity_twisties)*2
        price_twisties=str(price_twisties)
        cart_twisties=(name_twisties + "\t" + "05" + "\t" + "Twisties" + "\t" + quantity_twisties+"pack(s)" + "\t" + "RM"+price_twisties)
        #add into file
        twistiesfile=open("freshco_cart.txt","a")
        twistiesfile.write(cart_twisties)
        twistiesfile.close()
        print("Added to your cart")
        ask=input("\nDo you want to add more item(yes/no)?:")
        if ask=="yes":
            order()
            
        elif ask=="no":
            userpage()
            break
def lays():
    while True:
        name_lays=input("Enter your fullname:")
        quantity_lays=input("Enter how many packs of lays you want to add into your cart:")
    
    
        price_lays=int(quantity_lays)*3.5
        price_lays=str(price_lays)
        cart_lays=(name_lays + "\t" + "06" + "\t" + "Lays" + "\t" + quantity_lays+"pack(s)" + "\t" + "RM"+price_lays)
        #add into file
        laysfile=open("freshco_cart.txt","a")
        laysfile.write(cart_lays)
        laysfile.close()
        print("Added to your cart")
        ask=input("\nDo you want to add more item(yes/no)?:")
        if ask=="yes":
            order()
            
        elif ask=="no":
            userpage()
            break
def softener():
    while True:
        name_softener=input("Enter your fullname:")
        quantity_softener=input("Enter how many bottles of softeners you want to add into your cart:")

        price_softener=int(quantity_softener)*8.5
        price_softener=str(price_softener)
        cart_softener=(name_softener + "\t" + "07" + "\t" + "Softener" + "\t" + quantity_softener+"bottle(s)" + "\t" + "RM"+price_softener)
        #add into file
        softenerfile=open("freshco_cart.txt","a")
        softenerfile.write(cart_softener)
        softenerfile.close()
        print("Added to your cart")
        ask=input("\nDo you want to add more item(yes/no)?:")
        if ask=="yes":
            order()
            
        elif ask=="no":
            userpage()
            break
def detergent():
    while True:
        name_detergent=input("Enter your fullname:")
        quantity_detergent=input("Enter how many bottles of detergents you want to add into your cart:")
    
    
        price_detergent=int(quantity_detergent)*7.5
        price_detergent=str(price_detergent)
        cart_detergent=(name_detergent + "\t" + "08" + "\t" + "Detergent" + "\t" + quantity_detergent+"bottle(s)" + "\t" + "RM"+price_detergent)
        #add into file
        detergentfile=open("freshco_cart.txt","a")
        detergentfile.write(cart_detergent)
        detergentfile.close()
        print("Added to your cart")
        ask=input("\nDo you want to add more item(yes/no)?:")
        if ask=="yes":
            order()
            
        elif ask=="no":
            userpage()
            break
def vitagen():
    while True:
        name_vitagen=input("Enter your fullname:")
        quantity_vitagen=input("Enter how many packs of Vitagen you want to add into your cart:")
    
    
        price_vitagen=int(quantity_vitagen)*5
        price_vitagen=str(price_vitagen)
        cart_vitagen=(name_vitagen + "\t" + "09" + "\t" + "Vitagen" + "\t" + quantity_vitagen+"pack(s)" + "\t" + "RM"+price_vitagen)
        #add into file
        vitagenfile=open("freshco_cart.txt","a")
        vitagenfile.write(cart_vitagen)
        vitagenfile.close()
        print("Added to your cart")
        ask=input("\nDo you want to add more item(yes/no)?")
        if ask=="yes":
            order()
            
        elif ask=="no":
            userpage()
            break
def sprite():
    while True:
        name_sprite=input("Enter your fullname:")
        quantity_sprite=input("Enter how many bottles of sprite you want to add into your cart:")
    
    
        price_sprite=int(quantity_sprite)*6.5
        price_sprite=str(price_sprite)
        cart_sprite=(name_sprite + "\t" + "10" + "\t" + "Sprite" + "\t" + quantity_sprite+"bottle(s)" + "\t" + "RM"+price_sprite)
        #add into file
        spritefile=open("freshco_cart.txt","a")
        spritefile.write(cart_sprite)
        spritefile.close()
        print("Added to your cart")
        ask=input("\nDo you want to add more item(yes/no)?:")
        if ask=="yes":
            order()
            
        elif ask=="no":
            userpage()
            break
            
    

main()




    
        
        
        

