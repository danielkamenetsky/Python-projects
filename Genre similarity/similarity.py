#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
"""


'''
This function takes in the subscribers dictionary, and two subscribers, and calculates the sum
of ratings for each subscriber
'''
def rating_sums(d,sub1,sub2):
    sub1_list = []
    sub2_list = []
    sub1_sum = 0
    sub2_sum = 0
    #iterating key (name of subscriber),value (dictionary for that subscriber) in the dictionary
    for subscriber, ratings in d.items():
        #iterating genre(key) and score (value) in the nested dictionary
        for genre, score in ratings.items():
            #if the subscriber being iterated on matches our parameter, we append their scores to a list and calculate the sum
            if subscriber == sub1:
                sub1_list.append(score)
                sub1_sum = sum(sub1_list)
        
            elif subscriber == sub2:
                sub2_list.append(score)
                sub2_sum = sum(sub2_list)
                
                
    
    return sub1_sum, sub2_sum

"""
This function takes in the subscribers dictionary, and two subscribers, calls the subs_sums function in pass
in the sum values calculated for each of the two subscribers. The function calculates the similarity value by
iterating over the dictionaries of these subscribers, calculates each intersection sum and divides each by their 
respective rating sum.
"""
def similarity_val(d,sub1, sub2):
    a = rating_sums(d, sub1, sub2)
    sub1_sum = a[0]
    sub2_sum = a[1]
    
    inter_list = []
    for key in d[sub1].keys():
        if key in d[sub2]:
            # print(key)
            minval = min((d[sub1][key]),(d[sub2][key]))
            # print(minval)
            inter_list.append(minval)
            # print(d[sub1][key])
            # print(d[sub2][key])
    inter_sum = sum(inter_list)
            

    val1 = inter_sum/sub1_sum
    val2 = inter_sum/sub2_sum

    similarity = round(min(val1,val2),2)

    return similarity



if __name__ == "__main__":

    print("-----------------------------")
    subscribers = {"Justin Trudeau": {'Hip Hop': 5, 'Rap': 3, 'Classical': 2, 'Dance': 7, 'EDM': 9, 'Jazz': 7},
    "Bob Jones": {'Soul': 4, 'Country': 4, 'Reggae': 6, 'Opera': 9, 'EDM': 8, 'Hits': 10, 'Hip Hop': 7, 'Blues': 1, 'Metal': 2, 'Jazz': 3, 'Pop': 6},
    "Sam Frizzel": {'Country': 7, 'Opera': 5, 'Rap': 2, 'Hits': 3, 'Rock': 4, 'Soul': 6}}
    subs_1 = "Justin Trudeau"
    subs_2 = "Sam Frizzel"
    print()
    print("The sum for: ", subs_1, "and", subs_2, " is ", rating_sums(subscribers, subs_1, subs_2), " respectively\n", "Should return the sums as (33, 27)\n",)
    print("The similarity value for: ", subs_1, "and", subs_2, " is ", similarity_val(subscribers, subs_1, subs_2),"\nShould return a similarity value of: 0.06")

