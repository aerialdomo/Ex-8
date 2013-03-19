import twitter
import markov

api = twitter.Api(consumer_key = 'Mh9QZzIWqBcnSeQAifWGQ',
                  consumer_secret ='2Isj9UvjaUysZlHBVQlZmf14iWloDq6GCqQSNIO4',
                  access_token_key='1279013186-ohmMnlHVbWz96eISVytcgjauvFSzKAfdc8oLjrV',
                  access_token_secret='jlAhKY3qaWvc1O2qyCy1LWfrfPMLcOT16D2ZwLDVLuQ')

status = api.PostUpdate(tweet)
print status.text