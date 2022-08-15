from encodings import utf_8


txtfile=open("C:/Users/No Name/OneDrive/Desktop/Projects/Ljotic.txt", "r", encoding="utf_8")
datazero=txtfile.read()
data=datazero.casefold()
data1=data.replace(',', '')
data2=data1.replace('.', '')
data3=data2.replace(':', '')
data4=data3.replace("'", '')
data5=data4.replace('?', '')
data6=data5.replace('!', '')
print(data6)
dataList=data6.split()
print(dataList)
def remove_words(list1, stop_words):
    for word in list(list1):
        if word in stop_words:
            list1.remove(word)
    return list1
stop_wordsList=['i', 'do', 'o', 'nas', 'to', 'a', 'kao', 'se', 'će', 'ako', 'je', 'da', 'bi', 'na', 'od', 'smo', 'po', 'li', 'u', 'ka', 'taj', 'sa', 's', 'onaj', 'za', 'mi', 'ko']
print(remove_words(dataList, stop_wordsList))
print(len(stop_wordsList))