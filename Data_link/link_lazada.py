import requests
from bs4 import BeautifulSoup as b
import os
from fnmatch import fnmatch
import pandas as pd
import json
import time;
from pynput import mouse
import pyautogui
from pynput import keyboard
import shutil
import keyboard as ky
import pyperclip
Mobiles
Tablets
Laptops
Desktops
DSLR
Mirrorless
Point-Shoot
Instant Camera
Action/Video Cameras
Drones
Security Cameras
Console Gaming
data_all = {
    "อุปกรณ์-อิเล็กทรอนิกส์":[

    ]
    ,
    "อุปกรณ์เสริม-อิเล็กทรอนิกส์":[

    ],
    "ทีวีและเครื่องใช้ในบ้าน":[

    ],
    "สุขภาพและความงาม":[

    ],
    "ทารกและของเล่น":[

    ],
    "ของชำและสัตว์เลี้ยง":[

    ],
    "บ้านและไลฟ์สไตล์":[

    ],
    "แฟชั่นและเครื่องประดับผู้หญิง":[

    ],
    "แฟชั่นและเครื่องประดับผู้ชาย":[

    ],
    "กีฬาและการเดินทาง":[

    ],
    "ยานยนต์และรถจักรยานยนต์":[

    ]




}