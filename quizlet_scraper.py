from bs4 import BeautifulSoup
from urllib.request import Request, urlopen

# Set up quizlet scraper
## Example URL: https://quizlet.com/546386510/tapia-vocab-unit-2-flash-cards/
url = input('Enter the Quizlet URL: ')
req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
webpage = urlopen(req).read()
soup = BeautifulSoup(webpage, "html.parser")

# find list of all span elements containing both the words and definitions
termspan = soup.find_all('span', {'class' : 'TermText notranslate lang-en'})

# create list of lines corresponding to element texts 
allTerms = [span.get_text() for span in termspan]

# new liss
definitions = []
terms = []

# appending terms/definitions to new lists
n = 0
for every in allTerms:
    if n % 2 == 1:
        definitions.append(every)
    else:
        terms.append(every)
    n += 1

# printing out result
for term, definition in zip(terms, definitions):
    print (str(term) + ' - ' + str(definition))
