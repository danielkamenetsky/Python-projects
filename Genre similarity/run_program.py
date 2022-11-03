import user_interface
import main
import starter_code
import similarity 



if __name__ == '__main__':
    print("----------- EXECUTING THE PROGRAM -------------")
    subscribers = starter_code.subs_ratings()
    
    print("-----------Genre Recommendation -------------")
    user_interface.recommend_genre(subscribers, '')
    
    print("-----------Subscriber Match------------------")
    
    custname = input("Please enter a subscriber name: ")
    main.match_subscribers(subscribers, custname)
    print()
    print("-------- Subscriber Average Rating ----------")
    genre_avg = main.average_ratings(subscribers)
    main.table(genre_avg)
    print()
    print("--------Most Popular Genre ----------------")
    main.most_popular(subscribers)




