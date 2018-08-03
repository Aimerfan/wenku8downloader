# import downloader
import updater


def search_from_list(booklist, args):
    filtered = []
    for i in booklist:
        for key in args:
            if len(i) > config.lable2index[key] and i[config.lable2index[key]].find(args[key]) >= 0:
                flag = True
            else:
                flag = False
                break
        if flag:
            filtered.append(i)
    return filtered


test = {}
while True:
    inputline = input()
    if len(inputline) == 0:
        break
    split = inputline.split('=')
    test[split[0]] = split[1]
res = search_from_list(updater.loadlist(), test)
for i in res:
    print(i)
