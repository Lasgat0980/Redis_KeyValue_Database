# Name: Lastazia Dickens
# Date: November 14, 2026
# Assignment: PA Python Application Accessing a Key-Value Database
# Objective: Create a Python application that allows users to
# perform CRUD operations on a Redis key-value database.

import redis

#Notify when script is starting
print("Connecting to local Redis database...")

r = redis.StrictRedis(host='127.0.0.1', port=6379, db=1)

#Repeat the menu until the user exits
while True:
    #Display the menu options
    print("Type in a number and press enter to execute the menu option.")
    print("1. Query for set members")
    print("2. Add a new set")
    print("3. Update members of a set")
    print("4. Delete a set")
    print("5. Delete all data from the database")
    print("6. Exit the program")

    #Accept the user's menu selection
    choice = input()

    #Retrieve the members of a specific set
    if choice == "1":
        key = input("Enter the key of the set you wish to query: ")
        print("The member values of the set are:")
        print(r.smembers(key))

    #Add a new set to the database
    elif choice == "2":
        key = input("\nEnter the key you wish to add:\n")
        count = int(input("\nEnter how many members will this set have:\n"))

        for i in range(count):
            member = input("\nEnter the next member value:\n")
            r.sadd(key, member)

    
    #Update the members of a set
    elif choice == "3":
        key = input("\nEnter the key of the set you wish to update:\n")

        #Display the update menu
        print("\nPlease type in a number and press enter to execute the menu option")
        print("1. Add new member")
        print("2. Remove member")
        print("3. Remove all members")
        print("4. Exit Update Menu")

        update_choice = input()

        if update_choice == "1":
            member = input("\nEnter the new member value:\n")
            r.sadd(key, member)

        elif update_choice == "2":
            member = input("\nEnter the member value to remove:\n")
            r.srem(key, member)

        elif update_choice == "3":
            print("\nRemoving all set members...")
            while(r.scard(key) > 0):
                print("Removing Member: {}...".format(r.spop(key)))

            print("\nThe cardinality of the set is now:")
            print(r.scard(key))
    #Delete a set from the database
    elif choice == "4":
        key = input("Enter the key of the set you wish to delete: ")
        r.delete(key)
        print("Set removed.")

    #Delete all sets from the database
    elif choice == "5":
        print("\nRemoving all sets from the database...")
        r.flushdb()
        print("All sets removed.")

    #Display end of program message
    elif choice == "6":
        print("\n\nProgram has ended!")
        break
