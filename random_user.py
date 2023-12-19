


import json
from faker import Faker

# Create a Faker instance for Turkish
f = Faker()

# Create an empty list to store the user data
users = []

# Generate data for 100 users
for _ in range(30000):
    # Create a dictionary for the user
    user = {
        "username": f.user_name(),
        "name": f.name(),
        "followers_count": f.random_int(min=0, max=10000),
        "following_count": f.random_int(min=0, max=10000),
        "language": f.language_code(),
        "region": f.country_code(),
        "tweets": [f.sentence(nb_words=6, variable_nb_words=True) for _ in range(10)],  # adjust as needed
        "following": [f.user_name() for _ in range(10)],  # assuming each user is following 10 other users
        "followers": [f.user_name() for _ in range(10)],  # assuming each user has 10 followers
    }

    # Add the user to the list
    users.append(user)

# Save the generated users to a JSON file
file_path = 'C:/Users/Abdullah Amin/PycharmProjects/pythonProject/generated_users.json'  # specify the desired file path
with open(file_path, 'w', encoding='utf-8') as json_file:
    json.dump(users, json_file, indent=4, ensure_ascii=False)

print(f"Generated users saved to {file_path}")
