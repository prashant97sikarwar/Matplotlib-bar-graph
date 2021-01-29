import string
from matplotlib import pyplot as plt

plt.style.use('fivethirtyeight')   #Ploting style 

file = open("assignment2.txt", "r")  #file opening in reading mode

word_dict = dict()
total_words = 0
for line in file:
    line = line.strip()    
    line = line.lower()
    line = line.translate(line.maketrans("", "", string.punctuation))    # cleaning of data in file
    line = line.split(" ")
    for word in line:
        total_words += 1
        if word not in word_dict:
            word_dict[word] = 1
        else:
            word_dict[word] += 1

max_freq_of_word = -1

for word in word_dict:                      # find word with maximum frequency
    if word_dict[word] > max_freq_of_word:
        max_freq_of_word = word_dict[word]
        word_with_max_freq = word

print("total number of words in the text file is {}".format(total_words))
print("word with the max frequency is '{}' with frequency '{}'".format(word_with_max_freq,max_freq_of_word))

word_list = [x for x in sorted(word_dict,key = lambda x : word_dict[x],reverse=True)]
freq_list = [x for x in sorted(word_dict.values(),reverse=True)]

plt.rcParams['xtick.labelsize']=5    #fixing size of words text
plt.rcParams['ytick.labelsize']=10   #fixing size of frequency text
plt.rcParams['xtick.color'] = '#444444'   #color of words on x axis

plt.title('Word frequency in File')  #title of plot
plt.xlabel('Words',fontsize=15)     
plt.ylabel('Frequency',fontsize=15)
plt.xticks(rotation=90)

plt.bar(word_list,freq_list,color='#900C3F',edgecolor='black',label="freq count",linewidth=0.3)

plt.show()