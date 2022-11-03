#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
"""
import filehandler
"""
This function displays all the vehicle information in the database to the console or writes it into a textfile depending on what the user has entered for the parameter
"""
def display_vehicle(display_option):
    database = filehandler.readvehicle_info()

    #if selection is 1, function displays information on console
    if display_option == '1':
        for i in database:
            print(str(i))
            
    #if selection is 2, function writes in database to a textfile of user's choosing       
    elif display_option == '2':
        file_name = input("What would you like to call the file? \n")
        out_file = open(file_name, "w")
        for i in database:
            out_file.write(str(i)+"\n")
    
    elif display_option =='exit':
        print("you've exited the program.")

    else:
        print("invalid input, try again!\n")
    
        

'''
This function takes in a make, type or availability filter, and outputs the vehicle information for all vehicles of that respective filter
'''
def filter_vehicle(filter, vehicle_input):
    database = filehandler.readvehicle_info()

    if filter == '1':
        for i in database:
            
            if vehicle_input.lower() == str(i['make']).lower():
                print(i)

    elif filter == '2':
        for i in database:
            if vehicle_input.lower() == str(i['type']).lower():
                print(i)

    elif filter == '3':
        for i in database:
            if vehicle_input.lower() == str(i['availability']).lower():
                print(i)
                
    elif filter =='exit':
        print("you've exited the program.")

    else:
        print("invalid input, try again!")



    
    
def list_id(vehicle_make):
    database = filehandler.readvehicle_info()
    # vehicle_make = input("Please enter the vehicle make.")
    unique_list = []
    results_found = False
    for i in database:
        if vehicle_make.lower() == str(i['make']).lower():
            unique_list.append(i['vehicle ID'])
            results_found = True

    print("List of vehicle id's for the make " + vehicle_make + " is: ")
    print(unique_list)
    
    
    if results_found == False:
        print("no results found for this entry")
    
    return vehicle_make

def vehicle_keywordsearch(keyword):
    database = filehandler.readvehicle_info()
    # keyword = input("Please enter any keyword.")
    results_found = False
    for i in database:
        if keyword.lower() in str(i).lower():
            print(i)
            results_found = True
    if results_found == False:
        print("no results found for this entry")
    
    return keyword

def check_id():
    database = filehandler.readvehicle_info()
    while True:
        vehicle_id = input("please enter a numerical vehicle ID number: ")
        if vehicle_id.isnumeric() == True:
            for car in database:
                while vehicle_id == str(car['vehicle ID']):
                     print("Not Unique ID")
                     vehicle_id = input("please enter a unique vehicle ID number:")
                     if vehicle_id != str(car['vehicle ID']):
                         break
        break

    return vehicle_id

def unique_id():
        database = filehandler.readvehicle_info()
        while True:
            vehicle_id = input("please enter a numerical vehicle ID number: ")
            if vehicle_id.isnumeric() == True:
                for car in database:
                    
                    if vehicle_id == str(car['vehicle ID']):
                        print("id valid")
                    
                
                    elif vehicle_id != str(car['vehicle ID']):
                        vehicle_id = input("please enter a valid vehicle ID number:")
                    break
            break
        return vehicle_id



def vehicle_update():
    database = filehandler.readvehicle_info()
    vehicle_id = unique_id()

    action = input("Please enter the number corresponding to the action you want to perform: \n1. update odometer reading \n2. update cost of renting \n3. update availability \n4. remove vehicle from system?")

    if action == "1":
        for i in database:
            if vehicle_id == str(i['vehicle ID']):
                print(i)
                edit_dict = i
                for c in edit_dict:
                    if c == 'odometer rating':
                        new_rating = input("what is the new odometer rating")
                        edit_dict['odometer rating'] = new_rating
                        print("the odometer rating for vehicle ID# " + vehicle_id + " is: " + str(new_rating))
                        print(edit_dict)

    elif action == "4":
        for i in range(len(database)):
            if vehicle_id == str(database[i]['vehicle ID']):
                del database[i]
                break
        print(database)




def add_vehicle():
    database = display_vehicle()

    vehicle_id = check_id()

    vehicle_make = input("please enter the vehicle make: ")
    vehicle_type = input("please enter the vehicle type: ")

    while True:
        vehicle_odometer = input("please enter the odometer reading: ")
        if vehicle_odometer.isnumeric() == True:
            break

    while True:
        vehicle_rent = input("please enter the cost to rent/day: ")
        if vehicle_rent.isnumeric() == True:
            break

    while True:
        vehicle_used = input("please enter the number of times the vehicle has been rented out: ")
        if vehicle_used.isnumeric() == True:
            break
    vehicle_availability = input("please enter whether the vehicle is 'AVAILABLE' or 'RESERVED'': ")

    vehicle_info = {}


    vehicle_info['vehicle ID'] = int(vehicle_id)
    vehicle_info['make'] = str(vehicle_make)
    vehicle_info['type'] = str(vehicle_type)
    vehicle_info['odometer rating'] = int(vehicle_odometer)
    vehicle_info['cost to rent per day'] = int(vehicle_rent)
    vehicle_info['number of times vehicle has been rented'] = int(vehicle_used)
    vehicle_info['availability'] = 'AVAILABLE'

    database.append(vehicle_info)


        
if __name__ == "__main__":
    # print("Testing the display vehicle function")
    
    
    # while True:

    #     print(display_vehicle("1"), "Should return the database onto the console") 
    #     print(display_vehicle("2"), "Should return the database onto a textfile given name from user")
    #     print(display_vehicle("32"), "Should return 'invalid input, try again!' and then ask user for another input")
    #     print(display_vehicle("exit"), "Should print you've exited the program.")
    #     break
        
    # print()
    
    # print("Testing filter_vehicle function")
    
    # #creating a list of lists to test the functionality of each filter
    # test_data = [["1", "gmc", "make: gmc"],["2", "escape", "type: escape"],["3", "available", "availability: available"]]
    
   
    # for i in range(len(test_data)):
    #     filter = input("Please enter the number of the filter the vehicle information by:  \n1. Make  \n2. Type \n3. Availability \n")
    #     vehicle_input = input("Please enter information of selected filter \n")
        
    #     #printing the 1st, 2nd and 3rd element of the i'th element of the list test_data 
    #     print(filter_vehicle(test_data[i][0],test_data[i][1]), "should return vehicle information for " + test_data[i][2])
    
    # print(display_vehicle("exit"), "Should print:  you've exited the program.")
    # print(display_vehicle("123"), "Should print: invalid input, try again!")
    
    # print()
    # print(" Testing the list_id function ")
    
        
    # print(list_id("ford"), "should print out all the ID's for the ford  make: [23453, 31221]")
    # print(list_id("space x"), "should print out: no results found for this entry.")
    # print()
    
    # print("Testing vehicle_keywordsearch function")
    # print(vehicle_keywordsearch("gmc"), "should print out all vehicle info for GMC's")
    # print(vehicle_keywordsearch("yellow submarine"), "should print out no results found")
    # print()
    
    # print("Testing check id function")
    # print(check_id(), "Entering 31221 should print out: Not Unique ID)
    # print(check_id(), "Entering 11111 should print out '11111' as this is a unique ID)
    # print()
    
    print("Testing unique_id function")
    print(unique_id(), "Entering 11111 should print out: please enter a valid vehicle ID number")
    print(unique_id(), "Entering 31221 should print out '31221' as this is a valid vehicle ID number")
    print()


              
              