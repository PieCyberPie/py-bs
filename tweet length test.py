MAX_LENGTH = 140
tweet = input("type in ur tweet")

if len(tweet)>140:
    print(f"Shorten it by {len(tweet)-MAX_LENGTH} pls")
else:
    print("looks fire, bro")
