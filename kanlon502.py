from random import randint
import tweepy
import time


NUMBER_OF_TWEETS = 100

def authorize():
    consumer_key = "SfxDfZhiqI0to9TG3jvbyM8Y3"
    consumer_secret = "6JMmBf010CQhLzu2yzzWgyZLOPJEujw7fD13CS0T3WZ65C8BPh"
    access_token = "2373068712-6TXGkeNndyJ8m9LPDV9CDQBBvMbn3y8C2Y7OXeI"
    access_token_secret = "UO0R8l1V9aMbzMmhZrgxsRojDzCdy91HJU8Tmz4l0lrBz"

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    return tweepy.API(auth, wait_on_rate_limit = True)

api = authorize()

def get_tweets(kanlon):
    user = '%' + kanlon + '-filter replies -filter retweets'
    tweets = tweepy.Cursor(api.search, q=user, max_ids = user, lang = "en").items(NUMBER_OF_TWEETS)
    return [tweet.text for tweet in tweets]


def start_game():
    print ("Lets play the kanlon game!")
    print ("I will display one of kanye west's or elon musk's past tweets")
    print ("Your job is to guess who wrote which tweet")
    print ("")

def play_game():
    play = 'play'
    while play.lower() == 'play':
        again = input("type play if you want to start! type quit if you want to stop playing:\n")
    
        while (again.lower()!= "play") and (again.lower() != "quit"):
            print("you have to type play or quit in order to start or finish!")
            again = input("You can stay for as long as you want! Just type play to start and quit when you wish to stop\n")
        
        if again == 'play':
            musk = "elonmusk"
            ye = "kanyewest"
        else :
            break

        musk_tweets = get_tweets(musk)
        ye_tweets = get_tweets(ye)
        tweet_num = randint(0, NUMBER_OF_TWEETS - 1)

        randomTweet = randint(1, 2)
        if randomTweet == 1:
            print(musk_tweets[tweet_num])
            guess = input("who tweeted this?")
            if guess == musk:
                print("Thats right!")
            else:
                print("Wrong!")

        else:
            print(ye_tweets[tweet_num])
            guess = input("who tweeted this?")
            if guess == ye:
                print("That's right!")
            else:
                print("Wrong!")
    again = input("Enter play if you want to keep playing")

        
start_game()
play_game()

