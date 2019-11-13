import twitter 
from twitter.error import TwitterError

class Driver():
    def __init__(self):
        self.CONSUMER_KEY = "ph6IOGnibyVBSHIkzUmbNSVVT"
        self.CONSUMER_SECRET = "8tFKR8jHMpzjYNFTERqMNJT0l8fq5CYAO603AcEgcd8fFoYfH6"
        self.ACCESS_TOKEN_KEY = "859419037951983616-Ky5XwyPk39fFlGtOvxKKJr5wwa7mJ96"
        self.ACCESS_TOKEN_SECRET = "AHIiHR4cdaf9LYbxBbzwGAjCHgm4WUbGYUxfERpI5TpXd" 
        # self.ACCESS_TOKEN_SECRET = "wrong access token to test failure to authenticate"  # uncomment to test failure
        self.api = self.authenticate()

    def authenticate(self):
        api = twitter.Api(consumer_key=self.CONSUMER_KEY,
                          consumer_secret=self.CONSUMER_SECRET,
                          access_token_key=self.ACCESS_TOKEN_KEY,
                          access_token_secret=self.ACCESS_TOKEN_SECRET)

        print("---> Verifying Credentials")
        try:
            api.VerifyCredentials()
            print("---> Authentication Successful")
        except twitter.error.TwitterError:
            print("---> Could not authenticate")
            print("Verify your access tokens and api keys")
            print("Visit: https://developer.twitter.com/en/apps/16994059")
        
        return api

    def getUserTweets(self, username, maxtweets=20):
        timeline = self.api.GetUserTimeline(screen_name=username, count=maxtweets)
        return timeline 

    def getHashtagTweets(self, hashtag):
        tweets = []
        results = self.api.GetSearch(term=hashtag)
        for result in results:
            if result.hashtags:
                hashtaglist = []
                for resulthashtag in result.hashtags:
                    hashtaglist.append(resulthashtag.text)
                    if hashtag[1:] in hashtaglist:  # hashtag[1:] removes the hashtag itself
                        tweets.append(result)
        return tweets 

# ------ TEST FUNCTIONALITY -------
if __name__ == "__main__":
    driver = Driver()
    userinput = input("Twitter Username or hashtag: ")
    if userinput[0] == '#':
        results = driver.getHashtagTweets(userinput)
    else:
        results = driver.getUserTweets(userinput)

    for tweet in results:
        print(f'{tweet.created_at}: {tweet.text}')