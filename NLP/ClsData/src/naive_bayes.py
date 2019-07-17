import hazm
import math

f1 = int(input("Do you want test case data or my project data"))
f2 = int(input("do you want test the data or just train(believe me train is useless"))
test_mode = False
test_case = False

if f1:
    test_case = True
if f2:
    test_mode = True

training_results = {}
classes = ['Esteghlal', "Perspolis"]


def train(classes, test_case=False):
    train_results = {}
    if test_case:
        file = open('../TestCase/train.txt', 'r', encoding='utf-8')
        classes = ["c1", "c2"]
    else:
        file = open('../train.txt', 'r', encoding='utf-8')
    esteghlal_tokens_count = {}
    perspolis_tokens_count = {}
    sentences_count = 0
    esteghlal_counts = 0
    perspolis_counts = 0
    for line in file.readlines():
        sentences_count += 1
        tag_sentence = hazm.word_tokenize(line)
        tag = tag_sentence[0]
        sentence = tag_sentence[1:]
        if tag == classes[0]:
            esteghlal_counts += 1
            for word in sentence:
                if word not in esteghlal_tokens_count:
                    esteghlal_tokens_count[word] = 1
                else:
                    esteghlal_tokens_count[word] += 1
        elif tag == classes[1]:
            perspolis_counts += 1
            for word in sentence:
                if word not in perspolis_tokens_count:
                    perspolis_tokens_count[word] = 1
                else:
                    perspolis_tokens_count[word] += 1

    esteghlal_tokens_prob = {}
    perspolis_tokens_prob = {}
    for token in esteghlal_tokens_count:
        # laplace smoothing(unknown token is one of the tokens so V = number of tokens + 1->unknown token)
        esteghlal_tokens_prob[token] = (esteghlal_tokens_count[token] + 1) / (len(esteghlal_tokens_count) + 1
                                                                              + sum(esteghlal_tokens_count.values()))
    for token in perspolis_tokens_count:
        perspolis_tokens_prob[token] = (perspolis_tokens_count[token] + 1) / (len(perspolis_tokens_count) + 1
                                                                               + sum(perspolis_tokens_count.values()))
    esteghlal_tokens_prob['<Unk>'] = 1 / (len(esteghlal_tokens_count) + 1 + sum(esteghlal_tokens_count.values()))
    perspolis_tokens_prob['<Unk>'] = 1 / (len(perspolis_tokens_count) + 1 + sum(perspolis_tokens_count.values()))
    esteghlal_prob = esteghlal_counts / sentences_count
    perspolis_prob = perspolis_counts / sentences_count
    train_results[classes[0]] = (esteghlal_prob, esteghlal_tokens_prob)
    train_results[classes[1]] = (perspolis_prob, perspolis_tokens_prob)
    return train_results


def test(train_results, classes, test_case=False):
    if test_case:
        file = open("../TestCase/test.txt", 'r', encoding='utf-8')
        output = open("../TestCase/my-output.txt", 'w+', encoding='utf-8')
        output_2 = open("../../ClsModel/NaiveBayes/TestCase.output.txt", 'w+', encoding='utf-8')
        classes = ["c1", "c2"]
    else:
        file = open("../test.txt", 'r', encoding='utf-8')
        output = open("../output.txt", 'w+', encoding='utf-8')
        output_2 = open("../../ClsModel/NaiveBayes/Test.output.txt", 'w+', encoding='utf-8')
    for line in file.readlines():
        tag_sentence = hazm.word_tokenize(line)
        sentence = tag_sentence[1:]
        for c in classes:
            output.write(c + " ")
            output_2.write(c + " ")
            p = 0
            for word in sentence:
                if word in train_results[c][1]:
                    p += math.log10(train_results[c][1][word])
                else:
                    p += math.log10(train_results[c][1]['<Unk>'])
            p += math.log10(train_results[c][0])
            output.write(str(p) + " ")
            output_2.write(str(p) + " ")
        output.write("\n")
        output_2.write("\n")


if __name__ == '__main__':
    if test_case:
        if test_mode:
            train_case = train(classes, test_case=True)
            test(train_case, classes, test_case=True)
        else:
            train(classes)
    else:
        if test_mode:
            train_data = train(classes)
            test(train_data, classes)
        else:
            train(classes)