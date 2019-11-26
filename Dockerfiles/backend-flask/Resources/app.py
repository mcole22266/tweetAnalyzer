from flask import Flask, jsonify
import mysql.connector
import json

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

@app.route("/db/<tablename>")
def testDB(tablename):
    config = {
            'user': 'root',
            'password': 'r00tp4ss',
            'host': 'db',
            'port': '3306',
            'database': 'tweetanalyzer'
            }
    connection = mysql.connector.connect(**config)
    cursor = connection.cursor()
    cursor.execute(f'SELECT * FROM {tablename}')
    results = [{name: description} for (name, description) in cursor]
    cursor.close()
    connection.close()
    return json.dumps({tablename : results})


if __name__ == '__main__':
    api = Driver()
    app.run(host='0.0.0.0', port=5000)  # port 5000 is Flask default
