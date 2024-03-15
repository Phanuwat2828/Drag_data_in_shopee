from PIL import ImageGrab
path = 'C:\gitclone\Drag_data_in_shopee\Line_api\imag\Error.png'

def data_image():
    try:
        ImageGrab.grab().save(path)
    except Exception as e:
        print(e)


