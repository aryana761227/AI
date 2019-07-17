import hazm

flag = int(input("Do you want evaluate the TestCase?"))
if flag == 1:
    test_case = True
else:
    test_case = False
if test_case:
    classes = ["c1", "c2"]
    classified_file = open('../TestCase.output.txt', "r", encoding='utf-8')
    tagged_file = open('../../../ClsData/TestCase/test.txt', 'r', encoding='utf-8')
else:
    classes = ["Esteghlal", "Perspolis"]
    classified_file = open('../Test.output.txt', "r", encoding='utf-8')
    tagged_file = open('../../../ClsData/test.txt', 'r', encoding='utf-8')

classified_list = []
tagged_list = []
sentences = []
for line in tagged_file.readlines():
    x = line.split()
    tagged_list.append(x[0])
for line in classified_file.readlines():
    probs = {}
    x = line.split()
    probs[x[0]] = float(x[1])
    probs[x[2]] = float(x[3])
    classified_list.append(max(probs, key=probs.get))

tp_esteghlal = 0
tn_esteghlal = 0
fp_esteghlal = 0
fn_esteghlal = 0
tp_perspolis = 0
tn_perspolis = 0
fp_perspolis = 0
fn_perspolis = 0
if not test_case:
    file_tp_esteghlal = open("../groups_samples/tp-esteghlal.txt", "w+", encoding='utf-8')
    file_tn_esteghlal = open("../groups_samples/tn-esteghlal.txt", "w+", encoding='utf-8')
    file_fp_esteghlal = open("../groups_samples/fp-esteghlal.txt", "w+", encoding='utf-8')
    file_fn_esteghlal = open("../groups_samples/fn-esteghlal.txt", "w+", encoding='utf-8')
    file_tp_perspolis = open("../groups_samples/tp-perspolis.txt", "w+", encoding='utf-8')
    file_tn_perspolis = open("../groups_samples/tn-perspolis.txt", "w+", encoding='utf-8')
    file_fp_perspolis = open("../groups_samples/fp-perspolis.txt", "w+", encoding='utf-8')
    file_fn_perspolis = open("../groups_samples/fn-perspolis.txt", "w+", encoding='utf-8')

tagged_file.close()
tagged_file = open('../../../ClsData/test.txt', 'r', encoding='utf-8')
sent = tagged_file.readlines()
for i in range(len(classified_list)):
    if classified_list[i] == classes[0]:
        if classified_list[i] == tagged_list[i]:
            tp_esteghlal += 1
            tn_perspolis += 1
            if not test_case:
                x = hazm.word_tokenize(sent[i])[1:]
                for k in x:
                    file_tp_esteghlal.write(k + ' ')
                    file_tn_perspolis.write(k + ' ')
                file_tp_esteghlal.write('\n')
                file_tn_perspolis.write('\n')
        else:
            fp_esteghlal += 1
            fn_perspolis += 1
            if not test_case:
                x = hazm.word_tokenize(sent[i])[1:]
                for k in x:
                    file_fp_esteghlal.write(k + ' ')
                    file_fn_perspolis.write(k + ' ')
                file_fp_esteghlal.write('\n')
                file_fn_perspolis.write('\n')
    if classified_list[i] == classes[1]:
        if classified_list[i] == tagged_list[i]:
            tn_esteghlal += 1
            tp_perspolis += 1
            if not test_case:
                x = hazm.word_tokenize(sent[i])[1:]
                for k in x:
                    file_tn_esteghlal.write(k + ' ')
                    file_tp_perspolis.write(k + ' ')
                file_tn_esteghlal.write('\n')
                file_tp_perspolis.write('\n')
        else:
            fn_esteghlal += 1
            fp_perspolis += 1
            if not test_case:
                x = hazm.word_tokenize(sent[i])[1:]
                for k in x:
                    file_fn_esteghlal.write(k + ' ')
                    file_fp_perspolis.write(k + ' ')
                file_fn_esteghlal.write('\n')
                file_fp_perspolis.write('\n')

accuracy = (tp_esteghlal + tn_esteghlal)/(tp_esteghlal + tn_esteghlal + fp_esteghlal + fn_esteghlal)
esteghlal_precision = tp_esteghlal / (tp_esteghlal + fp_esteghlal)
esteghlal_recall = tp_esteghlal / (tp_esteghlal + fn_esteghlal)
esteghlal_f1_measure = (2 * esteghlal_precision * esteghlal_recall) / (esteghlal_precision + esteghlal_recall)
perspolis_precision = tp_perspolis / (tp_perspolis + fp_perspolis)
perspolis_recall = tp_perspolis / (tp_perspolis + fn_perspolis)
perspolis_f1_measure = (2 * perspolis_precision * perspolis_recall) / (perspolis_precision + perspolis_recall)
if test_case:
    report = open("../TestCase.report.txt", 'w+', encoding='utf-8')
else:
    report = open("../Test.report.txt", 'w+', encoding='utf-8')

report.write("Accuracy : " + str(accuracy))
report.write("\n")
report.write("{} : \n".format(classes[0]))
report.write("Precision : " + str(esteghlal_precision))
report.write("\n")
report.write("Recall : " + str(esteghlal_recall))
report.write("\n")
report.write("F1_measure : " + str(esteghlal_f1_measure))
report.write("\n")
report.write("{} : \n".format(classes[1]))
report.write("Precision : " + str(perspolis_precision))
report.write("\n")
report.write("Recall : " + str(perspolis_recall))
report.write("\n")
report.write("F1_measure : " + str(perspolis_f1_measure))
