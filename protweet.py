import tweepy

def get_api(cfg):
  auth = tweepy.OAuthHandler(cfg['consumer_key'], cfg['consumer_secret'])
  auth.set_access_token(cfg['access_token'], cfg['access_token_secret'])
  return tweepy.API(auth)

def main():
  # Fill in the values noted in previous step here
  cfg = { 
    "consumer_key"        : "ggGyOh4ntbTvMvFAa1MoLMSbl",
    "consumer_secret"     : "4oBPjWJvzGw93HTgAoiWXGPNSUNmDAvMoY5sJNslOZWK08uok8",
    "access_token"        : "968052079427235840-CDoU8Nr0mo1oP43vFyjafdxtd5WSFp7",
    "access_token_secret" : "PLPQWhmGZpEsE9lPKISFBmj89ATMVzE89QziOrd9KfFp7" 
    }

  api = get_api(cfg)
  tweet = "Hello, world!...."
  status = api.update_status(status=tweet) 
  # Yes, tweet is called 'status' rather confusing

if __name__ == "__main__":
  main()

