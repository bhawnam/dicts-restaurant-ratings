"""Restaurant rating lister."""

def restaurant_ratings_scores(filename):

    restaurant_data = open(filename)

    restaurant_dict = {}

    for line in restaurant_data:
        restaurant_name = line.rstrip().split(':')[0]
        rating = line.rstrip().split(':')[1]
        restaurant_dict[restaurant_name] = rating

    return restaurant_dict    


def print_ratings(scores_dict):

  for restaurant_name, rating in sorted(scores_dict.items()):
      print(f"{restaurant_name} is rated at {rating}")


def user_input(scores_dict):

    user_restaurant_name = input("Enter the restaurant name: ")
    user_rating = input("Enter the restaurant's rating: ")
    scores_dict[user_restaurant_name] = user_rating

    return scores_dict


scores_list = restaurant_ratings_scores("scores.txt")    

user_input(scores_list)

print_ratings(scores_list)