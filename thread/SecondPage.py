import threading
import time

from baiduQueue.baiduQueue import q_page,flag
from baiduRequest.baiduRequest import getUrl


class SecondPage(threading.Thread):
    def __init__(self):
        super().__init__()

    def run(self):
        while True:
            if q_page.empty():
                time.sleep(1)
            if q_page.empty() and flag:
                break
            try:
                time.sleep(3)
                [bank, keyword, title, href, seasonTime] = q_page.get(block=False)
                print(title)
                url, flagc = getUrl(bank, keyword, title, href)
                print(url)
                print(flagc)
            except Exception:
                print(Exception)
                continue
