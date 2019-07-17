import random
import threading
import hazm

file_1 = open("../../ProcessedData/label1.txt", "r", encoding="utf-8")
file_2 = open("../../ProcessedData/label2.txt", "r", encoding="utf-8")
stopwords = open('stopwords.txt', 'r', encoding='utf-8')
stopwords_list = ['\n', '\t', ' ']
for word in stopwords.readlines():
    stopwords_list.append(hazm.word_tokenize(word)[0])


test = open("../train.txt", "w+", encoding="utf-8")
train = open("../test.txt", "w+", encoding="utf-8")


def text_writer(class_name, file, stopwords_list):
    for line in file.readlines():
        if line == '\n':
            continue
        file_usage = None
        if random.random() < 0.2:
            file_usage = test
        else:
            file_usage = train
        file_usage.write(class_name + ' ')
        for x in hazm.word_tokenize(line):
            if x not in stopwords_list:
                file_usage.write(x + ' ')
        file_usage.write("\n")


try:
    t_esteghlal = threading.Thread(target=text_writer, args=("Esteghlal", file_1, stopwords_list))
    t_perspolis = threading.Thread(target=text_writer, args=("Perspolis", file_2, stopwords_list))
    t_esteghlal.start()
    t_perspolis.start()
    t_esteghlal.join()
    t_perspolis.join()
    test.close()
    train.close()
except:
    pass
