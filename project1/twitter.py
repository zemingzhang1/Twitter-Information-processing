'''
@author: Souvik Das
Institute: University at Buffalo
'''
# AAAAAAAAAAAAAAAAAAAAAIzqTwEAAAAAEQahqT7KDawAqs7%2BKrKT2MtoTx4%3DTqAwGt5Lgtw9DU6AHX5eAu9Lh54b90tLaJkefuDN8OID2mogm9
import tweepy


class Twitter:
    def __init__(self):
        self.auth = tweepy.OAuthHandler("N2M3AIYygmIJGrFPZsJML8cqX",
                                        "STQla0NOHkIaRNrRXYkLUAlDVj5a3Uv5vdVHxskNLWBYiXfPTS")

        self.auth.set_access_token("1324019007784128512-qCxuTUWhLbvXMhpL6K7v7bWOZCtp7p",
                                   "Qb3dv5dOqPhSpxZEsc5yhgREK1LRCjrXVdkX7EWCfHRWP")
        self.api = tweepy.API(self.auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

    def _meet_basic_tweet_requirements(self):
        '''
        Add basic tweet requirements logic, like language, country, covid type etc.
        :return: boolean
        '''
        raise NotImplementedError

    def get_tweets_by_poi_screen_name(self, username, count):
        '''
        Use user_timeline api to fetch POI related tweets, some postprocessing may be required.
        '''
        # tweetData = self.api.user_timeline(screen_name=username, count=count)
        # tweetData = [i.id for i in tweetData]
        # return tweetData

        return [status for status in tweepy.Cursor(self.api.user_timeline, screen_name=username, tweet_mode="extended").items()]
        '''
        :return: List
        '''
        raise NotImplementedError

    def get_tweets_by_lang_and_keyword(self, lang, keywords, count):
        '''
        Use search api to fetch keywords and language related tweets, use tweepy Cursor.
        '''
        total = len(lang) * count

        holderDict = {}

        for w in keywords:
            timeLine = self.api.search(w, count=count)
            print(len(timeLine))

            for post in timeLine:
                if post.lang in lang:
                    if post.lang in holderDict:
                        holderDict[post.lang].append(post.id)
                    else:
                        holderDict[post.lang] = [post.id]

        return holderDict

        '''
        :return: List
        '''
        raise NotImplementedError

    def get_replies(self):
        '''
        Get replies for a particular tweet_id, use max_id and since_id.
        For more info: https://developer.twitter.com/en/docs/twitter-api/v1/tweets/timelines/guides/working-with-timelines
        :return: List
        '''
        raise NotImplementedError


if __name__ == '__main__':
    tw = Twitter()
    # pt = tw.get_tweets_by_poi_screen_name("SpaceX", 500)
    # print(len(pt))
    t = tw.get_tweets_by_poi_screen_name('@realDonaldTrump', 500)
    print(t)
