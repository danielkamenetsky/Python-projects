#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
"""
import similarity
'''
This function takes in a dictionary of subscribers and prompts the user for a subscriber name. 
It then checks if the name is valid, and if it is then it finds the subscriber with the highest
similarity value, and then outputs the genre that the subscriber rated highest which was not
rated by the subscriber entered by the user. 
'''
def recommend_genre(subscribers, name_sub):
    name_sub = input("Please enter the name of the subscriber for which you would like us to recommend a genre to: ")
    dict_simvals = {}
    not_rated = {}
    
        
    for i in subscribers:
        
        #while subscriber entry does not exist, prompting user for a new entry
        while name_sub not in subscribers:
            name_sub = input("That customer does not exist, please try again: ")
        
        #as long as i is not the subscriber entry, store similarity values of all other subscribers
        if i != name_sub:
            dict_simvals[i] = similarity.similarity_val(subscribers, name_sub, i)
        
    
    max_sim = max(dict_simvals, key=dict_simvals.get)
    
    #storing the highest rated genre that wasn't rated by the given subscriber
    for i in subscribers[max_sim]:
        if i not in subscribers[name_sub]:
            not_rated[i] = subscribers[max_sim][i]
            

    genre = max(not_rated, key=not_rated.get)
    print("Since the subscriber most similar to", name_sub, "is ", max_sim, ",")
    print(name_sub, "should listen to ", genre, " as ", name_sub, " has not rated ", genre, 
          "and it is the genre that", max_sim, " has rated the highest that ", name_sub, " has not rated") 
    print()


if __name__ == "__main__":
    print("----------Testing recommend_genre function-------------------")
    subscribers = {"Justin Trudeau": {'Hip Hop': 5, 'Rap': 3, 'Classical': 2, 'Dance': 7, 'EDM': 9, 'Jazz': 7},
    "Bob Jones": {'Soul': 4, 'Country': 4, 'Reggae': 6, 'Opera': 9, 'EDM': 8, 'Hits': 10, 'Hip Hop': 7, 'Blues': 1, 'Metal': 2, 'Jazz': 3, 'Pop': 6, 'Rap': 4},
    "Sam Frizzel": {'Country': 7, 'Opera': 5, 'Rap': 2, 'Hits': 3, 'Rock': 4, 'Soul': 6}}
    recommend_genre(subscribers, "Justin Trudeau")
    print("When user enters Justin Trudeau, the function should return:\
          \n\
          \nSince the subscriber most similar to Justin Trudeau is  Bob Jones,\
          \nJustin Trudeau should listen to  Hits  as  Justin Trudeau  has not\
          \nrated Hits and it is the genre that Bob Jones  has rated the highest\
          \nthat Justin Trudeau has not rated")
    print()
