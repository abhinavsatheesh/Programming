def download(fullurl, downloadname):
    import os
    import requests

    from urllib.parse import urlparse
    from pathlib import Path

    a = urlparse(fullurl)
    fn=downloadname

    if os.path.isfile(fn):
        print('Skipping download, file exists {0}'.format(fn))
    else:
        print('Downloading file {0}'.format(fn))
        r=requests.get(fullurl, stream=True)
        with open(fn,'wb') as f:
            f.write(r.content)

import urllib.request
import webbrowser
import requests
import os
from bs4 import BeautifulSoup
url_orig =input('Enter the StarMaker Video URL')
u = urllib.request.urlopen(url_orig)
link=u.geturl()
recordingID=link.split('&')[3].replace("recordingId=","")
url=f'https://static.starmakerstudios.com/production/uploading/recordings/{recordingID}/master.mp4'
downloadpath=input('Enter the download path.')
download(url,f'{downloadpath}/{recordingID}.mp4')
question=print('Downloaded successfully')