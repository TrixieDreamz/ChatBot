import io
import random
import string
import warnings
import nltk
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from nltk.stem import WordNetLemmatizer
import Jimmeh_story_telling
import os

warnings.filterwarnings('ignore')
nltk.download('popular', quiet=True)

# Get the directory of the current script
current_directory = os.path.dirname(os.path.abspath(__file__))

# Define the paths to the text files
jimmeh_ideas_file = os.path.join(current_directory, 'JimmehResponse', 'Jimmeh_Ideas.txt')
my_text_file = os.path.join(current_directory, 'JimmehResponse','MyText.txt')

# Load responses from the Jimmeh_Ideas.txt file
with open(jimmeh_ideas_file, 'r', encoding='utf-8') as file:
    jimmeh_ideas = file.readlines()

# Load raw text from the MyText.txt file
with open(my_text_file, 'r', encoding='utf-8', errors='ignore') as data:
    rawText = data.read().lower()

sent_tokens = nltk.sent_tokenize(rawText)
word_tokens = nltk.word_tokenize(rawText)

lemmer = WordNetLemmatizer()

def LemTokens(tokens):
    return [lemmer.lemmatize(token) for token in tokens]

remove_punct_dict = dict((ord(punct), None) for punct in string.punctuation)

def LemNormalize(text):
    return LemTokens(nltk.word_tokenize(text.lower().translate(remove_punct_dict)))

def response(user_response):
    robo_response = ''
    
    # Check if user input matches any category
    categories = ['ideas', 'responses', 'happy', 'mad', 'sad', 'alien_desires']
    matched_category = None
    for category in categories:
        if category in user_response.lower():
            matched_category = category
            break
    
    # If a category is found in the user input
    if matched_category:
        try:
            # Load responses from the corresponding text file
            with open(f'Jimmeh_{matched_category.capitalize()}.txt', 'r', encoding='utf-8') as file:
                lines = file.readlines()
                robo_response = random.choice(lines).strip()
        except FileNotFoundError:
            robo_response = "I am sorry, I don't have anything to say on that topic."
    else:
        # Use TF-IDF approach if no category is found
        sent_tokens.append(user_response)
        TfidfVec = TfidfVectorizer(tokenizer=LemNormalize, stop_words='english')
        tfidf = TfidfVec.fit_transform(sent_tokens)
        vals = cosine_similarity(tfidf[-1], tfidf)
        idx = vals.argsort()[0][-2]
        flat = vals.flatten()
        flat.sort()
        req_tfidf = flat[-2]
        if req_tfidf == 0:
            robo_response = "I am sorry, I am not sure what you are talking about"
        else:
            robo_response = sent_tokens[idx]
    
    return robo_response

flag = True
print("Hi, my name is Jimmeh and I am going to give you some bad advice.")

while flag:
    user_response = input()
    user_response = user_response.lower()
    if user_response != 'bye':
        if user_response == 'thanks' or user_response == 'thank you':
            flag = False
            print("Ya, okay. Sure.")
        elif 'story' in user_response:
            # Call the function to generate a story
            story = Jimmeh_story_telling.generate_story()
            print("Jimmeh: " + story)
        else:
            print("Jimmeh: " + response(user_response))
    else:
        flag = False
        print("Jimmeh: Fine. Don't talk to me then.")
