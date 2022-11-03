from random import *
from math import *

def subs_ratings():
    # Please insert your defined functions here
    
    
    
    # initialize subscribers list and music_genre list
    subscribers = [
    			'Justin Trudeau',
    			'Bob Jones',
    			'Sam Frizzel',
    			'Captain Nemo',
    			'Joe Jameson',
    			'Paul Casindes',
    			'Justin Bieber',
    			'Natlie Portman',
    			'Bugs Bunny',
    			'Peter Rabbit',
    			'Mickey Mouse',
    			'Martin Melchor',
    			'Nada Neel',
    			'Kristin Karlin',
    			'Edmond Earls',
    			'Fredrick Foxwell',
    			'Thomas Twitty',
    			'Julieann Jenning',
    			'Anton Autin',
    			'Alix Ashmore',
    			'Tiffany Turgeon',
    			'Noella Nash',
    			'Esther Edgerton',
    			'Sanda Sewart',
    			'Fannie Ferrera',
    			'Bernardine Block',
    			'Roger Rudd',
    			'Yang Wu',
    			'Raisa Rohr',
    			'Cirocco Jones',
    			'Mickie Milling',
    			'Ronald McDonald',
    			'Tim Horton',
    			'Colonel Sanders',
    			'Joel Jerry',
    			'Leanora Lion',
    			'Oscar Oliverio',
    			'Jernau Fortier'
    		]
    		
    music_genres = [
    			'Jazz',
    			'Country',
    			'Rap',
    			'Blues',
    			'Reggae',
    			'Soul',
    			'EDM',
    			'Hip Hop',
    			'World',
    			'Rock',
    			'Funk',
    			'Dance',
    			'Pop',
    			'Metal',
    			'Easy Listening',
    			'Hits',
    			'Opera',
    			'Classical',
    			]
    
    			
    # create nested dictionary
    subscriber_ratings = {}
    num_genres = len(music_genres)
    for p in subscribers:
    	subscriber_ratings[p] = {}
    	num_ratings = randint(num_genres/3,num_genres*2/3)
    	chosen_genres = sample(music_genres,num_ratings)
    	for f in chosen_genres:
    		subscriber_ratings[p][f] = randint(1,10)
    
    
    # add the rest of the main program here
    
    for c in subscriber_ratings:
     	print (c,subscriber_ratings[c])	
        
    return subscriber_ratings

subs_ratings()