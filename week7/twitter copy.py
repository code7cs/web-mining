from selenium import webdriver
import time, codecs

url = 'https://twitter.com/SHAQ'

# open the browser and visit the url
driver = webdriver.Chrome('./chromedriver')
driver.get(url)

# scroll down twice to load more tweets
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(2)
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(2)

# find all elements with a class that ends in 'tweet-text'
tweets = driver.find_elements_by_css_selector("[class*=original-tweet]")

# write the tweets to a file
fw = codecs.open('tweets.txt', 'w', encoding='utf8')
for tweet in tweets:
    txt, retweets, replies, likes, time = 'NA', 'NA', 'NA', 'NA', 'NA'

    try:
        txt = tweet.find_element_by_css_selector("[class$=tweet-text]").text
    except:
        print('no text')

    try:
        replyElement = tweet.find_element_by_css_selector("[class$=js-actionReply]")
        replies = replyElement.find_element_by_css_selector('[class=ProfileTweet-actionCountForPresentation]').text
    except:
        print('no replies')

    try:
        retweetElement = tweet.find_element_by_css_selector("[class$=js-actionRetweet]")
        retweets = retweetElement.find_element_by_css_selector('[class=ProfileTweet-actionCountForPresentation]').text
    except:
        print('no retweets')

    try:
        likeElement = tweet.find_element_by_css_selector("[class$=js-actionFavorite]")
        likes = likeElement.find_element_by_css_selector('[class=ProfileTweet-actionCountForPresentation]').text
    except:
        print('no likes')
    try:
        timeElement = tweet.find_element_by_css_selector("[class*=tweet-timestamp]")
        time = timeElement.find_element_by_css_selector("[class*=js-short-timestamp]").text
    except:
        print('no time')

    fw.write(txt.replace('\n', ' ') + '\t' + str(replies) + '\t' + str(retweets) + '\t' + str(likes) + '\t' + str(
        time) + '\n')

fw.close()

# driver.quit()#close the browser
