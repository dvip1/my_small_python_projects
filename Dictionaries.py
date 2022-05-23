#I made this project using Dictionaries, just wanted to use it somewhere 
def shopping():
  shopping_list= []
  cost=0
  a= input("Hello Traveler! Would you like to play this game?(yes/no) ")
  while True:
    if a=="yes":
        print("Less goo...!\n")
    elif a=="no":
        print("It was nice to have you here!")
        break
    print("*****Welcome to our fruit shop!***** \n*****We got the best fruits of 'em all*****\n\n")
    fruits_prices= {"Snake_fruit(1)":3500, "Cranberry(2)": 700, "Pomegranate(3)": 40, "Banana(4)": 12, "Mango(5)": 80, "apple(6)": 180}
    for i in fruits_prices:
        print(i)
    a=input("What would you like to order?, \nNote: Please enter the name as specified above, or number associated with it!\n")
    if a=="Snake_fruit" or a=="1":
        print("Snake fruit is selling for {} rupees per packet".format(fruits_prices["Snake_fruit(1)"])) 
        buy=input("Would you like to buy it? (yes/no): ")
        if buy=="yes": 
            print("It is added into cart! ")
            shopping_list.append("Snake fruit")
            cost+=fruits_prices["Snake_fruit(1)"]
    if a=="Cranberry" or a=="2":
        print("Cranberry is selling for {} rupees per kg".format(fruits_prices["Cranberry(2)"]))
        buy=input("Would you like to buy it? (yes/no): ")
        if buy=="yes": 
            print("It is added into cart! ")
            shopping_list.append("Cranberry")
            cost+=fruits_prices["Cranberry(2)"]
    if a=="Pomegranate" or a=="3":
        print("Pomegranate is selling for {} rupees per kg".format(fruits_prices["Pomegranate(3)"]))
        buy=input("Would you like to buy it? (yes/no): ")
        if buy=="yes": 
            print("It is added into cart! ")
            shopping_list.append("Pomegranate")
            cost+=fruits_prices["Pomegranate(3)"]
    if a=="Banana" or a=="4":
        print("Banana is selling for {} rupees per kg".format(fruits_prices["Banana(4)"]))
        buy=input("Would you like to buy it? (yes/no): ")
        if buy=="yes": 
            print("It is added into cart! ")
            shopping_list.append("Banana")
            cost+=fruits_prices["Banana(4)"]
    if a=="Mango" or a=="5":
        print("Mango is selling for {} rupees per kg".format(fruits_prices["Mango(5)"]))
        buy=input("Would you like to buy it? (yes/no): ")
        if buy=="yes": 
            print("It is added into cart! ")
            shopping_list.append("Mango")
            cost+=fruits_prices["Mango(5)"]
    if a=="apple" or a==6:
        print("Apple is selling for {} rupees per kg".format(fruits_prices["apple(5)"]))
        buy=input("Would you like to buy it? (yes/no): ")
        if buy=="yes": 
            print("It is added into cart! ")
            shopping_list.append("apple")
            cost+=fruits_prices["apple(6)"]
    print("You have purchased ", end="")
    for i in shopping_list:
        print(i)
    ab= input("Would you like to buy something else (yes/no): ")
    if ab=="no":
        print("your total cost is {} rupees".format(cost))
        print("Thanks for shopping!\nPlease come back again!")
        break           
        
shopping()
    
                 
