from selenium import webdriver
import time
import codecs
import re

driver = webdriver.Chrome('./chromedriver')
fw = codecs.open('articles_kdd.txt', 'w', encoding='utf8')

for i in range(0, 5):
    time.sleep(2)
    url = 'https://dl.acm.org/results.cfm?query=kdd&start=' + str(i * 20)
    # open the browser and visit the url
    driver.get(url)
    time.sleep(1)

    # scroll down twice to load more articles
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)

    articles = driver.find_elements_by_css_selector("[class=details]")

    for article in articles:
        authorName, paperAbstract, paperTitle, institutions, publicationYear = 'NA', 'NA', 'NA', 'NA', 'NA'

        try:
            authorName = article.find_element_by_css_selector("[class=authors]").text
        except:
            print('no author')

        try:
            paperAbstract = article.find_element_by_css_selector("[class=abstract]").text
        except:
            print('no paperAbstract')

        try:
            paperTitle = article.find_element_by_css_selector("[class=title]").text
        except:
            print('no paperTitle')

        try:
            institutions = \
            article.find_element_by_css_selector("[class=source]").find_elements_by_tag_name("span")[1].text.split(":")[
                0]
        except:
            print('no institutions')

        try:
            publicationYear = re.findall(r"\d+", article.find_element_by_css_selector("[class=publicationDate]").text)[
                0]
        except:
            print('no publicationYear')

        fw.write(str(authorName) + '\t\t' + str(paperAbstract) + '\t\t' + str(paperTitle) + '\t\t' + str(institutions)
                 + '\t\t' + publicationYear + '\n')

fw.close()

driver.quit()  # close the browser
