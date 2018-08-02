import updater
import downloader

test = {}
while True:
    inputline = input()
    if len(inputline) == 0:
        break
    split = inputline.split('=')
    test[split[0]] = split[1]
res = downloader.search_from_list(updater.loadlist(), test)
for i in res:
    print(i)
