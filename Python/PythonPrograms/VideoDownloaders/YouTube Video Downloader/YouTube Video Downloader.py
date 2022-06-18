'''
 This Will help you to Download any YouTube videos
'''



# imports
from pytube import YouTube

link = ""
Download_path = "./"


def startDownload():
    global link
    global Download_path
    try:
        link = input("Paste the Link: ")
        Download_path = input("Enter a valid Download Path: ")
        '''
         If need to download to
         to Current Folder comment out the above line.
         Default Download_path is './'
        '''
        print('Connecting to server....')
        print("Downloading...")
        print('Wait Until Download is Complete.. Wait for 1 or 2 Minutes')

        YouTube(link).streams.first().download(Download_path)

        print("DownLoad Complete!!!!")

    except:
        print("Connection Timed Out Try Again")
    pass


startDownload()
