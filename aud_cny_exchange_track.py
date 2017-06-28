# -*- coding: utf-8 -*-
import requests
import smtplib
from bs4 import BeautifulSoup
from apscheduler.schedulers.blocking import BlockingScheduler

DEFAULT_HEADER = {
    'Referer': 'http://www.boc.cn/index.html',
    'Host': 'www.boc.cn',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36' +
                  '(KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36',
    'Accept-Encoding': 'gzip, deflate, sdch'
}

BASE_URL = 'http://www.boc.cn/sourcedb/whpj/'

THRESH = 515


def send_email(result):
    """
    send email notification
    """
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login("knight3001@gmail.com", "MhGXMHPqRCSLlQhU6Q5Y")

    msg = "\r\n".join([
        "From: knight3001@gmail.com",
        "To: terry@bneing.com",
        "Subject: Currency Warning",
        "",
        "AUD Currency Drop below " + str(float(THRESH) / 10) + " to " + str(result)
    ])
    server.sendmail("knight3001@gmail.com", "terry@bneing.com", msg)
    print("Email sent")
    server.close()


def main():
    """
    main function
    """
    html = requests.get(BASE_URL, headers=DEFAULT_HEADER).content
    soup = BeautifulSoup(html, "html.parser")
    result = soup.find("td", text=u"澳大利亚元").find_next_sibling("td") \
        .find_next_sibling("td").find_next_sibling("td").text

    if float(result) < float(THRESH):
        send_email(result)
    else:
        print("Not Dropped: " + str(result))

SCHEDULER = BlockingScheduler()
SCHEDULER.add_job(main, 'interval', hours=1)
SCHEDULER.start()


#if __name__ == '__main__':
#    main()
