


class Business:
    # Describe the NAME and CUISINE TYPE of a restaurant
    def __init__(self, business_type, name):
        # Initialize attributes to describe Restaurant
        self.business_type = business_type
        self.name = name
        

    def describe_business(self):
        # Describes restaurant NAME and CUISINE
        print(f"This is a {self.business_type} named {self.name}!")


Restaurant = Business('Restaurant', 'Big Italy')
# restaurant class calls the method in Business class
Restaurant.describe_business()

# Makes new class and inherits to parent Business class
class Restaurant(Business):
    cuisine_type = 'Italian'
    hours_open = '9 AM - 10 PM'
    print(f"This business serves {cuisine_type} food, and is open from {hours_open}!")


# makes a space in the output
print()



Movie_Theater = Business('Movie Theater', 'Red Carpet Entertainment')
# Movie_Theater class calls the method in Business class
Movie_Theater.describe_business()

# Makes new class and inherits to parent Business class
class Movie_Theater(Business):
    locations = 'Redmond, Woodinville, Bothell, and Bellevue'
    type_of_movies = 'all the major Blockbuster hits!'
    print(f"This movie theater has locations in {locations}, and is known for playing {type_of_movies}!")
