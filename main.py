

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import NoSuchElementException
import json

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://rpa.hybrydoweit.pl/#articles")

articles = driver.find_elements_by_class_name("rpa-article-card")
results = {}
for i, article in enumerate(articles):
    try:
        meta_element = article.find_element_by_class_name('rpa-article-card__metadata-item')
        meta_element = meta_element.text
    except NoSuchElementException:
        meta_element = None
    try:
        link_element = article.find_element_by_class_name('rpa-article-card__link')
    except NoSuchElementException:
        link_element = None

    article_data = {
        'title': link_element.get_attribute('title'),
        'link': link_element.get_attribute('href'),
        'business': meta_element
    }
    print(article_data)
    results[i] = article_data

with open('results.json', 'w') as f:
    json.dump(results, f, indent=True, ensure_ascii=False)

driver.close()


