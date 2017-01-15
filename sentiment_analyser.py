import tkinter as tk
from tkinter import *
import sys
import os
import numpy as np
import re

import sys
import os
import numpy as np
import scipy
from sklearn import datasets
from sklearn.datasets import load_files
import nltk
from nltk.corpus import stopwords
from sklearn import metrics
from sklearn.linear_model import LogisticRegression
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.cross_validation import cross_val_score
from sklearn import svm
from sklearn.naive_bayes import GaussianNB
#required classes
class SampleApp(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)#interface
        Tk.geometry(self,"400x400")
        Tk.title(self, 'Sentiment Analysis')
        Tk.configure(self,background='#add8e6')
        # self.mainwindow.resizable(self, width=False, height=False)
        v = ('helvetica',30)
        self.heading = tk.Label(text="Sentiment Analysis", font=v, bg='#add8e6',fg='#4b4640')
        self.heading.pack(fill=X,pady=20)
        v1 = ('helvetica', 15)
        t = "Please write any sentence and we will predict the sentiment"
        self.instructions = tk.Label(self,text=t,font=v1)
        self.instructions.pack()
        self.entry = tk.Text(self,font='helvetica',height=5,width=20)
        self.button = tk.Button(self, text="Submit", command=self.on_button,bg='#c8bcac',fg='white',font='helvetica')
        self.entry.pack(fill=X,pady=20)
        self.entry.focus_set()
        self.button.pack()
        var = 'Prediction'
        self.l = tk.Label(self,text=var,font=v1)
        self.l.pack(side='left')
        
    def on_button(self):#when the user enters input statement,
        var = self.entry.get('1.0','end')
        # print var
        v1 = ('helvetica', 15)
        self.entry.delete('1.0','end')
        fo = open("C:\\Python34\\input\\tweet\\input.txt", "w")#read input file
        fo.write(re.sub('[^A-Za-z0-9]+', ' ', var))
        fo.close()
        
        #######################
        print ('loading data......')
        data1=load_files('C:\\Python34\\Senti')#data from this page is read 
        #data1=datasets.load_iris()
        print ('Data Loaded...........')
        #print (data1.data)
        #np.random.seed(0)
        #print(len(data1))
        #print(len(data1.data))
        
        stop_words1 = []#["a", "about", "above", "above", "across", "after", "afterwards", "again", "against", "all", "almost", "alone", "along", "already", "also","although","always","am","among", "amongst", "amoungst", "amount",  "an", "and", "another", "any","anyhow","anyone","anything","anyway", "anywhere", "are", "around", "as",  "at", "back","be","became", "because","become","becomes", "becoming", "been", "before", "beforehand", "behind", "being", "below", "beside", "besides", "between", "beyond", "bill", "both", "bottom","but", "by", "call", "can", "cannot", "cant", "co", "con", "could", "couldnt", "cry", "de", "describe", "detail", "do", "done", "down", "due", "during", "each", "eg", "eight", "either", "eleven","else", "elsewhere", "empty", "enough", "etc", "even", "ever", "every", "everyone", "everything", "everywhere", "except", "few", "fifteen", "fify", "fill", "find", "fire", "first", "five", "for", "former", "formerly", "forty", "found", "four", "from", "front", "full", "further", "get", "give", "go", "had", "has", "hasnt", "have", "he", "hence", "her", "here", "hereafter", "hereby", "herein", "hereupon", "hers", "herself", "him", "himself", "his", "how", "however", "hundred", "ie", "if", "in", "inc", "indeed", "interest", "into", "is", "it", "its", "itself", "keep", "last", "latter", "latterly", "least", "less", "ltd", "made", "many", "may", "me", "meanwhile", "might", "mill", "mine", "more", "moreover", "most", "mostly", "move", "much", "must", "my", "myself", "name", "namely", "neither", "never", "nevertheless", "next", "nine", "no", "nobody", "none", "noone", "nor", "not", "nothing", "now", "nowhere", "of", "off", "often", "on", "once", "one", "only", "onto", "or", "other", "others", "otherwise", "our", "ours", "ourselves", "out", "over", "own","part", "per", "perhaps", "please", "put", "rather", "re", "same", "see", "seem", "seemed", "seeming", "seems", "serious", "several", "she", "should", "show", "side", "since", "sincere", "six", "sixty", "so", "some", "somehow", "someone", "something", "sometime", "sometimes", "somewhere", "still", "such", "system", "take", "ten", "than", "that", "the", "their", "them", "themselves", "then", "thence", "there", "thereafter", "thereby", "therefore", "therein", "thereupon", "these", "they", "thickv", "thin", "third", "this", "those", "though", "three", "through", "throughout", "thru", "thus", "to", "together", "too", "top", "toward", "towards", "twelve", "twenty", "two", "un", "under", "until", "up", "upon", "us", "very", "via", "was", "we", "well", "were", "what", "whatever", "when", "whence", "whenever", "where", "whereafter", "whereas", "whereby", "wherein", "whereupon", "wherever", "whether", "which", "while", "whither", "who", "whoever", "whole", "whom", "whose", "why", "will", "with", "within", "without", "would", "yet", "you", "your", "yours", "yourself", "yourselves", "the"]
        count_vect = CountVectorizer(stop_words=stop_words1)
        data_freq = count_vect.fit_transform(data1.data)
        #print(data_freq)
        #print(data_freq.shape)
        
        #### Now read the test data
        ####Reading data from test file #####################
        ## Please note that you should not use defined keyword input for variable name !
        
        input1=load_files('C:\Python34\input')
        print (input1)
        
        input_data = input1.data
        print(input_data)
        #################
        
        
        ##### Mapping test data to term frequency. 
        #### Note that you have to pass vocabulary obtained from the train data to the test data 
        #### CountVectorizer.
        count_vect2 = CountVectorizer(vocabulary=count_vect.vocabulary_,stop_words=stop_words1)
        data_freq1 = count_vect2.fit_transform(input_data)
        #print (count_vect.vocabulary_)
        print(data_freq1)
        
        
        ### Use classifiers for models and prediction
        
        
        clf_logR=LogisticRegression()
        ## Cross validation
        '''scores_logR=cross_val_score(clf_logR,data_freq.toarray(),data1.target,cv=10)
        
        print('10-fold CV for each fold using logR:',scores_logR)
        print('10-fold CV average accuracy (logR):',np.mean(scores_logR))'''
        
        ## Build model using whole train data (data_freq) and predict on test data (data_freq1)
        clf_logR.fit(data_freq, data1.target)
        predicted_logR = clf_logR.predict(data_freq1)
        #data1.target_names represents the class names
        print('Prediction using logR:',predicted_logR,data1.target_names[predicted_logR[0]])
        #fo = open("C:\Python34\output.txt",'w')
        #fo.write(re.sub('[^A-Za-z0-9]+', ' ', predicted_logR))
        #fo.close()
        
        
        
        ### Use Naive Bayes Classifier
        clf_nb= GaussianNB()
        '''## Cross validation
        scores_nb=cross_val_score(clf_nb,data_freq.toarray(),data1.target,cv=10)
        print('10-fold CV for each fold using Naive Bayes:',scores_nb)
        print('10-fold CV average accuracy (Naive Bayes):',np.mean(scores_nb))'''
        
        ## Build model using whole train data (data_freq) and predict on test data (data_freq1)
        clf_nb.fit(data_freq.toarray(), data1.target)
        predicted_nb = clf_logR.predict(data_freq1.toarray())
        #data1.target_names represents the class names
        print('Prediction using Naive Bayes:',predicted_nb,data1.target_names[predicted_nb[0]])
        fo = open("C:\Python34\output.txt",'w')
        fo.write(str(predicted_nb))
        fo.close()

        #######################
        
        self.l1 = tk.Label(self, font=v1,bg='#add8e6')
        fo = open("C:\Python34\output.txt", "r")
        k = fo.readline()
        if(k=='[0]'):
            k='negative'
        else:
            k='positive'
        self.l1.config(text=k)
        self.l1.pack(side='left')
        #self.l1.pack_forget()
        
        fo.close()
        
        #self.l1.delete("1.0","end")



        

        
app = SampleApp()
app.mainloop()
