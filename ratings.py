"""Restaurant rating lister."""

def restaurant_ratings_scores(filename):
    """ Read a file, store the contents in a dictionary and return the dictionary."""
    
    restaurant_data = open(filename)
    restaurant_dict = {}
 
    for line in restaurant_data:
        restaurant_name = line.rstrip().split(':')[0]
        rating = line.rstrip().split(':')[1]
        restaurant_dict[restaurant_name] = int(rating)

    return restaurant_dict    


def print_ratings(scores_dict):
    """ Print the contents of the dictionary in a sorted order."""

    for restaurant_name, rating in sorted(scores_dict.items()):
      print(f"{restaurant_name} is rated at {rating}")


def user_input(scores_dict):
    """ Add a user entered resturant name and rating to the exixting dictionary """

    user_restaurant_name = input("Enter the restaurant name: ")
    user_rating = int(input("Enter the restaurant's rating: "))
    scores_dict[user_restaurant_name] = user_rating

    return scores_dict


scores_list = restaurant_ratings_scores("scores.txt")    

user_input(scores_list)

print_ratings(scores_list)