import twitter
import markov

api = twitter.Api(consumer_key = xxx,
                  consumer_secret =xxx,
                  access_token_key=xxx,
                  access_token_secret=xxx

status = api.PostUpdate(tweet)
print status.text
