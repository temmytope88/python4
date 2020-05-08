import random
import os
print("welcome to the banking system")
options = input ("Do you want to login? Enter Yes or No>>> ")
if options.upper() == "NO":
    print("Thanks for you time")
else:
    print("Enter you username and password")
    username = input("Username: ")
    password = input("Password: ")

    content = open("staff.txt", "r")
    for line in content:
        contentdetails = line.split()
        if username == contentdetails[0] and password == contentdetails[2]:
            content.close()
            options = input ("""if you want to create or check account enter 'A' 
            if you want logout enter 'B'""")
            if options.upper() == "A":
                status = True
                while status:
                    accountOptions= input("""if you want to create account enter 'A', 
                    if you want to check account details enter 'b'""")
                    if accountOptions.upper() == "A":
                        print("Enter the account details")
                        accountEmail = input("AccountEmail: ")
                        accountName = input("AccountName: ")
                        accountType = input("AccountType: ")
                        openingBalance = input("Opening: ")
                        accountGeneration = random.randint(1234506789, 9876543210)
                        accountNumber = str(accountGeneration)

                        account = open("customer.txt", "a")
                        account.write(accountEmail+ " "+accountName +" " +accountType+" " +accountNumber+" " +accountName+"\n")
                        account.close()
                    else:
                        customerAccountNum = input("Account Number: ")
                        customer = open("customer.txt", "r")
                        for row in customer:

                            customerDetails = row.split()
                            if customerDetails[3] == customerAccountNum:
                                print(customerDetails)

                    user = input("Would you like to continue? enter yes or no ")
                    if user.upper() == "NO":
                        status = False
                        print("successfully logged out")
                    else:
                        status = True
            else:
                print("you have successfully logged out")
            break
    else:
        print("session terminated due to invalid details")













