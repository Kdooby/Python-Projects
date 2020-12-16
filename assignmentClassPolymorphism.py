


class Business:
    # Describe the NAME and CUISINE TYPE of a restaurant
    business_type = "unknown"
    name = "unknown"
        
    def intro(self):
        msg = "There are numerous types of businesses out there!\n"
        return msg


    def describe_business(self):
        # Describes restaurant NAME and TYPE
        msg = f"This is a {self.business_type} named {self.name}!"
        return msg

    def type_hours_locations(self):
        msg = "The hours and locations for each business will vary, depending on the type of business it is."
        return msg
    
    




# Makes new class and inherits to parent Business class
class Restaurant(Business):
    business_type = 'Restaurant'
    name = 'Big Italy'
    cuisine_type = 'Italian'
    hours_open = '9 AM - 10 PM'

    def type_hours_locations(self):
        msg = f"This business serves {self.cuisine_type} food, and is open from {self.hours_open}!\n"
        return msg



# Makes new class and inherits to parent Business class
class Movie_Theater(Business):
    business_type = 'Movie Theater'
    name = 'Red Carpet Entertainment'
    locations = 'Redmond, Woodinville, Bothell, and Bellevue'
    type_of_movies = 'all the major Blockbuster hits!'

    def type_hours_locations(self):
        msg = f"This movie theater has locations in {self.locations}, and is known for playing {self.type_of_movies}!"
        return msg


if __name__ == "__main__":

    business = Business()
    print(business.intro())
    
    restaurant = Restaurant()
    print(restaurant.describe_business())
    print(restaurant.type_hours_locations())

    movie_theater = Movie_Theater()
    print(movie_theater.describe_business())
    print(movie_theater.type_hours_locations())
