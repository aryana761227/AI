from bs4 import BeautifulSoup
import csv
import io


def scrapper(page, file_name='scrape'):
    tweets_list = []
    global soup
    ban_list1 = list('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.#$!@&^*%~`\\/…')
    ban_list2 = list('\n\t()[]}{\"\'-+=_;:?><’,|')

    soup = BeautifulSoup(page, "html.parser")
    tweets = soup.findAll('div', attrs={'class': 'tweet'})
    for tweet in tweets:
        content = tweet.find('div', attrs={'class', 'content'})
        container = content.find('div', attrs={'class': 'js-tweet-text-container'})
        paragraph = container.find('p')
        x = ""
        for i in paragraph.text:
            if i in ban_list1:
                pass
            elif i in ban_list2:
                x += ' '
            else:
                x += i
        tweets_list.append(x)

    result_writer(tweets_list, file_name)


def result_writer(tweets_list, file_name):
    file_out = "../{}.txt".format(file_name)

    with io.open(file_out, "w", encoding="utf-8") as csvfile:

        writer = csv.writer(csvfile, lineterminator='\n', delimiter=',', quotechar='"')

        for i in tweets_list:
            if len(i) > 0:
                newrow = i,
                writer.writerow(newrow)
            else:
                pass

# main
if __name__ == "__main__":
    esteghlal_page = open("../../RawData/esteghlal_page.html", "r", encoding='utf-8')
    scrapper(esteghlal_page, file_name='label1')
    perspolis_page = open("../../RawData/perspolis_page.html", "r", encoding='utf-8')
    scrapper(perspolis_page, file_name='label2')