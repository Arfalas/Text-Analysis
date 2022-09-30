from encodings import utf_8

'''
The main idea behind the code was to analyse two batches of textual data in order to spot similiarities and map
those parts of the text that are copied from the older text to the newer. A comprehensive list removes stop-words,
and the rest of the text is marked in bold in a separate HTML file. 
'''
import time
start_time=time.time()
# opening the .txt file and removing interpunction signs
txtfile=open("C:/Users/No Name/OneDrive/Desktop/Projects/Ljotic.txt", "r", encoding="utf_8")
datazero=txtfile.read()
data=datazero.casefold()
data1=data.replace(',', '')
data2=data1.replace('.', '')
data3=data2.replace(':', '')
data4=data3.replace("'", '')
data5=data4.replace('?', '')
data6=data5.replace('!', '')
data7=data6.replace('"', '')
data8=data7.replace('-', '')
#print(data6)
dataList=data8.split()
#print(dataList)

# removing stop-words from a 1st list
def Remove_words(list1, stop_words):
    for word in list(list1):
        if word in stop_words:
            list1.remove(word)
    return list1
stop_word_str=open('C:/Users/No Name/OneDrive/Desktop/Projects/Stop Words BCS Final.txt', 'r', encoding='utf_8')
stop_word=stop_word_str.read()
stop_wordList=stop_word.split()
#print(stop_wordList)
pure_txt=Remove_words(dataList, stop_wordList)
#print(pure_txt)

# creating another list without stop-words for the 2nd text - replicating the above process
txtfile_1=open("C:/Users/No Name/OneDrive/Desktop/Projects/Protocols.txt", "r", encoding="utf_8")
datazero_1=txtfile_1.read()
data_1=datazero_1.casefold()
data1_1=data_1.replace(',', '')
data2_1=data1_1.replace('.', '')
data3_1=data2_1.replace(':', '')
data4_1=data3_1.replace("'", '')
data5_1=data4_1.replace('?', '')
data6_1=data5_1.replace('!', '')
data7_1=data6_1.replace('"', '')
data8_1=data7_1.replace('-', '')
#print(data6_1)
dataList_1=data8_1.split()
#print(dataList_1)
def remove_words_1(list1_1, stop_words_1):
    for word_1 in list(list1_1):
        if word_1 in stop_words_1:
            list1_1.remove(word_1)
    return list1_1
pure_txt_1=remove_words_1(dataList_1, stop_wordList)
#print(pure_txt_1)

# see word frequency from text B

import collections
word_frequency=collections.Counter(pure_txt_1)
print(word_frequency)

# marking the words that repeat in both lists with <strong> element for HTML use
import json
markup = lambda e : '<strong>%s</strong>'%e if e in list(set(pure_txt_1)&set(pure_txt)) else str(e)
 
with open('C:/Users/No Name/OneDrive/Desktop/Projects/vezba.txt','w', encoding="utf_8") as fio:
    json.dump([markup(e) for e in pure_txt], fio)

# converting the analysed list into string and clearing up symbols
txtfile_12=open("C:/Users/No Name/OneDrive/Desktop/Projects/vezba.txt", "r", encoding="utf_8")
datazero_12=txtfile_12.read()
data_12=datazero_12.replace('"', '')
data_13=data_12.replace(',', '')
with open("C:/Users/No Name/OneDrive/Desktop/Projects/html.txt", "w", encoding="utf_8") as f:
    f.write(data_13)

end_time=time.time()
elapsed_time=end_time - start_time
print('App execution time: ', elapsed_time)
