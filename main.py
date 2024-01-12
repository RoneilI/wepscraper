import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://oxylabs.io/blog")

results = []
content = driver.page_source
soup = BeautifulSoup(content, features= "html.parser")


driver.quit()

for i in soup.findAll(attrs = "css-bnfvmw ez2v0aa1"):
    wam = i.find("a")
    if wam not in results:
        results.append(wam.text)


print(results)





