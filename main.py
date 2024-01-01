
import json
import re

import matplotlib
import matplotlib.pyplot as plt
# print(matplotlib.__version__)
import networkx as nx

import random

import ilgi_alani



import Kullanici_sinifi
import Veri_Yapilari


file_path = 'C:/Users/Abdullah Amin/PycharmProjects/pythonProject/100data.json'

with open(file_path, 'r', encoding='utf-8') as json_file:
    data = json.load(json_file)

user_dict = {}

for user_data in data:
    user = Kullanici_sinifi.User(
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


fig = plt.figure(figsize=(12, 10))  # Set the figure size
pos = nx.random_layout(G)
nx.draw(G, pos, node_color="red", node_size=10)
plt.title("blah blah", size = 20, color = "blue")
print(" 1- Her kullanıcı bir düğüm (node) ve takipçi-takip edilen ilişkileri de kenarlar(edge)\n olarak temsil edilmiştir.\n\n")
plt.show()




topic_hashtags = {
    'travel': ['#wanderlust', '#travelgram', '#explore', '#adventure', '#vacation'],
    'food': ['#foodie', '#delicious', '#foodporn', '#culinary', '#yum'],
    'fashion': ['#style', '#fashionista', '#trendy', '#ootd', '#fashionaddict'],
    'music': ['#musiclover', '#playlist', '#concert', '#musicians', '#melody'],
    'movies': ['#filmlover', '#movienight', '#cinema', '#moviebuff', '#hollywood'],
    'books': ['#booklover', '#readinglist', '#bookworm', '#literature', '#bestsellers'],
    'science': ['#scientific', '#research', '#discoveries', '#innovation', '#scientists'],
    'nature': ['#naturelover', '#outdoors', '#wildlife', '#environment', '#naturalbeauty'],
    'art': ['#artistic', '#creative', '#artgallery', '#modernart', '#artlovers'],
    'fitness': ['#fitlife', '#healthyliving', '#exercise', '#wellness', '#fitfam'],
    'photography': ['#photography', '#photooftheday', '#capturethemoment', '#visualart', '#photographer'],
    'sciencefiction': ['#scifi', '#sciencefiction', '#aliens', '#spaceadventure', '#futureworld'],
    'history': ['#historybuff', '#historical', '#timeless', '#historicalplaces', '#historygeek'],
    'fitnessmotivation': ['#fitmotivation', '#workoutinspiration', '#fitjourney', '#healthylifestyle', '#fitnessgoals'],
    'pets': ['#petlovers', '#furryfriends', '#petsofinstagram', '#animallove', '#petcare'],
    'cooking': ['#cookingadventures', '#homechef', '#foodgasm', '#culinaryart', '#cookingathome'],
    'motivation': ['#motivation', '#inspiration', '#positivity', '#selfimprovement', '#successmindset'],
    'gaming': ['#gamingcommunity', '#gamerlife', '#gamergirl', '#videogames', '#gamingsetup'],
    'architecture': ['#architecturelovers', '#architecturaldesign', '#modernarchitecture', '#archilovers', '#architecturedaily'],
    'selfcare': ['#selfcare', '#wellbeing', '#mindfulness', '#selflove', '#mentalhealth'],
}


def find_topic_by_hashtag(first_hashtag, topic_hashtags):
    found_key = None
    first_hashtag = "#" + first_hashtag

    for key, hashtags in topic_hashtags.items():

        if first_hashtag in hashtags:
            found_key = key
            # print(found_key)
            break

    return found_key


def find_user_interests(username, user_dict, topic_hashtags):
    user_interests = set()
    first_hashtag = None

    if username in user_dict:
        user = user_dict[username]

        for tweet in user.tweets:

            first_line = tweet.split('\n')[0]


            current_hashtag = re.search(r"#(\w+)", first_line)

            if current_hashtag:
                first_hashtag = current_hashtag.group(1)
                break

        found_key = find_topic_by_hashtag(first_hashtag, topic_hashtags)

        if(found_key) :
            print(f"Bu kullanıcının  '{found_key}' alanına ilgisi var'.\n\n")
        else:
            print(f"Bu kullanıcının ilgi alanı Bulanamadı")


#buradan//////////////////



def find_user_interests_2_(username, user_dict, topic_hashtags):
    user_interests = set()
    first_hashtag = None

    if username in user_dict:
        user = user_dict[username]

        for tweet in user.tweets:

            first_line = tweet.split('\n')[0]

            current_hashtag = re.search(r"#(\w+)", first_line)

            if current_hashtag:
                first_hashtag = current_hashtag.group(1)
                break

        found_key = find_topic_by_hashtag(first_hashtag, topic_hashtags)

        return  found_key

#buradan//////////////////

        # if first_hashtag:
        #     print(f"The first hashtag in the first tweet is: {first_hashtag}")




# burada başla /////////

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


user_tweets = {username: ' '.join(user.tweets) for username, user in user_dict.items()}


vectorizer = TfidfVectorizer()
tfidf_matrix = vectorizer.fit_transform(user_tweets.values())


cosine_similarities = cosine_similarity(tfidf_matrix)

usernames = list(user_tweets.keys())
for i in range(len(usernames)):
    for j in range(i+1, len(usernames)):
        if cosine_similarities[i, j] > 0.5:  # Benzerlik eşiği
            print(f"{usernames[i]} ve {usernames[j]} ortak ilgi alanlarına sahip.")



# burada bitir /////////





username = input(" 2- Kullanıcının ilgi alanını görmek için kullanıcı adı girin : ")

find_user_interests(username, user_dict, topic_hashtags)




username = input("\n\n 3- Beli bi kullanıcının bağlantılarını görmek için Kullanıcı Adı girin:")

if username in G:

    nodes = [username] + list(G[username])

    H = G.subgraph(nodes)

    pos = nx.spring_layout(H)
    nx.draw(H, pos, with_labels=True, node_color="red", node_size=500)

    plt.show()
else:
    print(f" '{username}' Bu kullanıcı Adı Bulunamadı.")







def dfs_list_tweets_with_keywords(G, user_dict, start_user, keywords):
    marked = set()

    def dfs(username):
        marked.add(username)
        user = user_dict.get(username)

        count = 1
        if user:
            for tweet in user.tweets:

                if any(keyword in tweet for keyword in keywords):
                    print(f"{count}. {username}: {tweet}")
                    count += 1

            for neighbor in G.neighbors(username):
                if neighbor not in marked:
                    dfs(neighbor)

    if start_user in G:
        dfs(start_user)
    else:
        print(f"'{start_user}' adlı kullanıcı bulunamadı.")

starting_user = input("\n\n 4- Kullanıcıların tweet içeriklerinde belirli anahtar kelimeleri\n ve hashtagleri içeren tweetler DFS algoritması kullanarak listelenmek için\n kullanıcı adı girin : ")

def get_user_keywords():
    keywords_input = input("Anahtar kelimeleri girin(anahtar kelimeler arasında boşluk olması gerekiyor): ")
    keywords_list = keywords_input.split()
    return keywords_list

keywords_to_search = get_user_keywords()


dfs_list_tweets_with_keywords(G, user_dict, starting_user, keywords_to_search)




from collections import Counter

def find_trending_hashtags_by_region_and_language(user_dict, target_region, target_language):
    hashtags_counter = Counter()

    for user in user_dict.values():
        if user.region == target_region and user.language == target_language:
            for tweet in user.tweets:
                hashtags = re.findall(r'#(\w+)', tweet)
                hashtags_counter.update(hashtags)

    trending_hashtags = hashtags_counter.most_common(10)

    print(f"Trend olan hashtaglar {target_language} dili ve {target_region} bölgesi için:")
    for hashtag, count in trending_hashtags:
        print(f"{hashtag}: {count} kere tekrarlanmıştır")

print("\n\n 5- Belirli bölge (konum) ve dil için trend olan hashtagler veya konular listelenmek için")

target_region = input("Hedef olan Bölegeyi giriniz: ")
target_language = input("Hedef olan dili giriniz: ")

# Call the function to find trending hashtags
find_trending_hashtags_by_region_and_language(user_dict, target_region, target_language)





def find_common_interest_followers(user_dict, user1, user2, topic_hashtags):
    common_followers = set(user_dict[user1].followers) & set(user_dict[user2].followers)

    for follower_username in common_followers:
        interests_user1 = set(find_user_interests_2_(user1, user_dict, topic_hashtags))
        interests_user2 = set(find_user_interests_2_(user2, user_dict, topic_hashtags))

        common_interests = interests_user1 & interests_user2

        if common_interests:
            print(f"Ortak ilgi alanına sahip kullanıcı: {follower_username}")

            print("-" * 30)


print("\n\n 6- Belirli iki kullanıcının takipçilerinden ilgi alanına göre filtreleme yapılarak ortak ilgi alanına sahip kullanıcılar litelenmek için : ")
user1 = input("İlk kullanıcının adını girin: ")
user2 = input("İkinci kullanıcının adını girin: ")


find_common_interest_followers(user_dict, user1, user2, topic_hashtags)

def create_interest_analysis_report(user_dict, topic_hashtags, output_file):
    with open(output_file, 'w', encoding='utf-8') as report_file:
        for username, user in user_dict.items():
            interests = find_user_interests_2_(username, user_dict, topic_hashtags)
            report_file.write(f"Kullanıcı Adı: {username}\n")
            report_file.write(f"İlgi Alanı: {''.join(interests)}\n")

            # Count common words among the user's tweets
            common_words_counter = Counter()
            for tweet in user.tweets:
                words = re.findall(r'\b\w+\b', tweet.lower())
                common_words_counter.update(words)

            # Include the most common words in the report
            if common_words_counter:
                report_file.write("Ortak Kelimeler:\n")
                for word, count in common_words_counter.most_common(3):
                    report_file.write(f"{word}: {count} kere\n")

            hashtag_details = []
            for interest in interests:
                if interest in topic_hashtags:
                    hashtags = topic_hashtags[interest]
                    hashtag_details.append(f"{interest}: {', '.join(hashtags)}")

            if hashtag_details:
                report_file.write("\nİlgi Alanlarına Ait Hashtagler:\n")
                report_file.write('\n'.join(hashtag_details))
                report_file.write('\n')

            report_file.write('-' * 50)
            report_file.write('\n')

output_file_path = 'ilgi_analiz_raporu.txt'
create_interest_analysis_report(user_dict, topic_hashtags, output_file_path)
print(f"Ve en son da İlgi analiz raporu başarıyla oluşturuldu ve '{output_file_path}' adlı dosyaya kaydedildi.")