import re
import requests
import json
import random
import ast


def my_fu():
	'''Starts with the main 
signup/loginlogout page.'''

	return None

print("Using __doc__:")
print(my_fu.__doc__)

print("===================================================")


username=""
print("WELOCOME....WE ARE HAPPY TO HAVE YOU.....")
print()
while(True):
    # global username
    print("1. SIGNUP")
    print("2. LOGIN")
    print("3. LOGout")
    print("4. Close the application")
    
    inp = int(input("Enter your choice please.....:"))
    if inp == 1:
        if(username!=""):
            print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
            print("Invalid operation")
            print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
            
        # id = int(input("Enter id number:"))
        else:
            username = input("Enter username:")
            password = input("Enter password:")

            response = requests.post("http://127.0.0.1:5000/signup",
                                    json={
                                        'username': username,
                                        'password': password
                                    })
            print(response.content)
            print("===================================================")
        
    elif inp == 2:
        # id = int(input("Enter id number:"))
        
        username = input("Enter username:")
        password = input("Enter password:")
        dic = {"username": username, "password": password}
        response = requests.post('http://localhost:5000/signin',
                                json={
                                    'username': username,
                                    'password': password
                                })
        print(response.content)
        # print("hello")
        if (response.content == b'LOG IN SUCCESSFUL'):



            def my_fun():
                '''Once the user logs in successfully ,display the options that he has.'''

                return None

            print("Using __doc__:")
            print(my_fun.__doc__)
            print("===================================================")
            print()

            if (username == "chef"):

                while True:
                    print("WELOCOME....You have logged in as the chef....")
                    print()
                    print("1. Read the menu")
                    print("2. Order food items")
                    # print("3. Generate bill")
                    print("3. View previous transactions")
                    print("4. Add new items in the database")
                    print("5. Go back to the login/signup/signout page")
                    inp = int(input("Enter your choice please.....:"))

                    if inp == 1:

                    
                        def my_fuc():
                            '''Reading the menu.'''

                            return None

                        print("Using __doc__:")
                        print(my_fuc.__doc__)
                        print("===================================================")
                        print()

                        # response = requests.post('http://localhost:5000/readbill',
                        #                         json={
                        #                             'username': username,
                                                    
                        #                         })
                        # print(response.content)
        # print("hello")
                        # if (response.content == b'yes'):
                        #     response = requests.get('http://localhost:5000/read')
                        #     # print(response.content)
                        #     data = json.loads(response.content)
                        #     print()
                        #     print("itenmo"+'\t'+"halfprice"+'\t'+"fullprice")
                        #     for key, value in data.items(): 
                        #         print(key, end='\t')
                        #         for k, v in value.items(): 
                        #             print(v, end='\t\t')
                        #         print()
                        #     print("===================================================")
                        # else:
                        #     print("You are not logged in")



                        response = requests.get('http://localhost:5000/read')
                        # print(response.content)
                        data = json.loads(response.content)
                        print()
                        print("itenmo"+'\t'+"halfprice"+'\t'+"fullprice")
                        for key, value in data.items(): 
                            print(key, end='\t')
                            for k, v in value.items(): 
                                print(v, end='\t\t')
                            print()
                        print("===================================================")
                    if inp == 4:

                        def my_fuc1():
                            '''Modifying the menu.'''

                            return None

                        print("Using __doc__:")
                        print(my_fuc1.__doc__)
                        print("===================================================")
                        print()



                        itemno=int(input("Enter the itemno: "))
                        halfprice =int( input("Enter halfprice:"))
                        fullprice= int(input("Enter fullprice:"))

                        response = requests.post("http://127.0.0.1:5000/additems",
                                                json={
                                                    'itemno': itemno,
                                                    'halfprice': halfprice,
                                                    'fullprice':fullprice
                                                })
                        print(response.content)

                    if inp == 2:





                        def my_fuc2():
                            '''Ordering items and generating the bills.'''

                            return None

                        print("Using __doc__:")
                        print(my_fuc2.__doc__)

                        print("===================================================")
                        print()
                        # orderid=int(input("Enter the orderid: "))
                        # itemno=int(input("Enter the itemno: "))
                        # username = input("Enter username:")
                        # quantity = input("Enter quantity:")
                        # plates= int(input("Enter no.of plates:"))

                        # response = requests.post("http://127.0.0.1:5000/orderitems",
                        #                         json={
                        #                             'orderid':orderid,
                        #                             'itemno': itemno,
                        #                             'username': username,
                        #                             'quantity':quantity,
                        #                             'plates':plates
                        #                         })
                        # print(response.content)
                        while True:

                            print("Time for the order")
                            print()
                            number_of_items=int(input("Enter the no.of items: after which your bill will be generated..."))

                            """Taking the order"""


                            items=[]
                            keeptrack={}
                            total=0
                            for each in range(number_of_items):
                                list_for_one_item=[]
                                item_id=input("Enter the item id of  " + str(each+1) + " order: ")
                                list_for_one_item.append(item_id)
                                quantity=input("Enter half/full : ")
                                list_for_one_item.append(quantity)
                                st=str(item_id)+quantity
                                
                                no_of_plates=int(input("Enter the no.of plates(quantity) : "))
                                list_for_one_item.append(no_of_plates)
                                if st in keeptrack:
                                    keeptrack[st]+=no_of_plates
                                    keeptrack[st]=(no_of_plates)
                                    print(type(keeptrack[st]))
                                else:
                                    keeptrack[st]=no_of_plates
                                    keeptrack[st]=(no_of_plates)
                                    print(type(keeptrack[st]))
                                items.append(list_for_one_item)
                                print()
                                print()

                            print("The available choices for the tip percentage are as follows:")
                            print("Please choose one from them: ")
                            print()
                            print("0%  Enter 0 for it..")
                            print("10% Enter 10 for it..")
                            print("20% Enter 20 for it..")
                            print()
                            tip_percentage=int(input("Your tip percentage would be......"))
                            print()

                            response = requests.get('http://localhost:5000/read')
                    # print(response.content)
                            data = json.loads(response.content)

                            # print(data)
                            
                            
                            for each in items:
                                # print(each[0])
                                # print(data[(each[0])])
                                x=data[(each[0])]
                                print(x['halfprice'])
                                if each[1]=="half":
                                    total+=int((data[(each[0])])['halfprice'])*int(each[2])
                                elif each[1]=="full":
                                    total+=int((data[(each[0])])['fullprice'])*int(each[2])
                                
                            fprice=0
                            listing=[]   
                            # print("hello")
                            for k,v in keeptrack.items():
                                list_for_one_item=[]
                                tprice=0
                                itemno=int(k[0])
                                list_for_one_item.append((k[0]))
                                half_or_full=k[1:]
                                list_for_one_item.append(half_or_full)
                                list_for_one_item.append(str(v))
                                if half_or_full=="half" :
                                    
                                    dict=data[str(itemno)]
                                    halfp=int(dict['halfprice'])
                                    # print(halfp)
                                    # print(type(halfp))
                                    tprice =tprice +  halfp*v
                                    half_or_full="Half"
                                else:
                                    # tprice+=int((data[str(itemno)])['fullprice'])*v
                                    dict=data[str(itemno)]
                                    fullp=int(dict['fullprice'])
                                    # print(fullp)
                                    # print(type(fullp))
                                    tprice =tprice +  fullp*v
                                    half_or_full="Full"
                                # print(f"item {itemno} [{half_or_full}] [{v}]:","{:.2f}".format(tprice))
                                listing.append(list_for_one_item)
                                fprice+=tprice
                            # print("hello")
                            # print("The listing value is" )
                            # print(listing)

                            response = requests.post("http://127.0.0.1:5000/orderitems",
                                            json={
                                                # 'orderid':orderid,
                                                # 'itemno': itemno,
                                                'username': username,
                                                'orderdetails':listing,
                                                'totalprice':total
                                            })
                            print(response.content)

                            print()
                            print("Time for the bill generation....")


                            total=total+ total*(tip_percentage/100)
                            print("TIME TO TEST YOUR LUCK")
                            print("===================================================")
                            print()
                            print()
                            print("Do you want to test your luck : tpye y/Y  for yes and n/N for no ")
                            decision=input()
                            print()
                            print()
                            chance=["50%_discount","25%_discount","10%_discount","0_discount","20%_increase"]
                            prob=[.05,.1,.15,.2,.5]
                            chance_that_comes=""
                            flag=True
                            discountmoney=0
                            increasemoney=0
                            if(decision=='y' or decision=='Y'):
                                chance_that_comes=random.choices(chance,prob)
                                
                                if(chance_that_comes==['50%_discount']):
                                    print("Congratulations!  You got a 50%"+" discount")
                                    discountmoney=total*0.5
                                    total=total-total*0.5
                                    
                                elif(chance_that_comes==['25%_discount']):
                                    print("Congratulations!  You got a 25%"+" discount")
                                    discountmoney=total*0.25
                                    total=total-0.25*total
                                
                                elif(chance_that_comes==['10%_discount']):
                                    print("Congratulations!  You got a 10%"+" discount")
                                    discountmoney=total*0.1
                                    total=total-total*0.1

                                elif(chance_that_comes==['0_discount']):
                                    print("Sorry! No discount")
                                    # discountmoney=-total*0.1
                                    flag=False

                                else:
                                    print("Sorry! You have to pay extra")
                                    increasemoney=total*0.2
                                    total=total+0.2*total
                                    flag=False
                            else:
                                pass
                            print()
                            if(flag==True and (decision=='y' or decision=='Y' )):
                                print("The discount you got  is = ","{:.2f}".format(discountmoney))
                                print()
                                print("\t****\t\t****")
                                print("\t|  |\t\t|  |")
                                print("\t|  |\t\t|  |")
                                print("\t|  |\t\t|  |")
                                print("\t****\t\t****")
                                print("\t\t{}")
                                print("\t      ______")
                            elif(flag==False and (decision=='y' or decision=='Y' )):
                                print("The increase you got  is = ","{:.2f}".format(increasemoney))
                                print()
                                print("\t****")
                                print("\t*  *")
                                print("\t*  *")
                                print("\t*  *")
                                print("\t****")
                            elif(decision=='n' or decision=='N'):
                                pass

                            """ Calculating the chance and printing the pattern likewise"""


                            response = requests.post("http://127.0.0.1:5000/addbill",
                                                json={
                                                    # 'orderid':orderid,
                                                    # 'itemno': itemno,
                                                    'username': username,
                                                    'discount_increase':chance_that_comes,
                                                    'tip':tip_percentage,
                                                    'finaltotal':total
                                                })
                            print(response.content)   
                                


                            
                            print("Do you want to place more orders or stop:..??")
                            print("1. To place more orders press..1")
                            print("2. To stop ordering press ...and get back to main menu press...2")
                            decide=int(input())
                            if(decide==1):
                                pass
                            else:
                                break


                    if inp == 3:





                        def my_fuc3():
                            '''Viewing the previous transactions.'''

                            return None

                        print("Using __doc__:")
                        print(my_fuc3.__doc__)

                        print("===================================================")
                        print()
                        # print("hello")
                        # print("username")
                        # username = input("Enter username:")
                        # password = input("Enter password:")
                        # dic = {"username": username, "password": password}
                        response = requests.post('http://localhost:5000/readbill',
                                                json={
                                                    'username': username,
                                                    
                                                })
                        # response = requests.get('http://localhost:5000/readbill')
                        # print(response.content)
                        # data = json.loads(response.content)

                        

                        # itemno=int(input("Enter the itemno: "))
                        # halfprice =int( input("Enter halfprice:"))
                        # fullprice= int(input("Enter fullprice:"))

                        # response = requests.get("http://127.0.0.1:5000/readbill",
                        #                         json={
                        #                             'itemno': itemno,
                        #                             'halfprice': halfprice,
                        #                             'fullprice':fullprice
                        #                         })
                        # print(response.content)
                        # print("Time to read")
                        response = requests.get('http://localhost:5000/readbill')
                        # print(response)
                        Response=response.content.decode()
                        # print(type(Response))
                        # print(Response)
                        # print(type(json.loads(Response)))
                        # print(response.content)
                        data = json.loads(Response)
                        # print(type(data))
                        # print(data)
                        print("The bills that have generated for your orders are: ")
                        # print(type((ast.literal_eval(response.content.decode('utf-8')))))
                        # for key,value
                        for k,v in data.items():
                            print("BILL NO: " + str(k))
                        print()
                        print("Please select the transaction/bill no you want to see......")
                        print()
                        bill_number=(input())
                        # for k,v in data[bill_number].items():
                        x=(data[bill_number])
                        # print(type(x))
                        order_details=x['orderdetails']
                        splitted_list = order_details.split("&")
                        # # for i in range(0,2):
                        # # l=[1,2,3,4,5,6]
                        print("The order details are as follows")
                        count=0

                        n=len(splitted_list)
                        n=int(n/3)
                        # print(n)
                        for i in range  (1,n+1):
                            # count+=1
                            # print(i)
                            x=splitted_list[count]
                            count+=1
                            y=splitted_list[count]
                            count+=1
                            z=splitted_list[count]
                            count+=1
                            print(str(x)+"  "+str(y)+"  "+str(z))
                        print("---------------------------------------------")
                        print("The price total for the order is: " +str((data[bill_number])['totalprice']))
                        print("---------------------------------------------")
                        print("The tip percentage for the order is: " +str((data[bill_number])['tip']))
                        print("---------------------------------------------")
                        print("The discount/increase/no inctrease for the order is: " +(data[bill_number])['discount_increase'])
                        print("---------------------------------------------")
                        print("The grand total  for the order is: " +str((data[bill_number])['finaltotal']))
                        # print(f"item {itemno} [{half_or_full}] [{v}]:","{:.2f}".format(tprice))


                        # print("itenmo"+'\t'+"halfprice"+'\t'+"fullprice")
                        # for key, value in data.items(): 
                        #     print(key, end='\t')
                        #     for k, v in value.items(): 
                        #         print(v, end='\t\t')
                        #     print()
                    if(inp==5):
                        break


            else:
                while True:
                    print("WELOCOME....You have logged in as the customer....")
                    print()
                    print("1. Read the menu")
                    print("2. Order food items and generate current bill")
                    # print("3. Generate bill")
                    print("3. View previous transactions")
                    print("4. Go back to the login/signup/signout page")
                    inp = int(input("Enter your choice please.....:"))
                    if inp == 1:
                        def my_fuccust():
                            '''Reading the menu.'''

                            return None

                        print("Using __doc__:")
                        print(my_fuccust.__doc__)

                        print("===================================================")
                        print()
                    
                        response = requests.get('http://localhost:5000/read')
                        # print(response.content)
                        data = json.loads(response.content)
                        print()
                        print("itenmo"+'\t'+"halfprice"+'\t'+"fullprice")
                        for key, value in data.items(): 
                            print(key, end='\t')
                            for k, v in value.items(): 
                                print(v, end='\t\t')
                            print()
                        print("===================================================")

                    if inp == 2:

                        def my_fuc2cust():
                            '''Ordering items and generating the bills.'''

                            return None

                        print("Using __doc__:")
                        print(my_fuc2cust.__doc__)

                        print("===================================================")
                        print()

                                    #while True:

                    #         print("Time for the order")
                    #         print()
                    #         number_of_items=int(input("Enter the no.of items: after which your bill will be generated..."))

                    #         """Taking the order"""


                    #         items=[]
                    #         keeptrack={}
                    #         total=0
                    #         for each in range(number_of_items):
                    #             list_for_one_item=[]
                    #             item_id=input("Enter the item id of  " + str(each+1) + " order: ")
                    #             list_for_one_item.append(item_id)
                    #             quantity=input("Enter half/full : ")
                    #             list_for_one_item.append(quantity)
                    #             st=str(item_id)+quantity
                                
                    #             no_of_plates=int(input("Enter the no.of plates(quantity) : "))
                    #             list_for_one_item.append(no_of_plates)
                    #             if st in keeptrack:
                    #                 keeptrack[st]+=no_of_plates
                    #             else:
                    #                 keeptrack[st]=no_of_plates
                    #             items.append(list_for_one_item)
                    #             print()
                    #             print()

                    #         print("The available choices for the tip percentage are as follows:")
                    #         print("Please choose one from them: ")
                    #         print()
                    #         print("0%  Enter 0 for it..")
                    #         print("10% Enter 10 for it..")
                    #         print("20% Enter 20 for it..")
                    #         print()
                    #         tip_percentage=int(input("Your tip percentage would be......"))
                    #         print()

                    #         response = requests.get('http://localhost:5000/read')
                    # # print(response.content)
                    #         data = json.loads(response.content)

                    #         print("hello")
                    #         for each in items:
                    #             if each[1]=="half":
                    #                 total+=int((data[int(each[0])])['halfprice'])*each[2]
                    #             elif each[1]=="full":
                    #                 total+=int((data[int(each[0])])['fullprice'])*each[2]
                    #         fprice=0
                    #         listing=[]   
                    #         print("hello")
                    #         for k,v in keeptrack.items():
                    #             list_for_one_item=[]
                    #             tprice=0
                    #             itemno=int(k[0])
                    #             list_for_one_item.append((k[0]))
                    #             half_or_full=k[1:]
                    #             list_for_one_item.append(half_or_full)
                    #             list_for_one_item.append(str(v))
                    #             if half_or_full=="half" :
                    #                 tprice+=int((data[int(each[0])])['halfprice'])*v
                    #                 half_or_full="Half"
                    #             else:
                    #                 tprice+=int((data[int(each[0])])['fullprice'])*v
                    #                 half_or_full="Full"
                    #             # print(f"item {itemno} [{half_or_full}] [{v}]:","{:.2f}".format(tprice))
                    #             listing.append(list_for_one_item)
                    #             fprice+=tprice
                    #         print("hello")
                    #         print("The listing value is" +listing)
                    #         response = requests.post("http://127.0.0.1:5000/orderitems",
                    #                         json={
                    #                             # 'orderid':orderid,
                    #                             # 'itemno': itemno,
                    #                             'username': username,
                    #                             'orderdetails':listing,
                    #                             'totalprice':fprice
                    #                         })
                    #         print(response.content)


                    #         print("Time for the bill generation....")


                    #         total=total+ total*(tip_percentage/100)
                    #         print("TIME TO TEST YOUR LUCK")
                    #         print("Do you want to test your luck : tpye y/Y  for yes and n/N for no ")
                    #         decision=input()
                    #         print()
                    #         print()
                    #         chance=["50%_discount","25%_discount","10%_discount","0_discount","20%_increase"]
                    #         prob=[.05,.1,.15,.2,.5]
                    #         chance_that_comes=""
                    #         flag=True
                    #         discountmoney=0
                    #         increasemoney=0
                    #         if(decision=='y' or decision=='Y'):
                    #             chance_that_comes=random.choices(chance,prob)
                                
                    #             if(chance_that_comes==['50%_discount']):
                    #                 print("Congratulations!  You got a 50%"+" discount")
                    #                 discountmoney=total*0.5
                    #                 total=total-total*0.5
                                    
                    #             elif(chance_that_comes==['25%_discount']):
                    #                 print("Congratulations!  You got a 25%"+" discount")
                    #                 discountmoney=total*0.25
                    #                 total=total-0.25*total
                                
                    #             elif(chance_that_comes==['10%_discount']):
                    #                 print("Congratulations!  You got a 10%"+" discount")
                    #                 discountmoney=total*0.1
                    #                 total=total-total*0.1

                    #             elif(chance_that_comes==['0_discount']):
                    #                 print("Sorry! No discount")
                    #                 # discountmoney=-total*0.1
                    #                 flag=False

                    #             else:
                    #                 print("Sorry! You have to pay extra")
                    #                 increasemoney=total*0.2
                    #                 total=total+0.2*total
                    #                 flag=False
                    #         else:
                    #             pass
                    #         print()
                    #         if(flag==True and (decision=='y' or decision=='Y' )):
                    #             print("The discount you got  is = ","{:.2f}".format(discountmoney))
                    #             print()
                    #             print("\t****\t\t****")
                    #             print("\t|  |\t\t|  |")
                    #             print("\t|  |\t\t|  |")
                    #             print("\t|  |\t\t|  |")
                    #             print("\t****\t\t****")
                    #             print("\t\t{}")
                    #             print("\t      ______")
                    #         elif(flag==False and (decision=='y' or decision=='Y' )):
                    #             print("The increase you got  is = ","{:.2f}".format(increasemoney))
                    #             print()
                    #             print("\t****")
                    #             print("\t*  *")
                    #             print("\t*  *")
                    #             print("\t*  *")
                    #             print("\t****")
                    #         elif(decision=='n' or decision=='N'):
                    #             pass

                    #         """ Calculating the chance and printing the pattern likewise"""


                    #         response = requests.post("http://127.0.0.1:5000/addbill",
                    #                             json={
                    #                                 # 'orderid':orderid,
                    #                                 # 'itemno': itemno,
                    #                                 'username': username,
                    #                                 'discount_increase':chance_that_comes,
                    #                                 'tip':tip_percentage,
                    #                                 'finaltotal':total
                    #                             })
                    #         print(response.content)   
                                


                            
                    #         print("Do you want to place more orders or stop:..??")
                    #         print("1. To place more orders press1..")
                    #         print("2. To stop ordering press 0...")
                    #         decide=int(input())
                    #         if(decide==0):
                    #             pass
                    #         else:
                    #             break
                    
                        while True:

                            print("Time for the order")
                            print()
                            number_of_items=int(input("Enter the no.of items: after which your bill will be generated..."))

                            """Taking the order"""


                            items=[]
                            keeptrack={}
                            total=0
                            for each in range(number_of_items):
                                list_for_one_item=[]
                                item_id=input("Enter the item id of  " + str(each+1) + " order: ")
                                list_for_one_item.append(item_id)
                                quantity=input("Enter half/full : ")
                                list_for_one_item.append(quantity)
                                st=str(item_id)+quantity
                                
                                no_of_plates=int(input("Enter the no.of plates(quantity) : "))
                                list_for_one_item.append(no_of_plates)
                                if st in keeptrack:
                                    keeptrack[st]+=no_of_plates
                                    keeptrack[st]=(no_of_plates)
                                    print(type(keeptrack[st]))
                                else:
                                    keeptrack[st]=no_of_plates
                                    keeptrack[st]=(no_of_plates)
                                    print(type(keeptrack[st]))
                                items.append(list_for_one_item)
                                print()
                                print()

                            print("The available choices for the tip percentage are as follows:")
                            print("Please choose one from them: ")
                            print()
                            print("0%  Enter 0 for it..")
                            print("10% Enter 10 for it..")
                            print("20% Enter 20 for it..")
                            print()
                            tip_percentage=int(input("Your tip percentage would be......"))
                            print()

                            response = requests.get('http://localhost:5000/read')
                    # print(response.content)
                            data = json.loads(response.content)

                            # print(data)
                            
                            
                            for each in items:
                                # print(each[0])
                                # print(data[(each[0])])
                                x=data[(each[0])]
                                # print(x['halfprice'])
                                if each[1]=="half":
                                    total+=int((data[(each[0])])['halfprice'])*int(each[2])
                                elif each[1]=="full":
                                    total+=int((data[(each[0])])['fullprice'])*int(each[2])
                                
                            fprice=0
                            listing=[]   
                            # print("hello")
                            for k,v in keeptrack.items():
                                list_for_one_item=[]
                                tprice=0
                                itemno=int(k[0])
                                list_for_one_item.append((k[0]))
                                half_or_full=k[1:]
                                list_for_one_item.append(half_or_full)
                                list_for_one_item.append(str(v))
                                if half_or_full=="half" :
                                    
                                    dict=data[str(itemno)]
                                    halfp=int(dict['halfprice'])
                                    # print(halfp)
                                    # print(type(halfp))
                                    tprice =tprice +  halfp*v
                                    half_or_full="Half"
                                else:
                                    # tprice+=int((data[str(itemno)])['fullprice'])*v
                                    dict=data[str(itemno)]
                                    fullp=int(dict['fullprice'])
                                    # print(fullp)
                                    # print(type(fullp))
                                    tprice =tprice +  fullp*v
                                    half_or_full="Full"
                                # print(f"item {itemno} [{half_or_full}] [{v}]:","{:.2f}".format(tprice))
                                listing.append(list_for_one_item)
                                fprice+=tprice
                            # print("hello")
                            # print("The listing value is" )
                            # print(listing)

                            response = requests.post("http://127.0.0.1:5000/orderitems",
                                            json={
                                                # 'orderid':orderid,
                                                # 'itemno': itemno,
                                                'username': username,
                                                'orderdetails':listing,
                                                'totalprice':total
                                            })
                            print(response.content)


                            print("Time for the bill generation....")


                            total=total+ total*(tip_percentage/100)
                            print("TIME TO TEST YOUR LUCK")
                            print("===================================================")
                            print()
                            print()
                            print("Do you want to test your luck : tpye y/Y  for yes and n/N for no ")
                            decision=input()
                            print()
                            print()
                            chance=["50%_discount","25%_discount","10%_discount","0_discount","20%_increase"]
                            prob=[.05,.1,.15,.2,.5]
                            chance_that_comes=""
                            flag=True
                            discountmoney=0
                            increasemoney=0
                            if(decision=='y' or decision=='Y'):
                                chance_that_comes=random.choices(chance,prob)
                                
                                if(chance_that_comes==['50%_discount']):
                                    print("Congratulations!  You got a 50%"+" discount")
                                    discountmoney=total*0.5
                                    total=total-total*0.5
                                    
                                elif(chance_that_comes==['25%_discount']):
                                    print("Congratulations!  You got a 25%"+" discount")
                                    discountmoney=total*0.25
                                    total=total-0.25*total
                                
                                elif(chance_that_comes==['10%_discount']):
                                    print("Congratulations!  You got a 10%"+" discount")
                                    discountmoney=total*0.1
                                    total=total-total*0.1

                                elif(chance_that_comes==['0_discount']):
                                    print("Sorry! No discount")
                                    # discountmoney=-total*0.1
                                    flag=False

                                else:
                                    print("Sorry! You have to pay extra")
                                    increasemoney=total*0.2
                                    total=total+0.2*total
                                    flag=False
                            else:
                                pass
                            print()
                            if(flag==True and (decision=='y' or decision=='Y' )):
                                print("The discount you got  is = ","{:.2f}".format(discountmoney))
                                print()
                                print("\t****\t\t****")
                                print("\t|  |\t\t|  |")
                                print("\t|  |\t\t|  |")
                                print("\t|  |\t\t|  |")
                                print("\t****\t\t****")
                                print("\t\t{}")
                                print("\t      ______")
                            elif(flag==False and (decision=='y' or decision=='Y' )):
                                print("The increase you got  is = ","{:.2f}".format(increasemoney))
                                print()
                                print("\t****")
                                print("\t*  *")
                                print("\t*  *")
                                print("\t*  *")
                                print("\t****")
                            elif(decision=='n' or decision=='N'):
                                pass

                            """ Calculating the chance and printing the pattern likewise"""


                            response = requests.post("http://127.0.0.1:5000/addbill",
                                                json={
                                                    # 'orderid':orderid,
                                                    # 'itemno': itemno,
                                                    'username': username,
                                                    'discount_increase':chance_that_comes,
                                                    'tip':tip_percentage,
                                                    'finaltotal':total
                                                })
                            print(response.content)   
                                


                            
                            print("Do you want to place more orders or stop:..??")
                            print("1. To place more orders press1..")
                            print("2. To stop ordering press 2...")
                            # print("===================================================")
                            print()
                            decide=int(input())
                            if(decide==1):
                                pass
                            else:
                                break

                    
                    if inp == 3:
                        def my_fuc3cust():
                            '''Viewing the previous transactions.'''

                            return None

                        print("Using __doc__:")
                        print(my_fuc3cust.__doc__)
                        print("===================================================")
                        print()
                        # print("hello")
                        # print("username")
                        # username = input("Enter username:")
                        # password = input("Enter password:")
                        # dic = {"username": username, "password": password}
                        response = requests.post('http://localhost:5000/readbill',
                                                json={
                                                    'username': username,
                                                    
                                                })
                        # response = requests.get('http://localhost:5000/readbill')
                        print(response.content)
                        # data = json.loads(response.content)

                        

                        # itemno=int(input("Enter the itemno: "))
                        # halfprice =int( input("Enter halfprice:"))
                        # fullprice= int(input("Enter fullprice:"))

                        # response = requests.get("http://127.0.0.1:5000/readbill",
                        #                         json={
                        #                             'itemno': itemno,
                        #                             'halfprice': halfprice,
                        #                             'fullprice':fullprice
                        #                         })
                        # print(response.content)
                        print("Time to read")
                        response = requests.get('http://localhost:5000/readbill')
                        # print(response)
                        Response=response.content.decode()
                        # print(type(Response))
                        # print(Response)
                        # print(type(json.loads(Response)))
                        # print(response.content)
                        data = json.loads(Response)
                        # print(type(data))
                        # print(data)
                        print("The bills that have generated for your orders are: ")
                        # print(type((ast.literal_eval(response.content.decode('utf-8')))))
                        # for key,value
                        for k,v in data.items():
                            print("BILL NO: " + str(k))
                        print()
                        print("Please select the transaction/bill no you want to see......")
                        bill_number=(input())
                        # for k,v in data[bill_number].items():
                        x=(data[bill_number])
                        # print(type(x))
                        order_details=x['orderdetails']
                        splitted_list = order_details.split("&")
                        # # for i in range(0,2):
                        # # l=[1,2,3,4,5,6]
                        print("The order details are as follows")
                        count=0

                        n=len(splitted_list)
                        n=int(n/3)
                        # print(n)
                        for i in range  (1,n+1):
                            # count+=1
                            # print(i)
                            x=splitted_list[count]
                            count+=1
                            y=splitted_list[count]
                            count+=1
                            z=splitted_list[count]
                            count+=1
                            print(str(x)+"  "+str(y)+"  "+str(z))
                        print("---------------------------------------------")
                        print("The price total for the order is: " +str((data[bill_number])['totalprice']))
                        print("---------------------------------------------")
                        print("The tip percentage for the order is: " +str((data[bill_number])['tip']))
                        print("---------------------------------------------")
                        print("The discount/increase/no inctrease for the order is: " +(data[bill_number])['discount_increase'])
                        print("---------------------------------------------")
                        print("The grand total  for the order is: " +str((data[bill_number])['finaltotal']))
                        # print(f"item {itemno} [{half_or_full}] [{v}]:","{:.2f}".format(tprice))


                    if(inp==4):
                        break

    elif(inp==3):
        # response = requests.post('http://localhost:5000/signout')
        if(username==""):
            print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
            print("Invalid operation")
            print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
        else:
            response = requests.post('http://localhost:5000/signout',
                                                    json={
                                                        'username': username,
                                                        
                                                    })
            print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
            print(response.content.decode())
            print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
    else:
        break

                        
                   
                   
    
