import json
from faker import Faker
import random

def topic_related_hashtags(topic, num_hashtags):
    fake = Faker()


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


    topic_lower = topic.lower()


    specific_hashtags = topic_hashtags.get(topic_lower, ['#general', '#interest', '#topic'])


    random_hashtags = ['#' + fake.word() for _ in range(num_hashtags - len(specific_hashtags))]


    hashtags = specific_hashtags + random_hashtags

    random.shuffle(hashtags)

    return hashtags[:num_hashtags]

users = []

for _ in range(30000):
    f = Faker()
    degisken1 = f.random_int(min=0, max=20)
    degisken2 = f.random_int(min=0, max=20)

    degisken3 = random.choice(['travel', 'food', 'fashion', 'music', 'movies', 'books', 'science', 'nature', 'art', 'fitness', 'photography', 'sciencefiction', 'history', 'fitnessmotivation', 'pets', 'cooking', 'motivation', 'gaming', 'architecture', 'selfcare'])

    user = {
        "username": f.user_name(),
        "name": f.name(),
        "followers_count": degisken1,
        "following_count": degisken2,
        "language": f.language_code(),
        "region": f.country_code(),
        "tweets": [f.sentence(nb_words=6, variable_nb_words=True) + ' '.join(topic_related_hashtags(degisken3, 1)) for _ in range(10)],  # Generate 10 random tweets
        "following": [f.user_name() for _ in range(degisken1)],
        "followers": [f.user_name() for _ in range(degisken2)],
    }

    users.append(user)

file_path = 'C:/Users/Abdullah Amin/Desktop/30kData_1.json'
with open(file_path, 'w', encoding='utf-8') as json_file:
    json.dump(users, json_file, indent=4, ensure_ascii=False)

print(f"Generated users with consistent hashtags saved to {file_path}")
