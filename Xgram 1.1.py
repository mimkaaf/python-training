# Create a compound data structure that stores all data from version 1.0
user_data = {
    "Alice": {
        "posts": ["Got my ticket!", "On my way to DC!", "Wow! I'm finally in DC!", "Great music @ Kennedy Center!"],
        "images": ["https://bit.ly/2EhtSpO", "https://bit.ly/34p23GB"]
    },
    "Bob": {
        "posts": ["Great time at python class!", "I just learned about lists!"],
        "images": ["https://bit.ly/31kUEWR"]
    }
}
# Use tuples to pack image urls with the relavent posts
# For posts that don't have an image, set the url to empty string
user_data = {
    "Alice": {
        "posts": [("Got my ticket!", ""), ("On my way to DC!", "https://bit.ly/2EhtSpO"), 
                  ("Wow! I'm finally in DC!", "https://bit.ly/34p23GB"), ("Great music @ Kennedy Center!", "")],
    },
    "Bob": {
        "posts": [("Great time at python class!", "https://bit.ly/31kUEWR"), ("I just learned about lists!", "")],
    }
}
# Read the name of the user from the input function and print the last post including the url (if available)
user_name = input("Enter your name: ")
user_posts = user_data.get(user_name)
posts = user_posts["posts"]
print(f"{user_name}'s last two posts are: ", posts[-2][0], posts[-1][0])