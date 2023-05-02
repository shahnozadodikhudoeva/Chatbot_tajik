import nltk
import json
import pickle
import numpy as np
import random
from transliterate import translit
from fuzzywuzzy import fuzz
from keras.models import load_model




model = load_model('chatbot_model.h5')
intents = json.loads(open('intents.json').read())
words = pickle.load(open('words.pkl','rb'))
classes = pickle.load(open('classes.pkl','rb'))


som=[ 'сомона','сомон',  'сом','сомяк','см',  'сомони',
  'несомон',  'скм','см','сма','сми','смк','смн',
  'сой','сум','сом,там','сомана','сомани','сомда','сомени','сомнаи','сомни','сомон','сомон,',
  'сомона','сомонаи','сомонай','сомонам','сомонаш','сомонаю','сомоная','сомонба','сомонда','сомоне','сомони',
  'сомони+','сомони,','сомониш','сомонию','сомонй','сомонӣ','сор', 'соҳ',  'сум',
 ]

megabayt= ['мегабайташ','мгбайт','мегабит','мегабает','мегабай','мегабайд','мегабайт','мегабайта','мегабайтам','мегабайтамро',
  'мегабайтан','мегабайташ','мегабайтза','мегабайти','мегабайтим','мегабайтовот','мегабайтош','мегабайтхо','мегабайтхова',
  'мегабайтш','мегабайты','мегабайтыя','мегахай','мигабайт','мнгабайти','мг','мб']
sms=['смс','сми','сообщен','сообшение','собшен','собшение','сообщение','собшен', 'сообщения','собшенша', "смска"]
minutes=['минут','минута','мин', 'мн','минута','минутаба', 'мнут','минуташ','минутба',]
unlimited=['"безлимит','«+безлимит','белимит','безлим','безлими','безлиминт''безлимит','безлимит+','безлимит,','безлимита',
  'безлимитаво','безлимитада', 'безлимитай', 'безлимитайне', 'безлимитау', 'безлимиташ' 'безлимитесть', 'безлимити',
  'безлимити,','безлимитины','безлимитка','безлимитна','безлимитная','безлимитни','безлимитной','безлимитном',
  'безлимитны','безлимитные','безлимитный','безлимитных,','безлимитому','безлимитро','безлимитхои','безлимитхуб',
  'безлимить','безлимт','безлимта','безлмит','безнимит','безнимити','безнимитш','безоимит','белимит','белимит9','белимити',
  'бзлимит','бнзлимит','кненбезлимит','сумбезлимит','хобезлимит', 'бемахдуд', 'бемахдуди', 'бемаҳдуд', 'махдуд']
darkor=['дарко','даркр','дакор','дркр','дарокор']

internet= ['"+интернет','+интернет','+интирнет', 'аинтернет', 'акаинтернет', 'акоинтернет', 'астинтернети',
  'баинтернет','бариинтернет','интенет','интергети','интерен','интеренет','интеренети','интеретш','интерне','интернеи','интернест',
  'интернет','интернет+','интернет,','интернев','интернета','интернетавот','интернетам','интернетама','интернетамон',
  'интернетаон','интернетатор','интернетау','интернетаха','интернеташ','интернеташро','интернетба','интернетв','интернетвы',
  'интернетга','интернете','интернети','интернетимо','интернетирон','интернетиш','интернеткак','интернетм',
  'интернетмой','интернетом','интернетомв','интернетон','интернетро','интернету','интернетуш','интернетчи',
  'интернетш','интернеты','интернетӣ','интернтш','интнернетам','интрнет','интрнети','кинтернет','кненинтернет',
  'манинтернет','мининтернет','нагзинтернет','сустинтернет','хастинтернет','чиинтернет','энтернет','《+интернет'],

megas=[1000, 1500, 2000, 3000, 4000, 5000, 6000, 8000, 10000, 15000, 18000, 20000, 22000, 30000, 60000, 100000]
soms=[30,60,100, 160, 200, 65, 105, 165, 205, 35, 65, 105, 165, 205, 59,99, 149, 299, 499, 899]
smses=[100, 300, 800, 1500, 2000, 300, 200, 150, 600, 15, 40, 100, 180, 220, ]
minuts=[10,60,100,160, 300]

darkors=[30,60,100,160,200]
interents=[65, 105, 165, 205, 35]
unlimiteds=[59,99,149,199,299, 499, 899]
socseti=[65, 105,165,205]

def removeConsecutiveDuplicates(s):
    if len(s)<2 or s.isdigit():
        return s
    if s[0]!=s[1]:
        return s[0]+removeConsecutiveDuplicates(s[1:])
    return removeConsecutiveDuplicates(s[1:])

# Find similar wording and change them
def similars(R):
    altered=[]
    for i in R:
        dictionary={}
        for j in words:
            Ratio = fuzz.ratio(i,j)
            dictionary[j]=Ratio
        valuesD=dictionary.values()
        maximum=max(valuesD)
        if maximum>=80:
            i=max(dictionary,key=dictionary.get)
        altered.append(i)
    return altered
 # Change some of the wordings in the beginning, so they wont bring any issues with writiing later:
def wordS(R):
    for i in range(len(R)):
        for j in som:
            ratio=fuzz.ratio(R[i],j)
            if ratio>=85:
                R[i]="сом"
        for j in megabayt:
            ratio=fuzz.ratio(R[i],j)
            if ratio>=85:
                R[i]="мб"
        for j in sms:
            ratio=fuzz.ratio(R[i],j)
            if ratio>=85:
                R[i]="смс"
        for j in minutes:
            ratio=fuzz.ratio(R[i],j)
            if ratio>=85:
                R[i]="мин"
        for j in unlimited:
            ratio=fuzz.ratio(R[i],j)
            if ratio>=85:
                R[i]="безлимит"
        for j in darkor:
            ratio=fuzz.ratio(R[i],j)
            if ratio>=85:
                R[i]="даркор"
        for j in internet:
            ratio=fuzz.ratio(R[i],j)
            if ratio>=85:
                R[i]="интернет"
    return R
 # numbers that are written with space should be one whole
import re
def numberSpace(R):
    R=wordS(R)
    for i in range(len(R)-1):
        if R[i].isdigit() and R[i+1].isdigit():
            R[i]=str(R[i])+str(R[i+1])
            R[i+1]=''
    if "" in R:
        R.remove("")
    R=[re.split(r'(\d+)', s) for s in R]
    m=[]
    for i in R:
        for j in i:
            if j!="":
                m.append(j)
    return m

    
def clean_up_sentence(sentence):
    # tokenize the pattern - split words into array
    sentence_words = nltk.word_tokenize(sentence)
    R=[]
    #lower the letters and convert to cyrillic
    for i in sentence_words:
        if i.isdigit():
            R.append(i)
        else:
            i = i.lower()
            i=translit(i, "ru")
            R.append(removeConsecutiveDuplicates(i))
    #remove word "darkor" at the end of the sentence as it may be misunderstood
    if len(R)>1:
        if R[-1]=="даркор" or R[-1]=="даркорай":
            R=R[:-1]
 
    R=numberSpace(R)
   
    #naming

    for i in range(1,len(R)):
        if  R[i].isdigit():
            if R[i-1]=='даркор':
                d={}
                for j in darkors:
                    d[j]=abs(int(j)-int(R[i]))
                minimum_distance=min(d,key=d.get)
                R[i]=str(minimum_distance)

            if R[i-1]=='безлимит':
                d={}
                for j in unlimiteds:
                    d[j]=abs(int(j)-int(R[i]))
                minimum_distance=min(d,key=d.get)
                R[i]=str(minimum_distance)

            if R[i-1]=='интернет':
                d={}
                for j in interents:
                    d[j]=abs(int(j)-int(R[i]))
                minimum_distance=min(d,key=d.get)
                R[i]=str(minimum_distance)

            if R[i-1]=='соцсети' or R[i-1]=='сети' or R[i-1]=='сет':
                d={}
                for j in socseti:
                    d[j]=abs(int(j)-int(R[i]))
                minimum_distance=min(d,key=d.get)
                R[i]=str(minimum_distance)

  
    # while different variety of numbers may be in the question bring them into specific order

    for i in range(len(R)-1):
        if  R[i].isdigit():
            if R[i+1]=='сом':
                d={}
                for j in soms:
                    d[j]=abs(int(j)-int(R[i]))
                minimum_distance=min(d,key=d.get)
                R[i]=str(minimum_distance)
                
            elif R[i+1]=='мб':
                d={}
                for j in megas:
                    d[j]=abs(int(j)-int(R[i]))
                minimum_distance=min(d,key=d.get)
                R[i]=str(minimum_distance)   

            elif R[i+1]=='мин':
                d={}
                for j in minuts:
                    d[j]=abs(int(j)-int(R[i]))
                minimum_distance=min(d,key=d.get)
                R[i]=str(minimum_distance )   

            elif R[i+1]=='смс':
                d={}
                for j in smses:
                    d[j]=abs(int(j)-int(R[i]))
                minimum_distance=min(d,key=d.get)
                R[i]=str(minimum_distance)  

    liste=['мб','смс','сом','минут']
    number=0
    for i in R:
        if i in liste:
            number+=1
    if number>=2:
        R=["вопрос"]
    print (similars(R))
    return similars(R)


   


# return bag of words array: 0 or 1 for each word in the bag that exists in the sentence

def bow(sentence, words, show_details=True):
    # tokenize the pattern
    sentence_words = clean_up_sentence(sentence)
    # bag of words - matrix of N words, vocabulary matrix
    bag = [0]*len(words)  
    for s in sentence_words:
        for i,w in enumerate(words):
            if w == s: 
                # assign 1 if current word is in the vocabulary position
                bag[i] = 1
                if show_details:
                    print ("found in bag: %s" %w)
    return(np.array(bag))


def predict_class(sentence, model):
    # filter out predictions below a threshold
    p = bow(sentence, words,show_details=False)
    res = model.predict(np.array([p]))[0]
    ERROR_THRESHOLD = 0.6
    results = [[i,r] for i,r in enumerate(res) if r>ERROR_THRESHOLD]
    # sort by strength of probability
    results.sort(key=lambda x: x[1], reverse=True)
    return_list = []
    for r in results:
        return_list.append({"intent": classes[r[0]], "probability": str(r[1])})
    return return_list


def getResponse(ints, intents_json):
    try:
        tag = ints[0]['intent']
        list_of_intents = intents_json['intents']
        for i in list_of_intents:
            if(i['tag']== tag):
                result = random.choice(i['responses'])
                break   
    except:
        result = "operator"
    return result

arrayN=[" "]
def chatbot_response(msg):
    arrayN.append(msg)
    if predict_class(msg,model)!=[]:
        ints = predict_class(msg, model)
    else:
        string=' '.join(arrayN[-2:])
        ints = predict_class(string, model)
    res = getResponse(ints, intents)
    return res
