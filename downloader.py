# search and download
import config


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
