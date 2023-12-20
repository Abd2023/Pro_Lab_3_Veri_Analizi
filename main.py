
import json

import matplotlib.pyplot as plt
import networkx as nx
import numpy as np
import random

import ilgi_alani

seed = 0
random.seed(seed)
np.random.seed(seed)

import User_Class
import Veri_Yapilari


# Read the JSON file with user data
file_path = 'C:/Users/Abdullah Amin/PycharmProjects/pythonProject/generated_users.json'

with open(file_path, 'r', encoding='utf-8') as json_file:
    data = json.load(json_file)

# Create a dictionary (hash table) to store users using usernames as keys
user_dict = Veri_Yapilari.MyDict()

# Convert the data to User objects and add them to the hash table
for user_data in data:
    user = User_Class.User(
        username=user_data['username'],
        name=user_data['name'],
        followers_count=user_data['followers_count'],
        following_count=user_data['following_count'],
        language=user_data['language'],
        region=user_data['region'],
        tweets=user_data['tweets'],
        following=user_data['following'],
        followers=user_data['followers'],
    )
    user_dict[user.username] = user





G = nx.Graph()


for user_data in data:
    for follower_username in user_data['followers']:
        G.add_edge(follower_username, user_data['username'])

for user_data in data:
    for following_username in user_data['following']:
        G.add_edge(following_username, user_data['username'])



# Visualize the graph with random layout
pos = nx.random_layout(G)
nx.draw(G, pos, node_color="red", node_size=10)
#plt.margins(0.2)
plt.show()


# Get the username from the console
username = input("Enter a username: ")

# Check if the username exists in the graph
if username in G:
    # Create a list of nodes to be included in the subgraph
    nodes = [username] + list(G[username])
    # Create the subgraph
    H = G.subgraph(nodes)
    # Visualize the subgraph
    pos = nx.spring_layout(H)
    nx.draw(H, pos, with_labels=True, node_color="red", node_size=500)
    plt.show()
else:
    print(f"User with username '{username}' not found.")




user_most_commaon_word = Veri_Yapilari.MyDict()
for username, user in user_dict.items():
    interests = ilgi_alani.find_interests(user.tweets)
    user_most_commaon_word[username] = interests

count = 0
for username in user_most_commaon_word.keys:
    count += 1
    print(count)
    print(username, user_most_commaon_word[username])






