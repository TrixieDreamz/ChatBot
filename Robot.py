import io, random, string, warnings, nltk
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from nltk.stem import WordNetLemmatizer

warnings.filterwarnings('ignore')

nltk.download('popular', quiet=True)
#nltk.download('punkt')
#nltk.download('wordnet')

with open('MyText.txt', 'r', encoding='utf8', errors='ignore') as data:
    rawText = data.read().lower()

sent_tokens = nltk.sent_tokenize(rawText)
word_tokens = nltk.word_tokenize(rawText)

lemmer = WordNetLemmatizer()
def LemTokens(tokens):
    return [lemmer.lemmatize(token) for token in tokens]

remove_punct_dict = dict((ord(punct), None) for punct in string.punctuation)
def LemNormalize(text):
    return LemTokens(nltk.word_tokenize(text.lower().translate(remove_punct_dict)))

greeting_inputs = ("yo", "what's up", "hi", "hey")
greeting_resp = ("yo", "what's up", "hi", "hey")

def greeting(sentence):
    for word in sentence.split():
        if word.lower() in greeting_inputs:
            return random.choice(greeting_resp)
        
def response(user_response):
    robo_response = ''
    sent_tokens.append(user_response)
    TfidfVec = TfidfVectorizer(tokenizer=LemNormalize, stop_words='english')
    tfidf = TfidfVec.fit_transform(sent_tokens)
    vals = cosine_similarity(tfidf[-1], tfidf)
    idx = vals.argsort()[0][-2]
    flat = vals.flatten()
    flat.sort()
    req_tfidf = flat[-2]
    if(req_tfidf == 0):
        robo_response = robo_response + "I am sorry, I am not sure what you are talking about"
    else:
        robo_response = robo_response + sent_tokens[idx]
    return robo_response if robo_response else "I am sorry, I am not sure what you are talking about"

    
flag = True
print("Hi, my name is Jimmeh and I am going to give you some bad advice.")

while(flag == True):
    user_response = input()
    user_response = user_response.lower()
    if(user_response != 'bye'):
        if(user_response == 'thanks' or user_response == 'thank you'):
            flag = False
            print ("Ya, okay. Sure.")
        else:
            if(greeting(user_response)!=None):
                print ("Jimmeh: " + response(user_response))
            else: 
                print("Jimmeh: " + response(user_response))
                sent_tokens.remove(user_response)
    else:
        flag = False
        print("Jimmeh: " + "Fine. Dont talk to me then.") 
