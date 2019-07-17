from hazm import word_tokenize


# loading data
def read_data(group, test_flag):
    if test_flag == 1:
        file = open("../test/in.1gram", 'r', encoding='utf-8')
    else:
        file = open("../../SplitData/train/label{}.txt".format(group), 'r', encoding='utf-8')
    sent_list = []
    for i in file.readlines():
        words_list = word_tokenize(i)
        words_list.insert(0, '<s>')
        words_list.append('</s>')
        sent = ''
        for word in words_list:
            sent += word
            sent += ' '
        sent_list.append(sent[:-1])
    return sent_list


# language models
def uni_gram(text_list):
    words_count = 0
    uni_words_counter = {'<UNK>' : 0}
    word_probability = {}
    for sentence in text_list:
        words = sentence.split(' ')
        for word in words:
            if word == '<s>' or word == '</s>':
                pass
            else:
                words_count += 1
                if word in uni_words_counter:
                    uni_words_counter[word] += 1
                else:
                    uni_words_counter[word] = 1
    for i in uni_words_counter:
        word_probability[i] = (uni_words_counter[i] + 1) / (words_count + len(uni_words_counter))
    return word_probability


def bi_gram(text_list):
    bi_words_counter = {('<UNK>', '<UNK>') : 0}
    uni_words_counter = {'<UNK>' : 0}
    word_probability = {}

    for sentence in text_list:
        words = sentence.split(' ')
        for i in range(len(words)):
            if i < len(words) - 1 :
                if (words[i], words[i+1]) not in bi_words_counter:
                    bi_words_counter[(words[i], words[i+1])] = 1
                else:
                    bi_words_counter[(words[i], words[i+1])] += 1

            if i < len(words):
                if words[i] in uni_words_counter:
                    uni_words_counter[words[i]] += 1
                else:
                    uni_words_counter[words[i]] = 1

    for i in bi_words_counter:
        word_probability['{}|{}'.format(i[0], i[1])] = (bi_words_counter[i] + 1) / (
        uni_words_counter[i[0]] + len(uni_words_counter) - 2)
    return word_probability


def tri_gram(text_list):
    tri_words_counter = {('<UNK>', '<UNK>', '<UNK>') : 0}
    bi_words_counter = {('<UNK>', '<UNK>') : 0}
    uni_words_counter = {'<UNK>': 0}
    word_probability = {}
    for sentence in text_list:
        words = sentence.split(' ')
        for i in range(len(words)):

            if i < len(words) - 2:
                if (words[i], words[i + 1], words[i + 2]) not in tri_words_counter:
                    tri_words_counter[(words[i], words[i + 1], words[i + 2])] = 1
                else:
                    tri_words_counter[(words[i], words[i + 1], words[i + 2])] += 1
            if i < len(words) - 1:
                if (words[i], words[i+1]) not in bi_words_counter:
                    bi_words_counter[(words[i], words[i+1])] = 1
                else:
                    bi_words_counter[(words[i], words[i+1])] += 1
            if i < len(words):
                if words[i] in uni_words_counter:
                    uni_words_counter[words[i]] += 1
                else:
                    uni_words_counter[words[i]] = 1

        for i in tri_words_counter:
            word_probability['{}|{}|{}'.format(i[0], i[1], i[2])] = (tri_words_counter[i] + 1) / (
            bi_words_counter[(i[0], i[1])] + len(uni_words_counter) - 2)
    return word_probability


# save data
def store_data(group, n_gram, test_flag=0):
    if test_flag == 1:
        file = open("../test/{}.{}gram.lm".format(group, n_gram), 'w+', encoding='utf-8')
    else:
        file = open("../label{}.{}gram.lm".format(group, n_gram), 'w+', encoding='utf-8')
    text_list = read_data(group, test_flag)
    if n_gram == 1:
        prob_dic = uni_gram(text_list)
        for i in prob_dic :
            file.write(i)
            file.write('|')
            file.write(str(prob_dic[i]))
            file.write('\n')
    elif n_gram == 2:
        prob_dic = bi_gram(text_list)
        for i in prob_dic:
            file.write(i)
            file.write('|')
            file.write(str(prob_dic[i]))
            file.write('\n')
    elif n_gram == 3:
        prob_dic = tri_gram(text_list)
        for i in prob_dic:
            file.write(i)
            file.write('|')
            file.write(str(prob_dic[i]))
            file.write('\n')


if __name__  == '__main__':
    test_flag = int(input("if you want test this code write 1 else for data processing of this project write 0 then press enter"))
    if test_flag == 1:
        for n_gram in [1, 2, 3]:
            store_data('out', n_gram, test_flag=test_flag)
    else :
        for group in [1, 2]:
            for n_gram in [1, 2, 3]:
                store_data(group, n_gram)