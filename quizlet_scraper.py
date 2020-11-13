from bs4 import BeautifulSoup
from urllib.request import Request, urlopen

## Example URL: https://quizlet.com/546386510/tapia-vocab-unit-2-flash-cards/

def getVocabulary(quizletURL):
    req = Request(quizletURL, headers={'User-Agent': 'Mozilla/5.0'})
    webpage = urlopen(req).read()
    soup = BeautifulSoup(webpage, "html.parser")

    # find list of all span element text containing both words/definitions
    termspan = soup.find_all('span', {'class' : 'TermText notranslate lang-en'})
    vocab = [span.get_text() for span in termspan]

    # new lists
    definitions = []
    terms = []

    # appending terms/definitions to new lists
    n = 0
    for vocabTerm in vocab:
        if n % 2 == 1:
            definitions.append(vocabTerm)
        else:
            terms.append(vocabTerm)
        n += 1

    # returning result
    result = ""
    for term, definition in zip(terms, definitions):
        result += str(term) + ' - ' + str(definition + '\n')
        
    return result

url = 'https://quizlet.com/546386510/tapia-vocab-unit-2-flash-cards/'
print(getVocabulary(url))
