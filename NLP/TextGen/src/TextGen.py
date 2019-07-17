import random


def header_finder(words_list, header):
    gram_with_specific_header = []
    for i in words_list:
        if i[0] == header:
            gram_with_specific_header.append(i)
    return gram_with_specific_header


n = int(input("please enter number of generating sentence from each model"))
classes = [1, 2]
grams = [1, 2, 3]
unigram_sentence_size = int(input("please enter the size of unigram sentences you want"))
for n_gram in grams:
    list_of_grams = []
    for group in classes:
        f = open('../../Model/label{}.{}gram.lm'.format(group, n_gram), 'r', encoding='utf-8')
        for line in f.readlines():
            list_of_grams.append(line.split("|")[:n_gram])
        generated_texts = []
        if n_gram == 1:
            for _ in range(n):
                temp = []
                for _ in range(unigram_sentence_size):
                    temp.append(random.choice(list_of_grams))
                generated_texts.append(temp)
        else:
            while len(generated_texts) != n:
                temp = []
                temp_headers = header_finder(list_of_grams, '<s>')
                temp.append(random.choice(temp_headers))
                # print(temp)
                while len(temp_headers) != 0:
                    if temp[-1][-1] == '</s>':
                        break
                    temp.append(random.choice(temp_headers))
                    temp_headers = header_finder(list_of_grams, temp[-1][-1])
                if temp[-1][-1] == '</s>':
                    generated_texts.append(temp)
        f.close()
        file = open("../label{}.{}gram.gen".format(group, n_gram), 'w+', encoding='utf-8')
        for sentence in generated_texts:
            for gram in sentence:
                for word in gram:
                    if n_gram == 1:
                        file.write(word + " ")
                    else:
                        if sentence.index(gram) == len(sentence) - 1:
                            file.write(word + " ")
                        else:
                            if gram.index(word) == len(gram) - 1:
                                continue
                            else:
                                file.write(word + " ")
            file.write("\n")
