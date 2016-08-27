import nltk
#import nltk.corpus
#import nltk.tag
#from nltk import pos_tag
from nltk.tokenize import TweetTokenizer
from nltk.corpus import stopwords
from nltk.stem.wordnet import WordNetLemmatizer
from string import punctuation
import csv

csv_file = open('second.csv')
reader = csv.reader(csv_file,delimiter =',')

result_file = open("output_second.csv",'w')
wr = csv.writer(result_file,delimiter = ',')

#lem = WordNetLemmatizer()

for row in reader:
    label = list(row[0])
    data = row[2]
    data_lower = data.lower() # To do the stop words removal
    tknzr = TweetTokenizer(strip_handles = True,reduce_len = True)
    word_list = tknzr.tokenize(data_lower)
    word_save = list(word_list)
    
    remove_value  = ['0','1','2','3','4','5','6','7','8','9','#','http','https']

    emotion_happy = [':-)',':)','(:','(-:',':-D',':D','X-D', 'XD', 'xD','<3', ':\*']
    emotion_sad = [':-(', ':(', '(:', '(-:',':,(', ':\'(', ':"(', ':((']

    neg_word = ['no','nor','not','never','without','against']
    punct_exclaim = ['!', '¡']
    punct_quest = ['?', '¿']
    
    n =0

    emot_hap = 0
    emot_sad = 0
    punct_excl = 0
    punct_ques = 0

    neg =0
    
    for word in word_list:
        l = 0

        if word in list(neg_word):
            neg =1
        if word in stopwords.words('english'):
            word_save.remove(word);
            l = 1
            
        for p in list(remove_value):
           if p in word:
               word_save.remove(word);
               l =1
               break
        
        if l==0:    
            for e_1 in list(emotion_happy):
                if e_1 in word:
                    word_save.remove(word)
                    emot_hap=+1
                    l = 1
                    break
        if l == 0:
            for e_2 in list(emotion_sad):
                if e_2 in word:
                    word_save.remove(word)
                    emot_sad+=1
                    l = 1
                    break
        if l ==0:
            for p_2 in list(punct_quest):
                if p_2 in word:
                    word_save.remove(word)
                    punct_ques+=1
                    l = 1
                    break
        if l ==0:
            for p_1 in list(punct_exclaim):
                if p_1 in word:
                    word_save.remove(word)
                    punct_excl+=1
                    l =1
                    break
        if l==0:
            for pun in list(punctuation):
                if pun in word and l==0:
                    word_save.remove(word);
                    break
        n=n+1
        
    eh_list = [emot_hap]
    es_list = [emot_sad]
    ee_list = [punct_excl]
    eq_list = [punct_ques]
   
    n = [neg]
    word_buffer= label+n+eh_list+es_list+ee_list+eq_list+word_save
    wr.writerow(word_buffer)
result_file.close()
csv_file.close()



