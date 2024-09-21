import spacy
import nltk
from nltk.corpus import stopwords
import string
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer

# Download necessary NLTK resources run for one time
# nltk.download('punkt')
# nltk.download('stopwords')
# nltk.download('wordnet')

# Load spaCy English model
nlp = spacy.load('en_core_web_sm')

doc = nlp("""<p id="original-text">
Welcome to the world of Natural Language Processing (NLP)! 
This paragraph delves into the fascinating realm of text analysis, where we'll unravel the magic behind understanding & manipulating human language. Let's embark on a journey through an NLP pipeline, transforming raw text into structured insights. We'll encounter challenges like contractions (e.g., "can't," "wouldn't"), possessives ("Mary's cat," "the company's profits"), hyphenated words ("state-of-the-art," "well-being"), and even emoticons (:-), 😉). Punctuation marks like commas, semicolons (;), and exclamation points (!) will also play a role. Brace yourselves for a captivating exploration of how machines decipher the intricacies of human communication! 
</p>""")


print("Step 1: Sentence Segmentation")
sentences = [sent.text for sent in doc.sents]
print("Sentence Segmentation:")
for sentence in sentences:
    print(sentence)