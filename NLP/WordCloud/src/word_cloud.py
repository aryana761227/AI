import os

from bidi.algorithm import get_display
from persian_wordcloud import wordcloud
import matplotlib.pyplot as plt
from arabic_reshaper import arabic_reshaper


f1 = open("../../ProcessedData/label1.txt", 'r', encoding='utf-8')
f1 = f1.read()
cloud = wordcloud.PersianWordCloud(background_color="white").generate(f1)
plt.imshow(cloud)
plt.axis('off')
plt.savefig("../out/1.jpg")

f2 = open("../../ProcessedData/label2.txt", 'r', encoding='utf-8')
f2 = f2.read()
cloud = wordcloud.PersianWordCloud(background_color="white").generate(f2)
plt.imshow(cloud)
plt.axis('off')
plt.savefig("../out/2.jpg")

f1_2 = open("../../ProcessedData/label1.txt", 'r', encoding='utf-8')
f1_2 = f1_2.read()
sub_list = list(f2)
wordcloud.add_stop_words(sub_list)
cloud = wordcloud.PersianWordCloud(background_color="white").generate(f1_2)
plt.imshow(cloud)
plt.axis('off')
plt.savefig("../out/3.jpg")

f2_1 = open("../../ProcessedData/label2.txt", 'r', encoding='utf-8')
f2_1 = f2_1.read()
sub_list = list(f1)
wordcloud.add_stop_words(sub_list)
cloud = wordcloud.PersianWordCloud(background_color="white").generate(f2_1)
plt.imshow(cloud)
plt.axis('off')
plt.savefig("../out/4.jpg")




swf = open("../stopwords.txt", "r", encoding='utf-8')


def split(param):
    li = []
    x = ""
    for i in param:
        if i == '\n' or i == '\ufeff':
            li.append(x)
            x = ""
        else:
            x += i
    return li


# stop_words_list = split(swf.read())
stop_words_list = ['کرد', 'باشگاه', 'لینک', 'خبر', 'باید', 'متن', 'کامل',
                   'هستم', 'دیدار', 'بازی', 'انجام', 'رسمی', 'دقیقه', 'نتیجه',
                   'قرار', 'تمرین', 'مشخص', 'مصاف', 'جلسه', 'ساعت', 'تیم',
                   'فصل', 'استقلال', 'پرسپولیس', 'هواداران']
stop_words = wordcloud.add_stop_words(stop_words_list)

f1_stopword = open("../../ProcessedData/label1.txt", 'r', encoding='utf-8')
f1_stopword = f1_stopword.read()
cloud = wordcloud.PersianWordCloud(background_color="white").generate(f1_stopword)
plt.imshow(cloud)
plt.axis('off')
plt.savefig("../out/5.jpg")


f2_stopword = open("../../ProcessedData/label2.txt", 'r', encoding='utf-8')
f2_stopword = f2_stopword.read()
wordcloud.add_stop_words(stop_words_list)
cloud = wordcloud.PersianWordCloud(background_color="white", stopwords=stop_words).generate(f2_stopword)
plt.imshow(cloud)
plt.axis('off')
plt.savefig("../out/6.jpg")

f1_2_stopword = open("../../ProcessedData/label1.txt", 'r', encoding='utf-8')
f1_2_stopword = f1_2_stopword.read()
wordcloud.add_stop_words(stop_words_list)
sub_list = list(f2_stopword)
wordcloud.add_stop_words(sub_list)
cloud = wordcloud.PersianWordCloud(background_color="white", stopwords=stop_words).generate(f1_2_stopword)
plt.imshow(cloud)
plt.axis('off')
plt.savefig("../out/7.jpg")

f2_1_stopword = open("../../ProcessedData/label2.txt", 'r', encoding='utf-8')
f2_1_stopword = f2_1_stopword.read()
wordcloud.add_stop_words(stop_words_list)
sub_list = list(f1_stopword)
wordcloud.add_stop_words(sub_list)
cloud = wordcloud.PersianWordCloud(background_color="white", stopwords=stop_words).generate(f2_1_stopword)
plt.imshow(cloud)
plt.axis('off')
plt.savefig("../out/8.jpg")
