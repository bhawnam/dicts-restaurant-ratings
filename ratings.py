"""Restaurant rating lister."""

def restaurant_ratings_list(filename):

    restaurant_data = open(filename)

    restaurant_dict = {}

    for line in restaurant_data:
        restaurant_name = line.rstrip().split(':')[0]
        rating = line.rstrip().split(':')[1]
        restaurant_dict[restaurant_name] = rating

    return restaurant_dict    


def ordered_ratings(rated_dict):

  for restaurant_name, rating in sorted(rated_dict.items()):
      print(f"{restaurant_name} is rated at {rating}")


def user_input(original_dict):

    user_restaurant_name = input("Enter the restaurant name: ")
    user_rating = input("Enter the restaurant's rating: ")
    original_dict[user_restaurant_name] = user_rating

    return original_dict

scores_list = restaurant_ratings_list("scores.txt")    

user_input(scores_list)

ordered_ratings(scores_list)