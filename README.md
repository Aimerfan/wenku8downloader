# wenku8downloader

[輕小說文庫](http://www.wenku8.com)

功能如題，主要是個人練習網頁爬蟲的小作品。

本程式僅做python程式語言學習使用，請勿用於營利用途。

下載之資料請於24小時內刪除，非法使用之後果程式作者概不負責。

### Description
* wenku8donloader.py: **主程式，未完工**，預計提供一些搜尋並指定下載的能力。
* config.py: 某些跨檔案公用變數, 方法的存放區。
* updater.py: 書庫索引的updater。
* booklist.csv: 書庫的索引資料庫，正常狀況會先從這裡找出要下載的id後再利用downloader下載全文。
* downloader.py: 可以索引並下載指定的書籍系列

### Reference
* [wenku8](https://github.com/Messiahhh/wenku8)
* [CSNovelCrawler](https://github.com/rngmontoli/CSNovelCrawler)