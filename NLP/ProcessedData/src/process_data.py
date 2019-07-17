import hazm as Hazm1
import hazm as Hazm2


def pre_process_data():
    f_1 = open("../../Data/label1.txt", "r", encoding="utf-8")
    f1 =f_1.readlines()
    f1_preproc = open("../label1.txt", "w+", encoding="utf-8")
    for j in f1:
        normalized_f1 = Hazm1.Normalizer().normalize(j)
        tokenized_f1 = Hazm1.word_tokenize(normalized_f1)
        for i in tokenized_f1:
            f1_preproc.write(i)
            f1_preproc.write(' ')
        f1_preproc.write('\n')

    f_2 = open("../../Data/label2.txt", "r", encoding="utf-8")
    f2 = f_2.readlines()
    f2_preproc = open("../label2.txt", "w+", encoding="utf-8")
    for j in f2:
        normalized_f2 = Hazm2.Normalizer().normalize(j)
        tokenized_f2 = Hazm2.word_tokenize(normalized_f2)
        for i in tokenized_f2:
            f2_preproc.write(i)
            f2_preproc.write(' ')
        f2_preproc.write('\n')

if __name__=='__main__':
    pre_process_data()