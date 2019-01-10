# import libraries
import urllib.request
from bs4 import BeautifulSoup

# specify the url
my_page='https://www.investopedia.com/terms/a/'

# query the website and return the html to the variable ‘page’
page = urllib.request.urlopen(my_page)

# parse the html using beautiful soup and store in variable `soup`
soup = BeautifulSoup(page,"html.parser")

# Take out the <div> of name and get its value
name_box = soup.find("ol", attrs={"class": "list gaEvent"})

name = name_box.text.strip() # strip() is used to remove starting and trailing
print(name)

