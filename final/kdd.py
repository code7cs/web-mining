from selenium import webdriver
import time
import codecs
import re

# One line per paper
# Each line has 5 columns, separated by a tab.
# 1st column is a list of author names, separated by ':'. For example: Theodoros Lappas:Benjamin Arai:Manolis Platakis
# 2nd column is the paper abstract.
# 3rd column is the title of the paper
# 4th column is the list of institutions with which the authors are affiliated.  The order should match the order of the authors in the first column. For example:
#     University of California, Riverside, Riverside, CA, USA:University of California, Riverside, Riverside, CA, USA:University of Athens, Athens, Greece
# 5th column includes the paper's publication year.

driver = webdriver.Chrome('./chromedriver')
fw = codecs.open('articles_kdd.txt', 'w', encoding='utf8')

# url = 'https://dl.acm.org/results.cfm?query=kdd&start=0&filtered=series%2EseriesAbbr%3DKDD&within=owners%2Eowner%3DHOSTED&dte=&bfr=&srt=%5Fscore'
for i in range(0, 5):
    time.sleep(2)
    url = 'https://dl.acm.org/results.cfm?query=kdd&start=' + str(
        i * 20) + '&filtered=series%2EseriesAbbr%3DKDD&within=owners%2Eowner%3DHOSTED&dte=&bfr=&srt=%5Fscore'
    # open the browser and visit the url
    driver.get(url)
    time.sleep(1)

    # scroll down twice to load more articles
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)

    articles = driver.find_elements_by_css_selector("[class=details]")

    for article in articles:
        authorName, paperAbstract, paperTitle, institutions, publicationYear = 'NA', 'NA', 'NA', 'NA', 'NA'
        # try:
        #     article.find_element_by_css_selector("[class=title]").click()
        #     time.sleep(2)
        #     driver.switch_to_window(driver.window_handles[1])
        #     time.sleep(2)
        #     institutions = driver.find_element_by_xpath('//*[@id="divmain"]/table/tbody/tr/td[1]/table[2]/tbody/tr/td[3]/a').text
        #     time.sleep(2)
        #     print(institutions)
        #     driver.back()
        #     time.sleep(2)
        #     driver.switch_to_window(driver.window_handles[0])
        #     time.sleep(2)
        # except:
        #     print('wrong')
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
            # institutions = \
            # article.find_element_by_css_selector("[class=source]").find_elements_by_tag_name("span")[1].text.split(":")[
            #     0]
            institutions = 'NA'
        except:
            print('no institutions')

        try:
            publicationYear = re.findall(r"\d+", article.find_element_by_css_selector("[class=publicationDate]").text)[
                0]
        except:
            print('no publicationYear')

        fw.write(str(authorName).replace(",", ":") + '\t' + str(paperAbstract) + '\t' + str(paperTitle) + '\t' + str(
            institutions)
                 + '\t' + publicationYear + '\n')

fw.close()

driver.quit()  # close the browser
