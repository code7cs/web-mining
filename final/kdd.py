from selenium import webdriver
import time
import codecs

url = 'https://dl.acm.org/results.cfm?query=kdd&Go.x=0&Go.y=0'

# open the browser and visit the url
driver = webdriver.Chrome('./chromedriver')
driver.get(url)

# scroll down twice to load more articles
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(2)
# driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
# time.sleep(2)

# find all elements with a class that ends in 'article-text'
articles = driver.find_elements_by_css_selector("[class*=original-article]")

# write the articles to a file
fw = codecs.open('articles.txt', 'w', encoding='utf8')
for article in articles:
    txt, comments, retweets, likes, date = 'NA', 'NA', 'NA', 'NA', 'NA'

    try:
        txt = article.find_element_by_css_selector("[class$=article-text]").text
    except:
        print('no text')

    # comments
    try:
        commentElement = article.find_element_by_css_selector("[class$=js-actionReply]")
        comments = commentElement.find_element_by_css_selector("[class=ProfileTweet-actionCountForPresentation]").text
    except:
        print('no comments')

    try:
        retweetElement = article.find_element_by_css_selector("[class$=js-actionRetweet]")
        retweets = retweetElement.find_element_by_css_selector('[class=ProfileTweet-actionCountForPresentation]').text
    except:
        print('no retweets')

    try:
        likeElement = article.find_element_by_css_selector("[class$=js-actionFavorite]")
        likes = likeElement.find_element_by_css_selector('[class=ProfileTweet-actionCountForPresentation]').text
    except:
        print('no likes')

    try:
        time = article.find_element_by_css_selector("[class*=time]")
        date = time.find_element_by_css_selector("[class*=_timestamp]").text
    except:
        print('no date')

    fw.write(txt.replace('\n', ' ') + '\t' + str(comments) + '\t' + str(retweets) + '\t' + str(likes) + '\t' + str(
        date) + '\n')

fw.close()

driver.quit()  # close the browser
