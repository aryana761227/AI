from hazm import word_tokenize


def compute_perplexity(sentence, model):
    words_list = word_tokenize(sentence)
    perplexity = 1
    if len(words_list) != 0:
        if model[0] == 1:
            if len(words_list) != 0:
                for word in words_list:
                    if word in model[1]:
                        perplexity *= 1 / (model[1][word])
                    else:
                        perplexity *= 1 / (model[1]['<UNK>'])

        elif model[0] == 2:
            words_list.insert(0, '<s>')
            words_list.append('</s>')
            for i in range(len(words_list)):
                if i < len(words_list) - 1:
                    if (words_list[i], words_list[i + 1]) in model[1]:
                        perplexity *= 1 / (model[1][(words_list[i], words_list[i + 1])])
                    else:
                        perplexity *= 1 / (model[1][('<UNK>', '<UNK>')])


        elif model[0] == 3:
            words_list.insert(0, '<s>')
            words_list.append('</s>')
            for i in range(len(words_list)):
                if i < len(words_list) - 2:
                    if (words_list[i], words_list[i + 1], words_list[i + 2]) in model[1]:
                        perplexity *= 1 / (model[1][(words_list[i], words_list[i + 1], words_list[i + 2])])
                    else:
                        perplexity *= 1 / (model[1][('<UNK>', '<UNK>', '<UNK>')])

        perplexity **= 1 / (len(words_list))
    return perplexity


def model_loading(group, n_gram):
    model_dict = {}
    file = open('../../Model/label{}.{}gram.lm'.format(group, n_gram), 'r', encoding='utf-8')
    for line in file.readlines():
        word_list = line.split('|')[:-1]
        if len(word_list) == 1:
            gram = word_list[0]
        else:
            gram = tuple(word_list)

        probability = float(line.split('|')[-1])
        model_dict[gram] = probability
    return n_gram, model_dict


def context_loading(group, test=False):
    if test is True:
        folder = 'test'
    else:
        folder = 'train'
    file = open('../../SplitData/{}/label{}.txt'.format(folder, group), 'r', encoding='utf-8')
    return file


if __name__ == '__main__':
    for n_gram in [1, 2, 3]:
        for test_flag in [True, False]:
            for group in [1, 2]:
                if test_flag is True:
                    root = 'test'
                else:
                    root = 'train'
                out = open('../{}.label{}.{}gram.ppx'.format(root, group, n_gram), 'w+', encoding='utf-8')
                file = context_loading(group, test_flag)
                model = model_loading(group, n_gram)
                sum = 0
                lines_count = 0
                for line in file.readlines():
                    sum += compute_perplexity(line, model)
                    lines_count += 1
                average_perplexity = sum / lines_count
                out.write('average complexity:' + str(average_perplexity))
                out.close()
                file.close()