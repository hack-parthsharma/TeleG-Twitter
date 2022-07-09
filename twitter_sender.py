import tweepy

import config


class TwiAPI():
    def __init__(self):
        auth = tweepy.OAuthHandler(config.CONSUMER_KEY, config.CONSUMER_SECRET)
        auth.set_access_token(config.ACCESS_TOKEN, config.ACCESS_SECRET)

        self.api = tweepy.API(auth_handler=auth, proxy=config.proxy)

    def send_status(self, text):
        geo = self.api.reverse_geocode(config.lon, config.lat)
        print(geo[0].id)
        try:
            status = self.api.update_status(text, place_id=geo[0].id)
        except Exception as e:
            return 'Error with twitter api: {}'.format(e)
        else:
            return 'Done: id: {}'.format(status.id_str)

    def del_status(self, id_str):
        try:
            status = self.api.destroy_status(id_str)
        except Exception as e:
            return 'Error with twitter api: {}'.format(e)
        else:
            print(status)
            return 'Done: tweet with text: "{}" was deleted'.format(status.text)
