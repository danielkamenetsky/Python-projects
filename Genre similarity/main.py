#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

"""


import similarity

'''
This function takes in a dictionary of subscribers as well as a subscriber name as its parameters.
Following this, the function calls the similarity module and function similarity_val and calculates
the similarity value between the custname parameter and every other subscriber in the list.
The function returns the name of the subscriber with the highest similarity value
'''
def match_subscribers(subscribers, custname):
    dict_simvals = {}
    for i in subscribers:
        
        #calling similarity_val function as long as subscriber is not that one that was entered
        if i != custname:
            dict_simvals[i] = similarity.similarity_val(subscribers, custname, i)
    
    
    #determining the key with the highest similarity value
    max_sim = max(dict_simvals, key=dict_simvals.get)
            
    print("The subscriber with the highest similarity value to ", custname, "is: ", max_sim)
    return max_sim

'''
This function takes in the genre_avg dictionary and formats it into a table
'''

def table(genre_avg):
    print ("{:<8} {:<15}".format('GENRE','AVERAGE RATING'))
    for i,j in genre_avg.items():
        print ("{:<13} {:<20}".format(i, j))
    print()
    return genre_avg

'''
This function takes in a dictionary of subscribers, and creates three empty dictionaries to store the sum of genre ratings, 
the number of times a genre has been rated, and the average rating for each genre. It iterates through the subscribers
and then determines the average rating for each genre based on the ratings made by the subscribers. Finally, it displays
a table of the average ratings for each genre. 
'''
def average_ratings(subscribers):
    genre_rating = {}
    genre_count = {}
    genre_avg = {}
                
    
    #iterating over the dictionary of subscribers, and iterating over the genres rated by each subscriber.
    for subscriber in subscribers:
        for genre in subscribers[subscriber]:
            
            #if the genre is not in the dictionary add the genre as the key and the rating as its value to the dictionary,
            #store the number of times the genre has been rated to 1 in genre_count , and store average in genre_avg.
            if genre not in genre_rating:
                genre_rating[genre] = subscribers[subscriber][genre]
                genre_count[genre] = 1  
                genre_avg[genre] = genre_rating[genre]/genre_count[genre]
                
            #if the genre is in the dictionary, add the rating value to the existing rating value of that genre
            #increment the number of times the genre has been rated by 1 in genre_count , and calculate average in genre_avg.
            else:
                genre_rating[genre] += subscribers[subscriber][genre]
                genre_count[genre] += 1
                genre_avg[genre] = genre_rating[genre]/genre_count[genre]
                
    return genre_avg
    



'''
This function calls the average_ratings function stores it in a variable, and then prints out the name of the genre
with the highest average rating.
'''
def most_popular(subscribers):

    genre_rating = average_ratings(subscribers)

    print(max(genre_rating, key=genre_rating.get))   
    
    return genre_rating





if __name__ == "__main__":

    print("----------Testing match_subscriber function-------------------")
    print()
    
    #The line below may be replaced with subscribers = starter_code.subs_ratings() to see functionality on entire dictionary
    subscribers = {"Justin Trudeau": {'Hip Hop': 5, 'Rap': 3, 'Classical': 2, 'Dance': 7, 'EDM': 9, 'Jazz': 7},
    "Bob Jones": {'Soul': 4, 'Country': 4, 'Reggae': 6, 'Opera': 9, 'EDM': 8, 'Hits': 10, 'Hip Hop': 7, 'Blues': 1, 'Metal': 2, 'Jazz': 3, 'Pop': 6},
    "Sam Frizzel": {'Country': 7, 'Opera': 5, 'Rap': 2, 'Hits': 3, 'Rock': 4, 'Soul': 6}}
    custname = "Justin Trudeau"
    match_subscribers(subscribers, custname)
    print("Should print out: Bob Jones")
    print()
    
    print("----------Testing average_ratings function-------------------")
    print()
    subscribers = {"Justin Trudeau": {'Hip Hop': 5, 'Rap': 3, 'Classical': 2, 'Dance': 7, 'EDM': 9, 'Jazz': 7},
    "Bob Jones": {'Soul': 4, 'Country': 4, 'Reggae': 6, 'Opera': 9, 'EDM': 8, 'Hits': 10, 'Hip Hop': 7, 'Blues': 1, 'Metal': 2, 'Jazz': 3, 'Pop': 6, 'Rap': 4},
    "Sam Frizzel": {'Country': 7, 'Opera': 5, 'Rap': 2, 'Hits': 3, 'Rock': 4, 'Soul': 6}}
    genre_avg = average_ratings(subscribers)
    table(genre_avg)
    
    print('''Should return a table with Genre and Average Ratings:\n
    GENRE    AVERAGE RATING 
    Hip Hop       6.0                 
    Rap           3.0                 
    Classical     2.0                 
    Dance         7.0                 
    EDM           8.5                 
    Jazz          5.0                 
    Soul          5.0                 
    Country       5.5                 
    Reggae        6.0                 
    Opera         7.0                 
    Hits          6.5                 
    Blues         1.0                 
    Metal         2.0                 
    Pop           6.0                 
    Rock          4.0
    ''')
    print()
    
    print("----------Testing most_popular function-------------------")
    print()
    subscribers = {"Justin Trudeau": {'Hip Hop': 5, 'Rap': 3, 'Classical': 2, 'Dance': 7, 'EDM': 9, 'Jazz': 7},
    "Bob Jones": {'Soul': 4, 'Country': 4, 'Reggae': 6, 'Opera': 9, 'EDM': 8, 'Hits': 10, 'Hip Hop': 7, 'Blues': 1, 'Metal': 2, 'Jazz': 3, 'Pop': 6, 'Rap': 4},
    "Sam Frizzel": {'Country': 7, 'Opera': 5, 'Rap': 2, 'Hits': 3, 'Rock': 4, 'Soul': 6}}
    most_popular(subscribers)
    print("Function should return EDM")
    print()
    


