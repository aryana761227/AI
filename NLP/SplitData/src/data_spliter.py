import random

f_label1 = open('../../ProcessedData/label1.txt', 'r', encoding='utf-8')
label1 = f_label1.readlines()
train_label1 = open('../train/label1.txt', 'w+', encoding='utf-8')
test_label1 = open('../test/label1.txt', 'w+', encoding='utf-8')
for i1 in label1:
    if 0 <= random.random() <= 0.2:
        test_label1.write(i1)
    else:
        train_label1.write(i1)

f_label2 = open('../../ProcessedData/label2.txt', 'r', encoding='utf-8')
label2 = f_label2.readlines()
train_label2 = open('../train/label2.txt', 'w+', encoding='utf-8')
test_label2 = open('../test/label2.txt', 'w+', encoding='utf-8')
for i2 in label2:
    if 0 <= random.random() <= 0.2:
        test_label2.write(i2)
    else:
        train_label2.write(i2)