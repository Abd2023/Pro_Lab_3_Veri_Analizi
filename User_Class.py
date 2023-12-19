class User:
    def __init__(self, username, name, followers_count, following_count, language, region, tweets, following, followers):
        self.username = username
        self.name = name
        self.followers_count = followers_count
        self.following_count = following_count
        self.language = language
        self.region = region
        self.tweets = tweets
        self.following = following
        self.followers = followers

    def __str__(self):
        return f"User(username={self.username}, name={self.name}, followers_count={self.followers_count}, \n" \
               f"following_count={self.following_count}, language={self.language}, region={self.region}, \n" \
               f"tweets={self.tweets}, following={self.following}, followers={self.followers})\n"
