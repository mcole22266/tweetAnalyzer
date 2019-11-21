from flask import Flask, jsonify

from twitterDriver import Driver 

app = Flask(__name__)

@app.route("/user/<username>")
def userTweets(username):
    '''Returns 20 Tweets based on given username'''
    return api.getUserTweets(username)

@app.route("/user/<username>/<numTweets>")
def userTweets_setnumber(username, numTweets):
    '''Returns specified number of Tweets based on given username and 
    desired number of Tweets (likely Twitter-imposed limitations)'''
    return api.getUserTweets(username, numTweets)

if __name__ == '__main__':
    api = Driver()
    app.run(host='0.0.0.0', port=8000)