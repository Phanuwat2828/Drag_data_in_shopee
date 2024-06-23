import requests;
from PIL import ImageGrab
import os
# path = r'C:\gitclone\Drag_data_in_shopee\Line_api'
token_line  = '12PezhTC3uVcjGTlwxxmmzIfoHUviIyNi5X8SghZxfG' ;
path = 'C:\gitclone\Drag_data_in_shopee\Line_api\imag\Error.png'


def data_image():
    try:
        ImageGrab.grab().save(path)
    except Exception as e:
        print(e)


def lineNotify(message):
    payload = {'message':message}
    return _lineNotify(payload);
def notifyFile(filename):
    file = {'imageFile':open(filename,'rb')}
    payload = {'message': 'test'}
    return _lineNotify(payload,file)

def notifyPicture(url):
    payload = {'message':" ",'imageThumbnail':url,'imageFullsize':url}
    return _lineNotify(payload)

def notifySticker(stickerID,stickerPackageID):
    payload = {'message':" ",'stickerPackageId':stickerPackageID,'stickerId':stickerID}
    return _lineNotify(payload)

def _lineNotify(payload,file=None):
    import requests
    url = 'https://notify-api.line.me/api/notify'
	#EDIT
    headers = {'Authorization':'Bearer '+token_line}
    return requests.post(url, headers=headers , data = payload, files=file)

# data_image()
print(lineNotify('Hello Bot i\'m batman and i\'ll kill you'))
# os.remove(path);
# send_problem('Hello This is python tester api',path+'\\test_api2.jpg')




