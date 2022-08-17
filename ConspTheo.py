from encodings import utf_8


txtfile=open("input_text", "r", encoding="utf_8")
datazero=txtfile.read()
data=datazero.casefold()
data1=data.replace(',', '')
data2=data1.replace('.', '')
data3=data2.replace(':', '')
data4=data3.replace("'", '')
data5=data4.replace('?', '')
data6=data5.replace('!', '')
#print(data6)
dataList=data6.split()
#print(dataList)
def remove_words(list1, stop_words):
    for word in list(list1):
        if word in stop_words:
            list1.remove(word)
    return list1
stop_word_str=open('stop_words.txt', 'r', encoding='utf_8')
stop_word=stop_word_str.read()
stop_wordList=stop_word.split()
#print(stop_wordList)
pure_txt=remove_words(dataList, stop_wordList)
print(pure_txt)
