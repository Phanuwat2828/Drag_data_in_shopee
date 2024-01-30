
import requests
def postAPI_DB(data,id_shop):
    try:
        response = requests.post(
            f"https://1e39-202-28-35-198.ngrok-free.app/addb?id={id_shop}&&web=lazada",
            headers={
                "Content-type":"application/x-www-form-urlencoded"
            },
            data={
                 "data":data
            }
        )
    except: 
        response = "API error"
    return response