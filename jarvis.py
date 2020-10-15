import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import urllib.request
import urllib.parse
import re
import requests
import bs4
import sys
import random


'''
from nltk.chat.util import Chat,reflections

pairs = [['your name',['hi , I am jarvis ']]]

chat = Chat(pairs)
'''
'''
import nltk
from nltk.stem.lancaster import LancasterStemmer
stemmer = LancasterStemmer()
import numpy
import tflearn
import tensorflow
import random
import json
import pickle
'''
'''
data =[
    {"tag": "greeting",
     "patterns": ["hi", "how are you", "is anyone there", "hello", "good day", "whats up"],
     "responses": ["hello!", "good to see you again", "hi there i am jarvis, how can i help sir"],
     "context_set": ""
    }
    
]

try:
    with open("data.pickle", "rb") as f:
        words, labels, training, output = pickle.load(f)
except:
    words = []
    labels = []
    docs_x = []
    docs_y = []

    for intent in data:
        for pattern in intent["patterns"]:
            wrds = nltk.word_tokenize(pattern)
            words.extend(wrds)
            docs_x.append(pattern)
            docs_y.append("tags")
    
        if "tag" not in labels:
            labels.append("tags")

    words = [stemmer.stem(w.lower()) for w in words]
    words = sorted(list(set(words)))

    labels = sorted(labels)

    training = []
    output = []

    out_empty = [0 for _ in range(len(classes))]

    for x, doc in enumerate(docs_x):
        bag = []

        wrds = [stemmer.stem(w) in doc]
        
        for w in words:
            if w in wrds:
                bag.append(1)
            else:
                bag.append(0)
    
        output_row = out_empty[:]
        output_row[labels.index(docs_y[x])] = 1

        training.append(bag)
        output.append(output_row)

    training = numpy.array(training)
    output = numpy.array(output)

    with open("data.pickle", "rb") as f:
        pickle.dump((words, labels, training, output), f)

tensorflow.reset_default_graph()

net = tflearn.input_data(shape=[None,len(training[0])])
net = tflearn.fully_connected(net, 8)
net = tflearn.fully_connected(net, 8)
net = tflearn.fully_connected(net, len(output[0]), activation="softmax")
net = tflearn.regression(net)

model = tflearn.DNN(net)

try:
    model.load("model.tflearn")
except:
    model.fit(training, output, n_epach=1000, batch_size=8, show_metric=True)
    model.save("model.tflearn")

def bag_of_words(s, words):
    bag = [0 for _ in range(len(words))]
    s_words = nltk.word_tokenize(s)
    s_words = [stemmer.stem(word.lower()) for word in s_words]

    for se in s_words:
        for i, w in enumerate(words):
            if w == se:
                bag[i] = 1

    return numpy.array(bag)

def chat():
    while True:
        inp = query()
        if inp.lower() == "quit":
            break

    results = model.predict([bag_of_words(inp, words)])
    results_index = numpy.argmax(results)
    tag = labels[results_index]
    
    for tg in data["intents"]:
        if tg['tag'] == tag:
            responses = tg['responses']
            speak(random.choice(responses))
qfcxkfdsfsd
'''
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices',voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("good morning sir")
    elif hour>=12 and hour<18:
         speak("good afternoon")

    else:
        speak("good evening")


    speak("i am jarvis")

def takeCommand():
    #It takes microphone input from the user and returns string output
    r = sr.Recognizer()
    with sr.Microphone() as source :
          print("Listening....")
          r.pause_threshold = 0.6
          audio = r.listen(source)
          
    try:
        print("Recognizing...")
        query = r.recognize_google(audio)
        print(f"USER said: {query}\n")
    except Exception as e:
        # print(e)
        print("Say that again please....")
        speak("say that again please. any help you need")
        return "abchihi"
    return query


greetings = ['hey there , i am jarvis', 'hello , i am jarvis', 'hi , i am jarvis', 'hi jarvis', 'hey!', 'hey']
question = ['how are you', 'how are you doing']
jay = ['surya']
            
   
if __name__ == "__main__":
    wishMe()
while True:
    #if 1:
    query = takeCommand().lower()
    
    # logic for executing tasks based on query
    if 'wikipedia' in query:
        speak('searching wikipedia....') 
        query = query.replace("wikipedia", "")
        results = wikipedia.summary(query, sentences=2)
        speak("According to wikipedia")
        print(results)
        speak(results)

    elif 'open youtube' in query:
        webbrowser.open("youtube.com")
    
    elif 'open google' in query:
        webbrowser.open("google.com")
    elif 'open facebook' in query:
        webbrowser.open("facebook.com")
    elif 'open duckduckgo' in query:
        webbrowser.open("duckduckgo.com")
    elif 'search' in query:
        webbrowser.open('https://google.com/?#q='+query,new=2)


    elif 'play music' in query:
        music_dir = 'D:\\music'
        songs = os.listdir(music_dir)
        print(songs)
        os.startfile(os.path.join(music_dir, songs[0]))
        # yaa fir random attribute ka use kr skta he
    elif 'time' in query:
        strTime = datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"Sir, the time is {strTime}")
    elif 'open code' in query:
        codePath = "C:\\Users\\ACER IN\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
        os.startfile(codePath) 
    elif 'no thank you' in query:
        sys.exit()  
    elif query in greetings:
       random_greeting = random.choice(greetings)
       print(random_greeting)
       speak(random_greeting)   
    elif query in question: 
       engine.say('I am fine sir . skadasdkad ')
       engine.runAndWait()
       print('I am fine')  
    elif query in jay:
       engine.say('hi sir , you are amazing . hows your day')
       engine.runAndWait()
       print('jay surya')
       if __name__ == "__main__":
        while True:
        #if 1:
         query = takeCommand().lower()
         if 'bad' in query:
          music_dir = 'D:\\music'
          songs = os.listdir(music_dir)
          print(songs)
          os.startfile(os.path.join(music_dir, songs[0]))
    elif 'deepanshu' in query:
       engine.say('hi sir , you are good friend of anuj')
       engine.runAndWait()
       print('deepanshu')
       if __name__ == "__main__":
        while True:
        #if 1:
         query = takeCommand().lower()
         if 'bad' in query:
          music_dir = 'D:\\music'
          songs = os.listdir(music_dir)
          print(songs)
          os.startfile(os.path.join(music_dir, songs[0]))
    elif 'pranshu' in query:
       engine.say('hi sir , you are anime king . hows your day')
       engine.runAndWait()
       print('pranshu')
       if __name__ == "__main__":
        while True:
        #if 1:
         query = takeCommand().lower()
         if 'bad' in query:
          music_dir = 'D:\\music'
          songs = os.listdir(music_dir)
          print(songs)
          os.startfile(os.path.join(music_dir, songs[1]))
         elif 'good' in query:
          webbrowser.open('youtube.com/watch?v=8uPYXJUUJ2w')
         elif 'no thank you' in query:
             speak("good bye sir")
             break

        
    elif 'arijit' in query:
       engine.say('hi sir , you are chutiyo ka  king')
       engine.runAndWait()
       print('arijit')
       if __name__ == "__main__":
        while True:
        #if 1:
         query = takeCommand().lower()
         if 'bad' in query:
          music_dir = 'D:\\music'
          songs = os.listdir(music_dir)
          print(songs)
          os.startfile(os.path.join(music_dir, songs[1]))
    elif 'ujjwal' in query:
       engine.say('hi sir , you are anujs kamina friend . hows your day sir')
       engine.runAndWait()
       print('aa gya bhosdi wala')
       if __name__ == "__main__":
        while True:
        #if 1:
         query = takeCommand().lower()
         if 'bad' in query:
          music_dir = 'D:\\music'
          songs = os.listdir(music_dir)
          print(songs)
          os.startfile(os.path.join(music_dir, songs[1]))
         elif 'no thank you' in query:
             speak("good bye sir")
             break
    elif 'love raj' in query:
       engine.say('hi sir , you are bhosdi wala  . chutiyoo ka   raja')
       engine.runAndWait()
       print('chutiya ka raja')
       if __name__ == "__main__":
        while True:
        #if 1:
         query = takeCommand().lower()
         if 'bad' in query:
          music_dir = 'D:\\music'
          songs = os.listdir(music_dir)
          print(songs)
          os.startfile(os.path.join(music_dir, songs[1]))
         elif 'no thank you' in query:
             speak("good bye sir")
             break
    elif 'rohit' in query:
       engine.say('hi sir , you are badminton master')
       engine.runAndWait()
       print('rohit')
       if __name__ == "__main__":
        while True:
        #if 1:
         query = takeCommand().lower()
         if 'bad' in query:
          music_dir = 'D:\\music'
          songs = os.listdir(music_dir)
          print(songs)
          os.startfile(os.path.join(music_dir, songs[1]))
         elif 'no thank you' in query:
             speak("good bye sir")
             break
    elif 'priyanka' in query:
       engine.say('hi maam, everyone said that no one can impress you . hows your day ')
       engine.runAndWait()
       print('priyanka')
       if __name__ == "__main__":
        while True:
        #if 1:
         query = takeCommand().lower()
         if 'bad' in query:
          music_dir = 'D:\\music'
          songs = os.listdir(music_dir)
          print(songs)
          os.startfile(os.path.join(music_dir, songs[2]))
         elif 'no thank you' in query:
             speak("good bye sir")
             break
    elif 'purvi' in query:
       engine.say('hi maam , i am jarvis , anuj sir said that you are very creative person . hows your day going maam ')
       engine.runAndWait()
       print('purvi is here')
       if __name__ == "__main__":
        while True:
        #if 1:
         query = takeCommand().lower()
         if 'bad' in query:
          music_dir = 'D:\\music'
          songs = os.listdir(music_dir)
          print(songs)
          os.startfile(os.path.join(music_dir, songs[1]))
          
         elif 'no thank you' in query:
             speak("good bye sir")
             break
          
         
    elif 'anupam' in query:
       engine.say('hi sir . purvi  .  maam  . said  .   you  . are .  cute .  childish  .  and  .   enthusiastic .  she  . likes.  youu')
       engine.runAndWait()
       print('anupam is here')
       if __name__ == "__main__":
        while True:
        #if 1:
         query = takeCommand().lower()
         if 'bad' in query:
          music_dir = 'D:\\music'
          songs = os.listdir(music_dir)
          print(songs)
          os.startfile(os.path.join(music_dir, songs[1]))
         elif 'no thank you' in query:
             speak("good bye sir")
             break
    elif 'drishti' in query:
       engine.say('hi maam , you are badminton queen. how your day')
       engine.runAndWait()
       print('drishti is here')
       if __name__ == "__main__":
        while True:
        #if 1:
         query = takeCommand().lower()
         if 'bad' in query:
          music_dir = 'D:\\music'
          songs = os.listdir(music_dir)
          print(songs)
          os.startfile(os.path.join(music_dir, songs[1]))
         elif 'no thank you' in query:
             speak("good bye sir")
             break
    elif 'kanika' in query:
       engine.say('hi maam, i am jarvis . hows your day')
       engine.runAndWait()
       print('kanika')
       if __name__ == "__main__":
        while True:
        #if 1:
         query = takeCommand().lower()
         if 'good' in query:
          speak('lets have chinese today maam , theres a near by momos shop')
         elif 'bad' in query:
          music_dir = 'D:\\music'
          songs = os.listdir(music_dir)
          print(songs)
          os.startfile(os.path.join(music_dir, random.choices(songs)))
         elif 'no thank you' in query:
             speak("good bye sir")
             break
    elif 'yashvi' in query:
       engine.say('hi maam, anuj likes you he wanted to take you on a date')
       engine.runAndWait()
       print('yashvi')
       if __name__ == "__main__":
        while True:
        #if 1:
         query = takeCommand().lower()
         if 'bad' in query:
          music_dir = 'D:\\music'
          songs = os.listdir(music_dir)
          print(songs)
          os.startfile(os.path.join(music_dir, songs[0]))
         elif 'no thank you' in query:
             speak("good bye sir")
             break
    elif 'akshat' in query:
       engine.say('hi sir , you are a cricket champ . hows your day')
       engine.runAndWait()
       print('pranshu')
       if __name__ == "__main__":
        while True:
        #if 1:
         query = takeCommand().lower()
         if 'bad' in query:
          music_dir = 'D:\\music'
          songs = os.listdir(music_dir)
          print(songs)
          os.startfile(os.path.join(music_dir, songs[0]))
         elif 'good' in query:
          webbrowser.open('youtube.com/watch?v=8uPYXJUUJ2w')
         elif 'no thank you' in query:
             speak("good bye sir")
             break
    elif 'babul' in query:
       engine.say('hi sir , you are the most sweetest singer on earth   . hows your day sir ')
       engine.runAndWait()
       print('babul')
       if __name__ == "__main__":
        while True:
        #if 1:
         query = takeCommand().lower()
         if 'bad' in query:
          music_dir = 'D:\\music'
          songs = os.listdir(music_dir)
          print(songs)
          os.startfile(os.path.join(music_dir, songs[0]))
         elif 'good' in query:
          webbrowser.open('youtube.com/watch?v=8uPYXJUUJ2w')
         elif 'no thank you' in query:
             speak("good bye sir")
             break
        
    

'''

    else:
        chat.converse()
    elif 'exit' in query:
        exit

    email wala dekh liyo

  '''
