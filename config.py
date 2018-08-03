import requests


book_path = 'http://www.wenku8.com/modules/article/articleinfo.php?id='
charset = '&charset=big5'


index2lable = ['id', 'title', 'lib', 'author', 'status', 'latest', 'length']
lable2index = {'id': 0, 'title': 1, 'lib': 2, 'author': 3, 'status': 4, 'latest': 5, 'length': 6}
index2clable = ['id', '書名', '文庫分類', '小說作者', '文章狀態', '最後更新', '全文長度']
clable2index = {'id': 0, '書名': 1, '文庫分類': 2, '小說作者': 3, '文章狀態': 4, '最後更新': 5, '全文長度': 6}


def get_web_page(url, encoding=''):
    page = requests.Session().get(url)
    try:
        page.raise_for_status()
    except requests.exceptions.HTTPError:
        print('http error, error code: {0}'.format(page.status_code))
    except requests.exceptions.RequestException:
        print('Unknown connection error, please check your Internet status.')
    else:
        if encoding:
            page.encoding = encoding
    return page
