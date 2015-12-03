from TwitterSearch import *



try:
    tso = TwitterSearchOrder() 
    #tso.set_keywords(['suffering', 'depression', 'I', 'my']) 
    tso.set_keywords(['the', 'a'])
    tso.set_language('en') 
    tso.set_include_entities(False) 

    ts = TwitterSearch(
        consumer_key = '1kj4GBRevJITV4S40kLXGHVG2',
        consumer_secret = 'c80dJF41IwQV2G4ynR8VYblMQU15M4bc8OFg3aG6l8Y0aoSFhU',
        access_token = '1708110452-e3unR8gR7WRMGDoCh3aZutMPL3bFBLFlqHz8tzy',
        access_token_secret = 'kkiZDDp8KXLB8cRDwsMqBDc5IxqiaVXSmbQ2XtZEij0tl'
     )


    for tweet in ts.search_tweets_iterable(tso):
        print tweet['user']['screen_name']

except TwitterSearchException as e: # take care of all those ugly errors if there are some
    print(e)