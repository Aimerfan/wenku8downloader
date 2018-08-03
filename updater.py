from bs4 import BeautifulSoup
import logging
import config
import csv
import os


def writelist(books):
    with open('booklist.csv', 'w', encoding='utf-8', errors='ignore', newline='') as csvfile:
        csv.writer(csvfile).writerows(books)


def update(start=1, end=10000):
    error = 0
    books = []

    for id in range(start, end):
        # 抓頁面
        page = config.get_web_page(config.book_path + str(id) + config.charset, encoding='big5')

        # 連線正常，判斷內容
        page = BeautifulSoup(page.text, 'html.parser')
        if page.find('title').text == '出現錯誤':
            error += 1
            logging.warning('book:{id} lost.'.format(id=id))
            # 連續抓空五次就當成結束
            if error == 5:
                print('Fetch over.')
                break
        else:
            for i in range(id-error, id):
                books.append([str(id)])
            error = 0
            table = page.find('table')
            attr = [str(id), table.find('b').text.replace('\x00', '')]
            detail = table.find_all('td', width='20%')
            for i in detail:
                # split('\x00') is execption process
                attr.append(i.text.split('︰')[1].split('\x00')[0])

            books.append(attr)
            print('book:{id} update success.'.format(id=id))

        id += 1

    print('Online Update book id {0}-{1} Success.'.format(start, end-1))
    return books


def loadlist(checknew=False, force=False):
    if force or not os.path.isfile('booklist.csv'):
        books = update()
        writelist(books)
    else:
        with open('booklist.csv', 'r', encoding='utf-8') as readcsv:
            books = [i for i in csv.reader(readcsv)]
            if checknew:
                news = update(len(books) + 1, 20)
                books.extend(news)
                writelist(books)
    return books


if __name__ == "__main__":
    update()

