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
url=input('Enter URL')
downloadpath=input('Enter the download path.')
download(url,f'{downloadpath}/FB.pdf')
print('Downloaded successfully')
