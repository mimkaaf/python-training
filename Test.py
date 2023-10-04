# Define the lists
users = ["Alice", "Bob"]
postsAlice = ["Wow! I'm finally in DC! Great music @ AKK", "Got my ticket!", "On my way to DC!"]
postsBob = ["Great time at python class!", "I just learned about lists!"]
imgsAlice = ["https://bit.ly/2EhtSpO", "https://bit.ly/34p23GB", ""]
imgsBob = ["https://bit.ly/31kUEWR", ""]

# Create a dictionary to store user data
data = {}

# Populate the dictionary with user data
for user, posts, images in zip(users, [postsAlice, postsBob], [imgsAlice, imgsBob]):
    user_data = [{"post": post, "image_url": img} for post, img in zip(posts, images)]
    data[user] = user_data

# Read the name of the user from the input function
user_name = input("Enter the user's name: ")

# Get the user's data from the dictionary
user_data = data.get(user_name, [])

# Find the last post with URL (if available)
last_post = next((d for d in reversed(user_data) if d["image_url"]), None)

# Print the last post with or without URL
if last_post:
    print(f"Last post by {user_name}: {last_post['post']}, URL: {last_post['image_url']}" if last_post['image_url'] else f"Last post by {user_name}: {last_post['post']} (No URL available)")
else:
    print(f"User '{user_name}' not found in the data.")
