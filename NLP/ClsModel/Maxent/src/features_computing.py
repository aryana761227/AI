import hazm

tokens = set()
for types in ["train", "test"]:

    file = open("../../../ClsData/{}.txt".format(types), 'r', encoding='utf-8')
    file_input = open('../input.{}.txt'.format(types), 'w+', encoding='utf-8')
    for line in file.readlines():
        tag_sentence = hazm.word_tokenize(line)
        sentence = tag_sentence[1:]
        for word in sentence:
            if types == 'train':
                tokens.add(word)
            if types == 'test' and word not in tokens:
                tokens.add('<Unk>')
    file.close()
    file = open("../../../ClsData/{}.txt".format(types), 'r', encoding='utf-8')
    for line in file.readlines():
        words_in_line_count = {}
        for i in tokens:
            words_in_line_count[i] = 0
        tag_sentence = hazm.word_tokenize(line)
        tag = tag_sentence[0]
        sentence = tag_sentence[1:]
        file_input.write(tag + ' ')
        for word in sentence:
            if word in tokens:
                words_in_line_count[word] += 1
            else:
                words_in_line_count['<Unk>'] += 1
        for token in words_in_line_count:
            file_input.write(token + ':' + str(words_in_line_count[token]) + ' ')
        file_input.write('\n')
    file_input.close()
