#!/bin/python

from datetime import datetime
from tqdm import tqdm
import requests,re,sys


def memek():
    try:
                bau = str(input("\n[!] Select Resolution\n\n1. HD (High Definition)\n2. SD (Standard Definition)\n\n[?] >>>. Please type 1 for HD and 2 for SD ")).upper()
                if bau == '1':
                    print("")
                    video_url = re.search(r'hd_src:"(.+?)"', html).group(1)
                    file_size_request = requests.get(video_url, stream=True)
                    file_size = int(file_size_request.headers['Content-Length'])
                    block_size = 1024 
                    filename = datetime.strftime(datetime.now(), '%Y-%m-%d-%H-%M-%S')
                    t=tqdm(total=file_size, unit='B', unit_scale=True, desc=filename, ascii=True)
                    with open(filename + '.mp4', 'wb') as f:
                        for data in file_size_request.iter_content(block_size):
                            t.update(len(data))
                            f.write(data)
                    t.close()
                    print("\n[!] Done") 
                    sys.exit(0)  

                if bau == '2':
                    print("")
                    video_url = re.search(r'hd_src:"(.+?)"', html).group(1)
                    file_size_request = requests.get(video_url, stream=True)
                    file_size = int(file_size_request.headers['Content-Length'])
                    block_size = 1024 
                    filename = datetime.strftime(datetime.now(), '%Y-%m-%d-%H-%M-%S')
                    t=tqdm(total=file_size, unit='B', unit_scale=True, desc=filename, ascii=True)
                    with open(filename + '.mp4', 'wb') as f:
                        for data in file_size_request.iter_content(block_size):
                            t.update(len(data))
                            f.write(data)
                    t.close()
                    print("\n[!] Done")
                    sys.exit(0)


    except(KeyboardInterrupt):
        print("\n[!] You stopped the process! Please restart the program again.")

try:
    while True:        
        url = input("\n[URL] >>> ")
        x = re.match(r'^(https:|)[/][/]www.([^/]+[.])*facebook.com', url)

        if x:
            html = requests.get(url).content.decode('utf-8')
        else:
            print("\n[!] Error")
            sys.exit(0)

        _qualityhd = re.search('hd_src:"https', html)
        _qualitysd = re.search('sd_src:"https', html)
        _hd = re.search('hd_src:null', html)
        _sd = re.search('sd_src:null', html)

        list = []
        _thelist = [_qualityhd, _qualitysd, _hd, _sd]
        for id,val in enumerate(_thelist):
            if val != None:
                list.append(id)

        memek()

except KeyboardInterrupt:
    print("\n[!] You stopped the process! Please restart the program again.")
    