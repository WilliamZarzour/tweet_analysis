import snscrape.modules.twitter as sntwitter
import pandas as pd

def scrape_tweets_to_csv():
    '''Takes a twitter advanced search query and saves a CSV and returns a dataframe of date,time, and tweets for the query'''
    # the more specific the Query the more reliable the data #Manual query or pasted query
    query = "(from:twitter) until:2023-03-10 since:2023-02-01"
    tweets = []
    limit = 500
    for tweet in sntwitter.TwitterSearchScraper(query).get_items():
        if len(tweets) == limit:
            break
        else:
            tweets.append([tweet.date, tweet.username, tweet.content])
    tweets_df = pd.DataFrame(tweets, columns=['Date', 'User', 'Tweet'])
    #print(tweets_df)

    # to save the dataframe to a CSV file
    file_name=input(f"Write CSV file name:")
    tweets_df.to_csv(file_name)
    return tweets_df

def nlp_analysis(tweets_data):
    '''load the csv file into a pandas dataframe'''
    all_words=[]
    keyword_list = []
    freq_dict={}
    flag=True

    # Define a list of keywords based on user input. Input must be accurate as there is no list editing atm. 
    while flag:
        keyword_input = input(f"Enter words: ").strip().lower()
        keyword_list.append(keyword_input)
        flag_input = input(f"Do you want to enter another word: Y or N\n>").strip().lower()
        if flag_input=="y":
            flag=True
        elif flag_input=="n":
            print(f"Your list of keywords is: {keyword_list}")
            flag=False
        else:
            print(f"Invalid Selection. Your list of keywords is: {keyword_list}")
    
    # Tokenize the words in the tweets Tokenization is a way of separating a piece of text into smaller units called tokens.
    tweets=tweets_data.loc[:,"Tweet"]
    for tweet in tweets:
        words = tweet.lower().split()
        all_words+=words

    #populate the dictionary with keywords and values of zero
    for keyword in keyword_list:
        freq_dict[keyword] = 0

    # iterate through each word and count the frequency for each keyword adding to the dictionary
    for word in all_words:
        if word in keyword_list:
            freq_dict[word] += 1
    
    for keyword in keyword_list:
        print(f"{keyword}: {freq_dict[keyword]}")
