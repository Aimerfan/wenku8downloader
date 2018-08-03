from bs4 import BeautifulSoup
import config
import os


class wenkuSuit:
    def __init__(self, id):
        self.id = id
        self.title = ''

    def get_list(self):
        bookpath = config.book_path + str(self.id) + config.charset
        page = config.get_web_page(bookpath, encoding='big5')
        page = BeautifulSoup(page.text, 'html.parser')
        indexurl = page.find('a', string='小說目錄').get('href')

        books = []
        page = config.get_web_page(indexurl + config.charset, encoding='big5')
        table = BeautifulSoup(page.text, 'html.parser')
        self.title = table.find('div', id='title').text.strip()
        table = table.find('table').find_all('td')
        for td in table:
            a = td.find('a')
            if td.get('colspan') == '4':
                books.append([td.text.strip()])
            elif a:
                books[-1].append((a.text.strip(), a.get('href')))
            else:
                pass

        return books

    def print_list(self):
        booklist = self.get_list()
        for i in booklist:
            print(i[0])
            for j in i[1:]:
                print('    {0}'.format(j[0]))

    def get_content(self):
        booklist = self.get_list()
        if not os.path.isdir(self.title):
            os.mkdir(self.title)
        os.chdir(self.title)

        for book in booklist:
            if not os.path.isdir(book[0]):
                os.mkdir(book[0])
            os.chdir(book[0])

            for chapter in book[1:]:
                content = config.get_web_page(chapter[1] + config.charset, encoding='big5')
                content = BeautifulSoup(content.text, 'html.parser').find('div', id='content')

                with open(chapter[0] + '.txt', 'w', encoding='utf-8') as chwriter:
                    chwriter.write(content.text.lstrip())

            os.chdir('..')

        os.chdir('..')
        print('{0} download success'.format(self.title))


if __name__ == '__main__':
    literal = wenkuSuit(1)
    literal.get_content()
