import downloader as d
import updater
import config
import os


def search_from_list(booklist, args):
    filtered = []
    for i in booklist:
        flag = True
        for key in args:
            if len(i) <= config.lable2index[key] or i[config.lable2index[key]].find(args[key]) == (-1):
                flag = False
                break
        if flag:
            filtered.append(i)
    return filtered


def search():
    print('可用的參數: ', end='')
    for i in config.index2lable[:5]:
        print('\'{0}\' '.format(i), end='')
    print('')

    test = {}
    inputline = input()
    parameter = inputline.split(',')
    for item in parameter:
        split = item.strip().split('=')
        split[0] = split[0].strip()
        split[1] = split[1].strip()
        if split[0] in config.index2lable[:5]:
            test[split[0]] = split[1]
        else:
            print('Paramater \'{0}\' is invaild.'.format(split[0]))

    res = search_from_list(updater.loadlist(), test)
    return res


def main():
    history = []
    while True:
        print('> ', end='')
        line = input().strip()
        if line == '':
            continue
        elif line == 'help':
            print('help: 印出說明文件。')
            print('exit: 離開程式。')
            print('search: 從資料庫搜尋書籍資料, 格式為\'搜尋參數\' = \'搜尋字串\', 有多個條件時中間以\',\'分隔，')
            print('        可用的搜尋參數會再使用時顯示。')
            print('update: 更新資料庫，需時較長請慎用，附加參數\'checknew\'只檢查新書(較快)。')
            print('summary: 查看指定書籍的章節狀況。')
            print('download: 下載指定書籍。')
        elif line == 'exit':
            break
        elif line == 'search':
            result = search()
            for item in result:
                print(item)
        elif line == 'summary':
            print('id = ', end='')
            id = input()
            if not id.isdigit():
                print('\'{0}\' is not digits.')
                continue
            item = None
            for i in history:
                if i.id == id:
                    item = i
                    break
            if item:
                item.print_list()
            else:
                history.append(d.wenkuSuit(id))
                history[-1].print_list()
        elif line == 'update':
            updater.loadlist(force=True)
        elif line == 'update checknew':
            updater.loadlist(True)
        elif line == 'download':
            print('id = ', end='')
            id = input()
            if not id.isdigit():
                print('\'{0}\' is not digits.')
                continue
            print('output path = ', end='')

            path = input()
            if not os.path.isdir(path):
                print('\'{0}\' is invaild.'.format(path))
                continue
            backup = os.getcwd()
            os.chdir(path)

            item = None
            for i in history:
                if i.id == id:
                    item = i
                    break
            if item:
                item.get_content()
            else:
                history.append(d.wenkuSuit(id))
                history[-1].get_content()

            os.chdir(backup)
        else:
            print('\'{0}\' is not a vaild instruchtion.'.format(line))


if __name__ == '__main__':
    main()
