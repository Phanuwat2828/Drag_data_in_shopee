
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

api_data = {"3887232320": {
      "categoriesLpMultiFloor": [
        {
          "level2TabList": [
            {
              "level3TabList": [
                {
                  "categoryUrl": "//www.lazada.co.th/shop-mobiles",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//my-live-02.slatic.net/p/4a2e7ec400cc9d411ce9a9fab3dd0fc0.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586647.OTHER_5980123137_4813160",
                  "categoryName": "Mobiles",
                  "categoryId": "3972"
                }
              ],
              "categoryIcon": "",
              "categoryUrl": "//www.lazada.co.th/shop-mobiles",
              "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel2TabDTO",
              "categoryName": "Mobiles",
              "categoryId": "3973"
            },
            {
              "level3TabList": [
                {
                  "categoryUrl": "//www.lazada.co.th/shop-tablet",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//sg-live.slatic.net/p/b22e7ebf8803d45ddced282a3d195652.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586647.OTHER_5980123138_4813160",
                  "categoryName": "Tablets",
                  "categoryId": "3975"
                }
              ],
              "categoryIcon": "",
              "categoryUrl": "//www.lazada.co.th/shop-tablet",
              "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel2TabDTO",
              "categoryName": "Tablets",
              "categoryId": "3974"
            },
            {
              "level3TabList": [
                {
                  "categoryUrl": "//www.lazada.co.th/shop-traditional-laptops",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//th-live.slatic.net/p/385c01fda2c6f63c6de799481368bd65.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586647.OTHER_5980123139_4813160",
                  "categoryName": "Traditional Laptops",
                  "categoryId": "6372"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-gaming-notebook",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//th-live.slatic.net/p/8536f2799102f3af39dd48d1d6d5176d.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586647.OTHER_5980123140_4813160",
                  "categoryName": "Gaming",
                  "categoryId": "9663"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-2in1-laptops",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//th-live.slatic.net/p/37732231169224b12b091748ec487d80.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586647.OTHER_5980123141_4813160",
                  "categoryName": "2-in-1s",
                  "categoryId": "7443"
                }
              ],
              "categoryIcon": "",
              "categoryUrl": "//www.lazada.co.th/shop-laptops",
              "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel2TabDTO",
              "categoryName": "Laptops",
              "categoryId": "3916"
            },
            {
              "level3TabList": [
                {
                  "categoryUrl": "//www.lazada.co.th/shop-desktop-computer-gaming",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//th-live.slatic.net/p/8536f2799102f3af39dd48d1d6d5176d.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586647.OTHER_5980123142_4813160",
                  "categoryName": "Gaming",
                  "categoryId": "9668"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-desktop-computer-all-in-one",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//th-live.slatic.net/p/7b5844a1cf5326a004cc74b0cfd1ce9d.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586647.OTHER_5980123143_4813160",
                  "categoryName": "All-In-One",
                  "categoryId": "9666"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-desktop-computer-diy",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//th-live.slatic.net/p/56b2bd4c343c01cd3fc0bd801e4d9f66.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586647.OTHER_5980123144_4813160",
                  "categoryName": "DIY",
                  "categoryId": "9670"
                }
              ],
              "categoryIcon": "",
              "categoryUrl": "//www.lazada.co.th/shop-desktop-computer",
              "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel2TabDTO",
              "categoryName": "Desktops",
              "categoryId": "3917"
            },
            {
              "level3TabList": [
                {
                  "categoryUrl": "//www.lazada.co.th/shop-dslr-sets",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//sg-live.slatic.net/original/a3b68f5f7cc66bbe688e9f371b48aaf9.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586647.OTHER_5980123145_4813160",
                  "categoryName": "Sets",
                  "categoryId": "6143"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-dslr-body-only",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//th-live.slatic.net/p/dcc4416d56ba39a41b49393da4c1d0a6.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586647.OTHER_5980123146_4813160",
                  "categoryName": "Body Only",
                  "categoryId": "9869"
                }
              ],
              "categoryIcon": "",
              "categoryUrl": "//www.lazada.co.th/shop-dslr-slr-camera",
              "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel2TabDTO",
              "categoryName": "DSLR",
              "categoryId": "4324"
            },
            {
              "level3TabList": "",
              "categoryIcon": "",
              "categoryUrl": "//www.lazada.co.th/shop-mirrorless",
              "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel2TabDTO",
              "categoryName": "Mirrorless",
              "categoryId": "4327"
            },
            {
              "level3TabList": [
                {
                  "categoryUrl": "//www.lazada.co.th/shop-point-shoot-cameras",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//sg-live.slatic.net/p/cc46ac184cddfa2cef828d0349c20bca.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586647.OTHER_5980123148_4813160",
                  "categoryName": "Point & Shoot",
                  "categoryId": "3336"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-point-shoot-underwater-cameras",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//my-live-02.slatic.net/p/f57da0041850c46a607b89d223c2d925.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586647.OTHER_5980123149_4813160",
                  "categoryName": "Underwater Digital Cameras",
                  "categoryId": "3337"
                }
              ],
              "categoryIcon": "",
              "categoryUrl": "//www.lazada.co.th/shop-point-shoot",
              "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel2TabDTO",
              "categoryName": "Point & Shoot",
              "categoryId": "3219"
            },
            {
              "level3TabList": [
                {
                  "categoryUrl": "//www.lazada.co.th/shop-instantcameras",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//th-live.slatic.net/p/2/fujifilm-instax-mini-90-neo-classic-black-1451018132-147331-1-catalog.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586647.OTHER_5980123150_4813160",
                  "categoryName": "Instant Cameras",
                  "categoryId": "7162"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-instant-camera-films",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//th-live.slatic.net/p/2/fujifilm-instax-square-sq10-10-1495795611-13735712-bf037870b582816324192e76f8486708-catalog.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586647.OTHER_5980123151_4813160",
                  "categoryName": "Instant Camera Films",
                  "categoryId": "7163"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-instant-camera-accessories",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//sg-live.slatic.net/p/2/portable-protective-case-accessory-cover-plastic-storage-bag-withremovable-adjustable-shoulder-strap-for-fujifilm-instax-mini-9-8-8model-instant-cameras-clear-intl-0385-28718123-0edb53e71099013f93c56e8bcff042fd-catalog.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586647.OTHER_5980123152_4813160",
                  "categoryName": "Instant Camera Accessories",
                  "categoryId": "7164"
                }
              ],
              "categoryIcon": "",
              "categoryUrl": "//www.lazada.co.th/shop-instantcamera",
              "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel2TabDTO",
              "categoryName": "Instant Camera",
              "categoryId": "7160"
            },
            {
              "level3TabList": [
                {
                  "categoryUrl": "//www.lazada.co.th/shop-action-camcoders",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//th-live.slatic.net/p/cf9d66b4ea47a46f3cd9a9afa45b8a01.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586647.OTHER_5980123153_4813160",
                  "categoryName": "Sports & Action Camera",
                  "categoryId": "9866"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-camera-camcoders",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//laz-img-cdn.alicdn.com/images/ims-web/TB11X1lXwZC2uNjSZFnXXaxZpXa.jpg",
                  "categoryName": "Video Camera",
                  "categoryId": "9867"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-360-cameras",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//th-live-03.slatic.net/p/2/waterproof-360-panoramic-wifi-4k-ultra-hd-vr-action-camera-sport-dv-camcorder-black-intl-1505123660-41060334-7f28f00b4ccda246752fd82d55f6fc2c-zoom.jpg",
                  "categoryName": "360 Cameras",
                  "categoryId": "4325"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-professional-video-camera",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//laz-img-cdn.alicdn.com/images/ims-web/TB1PqelXwZC2uNjSZFnXXaxZpXa.jpg",
                  "categoryName": "Professional Video Camera",
                  "categoryId": "5057"
                }
              ],
              "categoryIcon": "",
              "categoryUrl": "//www.lazada.co.th/shop-camcorder",
              "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel2TabDTO",
              "categoryName": "Action/Video Cameras",
              "categoryId": "4326"
            },
            {
              "level3TabList": "",
              "categoryIcon": "",
              "categoryUrl": "//www.lazada.co.th/shop-drones",
              "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel2TabDTO",
              "categoryName": "Drones",
              "categoryId": "9603"
            },
            {
              "level3TabList": [
                {
                  "categoryUrl": "//www.lazada.co.th/shop-ip-cameras",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//laz-img-cdn.alicdn.com/images/ims-web/TB1FCx0ebZnBKNjSZFhXXc.oXXa.jpg",
                  "categoryName": "IP Security Cameras",
                  "categoryId": "14396"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-cctv-cameras",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//laz-img-cdn.alicdn.com/images/ims-web/TB1KzSpeljTBKNjSZFuXXb0HFXa.jpg",
                  "categoryName": "CCTV Security Cameras",
                  "categoryId": "14397"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-cctv-security-systems",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//laz-img-cdn.alicdn.com/images/ims-web/TB1ZjGpeljTBKNjSZFuXXb0HFXa.jpg",
                  "categoryName": "CCTV Security Systems",
                  "categoryId": "14399"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-ip-security-systems",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//laz-img-cdn.alicdn.com/images/ims-web/TB174XZebZnBKNjSZFhXXc.oXXa.jpg",
                  "categoryName": "IP Security Systems",
                  "categoryId": "14398"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-dummy-security-cameras",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//laz-img-cdn.alicdn.com/images/ims-web/TB19YmlXwZC2uNjSZFnXXaxZpXa.jpg",
                  "categoryName": "Dummy Cameras",
                  "categoryId": "14442"
                }
              ],
              "categoryIcon": "",
              "categoryUrl": "//www.lazada.co.th/shop-security-cameras",
              "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel2TabDTO",
              "categoryName": "Security Cameras",
              "categoryId": "14446"
            },
            {
              "level3TabList": [
                {
                  "categoryUrl": "//www.lazada.co.th/shop-handheld-consoles",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//my-live-02.slatic.net/p/76742ffe5d928645f1eaec5f6b2ee29b.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586647.OTHER_5980123163_4813160",
                  "categoryName": "Handheld Consoles",
                  "categoryId": "10100425"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-console-gaming-consoles",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//laz-img-cdn.alicdn.com/images/ims-web/TB1eTBAcvuSBuNkHFqDXXXfhVXa.jpg",
                  "categoryName": "Consoles",
                  "categoryId": "10100427"
                }
              ],
              "categoryIcon": "",
              "categoryUrl": "//www.lazada.co.th/shop-console-gaming",
              "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel2TabDTO",
              "categoryName": "Console Gaming",
              "categoryId": "10100424"
            }
          ],
          "categoryName_zh": "",
          "categoryIcon": "ic-cat-ElectronicDev &#xe740;",
          "id": "6634008",
          "position": "top",
          "childId": "Level_1_Category_No1",
          "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel1TabDTO",
          "categoryName": "Electronic Devices",
          "level1CategoryId": "6634008"
        },
        {
          "level2TabList": [
            {
              "level3TabList": [
                {
                  "categoryUrl": "//www.lazada.co.th/shop-mobile-cases-and-covers",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//my-live-02.slatic.net/p/7e2a3910596cc0f42c1bf58cd5142845.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586648.OTHER_5980123237_4813161",
                  "categoryName": "Phone Cases & Covers",
                  "categoryId": "6888"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-mobile-tablets-power-bank",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//th-live.slatic.net/p/2/eloop-e12-power-bank-11000-mah-1507197505-42608344-1afb10411f83a4b78c7599af72db46b3-catalog.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586648.OTHER_5980123238_4813161",
                  "categoryName": "Power Banks",
                  "categoryId": "6892"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-mobile-cables",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//th-live-01.slatic.net/p/2/61-hyt-baofeng-kenwood-1469461837-7146547-ef727b8711cf1e569e4ae2c4f49b88ef-zoom.jpg",
                  "categoryName": "Cables & Converters",
                  "categoryId": "6130"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-wireless-mobile-chargers",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//th-live.slatic.net/p/d0cb397516c5bbb42b6443bc5fad6ab4.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586648.OTHER_5980123240_4813161",
                  "categoryName": "Wireless Chargers",
                  "categoryId": "14369"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-screen-protectors",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//th-live-03.slatic.net/p/2/cessory-iphone-6-47-026mm25d-premium-tempered-glass-9h-1448345104-4974581-1-zoom.jpg",
                  "categoryName": "Screen Protectors",
                  "categoryId": "6889"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-prepaid-cards",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//th-live.slatic.net/p/d00547c340ebacf728757f5992787d08.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586648.OTHER_5980123242_4813161",
                  "categoryName": "Prepaid Cards",
                  "categoryId": "6891"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-car-mounts",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//th-live.slatic.net/p/2/long-neck-sl-2-5780-88760701-8529b72e18362805dbe3c07d7c6d11c3-catalog.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586648.OTHER_5980123243_4813161",
                  "categoryName": "Car Mounts",
                  "categoryId": "3491"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-wired-mobile-chargers",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//my-live-02.slatic.net/p/cc81a56bc5f9577bb6466b079d5c25ee.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586648.OTHER_5980123245_4813161",
                  "categoryName": "Wall Chargers",
                  "categoryId": "14368"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-tablets-cases-covers",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//laz-img-cdn.alicdn.com/images/ims-web/TB1Dz5lXwZC2uNjSZFnXXaxZpXa.jpg",
                  "categoryName": "Tablet Cases & Covers",
                  "categoryId": "14366"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-mobile-replacement-parts",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//icms-image.slatic.net/images/ims-web/923406cb-1d22-45b2-993d-5838f1bddfa5.webp?scm=1003.4.icms-zebra-5000413-2586648.OTHER_6042100591_4813161",
                  "categoryName": "Replacement Parts",
                  "categoryId": "400317"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-mobile-phone-docks",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//icms-image.slatic.net/images/ims-web/52e65724-7916-46ed-9673-168ac576661a.webp?scm=1003.4.icms-zebra-5000413-2586648.OTHER_6042100601_4813161",
                  "categoryName": "Docks & Stands",
                  "categoryId": "400318"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-fashion-mobile-accessories",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//icms-image.slatic.net/images/ims-web/88b127e3-e7b0-4f64-b943-7e14f8af7d4e.webp?scm=1003.4.icms-zebra-5000413-2586648.OTHER_6042124665_4813161",
                  "categoryName": "Fashion Mobile Accessories",
                  "categoryId": "400325"
                }
              ],
              "categoryIcon": "",
              "categoryUrl": "//www.lazada.co.th/shop-mobile-accessories",
              "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel2TabDTO",
              "categoryName": "Mobiles Accessories",
              "categoryId": "6887"
            },
            {
              "level3TabList": [
                {
                  "categoryUrl": "//www.lazada.co.th/shop-audio-headphones",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//laz-img-cdn.alicdn.com/images/ims-web/TB1vGKjekomBKNjSZFqXXXtqVXa.jpg",
                  "categoryName": "Headphones & Headsets",
                  "categoryId": "4400"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-portable-speakers",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//th-live.slatic.net/original/2e90bd2f35bf19d6d6161566c04b77b8.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586648.OTHER_5980123248_4813161",
                  "categoryName": "Portable Speakers",
                  "categoryId": "10100398"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-home-audio-theater",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//laz-img-cdn.alicdn.com/images/ims-web/TB14Cx5eXkoBKNjSZFkXXb4tFXa.jpg",
                  "categoryName": "Home Entertainment",
                  "categoryId": "5075"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-mp3-players-ipods",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//laz-img-cdn.alicdn.com/images/ims-web/TB1kWyjekomBKNjSZFqXXXtqVXa.jpg",
                  "categoryName": "Portable Players",
                  "categoryId": "4389"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-dj-audio-equipment",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//laz-img-cdn.alicdn.com/images/ims-web/TB1YSipeljTBKNjSZFuXXb0HFXa.jpg",
                  "categoryName": "Professional Audio Equipment",
                  "categoryId": "7221"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-dj-audio-equipment",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//sg-live.slatic.net/p/9dd1e9dccf1ded81c9fe6c347a5dd57a.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586648.OTHER_5980123252_4813161",
                  "categoryName": "DJ Equipment",
                  "categoryId": "10100390"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-smart-speakers",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//th-live.slatic.net/p/5ed8a698992a5818b2ccabd93b43ca39.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586648.OTHER_5980123253_4813161",
                  "categoryName": "Smart Speakers",
                  "categoryId": "14387"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-bluetooth-transmitters-receivers",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//sg-live.slatic.net/p/2ccc9067623288365769f8cc49c83d66.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586648.OTHER_5980123254_4813161",
                  "categoryName": "BT Transmitters & Receivers",
                  "categoryId": "5522"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-streaming-media-players",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//sg-live.slatic.net/p/2/apple-tv-4k-64gb-1511750655-06161477-ec309f5ecdf84acb1cf44801f7782ff9-catalog.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586648.OTHER_5980123255_4813161",
                  "categoryName": "Streaming Media Players",
                  "categoryId": "10100889"
                }
              ],
              "categoryIcon": "",
              "categoryUrl": "//www.lazada.co.th/shop-audio-2",
              "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel2TabDTO",
              "categoryName": "Audio",
              "categoryId": "10100387"
            },
            {
              "level3TabList": [
                {
                  "categoryUrl": "//www.lazada.co.th/shop-smartwatches-and-accessories",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//th-live.slatic.net/original/eec6e080cec9452dc78e8ed3c1018377.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586648.OTHER_5980123256_4813161",
                  "categoryName": "Smartwatches & Accessories",
                  "categoryId": "10100413"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-fitness-trackers",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//th-live-01.slatic.net/p/2/jakcom-b3-smart-band-all-in-one-smart-watch-heart-rate-monitorsbluetooth-smartband-fitness-tracker-bracelet-for-iphone-android-intl-1488921724-51418031-6b78f46045880894aab1b21e54a712b0-zoom.jpg",
                  "categoryName": "Fitness Trackers & Accessories",
                  "categoryId": "7292"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-smart-tracking",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//sg-live.slatic.net/p/mdc/7ed70bc5580d513f548b28fc7da1cabf.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586648.OTHER_5980123258_4813161",
                  "categoryName": "Smart tracker",
                  "categoryId": "7294"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-vr",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//th-live-01.slatic.net/p/2/mini-58g-fpv-receiver-150ch-uvc-video-downlink-otg-for-vr-androidphone-1504238494-37647104-b6711f5d277203fb0921f8eb9f795336-zoom.jpg",
                  "categoryName": "Virtual Reality",
                  "categoryId": "6631"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-vr-accessories",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//th-live.slatic.net/p/2/jingle-wireless-bluetooth-vr-remote-control-compatible-all-vr-box-black-1564-3807467-95c35f29033b68103c17edb22342ce58-catalog.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586648.OTHER_5980123260_4813161",
                  "categoryName": "VR Accessories",
                  "categoryId": "6634"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-smart-glasses",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//my-test-11.slatic.net/original/9c058e8b78e6603258366c81b0562114.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586648.OTHER_5980123261_4813161",
                  "categoryName": "Smart Glasses",
                  "categoryId": "7293"
                }
              ],
              "categoryIcon": "",
              "categoryUrl": "//www.lazada.co.th/shop-smart-devices",
              "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel2TabDTO",
              "categoryName": "Wearables",
              "categoryId": "10100412"
            },
            {
              "level3TabList": [
                {
                  "categoryUrl": "//www.lazada.co.th/shop-electronics-gadgets-walkie-talkies",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//laz-img-cdn.alicdn.com/images/ims-web/TB1cr9lXwZC2uNjSZFnXXaxZpXa.jpg",
                  "categoryName": "Walkie-Talkies",
                  "categoryId": "5212"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-laser-pointers-gadgets",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//sg-live.slatic.net/p/dd271dddc5a30441414cfa1321890d2e.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586648.OTHER_5980123263_4813161",
                  "categoryName": "Remote Presenter",
                  "categoryId": "7276"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-metal-detectors-gadgets",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//sg-live.slatic.net/p/2/handheld-security-metal-detector-with-audio-and-vibration-alarm-2766-0254069-26d749bb3fb491222a4e1e255e74b0d1-catalog.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586648.OTHER_5980123264_4813161",
                  "categoryName": "Metal Detectors",
                  "categoryId": "7277"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-dictionaries-translators",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//my-live-02.slatic.net/p/fb4eae65e230bbd1d9e64de760ab1ee5.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586648.OTHER_5980123265_4813161",
                  "categoryName": "Dictionaries & Translators",
                  "categoryId": "7278"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-universal-chargers",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//sg-live.slatic.net/p/c1b0e02aa7e9b29b15d93c14e81aa184.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586648.OTHER_5980123266_4813161",
                  "categoryName": "Universal Chargers",
                  "categoryId": "5211"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-graphic-tablets",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//th-live-01.slatic.net/p/2/wacom-intuos-comic-pentouch-small-cth-490k1-c-black-1450695345-5864572-1-zoom.jpg",
                  "categoryName": "Graphic Tablets",
                  "categoryId": "10100364"
                }
              ],
              "categoryIcon": "",
              "categoryUrl": "//www.lazada.co.th/shop-consumer-electronics-gadgets",
              "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel2TabDTO",
              "categoryName": "Gadgets",
              "categoryId": "7509"
            },
            {
              "level3TabList": [
                {
                  "categoryUrl": "//www.lazada.co.th/shop-internal-hard-drives",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//th-live-01.slatic.net/p/2/western-digital-wd-wd10ezex-1tb-blue-1463451667-3943446-aa26e9b9951072a752f3a26b7169e709-zoom.jpg",
                  "categoryName": "Internal Hard Drives",
                  "categoryId": "3929"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-external-hard-drives",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//th-live-01.slatic.net/p/2/wd-new-my-passport-ultra-2tb-wdbbkd0020brd-portable-storagefestive-red2tb-1481774288-12707501-704a36a8676c6189816ce81339367adb-zoom.jpg",
                  "categoryName": "External Hard Drives",
                  "categoryId": "3937"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-camera-memory-cards",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//th-live-03.slatic.net/p/2/samsung-evo-plus-microsd-card-32gb-1498818567-22572082-edfa60673d5e4ce705bd8f19d763c521-zoom.jpg",
                  "categoryName": "Memory Cards",
                  "categoryId": "4383"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-otg-drives",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//th-live-03.slatic.net/p/2/i-flash-drive-hd-otg-64gb-kingston-dtduo3c-usb31type-c-1496509779-57372032-05ce14b7a0c67acc843f0264e5503131-zoom.jpg",
                  "categoryName": "OTG Drives",
                  "categoryId": "2335"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-usb-flash-drives",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//th-live-03.slatic.net/p/2/apacer-handy-drive-steno-ah326-8gb-black-1450758271-47328-1-zoom.jpg",
                  "categoryName": "Flash Drives",
                  "categoryId": "2336"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-storage-for-mac",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//th-live-02.slatic.net/p/2/transcend-jetdrive-lite-130-128gb-for-macbook-air-1334-1476956817-2584819-b3e15a43dc5362d04e33faee2cd4ce82-zoom.jpg",
                  "categoryName": "Storage for Mac",
                  "categoryId": "2337"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-solid-state-drives",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//th-live-03.slatic.net/p/2/samsung-ssd-850-evo-1-tb-1473647660-4852208-52656a9bed811bed19518a9f0994b15c-zoom.jpg",
                  "categoryName": "Internal Solid State Drives",
                  "categoryId": "14385"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-external-solid-state-drive",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//th-live-02.slatic.net/p/2/wd-new-my-passport-wdbk3e5120psl-wesns-ssd-512-black-and-silver-new-usb-type-c-1506315476-79717364-6076b19da99615308cb3f78ab84062d9-zoom.jpg",
                  "categoryName": "External Solid State Drives",
                  "categoryId": "14386"
                }
              ],
              "categoryIcon": "",
              "categoryUrl": "//www.lazada.co.th/shop-data-storage",
              "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel2TabDTO",
              "categoryName": "Data Storage",
              "categoryId": "10100386"
            },
            {
              "level3TabList": [
                {
                  "categoryUrl": "//www.lazada.co.th/shop-keyboards",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//th-live.slatic.net/original/3a063c03faaeb8c66ab248b5629cb53d.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586648.OTHER_5980123276_4813161",
                  "categoryName": "Keyboards",
                  "categoryId": "7220"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-computer-mouse",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//th-live-02.slatic.net/p/2/logitech-mouse-usb-lg-b100-black-1498631531-72147572-621b29fede029e1b2e9fb1b2992114d2-zoom.jpg",
                  "categoryName": "Mice",
                  "categoryId": "7465"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-software",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//sg-live.slatic.net/p/microsoft-windows-10-home-64bit-oem-dvd-7640-5657857-48c3f3d8cc08512105861b5cfaf49d73-catalog.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586648.OTHER_5980123278_4813161",
                  "categoryName": "Software",
                  "categoryId": "3921"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-computer-surge-protector",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//laz-img-cdn.alicdn.com/images/ims-web/TB19MejeRjTBKNjSZFuXXb0HFXa.jpg",
                  "categoryName": "Surge Protector",
                  "categoryId": "9672"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-mouse-pads",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//th-live-03.slatic.net/p/2/gaming-mouse-mat-1501853232-36602073-a072275dcb7c51835990955cb8aa8491-zoom.jpg",
                  "categoryName": "Mousepads",
                  "categoryId": "7365"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-computer-laptop-adapters-cables",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//ph-live-02.slatic.net/p/5/ali-pomade-ocean-waves-120g-strong-hold-water-based-1505876636-27589661-1521e848c8d8594556062c0221b2252a-zoom.jpg",
                  "categoryName": "Adapters & Cables",
                  "categoryId": "5611"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-pc-audio",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//th-live-03.slatic.net/p/2/nubwo-no-06-1472744255-3727297-bebdd10f75fb7376207c4628be68b39a-zoom.jpg",
                  "categoryName": "PC Audio",
                  "categoryId": "14373"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-monitors",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//th-live-03.slatic.net/p/2/dell-s2716dg-2734-qhd-144mhz1ms-led-gaming-monitor-with-nvidia-g-sync-1488438570-32681031-f0374c579e861539595eae486ce4b2a3-zoom.jpg",
                  "categoryName": "Monitor",
                  "categoryId": "3952"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-multi-function-printers",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//laz-img-cdn.alicdn.com/images/ims-web/TB1cfSjekomBKNjSZFqXXXtqVXa.jpg",
                  "categoryName": "Printers",
                  "categoryId": "3956"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-scanners",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//sg-live.slatic.net/p/c9b1723e557764106f6d7bfa7c79a38a.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586648.OTHER_5980123285_4813161",
                  "categoryName": "Scanners",
                  "categoryId": "3954"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-printer-ink",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//laz-img-cdn.alicdn.com/images/ims-web/TB1pYR6eXkoBKNjSZFkXXb4tFXa.jpg",
                  "categoryName": "Ink",
                  "categoryId": "7437"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-labeller",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//sg-live.slatic.net/original/1fe30398c482deca5b6f4ef00c6320fb.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586648.OTHER_5980123287_4813161",
                  "categoryName": "Label Printer",
                  "categoryId": "9576"
                }
              ],
              "categoryIcon": "",
              "categoryUrl": "//www.lazada.co.th/shop-computer-accessories",
              "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel2TabDTO",
              "categoryName": "Computers & Laptops Accessories",
              "categoryId": "3919"
            },
            {
              "level3TabList": [
                {
                  "categoryUrl": "//www.lazada.co.th/shop-motherboards",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//th-live-03.slatic.net/p/2/msi-mainboard-h110m-pro-vd-plus-ddr4-lga1151-1498462774-91709172-15a290f88e2bfb6f34b7f9d2de7d2459-zoom.jpg",
                  "categoryName": "Motherboards",
                  "categoryId": "3924"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-ram",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//th-live.slatic.net/p/2/gskill-ddr4-ram-pc-163200-trident-z-rgb-3200c16d-16gtzr-8x2h-0326-01528423-6e75b625efa92f486e82f2cecafa9c44-catalog.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586648.OTHER_5980123289_4813161",
                  "categoryName": "RAM",
                  "categoryId": "3925"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-processors",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//th-live-02.slatic.net/p/2/intel-core-i5-6500-bx80662i56500-1478658071-1229589-a29c794f355e4ed0cb8e580e349a22ac-zoom.jpg",
                  "categoryName": "Processors",
                  "categoryId": "3926"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-graphic-cards",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//th-live-03.slatic.net/p/2/zotac-geforce-gtx-1050-ti-4gb-gddr5-1499154133-89391592-15ed6919cf791806af88f9028ad5ef7f-zoom.jpg",
                  "categoryName": "Graphics Cards",
                  "categoryId": "3927"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-internal-optical-drives",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//th-live-03.slatic.net/p/2/asus-odd-optical-drive-internal-dvd-rw-asus-24d5mtblkbas-24x-bulk-bp-1491581940-3186764-9daaff2303cbccb6edf6d56553feabc9-zoom.jpg",
                  "categoryName": "Front Bay Devices",
                  "categoryId": "3930"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-power-supply-units",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//th-live-03.slatic.net/p/2/spec-ups-spec-800-plus-800va-320w-1470213432-1772267-f00a6e34f970195da99dcb7c8f77949c-zoom.jpg",
                  "categoryName": "Power Supply Units",
                  "categoryId": "3933"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-cabinet-fans",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//sg-live.slatic.net/original/c960122521cdf331c2be2aa5adc8c560.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586648.OTHER_5980123294_4813161",
                  "categoryName": "Cooling Fans",
                  "categoryId": "3935"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-cpu-fans-and-heatsinks",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//th-live-02.slatic.net/p/2/aigo-fan-case-120mm-r-12025-circular-white-led-1487590845-40289601-8cb1dc484a20944b836b3108c7d9790a-zoom.jpg",
                  "categoryName": "Heatsinks",
                  "categoryId": "3936"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-computer-sound-cards",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//th-live-01.slatic.net/p/2/usb-sound-usb-external-71-channel-stereo-sound-adapter-1500122046-61585333-0addc9c89c7c3736a16455d460a2f9a3-zoom.jpg",
                  "categoryName": "Sound cards",
                  "categoryId": "7368"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-water-cooling-system",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//th-live.slatic.net/p/4335e4589b6ee234fdea26755011d1fb.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586648.OTHER_5980123297_4813161",
                  "categoryName": "Water Cooling System",
                  "categoryId": "14382"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-cabinets",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//th-live.slatic.net/p/8e9989ba593176326f1690a87f54d440.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586648.OTHER_5980123298_4813161",
                  "categoryName": "Desktop Casings",
                  "categoryId": "3932"
                }
              ],
              "categoryIcon": "",
              "categoryUrl": "//www.lazada.co.th/shop-computer-components",
              "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel2TabDTO",
              "categoryName": "Computer Components",
              "categoryId": "3918"
            },
            {
              "level3TabList": [
                {
                  "categoryUrl": "//www.lazada.co.th/shop-routers",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//my-live-02.slatic.net/original/cd486b2aaaf5c3b6722e4c19872d6ab1.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586648.OTHER_5980123299_4813161",
                  "categoryName": "Routers",
                  "categoryId": "3963"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-switches",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//th-live.slatic.net/p/83c5b826d85c81f06f07e2f3d1f70e08.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586648.OTHER_5980123300_4813161",
                  "categoryName": "Switches",
                  "categoryId": "3966"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-wireless-usb-adapters",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//my-live-02.slatic.net/p/2/dual-band-600mbps-24ghz-5ghz-usb-wireless-adapter-wifi-antenna-80211abgnac-wifi-usb-adapter-for-mac-windows-black-0350-466293271-4f140619a4afd39e4d7af487ed6953e1-.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586648.OTHER_5980123301_4813161",
                  "categoryName": "Wireless USB Adapters",
                  "categoryId": "3968"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-modems",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//my-live-02.slatic.net/original/2dd529ecf5d1dbbf570d707c211ea2d6.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586648.OTHER_5980123302_4813161",
                  "categoryName": "Modems",
                  "categoryId": "7019"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-computer-mifi-modems",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//sg-live.slatic.net/p/d4eb9cdfa9cf26a05e1029208797b848.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586648.OTHER_5980123303_4813161",
                  "categoryName": "Mobile Wi-Fi Hotspots",
                  "categoryId": "5771"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-computer-usb-modems",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//my-live-02.slatic.net/p/bce938275eeb4f8c0c8dfc4962b9a54b.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586648.OTHER_5980123304_4813161",
                  "categoryName": "USB Modems",
                  "categoryId": "5772"
                }
              ],
              "categoryIcon": "",
              "categoryUrl": "//www.lazada.co.th/shop-network-components",
              "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel2TabDTO",
              "categoryName": "Network Components",
              "categoryId": "3922"
            },
            {
              "level3TabList": [
                {
                  "categoryUrl": "//www.lazada.co.th/shop-console-games",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//laz-img-cdn.alicdn.com/images/ims-web/TB1vh0ecByWBuNkSmFPXXXguVXa.jpg",
                  "categoryName": "Console Games",
                  "categoryId": "10100428"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-console-gaming-controllers",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//laz-img-cdn.alicdn.com/images/ims-web/TB1QuJ7cDXYBeNkHFrdXXciuVXa.jpg",
                  "categoryName": "Controllers",
                  "categoryId": "10100431"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-console-cases-and-covers",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//laz-img-cdn.alicdn.com/images/ims-web/TB1d.d2cDXYBeNkHFrdXXciuVXa.jpg",
                  "categoryName": "Cases & Covers",
                  "categoryId": "10100437"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-console-gaming-accessories-tablet-screen-protectors",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//sg-live.slatic.net/original/d38c80ac593bb5fac48c85dfca01f39a.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586648.OTHER_5980123308_4813161",
                  "categoryName": "Screen Protectors",
                  "categoryId": "10100438"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-console-gaming-accessories",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//laz-img-cdn.alicdn.com/images/ims-web/TB1o6hwcvuSBuNkHFqDXXXfhVXa.jpg",
                  "categoryName": "Accessories Game Consoles",
                  "categoryId": "10100440"
                }
              ],
              "categoryIcon": "",
              "categoryUrl": "//www.lazada.co.th/shop-console-gaming-accessories",
              "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel2TabDTO",
              "categoryName": "Console Gaming Accessories",
              "categoryId": "10100439"
            },
            {
              "level3TabList": [
                {
                  "categoryUrl": "//www.lazada.co.th/shop-camera-memory-cards",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//th-live-03.slatic.net/p/2/samsung-evo-plus-microsd-card-32gb-1498818567-22572082-edfa60673d5e4ce705bd8f19d763c521-zoom.jpg",
                  "categoryName": "Memory Cards",
                  "categoryId": "4383"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-camera-lenses",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//th-live.slatic.net/p/2/canon-lens-ef-50mm-f18-stm-1449222439-3788253-1-catalog.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586648.OTHER_5980123311_4813161",
                  "categoryName": "Lenses",
                  "categoryId": "3359"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-tripods-and-monopods",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//th-live.slatic.net/p/5c24beee5585b4798e63bff075dacee1.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586648.OTHER_5980123312_4813161",
                  "categoryName": "Tripods & Monopods",
                  "categoryId": "3597"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-camera-bags",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//th-live.slatic.net/p/mdc/93e5438df03a4b036d83889b5bde2e46.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586648.OTHER_5980123313_4813161",
                  "categoryName": "Camera Cases, Covers and Bags",
                  "categoryId": "4333"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-sport-action-camera-accessory-kits",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//my-live-02.slatic.net/p/2/black-reliable-anti-slide-elawastic-head-strap-band-for-gopro-hero-camera-1952-738196471-8e20f9196fda33302848f0d9bf3372cf-catalog.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586648.OTHER_5980123314_4813161",
                  "categoryName": "Action Camera Accessories",
                  "categoryId": "7269"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-camera-lighting-studio-equitment",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//th-live.slatic.net/p/60c9ab5a63684c142f32ac43641d77d0.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586648.OTHER_5980123315_4813161",
                  "categoryName": "Lighting & Studio Equipment",
                  "categoryId": "5087"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-camera-batteries",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//th-live-01.slatic.net/p/2/bls-5-ps-bls5-olympus-pene-pl2-e-pl5-e-pl6-e-pl7-e-pl8-e-pm2-olympus-stylus-1-1solympus-om-d-e-m10-e-m10-ii-olympus-e-m10-mark-ii-replacementbattery-for-olympus-1487127478-00955811-413a207bb8fbb510d657b96d7719acd0-zoom.jpg",
                  "categoryName": "Batteries",
                  "categoryId": "4336"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-gimbals-stabilizer",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//my-live-02.slatic.net/original/f826a33b20bf7ecd82a6811c183ed561.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586648.OTHER_5980123317_4813161",
                  "categoryName": "Gimbals & Stabilizers",
                  "categoryId": "14393"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-instant-camera-films",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//th-live.slatic.net/p/2/fujifilm-instax-square-sq10-10-1495795611-13735712-bf037870b582816324192e76f8486708-catalog.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586648.OTHER_5980123318_4813161",
                  "categoryName": "Instant Camera",
                  "categoryId": "4330"
                }
              ],
              "categoryIcon": "",
              "categoryUrl": "//www.lazada.co.th/shop-camera-accessories",
              "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel2TabDTO",
              "categoryName": "Camera Accessories",
              "categoryId": "4329"
            }
          ],
          "categoryName_zh": "",
          "categoryIcon": "ic-cat-ElectronicAcc &#xe73d;",
          "id": "6634009",
          "position": "top",
          "childId": "Level_1_Category_No2",
          "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel1TabDTO",
          "categoryName": "Electronic Accessories",
          "level1CategoryId": "6634009"
        },
        {
          "level2TabList": [
            {
              "level3TabList": [
                {
                  "categoryUrl": "//www.lazada.co.th/shop-smart-tv",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//th-live-02.slatic.net/p/2/samsung-uhd-smart-tv-55-ua55mu6100-1496994481-82953732-1a55d350732bfd0dd3556db6a18bb3bf-zoom.jpg",
                  "categoryName": "Smart Televisions",
                  "categoryId": "4364"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-digital-televisions",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//my-live-02.slatic.net/p/2/toshiba-4934-4k-uhd-smart-led-tv-49u9650vm-1504518285-01537158-a1edfc703d35fd4275d21372b09de47a-zoom.jpg",
                  "categoryName": "Digital Televisions",
                  "categoryId": "10100320"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-streaming-media-players",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//th-live-01.slatic.net/p/2/mini-m8s-ii-smart-tv-box-amlogic-s905x-quad-core-android-60-64bit4k-vp9-decoding-2gb-ddr3-8gb-emmc-support-bt-40-24ghz-wifi-intl-1494059579-92474971-f309c2e64e1ab80084cf3f1961b2b60f-zoom.jpg",
                  "categoryName": "Media Players",
                  "categoryId": "5992"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-electronics-video-projectors",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//th-live-01.slatic.net/p/2/mini-portable-rd-802-1080p-3d-hd-led-projector-home-multimedia-cinema-led-1080p-projector-hdmiavvgasdusbtv-proyector-1500554021-59628543-b2bbbf1a41cf3c7feb53c7edd1e71764-zoom.jpg",
                  "categoryName": "Projectors",
                  "categoryId": "4367"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-tv-receivers",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//th-live-01.slatic.net/p/2/10pcs-f-type-male-plug-compression-connectors-for-rg6-coax-coaxial-tv-cable-hq-intl-1506064504-33116754-aee88ec926561d363edfbf6bd32dee7c-zoom.jpg",
                  "categoryName": "TV Receivers",
                  "categoryId": "5483"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-electronics-tv-wall-mounts",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//th-live-02.slatic.net/p/2/1440-lcd-led-plasma-hdtv-hanging-rackholder-stand-1494223439-49116181-90831a80aacabfe05ea7237b55165907-zoom.jpg",
                  "categoryName": "Wall Mounts & Protectors",
                  "categoryId": "5526"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-tv-cables",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//th-live-02.slatic.net/p/2/hdmi-5m-v14-black-1488798341-18212131-8083ac9e8ecdb201083e355b3281154f-zoom.jpg",
                  "categoryName": "Cables",
                  "categoryId": "5529"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-electronics-remote-controllers",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//th-live-03.slatic.net/p/2/leegoal-wireless-presentation-pointer-laser-remote-controller-presenter-with-usb-receiver-for-powerpoint-ppt-speech-teaching-intl-1508986910-97004593-ccf3c666fdf5b1f702abe997b56cb46c-zoom.jpg",
                  "categoryName": "TV Remote Controllers",
                  "categoryId": "5527"
                }
              ],
              "categoryIcon": "",
              "categoryUrl": "//www.lazada.co.th/shop-consumer-electronics",
              "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel2TabDTO",
              "categoryName": "TVs & Video Devices",
              "categoryId": "3990"
            },
            {
              "level3TabList": [
                {
                  "categoryUrl": "//www.lazada.co.th/shop-air-conditioners",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//th-live-03.slatic.net/p/12/samsung-12000btu-ar5000inverter-1479527213-500469-37458a386b32f903baf67ec2a0315925-zoom.jpg",
                  "categoryName": "Air Conditioners",
                  "categoryId": "11802"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-refrigerators",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//th-live-03.slatic.net/p/12/toshiba-1-gr-b174zns-62-1484216463-4760522-8e63f2fb7952197c07b0a233951afc87-zoom.jpg",
                  "categoryName": "Refrigerators",
                  "categoryId": "11809"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-freezers",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//th-live-02.slatic.net/p/12/haier-hcf-228-2-n-198-1450720887-417043-1-zoom.jpg",
                  "categoryName": "Freezers",
                  "categoryId": "11810"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-washing-machines",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//laz-img-cdn.alicdn.com/images/ims-web/TB14rh0ebZnBKNjSZFhXXc.oXXa.jpg",
                  "categoryName": "Washing Machines",
                  "categoryId": "11806"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-dryers",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//th-live.slatic.net/p/9101e17684495208aeeead7fb4cddcab.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586649.OTHER_5981320574_4841894",
                  "categoryName": "Clothes Dryers",
                  "categoryId": "11808"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-ovens",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//th-live-01.slatic.net/p/12/electrolux-15-eot3805k-1450579796-6802031-1-zoom.jpg",
                  "categoryName": "Build-in Oven",
                  "categoryId": "11816"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-cooktops-ranges",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//th-live-02.slatic.net/p/12/thaivasion-500w-1491202150-32605541-111a81a685b961bddb3a72ec3c2b090e-zoom.jpg",
                  "categoryName": "Cooktops & Ranges",
                  "categoryId": "11814"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-water-purifiers",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//th-live-02.slatic.net/p/12/purify-carbon-block-cto-10-x-25-5-micron-x3-1478667625-6059598-eb26904f4efe9a021dc086551bf988b5-zoom.jpg",
                  "categoryName": "Drinking Filtration system",
                  "categoryId": "11826"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-appliances-water-dispensers",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//th-live-02.slatic.net/p/12/2-standard-by-rwc-1500894069-96474153-66baf4eff409bc4aa395c4665322d7df-zoom.jpg",
                  "categoryName": "Water Dispensers",
                  "categoryId": "11825"
                }
              ],
              "categoryIcon": "",
              "categoryUrl": "//www.lazada.co.th/shop-large-appliances",
              "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel2TabDTO",
              "categoryName": "Large Appliances",
              "categoryId": "10100871"
            },
            {
              "level3TabList": [
                {
                  "categoryUrl": "//www.lazada.co.th/shop-blenders-mixers-grinders",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//th-live-02.slatic.net/p/12/new-kitchen-tool-garlic-chopper-slicer-cutter-grinder-hand-twistpresser-masher-intl-1485961677-35196311-c86a12e52d358a298abad4525002968c-zoom.jpg",
                  "categoryName": "Food Preparation",
                  "categoryId": "3858"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-rice-cookers",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//th-live-01.slatic.net/p/12/toshiba-rc-18nmfwt-18-1471900292-5557287-13b2e4d4dcddcd316b68290125de7d6d-zoom.jpg",
                  "categoryName": "Rice Cookers",
                  "categoryId": "11766"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-gas-stoves",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//th-live.slatic.net/p/c6cb3dcb32c2118687aaeb0b76f22322.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586649.OTHER_5981320582_4841894",
                  "categoryName": "Gas Stoves",
                  "categoryId": "11819"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-small-electric-grills",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//th-live.slatic.net/original/48dd106af78433f780b54d76ca40b47f.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586649.OTHER_5981320583_4841894",
                  "categoryName": "Electric Contact Grills",
                  "categoryId": "11774"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-juicers-and-fruit-extractors",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//th-live-03.slatic.net/p/12/tefal-ze585h-1461149755-9566506-1-zoom.jpg",
                  "categoryName": "Juicers",
                  "categoryId": "3859"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-coffee-machines",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//laz-img-cdn.alicdn.com/images/ims-web/TB12wx6eXkoBKNjSZFkXXb4tFXa.jpg",
                  "categoryName": "Coffee Machines",
                  "categoryId": "11781"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-air-fryers",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//th-live.slatic.net/p/12/philips-airfryer-hd922020-1498214531-71307662-83ac90eabaf1f21c31e8cd394391b03c-catalog.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586649.OTHER_5981320586_4841894",
                  "categoryName": "Air Fryers",
                  "categoryId": "5476"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-microwaves",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//my-live-03.slatic.net/p/17/fotile-hw25800k-03g-built-in-microwave-oven-1492561846-47265062-5606ee057a40e08bbb8857ed53370890-zoom.jpg",
                  "categoryName": "Microwaves",
                  "categoryId": "11823"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-electric-kettles",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//laz-img-cdn.alicdn.com/images/ims-web/TB10xX0eiAnBKNjSZFvXXaTKXXa.jpg",
                  "categoryName": "Electric Kettles",
                  "categoryId": "5663"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-toasters",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//th-live.slatic.net/p/12/electrolux-ets3505-1447736761-6199822-1-catalog.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586649.OTHER_5981320589_4841894",
                  "categoryName": "Toasters",
                  "categoryId": "11775"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-steamers",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//th-live.slatic.net/p/12/tefal-9-vc1006-4343-52228993-8ff7895eb4e64ad6d53fe9896b683a57-catalog.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586649.OTHER_5981320590_4841894",
                  "categoryName": "Electric Food Steamers",
                  "categoryId": "11768"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-other-ska",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//th-live.slatic.net/p/12/homemate-0807-9650703-616fe75f3953194a41b8b81d19fe0e99-catalog.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586649.OTHER_5981320591_4841894",
                  "categoryName": "Other Appliances",
                  "categoryId": "10100296"
                }
              ],
              "categoryIcon": "",
              "categoryUrl": "//www.lazada.co.th/shop-small-kitchen-appliances",
              "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel2TabDTO",
              "categoryName": "Small Kitchen Appliances",
              "categoryId": "3840"
            },
            {
              "level3TabList": [
                {
                  "categoryUrl": "//www.lazada.co.th/shop-air-purifiers",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//th-live-02.slatic.net/p/12/sharp-ig-dc2b-crystal-red-1496027093-48695812-37831a982b0dfbf00977fc48eb967d85-zoom.jpg",
                  "categoryName": "Air Purifiers",
                  "categoryId": "5578"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-air-coolers",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//th-live-03.slatic.net/p/12/kool-double-kool-ac-801-coolingpack-2-white-1487048803-51474811-04efd5f327db7426c058d24ff738c6f0-zoom.jpg",
                  "categoryName": "Air Coolers",
                  "categoryId": "11804"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-stand-fans",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//th-live.slatic.net/p/12/hatari-ht-s14m3-grey-6890-69644369-4f10a9ffe50d0950475cf3765a34e5d2-catalog.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586649.OTHER_5981320595_4841894",
                  "categoryName": "Stand Fans",
                  "categoryId": "10100302"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-exhaust-fans-2",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//th-live.slatic.net/p/12/mitsubishi-phadlm-rabaay-aakaas-tidphnang-hnaataaekrng-8-niw-run-ex-20skc-siikhaaw-0429-7841973-1373152fec9c2398ddc7af49ed76e6ad-catalog.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586649.OTHER_5981320596_4841894",
                  "categoryName": "Exhaust Fans",
                  "categoryId": "10100300"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-desk-fans",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//th-live-02.slatic.net/p/12/hatari-8-ht-ps20m1-1449633779-1488313-1-catalog.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586649.OTHER_5981320597_4841894",
                  "categoryName": "Desk Fans",
                  "categoryId": "10100299"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-humidifiers",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//th-live-01.slatic.net/p/12/aroma-diffuser-300ml-essential-oil-diffuser-electric-ultrasonic-humidifier-aromatherapy-cool-mist-humidifier-air-purifier-7-color-led-lights-and-timer-settings-whisper-quiet-intl-1507482142-54713983-79f99dba1977045cc3861896be63ed26-zoom.jpg",
                  "categoryName": "Humidifiers",
                  "categoryId": "5580"
                }
              ],
              "categoryIcon": "",
              "categoryUrl": "//www.lazada.co.th/shop-small-cooling-and-air-treatment",
              "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel2TabDTO",
              "categoryName": "Small Cooling & Air treatments",
              "categoryId": "10100295"
            },
            {
              "level3TabList": [
                {
                  "categoryUrl": "//www.lazada.co.th/shop-water-heaters",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//th-live-01.slatic.net/p/12/haier-3500-ei35m-b-1475663965-9813078-2d0a55611f936ff14dc1cf5b7bbbfec2-zoom.jpg",
                  "categoryName": "Water Heaters",
                  "categoryId": "3896"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-heaters",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//th-live.slatic.net/p/56a2ba53adef8a5f0b8ec8ba54e2f9c0.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586649.OTHER_5981320601_4841894",
                  "categoryName": "Electric Heaters",
                  "categoryId": "3897"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-robotic-vacuum-cleaners",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//th-live.slatic.net/p/9e5e3bb99dfe0f11a2efa801410ad752.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586649.OTHER_5981320602_4841894",
                  "categoryName": "Robotic Vacuum Cleaners",
                  "categoryId": "10100311"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-canister-vacuum-cleaners",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//ph-live-01.slatic.net/p/11/high-efficiency-cyclone-separator-with-flange-base-dust-collectorsn50t3-intl-1489173773-61763521-f37af76b368f983e7142d8a6ceef3f88-zoom.jpg",
                  "categoryName": "Canister Vacuum Cleaners",
                  "categoryId": "10100308"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-stick-vacuum-cleaners",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//th-live.slatic.net/p/04c011eab040ff30970d715c43ce5e84.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586649.OTHER_5981320604_4841894",
                  "categoryName": "Stick Vacuum Cleaners",
                  "categoryId": "10100312"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-vacuum-cleaner-parts-accessories",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//th-live-02.slatic.net/p/12/universal-32mm-vacuum-cleaner-carpet-floor-nozzle-brush-attachments-head-tool-black-intl-1508630431-24316475-4656c7a3810f52c3ffa419f5800d7cbb-zoom.jpg",
                  "categoryName": "Vacuum Cleaner Parts & Filters",
                  "categoryId": "11799"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-irons",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//laz-img-cdn.alicdn.com/images/ims-web/TB1UoGlXwZC2uNjSZFnXXaxZpXa.jpg",
                  "categoryName": "Irons",
                  "categoryId": "3879"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-garment-steamers",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//laz-img-cdn.alicdn.com/images/ims-web/TB1ExCqeljTBKNjSZFuXXb0HFXa.jpg",
                  "categoryName": "Garment Steamers",
                  "categoryId": "3880"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-sewing-machines",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//laz-img-cdn.alicdn.com/images/ims-web/TB1mmyjekomBKNjSZFqXXXtqVXa.jpg",
                  "categoryName": "Sewing Machines",
                  "categoryId": "11765"
                }
              ],
              "categoryIcon": "",
              "categoryUrl": "//www.lazada.co.th/shop-small-household-appliances",
              "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel2TabDTO",
              "categoryName": "Small Household Appliances",
              "categoryId": "10100294"
            },
            {
              "level3TabList": [
                {
                  "categoryUrl": "//www.lazada.co.th/shop-hb-hair-styling-appliances",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//laz-img-cdn.alicdn.com/images/ims-web/TB1Mu80ebZnBKNjSZFhXXc.oXXa.jpg",
                  "categoryName": "Hair Styling Appliances",
                  "categoryId": "4347"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-hair-dryers-products",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//th-live.slatic.net/original/6a2e1731677853f1030378007e763b09.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586649.OTHER_5981320612_4841894",
                  "categoryName": "Hair Dryers",
                  "categoryId": "4352"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-hair-removal-appliances",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//th-live.slatic.net/p/mdc/ce6feb2d06f708f5623d7afb63579f3c.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586649.OTHER_5981320613_4841894",
                  "categoryName": "Hair Removal Appliances",
                  "categoryId": "4345"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-mens-shavers",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//th-live.slatic.net/original/029f54cd600d6d0a3d3fa375c8406d01.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586649.OTHER_5981320614_4841894",
                  "categoryName": "Electric Shavers",
                  "categoryId": "13721"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/trimmers-groomers-clippers",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//th-live.slatic.net/p/cd5d57e071217ef600000cd0f13fb429.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586649.OTHER_5981320615_4841894",
                  "categoryName": "Electric Groomer & Trimmers",
                  "categoryId": "13724"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-electric-toothbrushes",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//th-live.slatic.net/p/5/oral-b-vitality-pecision-clean-0659-67828347-7a76e461e4a6ace3c0b47617360e142e-catalog.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586649.OTHER_5981320616_4841894",
                  "categoryName": "Electric Toothbrushes",
                  "categoryId": "4194"
                }
              ],
              "categoryIcon": "",
              "categoryUrl": "//www.lazada.co.th/shop-personal-care-appliances",
              "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel2TabDTO",
              "categoryName": "Personal Care Appliances",
              "categoryId": "10100326"
            },
            {
              "level3TabList": [
                {
                  "categoryUrl": "//www.lazada.co.th/shop-air-purifier-parts-accessories",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//laz-img-cdn.alicdn.com/images/ims-web/TB17aXFcyOYBuNjSsD4XXbSkFXa.jpg",
                  "categoryName": "Air Purifier Replacement Filters",
                  "categoryId": "11801"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-air-purifier-accessories",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//laz-img-cdn.alicdn.com/images/ims-web/TB157GqeljTBKNjSZFuXXb0HFXa.jpg",
                  "categoryName": "Air Purifier Accessories",
                  "categoryId": "6021"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-air-conditioner-parts-accessories",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//th-live.slatic.net/p/df1297cb661ec15106a9dc72049e65af.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586649.OTHER_5981320620_4841894",
                  "categoryName": "Air Conditioner Parts",
                  "categoryId": "11803"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-air-conditioner-accessories",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//laz-img-cdn.alicdn.com/images/ims-web/TB1EGmmXwZC2uNjSZFnXXaxZpXa.jpg",
                  "categoryName": "Air Conditioner Accessories",
                  "categoryId": "5856"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-fan-accessories",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//laz-img-cdn.alicdn.com/images/ims-web/TB1m8R0eiAnBKNjSZFvXXaTKXXa.jpg",
                  "categoryName": "Fan Parts & Accessories",
                  "categoryId": "6023"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-blender-and-mixer-accessories",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//laz-img-cdn.alicdn.com/images/ims-web/TB1obCmXwZC2uNjSZFnXXaxZpXa.jpg",
                  "categoryName": "Small Kitchen Appliance Parts & Accessories",
                  "categoryId": "6080"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-coffee-accessories-parts",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//my-live-02.slatic.net/p/dcc184c2d21d36ba76c936a0e22599b3.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586649.OTHER_5981320624_4841894",
                  "categoryName": "Coffee Machine Parts & Accessories",
                  "categoryId": "5657"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-water-filters",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//th-live.slatic.net/original/090a93cfe3cc0263c4a1d65505824af9.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586649.OTHER_5981320625_4841894",
                  "categoryName": "Water Purifier Replacement Filters & Parts",
                  "categoryId": "11827"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-washer-and-dryer-accessories",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//laz-img-cdn.alicdn.com/images/ims-web/TB1VaWmXwZC2uNjSZFnXXaxZpXa.jpg",
                  "categoryName": "Washer & Dryer Parts & Accessories",
                  "categoryId": "6075"
                }
              ],
              "categoryIcon": "",
              "categoryUrl": "//www.lazada.co.th/shop-home-appliance-accesories",
              "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel2TabDTO",
              "categoryName": "Parts & Accessories",
              "categoryId": "5855"
            }
          ],
          "categoryName_zh": "",
          "categoryIcon": "ic-cat-ConsumerAppli &#xe73e;",
          "id": "6634010",
          "position": "top",
          "childId": "Level_1_Category_No3",
          "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel1TabDTO",
          "categoryName": "TV & Home Appliances",
          "level1CategoryId": "6634010"
        },
        {
          "level2TabList": [
            {
              "level3TabList": [
                {
                  "categoryUrl": "//www.lazada.co.th/shop-skincare-face-treatments-serums",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//th-live.slatic.net/p/5/estee-lauder-advanced-night-repair-synchronized-recovery-complex-ii-15ml-7905-56540701-d28b5e4ede7fa86e0b363f5711b39882-catalog.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586650.OTHER_5975741205_4746300",
                  "categoryName": "Serum & Essence",
                  "categoryId": "5891"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-facial-moisturizers",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//th-live.slatic.net/p/5/olay-regenerist-micro-sculpting-cream-10g-1267-02910527-bc6a162956f626b633be75f6fa1ba00e-catalog.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586650.OTHER_5975741206_4746300",
                  "categoryName": "Moisturizers and Cream",
                  "categoryId": "10100737"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-dermacare",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//th-live.slatic.net/p/5a1f98731e887afa80fc7bc99a3a215e.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586650.OTHER_5975741207_4746300",
                  "categoryName": "Dermacare",
                  "categoryId": "7295"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-face-cleanser",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//th-live.slatic.net/original/3a94a745e5d6e7c2b3056e53ca05e84f.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586650.OTHER_5975741208_4746300",
                  "categoryName": "Facial Cleansers",
                  "categoryId": "5873"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-skincare-toner-and-mists",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//th-live.slatic.net/p/c685a2d5dac29de0dcf555cbbaa05f82.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586650.OTHER_5975741209_4746300",
                  "categoryName": "Toner & Mists",
                  "categoryId": "5890"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-skincare-face-mask-packs",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//th-live.slatic.net/original/93614c041c805a4967db1a0caebdd50e.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586650.OTHER_5975741210_4746300",
                  "categoryName": "Face Mask & Packs",
                  "categoryId": "5870"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-eye-treatment",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//th-live.slatic.net/original/7c53eeecd8583a5c8334343aec220fae.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586650.OTHER_5975741211_4746300",
                  "categoryName": "Eye Care",
                  "categoryId": "10100734"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-skincare-sunscreen-aftersun-lotion",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//th-live.slatic.net/p/1ed8a4eefaa6f8df3dd681ee4916e8a5.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586650.OTHER_5975741212_4746300",
                  "categoryName": "Sunscreen and Aftersun",
                  "categoryId": "5885"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-lip-balm-and-treatment",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//th-live.slatic.net/p/057ecc0b0e68a0efa58816110f97076d.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586650.OTHER_5975741213_4746300",
                  "categoryName": "Lip Balm and Treatment",
                  "categoryId": "13555"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-skincare-face-scrubs-peels",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//th-live.slatic.net/p/8df0aa69c9a4335eeafdf0d7593e97f5.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586650.OTHER_5975741214_4746300",
                  "categoryName": "Face Scrubs & Exfoliators",
                  "categoryId": "5872"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-bath-and-body-sets",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//th-live.slatic.net/p/7b8776bc819cf778f03463a8ca97db0c.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586650.OTHER_5975741215_4746300",
                  "categoryName": "Gifts & Value Sets",
                  "categoryId": "4320"
                }
              ],
              "categoryIcon": "",
              "categoryUrl": "//www.lazada.co.th/shop-face-products",
              "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel2TabDTO",
              "categoryName": "Skincare",
              "categoryId": "4079"
            },
            {
              "level3TabList": [
                {
                  "categoryUrl": "//www.lazada.co.th/shop-face",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//th-live.slatic.net/original/a93f5510ce254168a5f17fc3cbbda246.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586650.OTHER_5975741217_4746300",
                  "categoryName": "Face",
                  "categoryId": "4091"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-lips",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//th-live.slatic.net/p/73749515d0d392f70caea5dee36038fe.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586650.OTHER_5975741218_4746300",
                  "categoryName": "Lips",
                  "categoryId": "4092"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-eyes",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//th-live.slatic.net/p/45de626faad2d5b46060313908a3ace2.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586650.OTHER_5975741219_4746300",
                  "categoryName": "Eyes",
                  "categoryId": "4093"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-blushes",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//th-live.slatic.net/original/013111ba144778196ad282fbdf9a32ea.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586650.OTHER_5975741220_4746300",
                  "categoryName": "Cheek",
                  "categoryId": "4101"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-nails",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//th-live.slatic.net/original/84bce9f5369abdb27ae3c88bd5b7901c.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586650.OTHER_5975741221_4746300",
                  "categoryName": "Nails",
                  "categoryId": "4094"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-compacts-powder",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//th-live.slatic.net/p/f6085e17fca3b5b51df30f44c6d44e3d.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586650.OTHER_5975741222_4746300",
                  "categoryName": "Compacts & Powder",
                  "categoryId": "4100"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-makeup-palettes-and-sets",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//th-live.slatic.net/p/a12a849cd5de0101f5778d228bde5947.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586650.OTHER_5975741223_4746300",
                  "categoryName": "Makeup Palettes & Sets",
                  "categoryId": "10100740"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-makeup-accessories",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//sg-live-02.slatic.net/original/0f98b4d7b406eb21358524bc73c34118.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586650.OTHER_5975741224_4746300",
                  "categoryName": "Brushes & Accessories",
                  "categoryId": "4098"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-makeup-bags-organizers",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//th-live.slatic.net/original/70bcc166d43588bf0c561feea3951a5e.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586650.OTHER_5975741225_4746300",
                  "categoryName": "Makeup Bags & Organizers",
                  "categoryId": "4133"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-makeup-removers",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//th-live.slatic.net/p/5/bioderma-sensibio-h2o-echdekhruue-ngsam-aang-samhrabphiwaephngaay-500-ml-1316-44112331-b5dffedd751aa9b1af5f6f8011e06b85-catalog.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586650.OTHER_5975741226_4746300",
                  "categoryName": "Makeup Removers",
                  "categoryId": "4096"
                }
              ],
              "categoryIcon": "",
              "categoryUrl": "//www.lazada.co.th/shop-makeup",
              "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel2TabDTO",
              "categoryName": "Make-Up",
              "categoryId": "4078"
            },
            {
              "level3TabList": [
                {
                  "categoryUrl": "//www.lazada.co.th/shop-conditioners",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//th-live.slatic.net/p/5/rejoice-riicch-ys-aechmphuu-3-in1-900-ml-2880-9571147-51edfe2970cd1d3131db756c19f41cb4-catalog.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586650.OTHER_5975741228_4746300",
                  "categoryName": "Shampoo",
                  "categoryId": "4169"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-hair-treatments",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//th-live.slatic.net/p/26300e6eeaf3572e1e4b91c1b71f3bdc.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586650.OTHER_5975741229_4746300",
                  "categoryName": "Hair Treatments",
                  "categoryId": "4172"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-wig-hair-extensions-pads",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//th-live.slatic.net/p/5/mannequin-manikin-training-head-with-synthetic-fiber-long-hairtable-clamp-holder-for-cosmetology-student-hairdressing-cuttingbraiding-practice-maroon-intl-6133-51305253-dd5f7a88c2f428230318d51697b4f69b-catalog.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586650.OTHER_5975741230_4746300",
                  "categoryName": "Wig & Hair Extensions & Pads",
                  "categoryId": "4192"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-hair-colors",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//th-live.slatic.net/original/8f040b662e1701ea509823b0e9417833.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586650.OTHER_5975741231_4746300",
                  "categoryName": "Hair Coloring",
                  "categoryId": "4173"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-hair-styling",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//th-live.slatic.net/p/f169738c749433cb3004328fa05bd952.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586650.OTHER_5975741232_4746300",
                  "categoryName": "Hair Styling",
                  "categoryId": "4170"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-conditioners-2",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//th-live.slatic.net/p/cd71ebb87babe37559fa2746d53df39b.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586650.OTHER_5975741233_4746300",
                  "categoryName": "Hair Conditioner",
                  "categoryId": "13559"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-hair-brushes-combs",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//th-live.slatic.net/original/6a7606a009d6e8aa518b30750306c0a6.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586650.OTHER_5975741234_4746300",
                  "categoryName": "Hair Brushes & Combs",
                  "categoryId": "9016"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-hair-accessories",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//my-live-02.slatic.net/p/13bde14eac753a1426518ef32fe20ecf.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586650.OTHER_5975741235_4746300",
                  "categoryName": "Hair Accessories",
                  "categoryId": "9017"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-bath-and-body-sets",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//th-live.slatic.net/p/7b8776bc819cf778f03463a8ca97db0c.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586650.OTHER_5975741236_4746300",
                  "categoryName": "Gifts & Value Sets",
                  "categoryId": "4320"
                }
              ],
              "categoryIcon": "",
              "categoryUrl": "//www.lazada.co.th/shop-hair-care",
              "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel2TabDTO",
              "categoryName": "Hair Care",
              "categoryId": "4081"
            },
            {
              "level3TabList": [
                {
                  "categoryUrl": "//www.lazada.co.th/shop-HealthBeauty-BathBody-BodySoapsShowerGels-BodyWash",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//th-live.slatic.net/p/5/laks-khriim-aabnam-ch-fth-thach-siichmphuu-500-ml-aela-laks-khriim-aabnam-ch-fth-thach-siichmphuu-chnidetim-450-ml-4092-8050108-38af58b5bd0b4afc06cd219f7fd097db-catalog.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586650.OTHER_5975741238_4746300",
                  "categoryName": "Body Soaps & Shower Gels",
                  "categoryId": "14560"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-moisturizer-and-creams",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//th-live.slatic.net/original/1ef1875672d0cf04d5825e8b363de1c0.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586650.OTHER_5975741239_4746300",
                  "categoryName": "Body Moisturizers",
                  "categoryId": "4134"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-body-and-essential-oils",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//th-live.slatic.net/p/chaokoh-100-200-ml-1-1862-6756921-1-catalog.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586650.OTHER_5975741240_4746300",
                  "categoryName": "Body & Massage Oils",
                  "categoryId": "4144"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-sun-protection",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//th-live.slatic.net/p/5/khriimkanaeddthaataw-baanaanaaobth-banana-boat-ultra-protect-sunscreen-lotion-spf50-pa-90ml-5586-47431051-31055486c24098c9554d030971c3183f-catalog.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586650.OTHER_5975741241_4746300",
                  "categoryName": "Sun Care for Body",
                  "categoryId": "8935"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-body-scrubs",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//th-live.slatic.net/original/2826f6f2299c23cad405001f803bc6d4.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586650.OTHER_5975741242_4746300",
                  "categoryName": "Body Scrubs",
                  "categoryId": "4142"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-hand-care",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//th-live.slatic.net/p/5/jergensjergens-hand-andamp-nail-cream-extra-dry-skin-moisturiserecch-rekns-khriimthaamuue-100ml-1hl-d-6686-0896127-83ade0ddce8ff7f247d6b890a761693c-catalog.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586650.OTHER_5975741243_4746300",
                  "categoryName": "Hand Care",
                  "categoryId": "13551"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-foot-care",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//th-live.slatic.net/p/5/scholl-velvet-smooth-express-pedi-4873-92398587-d1736b1782044e913ca0d536b81eb580-catalog.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586650.OTHER_5975741244_4746300",
                  "categoryName": "Foot Care",
                  "categoryId": "13553"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-hair-removal",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//th-live.slatic.net/p/444820c9e2aac049225b0b315184596a.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586650.OTHER_5975741245_4746300",
                  "categoryName": "Hair Removal",
                  "categoryId": "4145"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-body-breast-care",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//th-live.slatic.net/original/bb78491679cc0a4037316f83395b589a.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586650.OTHER_5975741246_4746300",
                  "categoryName": "Breast Care",
                  "categoryId": "8940"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-bath-and-body-accessories",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//th-live.slatic.net/original/7ce8925ee28e7d2aee1ce3e41aa3c8d6.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586650.OTHER_5975741247_4746300",
                  "categoryName": "Bath & Body Accessories",
                  "categoryId": "4147"
                }
              ],
              "categoryIcon": "",
              "categoryUrl": "//www.lazada.co.th/shop-bath-body",
              "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel2TabDTO",
              "categoryName": "Bath & Body",
              "categoryId": "4080"
            },
            {
              "level3TabList": [
                {
                  "categoryUrl": "//www.lazada.co.th/shop-mens-oral-care",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//th-live.slatic.net/p/mdc/c6747f8b359dea9ca02a28964e95c5cc.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586650.OTHER_5975741249_4746300",
                  "categoryName": "Oral Care",
                  "categoryId": "4175"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-personal-optical-care",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//th-live.slatic.net/p/4780239ab4064bf57dfb29d4f5dcdbd6.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586650.OTHER_5975741250_4746300",
                  "categoryName": "Eye Care",
                  "categoryId": "10100746"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-deodorants",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//th-live.slatic.net/p/5/nivea-diio-ephirl-ae-nd-biwtii-orl-n-50-ml-3472-1471164-9c435bdab80794b291e59c5efd9a97e7-catalog.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586650.OTHER_5975741251_4746300",
                  "categoryName": "Deodorants",
                  "categoryId": "4176"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-womans-hygiene",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//th-live.slatic.net/original/9419d7ad14e62a7d141a3236776d313f.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586650.OTHER_5975741252_4746300",
                  "categoryName": "Feminine Care",
                  "categoryId": "4177"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-sexual-wellness-personal-safety-security",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//th-live.slatic.net/p/5/80-2927-12813776-250a7a9008f02ba40c3fcc4806fa3000-catalog.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586650.OTHER_5975741253_4746300",
                  "categoryName": "Personal Safety & Security",
                  "categoryId": "4307"
                }
              ],
              "categoryIcon": "",
              "categoryUrl": "//www.lazada.co.th/shop-personal-care",
              "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel2TabDTO",
              "categoryName": "Personal Care",
              "categoryId": "4082"
            },
            {
              "level3TabList": [
                {
                  "categoryUrl": "//www.lazada.co.th/shop-women-fragrance",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//th-live.slatic.net/p/01709510030945f46d2a3eb31f788bab.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586650.OTHER_5975741255_4746300",
                  "categoryName": "Women Fragrances",
                  "categoryId": "13556"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-men-fragrance",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//th-live.slatic.net/p/5/davidoff-davidoff-cool-water-for-men-125-ml-9007-0917434-c03acfa7911e20fa85fe82ad47e91f3b-catalog.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586650.OTHER_5975741256_4746300",
                  "categoryName": "Men Fragrances",
                  "categoryId": "13557"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-unisex-fragrance",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//th-live.slatic.net/p/dba79210de99e52c030521f1eee45128.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586650.OTHER_5975741257_4746300",
                  "categoryName": "Unisex Fragrances",
                  "categoryId": "13558"
                }
              ],
              "categoryIcon": "",
              "categoryUrl": "//www.lazada.co.th/shop-fragrances",
              "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel2TabDTO",
              "categoryName": "Fragrances",
              "categoryId": "4083"
            },
            {
              "level3TabList": [
                {
                  "categoryUrl": "//www.lazada.co.th/shop-spa-products",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//th-live.slatic.net/original/b5ffd1138819fc0f1fd0afe6fb9e6e9c.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586650.OTHER_5975741259_4746300",
                  "categoryName": "Portable Sauna",
                  "categoryId": "9024"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-body-slimming-electric-massagers",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//th-live.slatic.net/p/c4718a9a3d4b62715d2e99cfbdcb9811.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586650.OTHER_5975741260_4746300",
                  "categoryName": "Body Slimming & Massagers",
                  "categoryId": "9022"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-body-skin-care-tools",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//th-live.slatic.net/p/5/watsons-1-2425-60768372-f20406155999e59339c5270024f6f471-catalog.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586650.OTHER_5975741261_4746300",
                  "categoryName": "Body Skin Care Tools",
                  "categoryId": "10100739"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-face-skin-care-tools",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//th-live.slatic.net/p/32d4bdc98125e1ec88d4e4a693c78d38.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586650.OTHER_5975741262_4746300",
                  "categoryName": "Face Skin Care Tools",
                  "categoryId": "10100738"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-foot-relief",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//th-live-02.slatic.net/p/5/3-0703-60300778-74ab3f9f21fbd4f237d5f669dbf2ad97-catalog.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586650.OTHER_5975741263_4746300",
                  "categoryName": "Foot Relief Tools",
                  "categoryId": "13560"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-hb-shavers-trimmers-accessories",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//th-live.slatic.net/p/911709e03382f6cd41e6ac9f45315d3a.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586650.OTHER_5975741264_4746300",
                  "categoryName": "Hair Removal Accessories",
                  "categoryId": "4346"
                }
              ],
              "categoryIcon": "",
              "categoryUrl": "//www.lazada.co.th/shop-health-beauty-tools",
              "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel2TabDTO",
              "categoryName": "Beauty Tools",
              "categoryId": "4085"
            },
            {
              "level3TabList": [
                {
                  "categoryUrl": "//www.lazada.co.th/shop-body-care",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//th-live.slatic.net/p/5/nivea-emn-b-dii-aiwthethnning-6482-8488605-063a1ed053128c91e499976c447ecbc2-catalog.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586650.OTHER_5975741266_4746300",
                  "categoryName": "Bath & Body",
                  "categoryId": "13565"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-face-care",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//th-live.slatic.net/p/e483e7394f292698b3ccce4634ba145c.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586650.OTHER_5975741267_4746300",
                  "categoryName": "Skin Care",
                  "categoryId": "13563"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-mens-shaving",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//th-live.slatic.net/p/5/gillette-mach-3-turbo-1510722006-37978576-b3584cfcc65631021a4fdcbbfcd31cc0-catalog.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586650.OTHER_5975741268_4746300",
                  "categoryName": "Shaving & Grooming",
                  "categoryId": "13564"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-mens-hair-care",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//th-live.slatic.net/p/c317897f45b77197a4ba2de90ddf5e34.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586650.OTHER_5975741269_4746300",
                  "categoryName": "Hair Care",
                  "categoryId": "4224"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-men-deodorant",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//th-live.slatic.net/p/5/ae-kch-sepry-aeblkh-150-ml-2-khwd-4088-4440108-72f4dc72da2d4a1de985affb92bfb485-catalog.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586650.OTHER_5975741270_4746300",
                  "categoryName": "Deodorants",
                  "categoryId": "13562"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-sexual-wellness-condoms",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//th-live.slatic.net/original/8c2a305212f4634b995d1703447adf76.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586650.OTHER_5975741271_4746300",
                  "categoryName": "Condoms",
                  "categoryId": "5394"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-sexual-wellness-lubricants",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//th-live.slatic.net/p/efe79837b769205d3f6a87ed219b4c5b.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586650.OTHER_5975741272_4746300",
                  "categoryName": "Lubricants",
                  "categoryId": "5406"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-sexual-health",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//th-live.slatic.net/original/57e5f527703f9bb2ec0b6b6e40415919.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586650.OTHER_5975741273_4746300",
                  "categoryName": "Sexual Health Vitamins",
                  "categoryId": "6968"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-sports-nutrition-supplement",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//th-live.slatic.net/p/optimum-whey-gold-standard-5-15lbs-strawberry-banana-4218-5795016-4f4dd17c3deaad57b960a0df740bd26c-catalog.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586650.OTHER_5975741274_4746300",
                  "categoryName": "Sports Nutrition",
                  "categoryId": "8997"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-mens-health",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//th-live.slatic.net/p/af4abb4159cd7b0a57839dd1a173798a.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586650.OTHER_5975741275_4746300",
                  "categoryName": "Men's Health Supplements",
                  "categoryId": "6970"
                }
              ],
              "categoryIcon": "",
              "categoryUrl": "//www.lazada.co.th/shop-mens-care",
              "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel2TabDTO",
              "categoryName": "Men's Care",
              "categoryId": "4084"
            },
            {
              "level3TabList": [
                {
                  "categoryUrl": "//www.lazada.co.th/shop-health-well-being",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//th-live.slatic.net/p/0bbb6f137752c044f84d684c137e6ac2.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586650.OTHER_5975741277_4746300",
                  "categoryName": "Well Being",
                  "categoryId": "8977"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-immune-system",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//th-live.slatic.net/original/88fa01b57aac061fd17fb069f0cbe2e8.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586650.OTHER_5975741278_4746300",
                  "categoryName": "Immunity",
                  "categoryId": "8987"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-bones-joints",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//th-live.slatic.net/p/0e81bdf137fef68bd586cd537f8c5b78.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586650.OTHER_5975741279_4746300",
                  "categoryName": "Bone & Joint Support",
                  "categoryId": "8980"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-brain-memory",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//th-live.slatic.net/p/vistra-salmon-fish-oil-75-tablets-wisthraa-nammanplaaaechlm-n-75-emd-4542-3904468-62bd096424cca53ca2717a9cf6c107ab-catalog.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586650.OTHER_5975741280_4746300",
                  "categoryName": "Brain & Memory",
                  "categoryId": "8981"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-liver-detox",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//th-live.slatic.net/p/681d95a5ac34b482a845aa862b5dbadc.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586650.OTHER_5975741281_4746300",
                  "categoryName": "Detoxification",
                  "categoryId": "8989"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-health-weight-loss",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//th-live.slatic.net/p/0274f62dac609071cdb49ce1e976db2d.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586650.OTHER_5975741282_4746300",
                  "categoryName": "Weight Management",
                  "categoryId": "8956"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-fat-burners",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//th-live.slatic.net/p/5/verena-sure-800-30-1-6616-72734712-06ad1407496f1705bb3ccd4f58ca6de9-catalog.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586650.OTHER_5975741283_4746300",
                  "categoryName": "Fat Blockers & Burners",
                  "categoryId": "13696"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-appetite-suppressants",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//th-live.slatic.net/p/5/chame-sye-s-plus-10-1-8028-09500179-c9768905a4f769e3178252161b0fc225-catalog.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586650.OTHER_5975741284_4746300",
                  "categoryName": "Appetite Suppressant",
                  "categoryId": "8957"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-skin-supplements",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//th-live.slatic.net/p/866b6b474b3f05649cc5ccae61aa5ea3.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586650.OTHER_5975741285_4746300",
                  "categoryName": "Skin Nourishment",
                  "categoryId": "8975"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-whitening-supplements",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//th-live.slatic.net/p/fb389dbcfd97d15c6fbf297c5d03b5f0.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586650.OTHER_5975741286_4746300",
                  "categoryName": "Whitening",
                  "categoryId": "8976"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-protein",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//th-live.slatic.net/p/optimum-whey-gold-standard-5-15lbs-strawberry-banana-4218-5795016-4f4dd17c3deaad57b960a0df740bd26c-catalog.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586650.OTHER_5975741287_4746300",
                  "categoryName": "Protein",
                  "categoryId": "13700"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-weight-gain-supplements",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//th-live.slatic.net/p/5/dymatize-super-mass-gainer-6-lbs-3821-38670441-91296680285fe8900d7f51c51b2c4cf3-catalog.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586650.OTHER_5975741288_4746300",
                  "categoryName": "Mass Gainer",
                  "categoryId": "9006"
                }
              ],
              "categoryIcon": "",
              "categoryUrl": "//www.lazada.co.th/shop-health-food-supplements-weight-management",
              "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel2TabDTO",
              "categoryName": "Vitamin & Supplements",
              "categoryId": "4087"
            },
            {
              "level3TabList": [
                {
                  "categoryUrl": "//www.lazada.co.th/shop-health-blood-pressure-monitors",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//th-live.slatic.net/p/977228f360af3c74f14346b62955da80.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586650.OTHER_5975741290_4746300",
                  "categoryName": "Blood Pressure Monitor",
                  "categoryId": "9053"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-glucose-level-analyzer-monitors",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//th-live.slatic.net/p/da6eb215859b4f6b26ff8e98c3944b99.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586650.OTHER_5975741291_4746300",
                  "categoryName": "Blood Glucose Monitor",
                  "categoryId": "9054"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-health-accessories",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//th-live.slatic.net/p/5/beurer-ekhruue-ngchwyfang-aichngaay-namhnakebaa-phlitcchaak-german-run-ha20-2967-64328331-c224ba72105cb3fd4a222c078b2f4f59-catalog.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586650.OTHER_5975741292_4746300",
                  "categoryName": "Health Accessories",
                  "categoryId": "4291"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-wheelchairs",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//th-live.slatic.net/p/5/kt-rthekhnphuupwykhnchraa-wheelchair-khnaek-wiilaechr-phabaid-kt907eb-laaysk-tnamenginehluue-ng-3050-7571973-9074f58a288796baebf57ce5be2ddc07-catalog.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586650.OTHER_5975741293_4746300",
                  "categoryName": "Wheelchairs",
                  "categoryId": "4794"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-hospital-beds",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//th-live.slatic.net/p/e9d6959e55c89fa9829ac516ad2dc0d6.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586650.OTHER_5975741294_4746300",
                  "categoryName": "Hospital Beds",
                  "categoryId": "4795"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-injury-support-and-braces",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//th-live.slatic.net/p/futuro-stabilizing-knee-size-l-upkrnphyungekhaa-fuuthuuor-esrimaeknaichslrun46165-2814-2043067-268c8030355deea12c9f34561e0296c2-catalog.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586650.OTHER_5975741295_4746300",
                  "categoryName": "Injury Support and Braces",
                  "categoryId": "4271"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-first-aid-supplies",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//th-live.slatic.net/p/395bd93c8f63bb388c855b8b0ae564cf.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586650.OTHER_5975741296_4746300",
                  "categoryName": "First Aid Supplies",
                  "categoryId": "4280"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-scale-body-fat-analyzers-monitors",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//th-live.slatic.net/p/5/omron-jpn2-made-in-japan-adapteromron-omron-7605-56726421-7310698b63d69c0cd7fb0606fee045df-catalog.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586650.OTHER_5975741297_4746300",
                  "categoryName": "Scale & Body Fat Analyzers",
                  "categoryId": "9058"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-nebulizer-aspirators",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//th-live-02.slatic.net/p/5/beurer-ih26-1-3-9516-92928287-1c2660f548d23321a338ebfb16e6d92f-catalog.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586650.OTHER_5975741298_4746300",
                  "categoryName": "Nebulizer & Aspirators",
                  "categoryId": "4286"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-thermometer",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//th-live.slatic.net/p/5/omron-digital-thermometerpr-thdicchit-l-runmc-245-0010-65999411-2b47f68345051fc07dd54309df19ba34-catalog.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586650.OTHER_5975741299_4746300",
                  "categoryName": "Thermometers",
                  "categoryId": "6131"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-healthbeauty-medicalsupplies-firstaidsupplies-ointmentsandcreams",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//th-live.slatic.net/p/59aa77ca9e68e69bc8629a7aa4a907b2.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586650.OTHER_5975741300_4746300",
                  "categoryName": "Ointments & Creams",
                  "categoryId": "14568"
                }
              ],
              "categoryIcon": "",
              "categoryUrl": "//www.lazada.co.th/shop-medical-equipment",
              "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel2TabDTO",
              "categoryName": "Medical Supplies",
              "categoryId": "4274"
            },
            {
              "level3TabList": "",
              "categoryIcon": "",
              "categoryUrl": "//www.lazada.co.th/shop-senior-health",
              "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel2TabDTO",
              "categoryName": "Adult Diapers & Incontinence",
              "categoryId": "9044"
            },
            {
              "level3TabList": [
                {
                  "categoryUrl": "//www.lazada.co.th/shop-sexual-wellness-condoms",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//th-live.slatic.net/original/8c2a305212f4634b995d1703447adf76.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586650.OTHER_5975741303_4746300",
                  "categoryName": "Condoms",
                  "categoryId": "5394"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-sexual-wellness-lubricants",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//th-live.slatic.net/p/efe79837b769205d3f6a87ed219b4c5b.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586650.OTHER_5975741304_4746300",
                  "categoryName": "Lubricants",
                  "categoryId": "5406"
                }
              ],
              "categoryIcon": "",
              "categoryUrl": "//www.lazada.co.th/shop-sexual-wellness",
              "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel2TabDTO",
              "categoryName": "Condoms & Lubricants",
              "categoryId": "6237"
            }
          ],
          "categoryName_zh": "",
          "categoryIcon": "ic-cat-HealthBeauty &#xe75b;",
          "id": "6634011",
          "position": "top",
          "childId": "Level_1_Category_No4",
          "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel1TabDTO",
          "categoryName": "Health & Beauty ",
          "level1CategoryId": "6634011"
        },
        {
          "level2TabList": [
            {
              "level3TabList": [
                {
                  "categoryUrl": "//www.lazada.co.th/shop-baby-nasal-aspirators",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//th-live.slatic.net/p/c533d92804d3d6a8c6d160a1327e03c3.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586651.OTHER_5982917446_4874068",
                  "categoryName": "Nasal Aspirators",
                  "categoryId": "14194"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-baby-thermometers",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//my-live.slatic.net/original/863fec6ad5d6c390497606e0aff06797.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586651.OTHER_5982917447_4874068",
                  "categoryName": "Thermometers",
                  "categoryId": "14197"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-baby-nail-care",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//th-live.slatic.net/p/01679ed4a04f5f1ec199f7927dc41920.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586651.OTHER_5982917448_4874068",
                  "categoryName": "Nail Care",
                  "categoryId": "14193"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-mask-repellents",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//th-live.slatic.net/p/02f25b337bc90aee9b131849e9b84b94.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586651.OTHER_5982917449_4874068",
                  "categoryName": "Masks & Repellents",
                  "categoryId": "14198"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-baby-crib-netting",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//my-live-02.slatic.net/original/3260a82bd6967a34063bf06ca03939e5.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586651.OTHER_5982917450_4874068",
                  "categoryName": "Crib Netting",
                  "categoryId": "14203"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-baby-monitors",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//my-live-02.slatic.net/p/31a90200862a66ea4840156c8225b188.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586651.OTHER_5982917451_4874068",
                  "categoryName": "Baby Monitors",
                  "categoryId": "14207"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-baby-rail-guards",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//th-live.slatic.net/p/4/myoshin-thiikanetiiyng-khnaad-150-cm-siikhaawlaayhmii-8421-30393231-8ecc1692e587497e1e91df29f528c2d4-catalog.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586651.OTHER_5982917452_4874068",
                  "categoryName": "Rails & Rail Guards",
                  "categoryId": "14208"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-baby-gifts",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//th-live.slatic.net/p/4/morestech-18-0796-35544074-f3d414eab121ddad2cd11d786d36eab1-catalog.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586651.OTHER_5982917453_4874068",
                  "categoryName": "Gifts",
                  "categoryId": "7964"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-maternity-wear",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//th-live.slatic.net/p/704c6e6b3a302f174a1d688e2ddefb7a.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586651.OTHER_5982917454_4874068",
                  "categoryName": "Maternity Wear",
                  "categoryId": "14213"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-pregnancy-pillows",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//th-live.slatic.net/p/06969dd665562baf4c9d412fb4cd77aa.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586651.OTHER_5982917455_4874068",
                  "categoryName": "Pregnancy Pillows",
                  "categoryId": "6476"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-maternity-accessories",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//th-live.slatic.net/p/083489e0b8ab4beba1ac2a7b239aeeb4.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586651.OTHER_5982917456_4874068",
                  "categoryName": "Maternity Accessories",
                  "categoryId": "3691"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-pacifiers-and-accessories",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//th-live.slatic.net/p/4/avent-soother-night-time-0-6m-2-7706-14155878-2cd97d9017a4eb02ccaaf10e6c0ea78d-catalog.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586651.OTHER_5982917457_4874068",
                  "categoryName": "Pacifiers & Accessories",
                  "categoryId": "7040"
                }
              ],
              "categoryIcon": "",
              "categoryUrl": "//www.lazada.co.th/shop-babies",
              "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel2TabDTO",
              "categoryName": "Mother & Baby",
              "categoryId": "5090"
            },
            {
              "level3TabList": [
                {
                  "categoryUrl": "//www.lazada.co.th/shop-diapers",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//th-live.slatic.net/p/f6cdd0b4070e4250b1503cd5f034c97d.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586651.OTHER_5982917458_4874068",
                  "categoryName": "Disposable Diapers",
                  "categoryId": "7232"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-nappies",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//th-live.slatic.net/p/4/babykids95-kaangekngphaa-mkannam-tpu-aephnchabchaaokhlhnaa5chan-6taw-6aephn-khlasii-7047-59318601-c1b97812ab96c06ca2ee404b0417744f-catalog.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586651.OTHER_5982917459_4874068",
                  "categoryName": "Cloth Diapers",
                  "categoryId": "3607"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-baby-wipes-refills",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//th-live.slatic.net/p/98e6f26a5f306951d5c35de36eaf8151.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586651.OTHER_5982917460_4874068",
                  "categoryName": "Wipes & Refills",
                  "categoryId": "5598"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-diapering-care",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//th-live.slatic.net/p/d1e824863f215a7697b6cdba2298d797.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586651.OTHER_5982917461_4874068",
                  "categoryName": "Diapering Care",
                  "categoryId": "7460"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-potty-seats",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//my-live-02.slatic.net/p/8c51a5efe1c5500cf4625f193e17f659.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586651.OTHER_5982917462_4874068",
                  "categoryName": "Potty Seats",
                  "categoryId": "14246"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-babies-diaper-bags",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//th-live.slatic.net/p/7/baby-life-2017-5-4047-13098976-a697997c0cd5c78dcf8fb83a6ad6ad75-catalog.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586651.OTHER_5982917463_4874068",
                  "categoryName": "Diaper Bags",
                  "categoryId": "5765"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-baby-changing-tables",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//th-live.slatic.net/p/d1e824863f215a7697b6cdba2298d797.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586651.OTHER_5982917464_4874068",
                  "categoryName": "Changing Tables",
                  "categoryId": "6730"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-diaper-changing-mats",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//th-live.slatic.net/p/9rak-jx810-5840-4008101-1-catalog.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586651.OTHER_5982917465_4874068",
                  "categoryName": "Pads & Covers",
                  "categoryId": "6731"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-cloth-diaper-inserts-and-liners",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//my-live-02.slatic.net/p/4f7889f09885b9d5fcaeeb9636d6dd63.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586651.OTHER_5982917466_4874068",
                  "categoryName": "Inserts & Liners",
                  "categoryId": "3609"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-potty-chair",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//th-live.slatic.net/original/954d9b4134b60ac65985ebc3661b78ce.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586651.OTHER_5982917467_4874068",
                  "categoryName": "Potty Chair",
                  "categoryId": "14245"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-nursery-step-stools",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//th-live.slatic.net/p/e29183cf8975ec746024d8c417a372f8.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586651.OTHER_5982917468_4874068",
                  "categoryName": "Step Stools",
                  "categoryId": "14247"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-stackers-caddies",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//my-live-02.slatic.net/p/4/baby-diaper-caddy-organizer-nursery-storage-bin-for-diapers-baby-wipes-kid-toys-portable-storage-basket-for-car-travel-changing-table-organizer-baby-shower-gift-newborn-registry-must-haves-1217-939538951-4daa058ef9df28cdfbac5df885e77f88-.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586651.OTHER_5982917469_4874068",
                  "categoryName": "Stackers & Caddies",
                  "categoryId": "14177"
                }
              ],
              "categoryIcon": "",
              "categoryUrl": "//www.lazada.co.th/shop-diapers-potties",
              "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel2TabDTO",
              "categoryName": "Diapering & Potty",
              "categoryId": "2975"
            },
            {
              "level3TabList": [
                {
                  "categoryUrl": "//www.lazada.co.th/shop-maternal-milk-formula",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//th-live.slatic.net/p/mdc/639bcf0a7be19036b7d1aca6fcb5168e.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586651.OTHER_5982917470_4874068",
                  "categoryName": "Maternal",
                  "categoryId": "2968"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-infant-milk-formula",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//th-live.slatic.net/p/b9b5c8bd195c4be920cdf5691a4ae252.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586651.OTHER_5982917471_4874068",
                  "categoryName": "Infant (0 - 6 mnths)",
                  "categoryId": "2969"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-followon-milk-formula",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//th-live-02.slatic.net/original/f532e2a0c3d047a4b5cb9600887bdb34.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586651.OTHER_5982917472_4874068",
                  "categoryName": "Follow On (6 - 12 mnths)",
                  "categoryId": "2970"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-toddler-milk-1-under-3-yrs",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//th-live.slatic.net/original/b309ddac7c57ff0c4152566208ca7e6b.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586651.OTHER_5982917473_4874068",
                  "categoryName": "Toddler Milk (1 - under 3 yrs)",
                  "categoryId": "4139"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-growth-milk-formula",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//th-live.slatic.net/p/52a86d3af68b30aa8c46545bb8683d74.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586651.OTHER_5982917474_4874068",
                  "categoryName": "Growing-up Milk (3yrs +)",
                  "categoryId": "2972"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-milk-formula-tailored-nutrition",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//th-live.slatic.net/original/32c75ea6a876ee76bda0de1662388840.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586651.OTHER_5982917475_4874068",
                  "categoryName": "Tailored Nutrition",
                  "categoryId": "4044"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-baby-juices-and-drinks",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//th-live.slatic.net/p/205150d72cc6ad8a41d626dd23fb9869.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586651.OTHER_5982917476_4874068",
                  "categoryName": "Beverages",
                  "categoryId": "6068"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-baby-food-cereal",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//th-live.slatic.net/original/7fe5b091acfd1ae51a5d780795ffec7b.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586651.OTHER_5982917477_4874068",
                  "categoryName": "Cereal",
                  "categoryId": "6069"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-baby-food-crackers-biscuits",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//th-live.slatic.net/p/19949c3bd096e0f0c84c6d6652f27f8d.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586651.OTHER_5982917478_4874068",
                  "categoryName": "Crackers & Biscuits",
                  "categoryId": "9608"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-baby-food-snacks",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//th-live.slatic.net/p/8c3ef2c8964bc7b61ad6f64f28f264b2.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586651.OTHER_5982917479_4874068",
                  "categoryName": "Snack Foods",
                  "categoryId": "9622"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-baby-puree",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//th-live.slatic.net/original/eecb5f867522f19701bc32913fb5bfcc.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586651.OTHER_5982917480_4874068",
                  "categoryName": "Puree",
                  "categoryId": "14239"
                }
              ],
              "categoryIcon": "",
              "categoryUrl": "//www.lazada.co.th/shop-milk-formula-and-baby-food",
              "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel2TabDTO",
              "categoryName": "Milk Formula & Baby Food",
              "categoryId": "10100747"
            },
            {
              "level3TabList": [
                {
                  "categoryUrl": "//www.lazada.co.th/shop-breast-pumps",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//th-live.slatic.net/p/da4df33ee369c12866b29268ef6a2647.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586651.OTHER_5982917481_4874068",
                  "categoryName": "Breast Pumps",
                  "categoryId": "7263"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-breast-pumps-accessories",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//th-live.slatic.net/p/8b6a2dd7861c201903ff2e28f5a9d0d3.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586651.OTHER_5982917482_4874068",
                  "categoryName": "Breast Pump Accessories",
                  "categoryId": "14241"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-baby-bottles",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//th-live.slatic.net/p/daa727735cbf180bbdf162078fce6717.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586651.OTHER_5982917483_4874068",
                  "categoryName": "Bottles",
                  "categoryId": "3736"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-bottle-care-cleaning",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//th-live.slatic.net/original/0b12388eb20b19f9f8d6ace292093ce8.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586651.OTHER_5982917484_4874068",
                  "categoryName": "Bottle Care & Cleaning",
                  "categoryId": "14240"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-baby-bottle-nipples",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//th-live.slatic.net/p/3d0dd79a1a3f32f38effa18a38d45e12.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586651.OTHER_5982917485_4874068",
                  "categoryName": "Bottle Nipples & Accessories",
                  "categoryId": "3734"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-sterilizers-warmers",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//th-live.slatic.net/p/f4cc0b1fb9dc9b6d7db9c3993cc52160.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586651.OTHER_5982917486_4874068",
                  "categoryName": "Warmers & Sterlizers",
                  "categoryId": "9644"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-nursing-covers",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//my-live-02.slatic.net/p/e1fae0280c043671ba6c76159e77466f.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586651.OTHER_5982917487_4874068",
                  "categoryName": "Nursing Covers",
                  "categoryId": "4262"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-baby-formula-dispensers",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//th-live.slatic.net/p/4208ae4e54a26f82a16a6b70d08ccef8.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586651.OTHER_5982917488_4874068",
                  "categoryName": "Formula Dispensers & Mixers",
                  "categoryId": "9625"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-baby-food-processors",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//th-live.slatic.net/original/52ae3965ee65c3af185a68ff5f4191a8.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586651.OTHER_5982917489_4874068",
                  "categoryName": "Baby Food Blenders",
                  "categoryId": "3747"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-baby-utensils",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//th-live.slatic.net/p/4/mothers-corn-petit-smart-ecotainert-set-7341-6811316-c5fe28e91ff90fcbfe0b3776936788f9-catalog.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586651.OTHER_5982917490_4874068",
                  "categoryName": "Utensils",
                  "categoryId": "6871"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-baby-feeding-pillow-and-stools",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//th-live.slatic.net/p/236f6991107d4ab62ff28ea64f89e46c.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586651.OTHER_5982917491_4874068",
                  "categoryName": "Pillows & Stools",
                  "categoryId": "7950"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-high-chairs-boosters",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//th-live.slatic.net/p/mdc/6eb3d6a338358fedd2ae909670e3ebac.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586651.OTHER_5982917492_4874068",
                  "categoryName": "Highchairs & Booster Seats",
                  "categoryId": "7178"
                }
              ],
              "categoryIcon": "",
              "categoryUrl": "//www.lazada.co.th/shop-feeding-nursing",
              "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel2TabDTO",
              "categoryName": "Feeding Essentials",
              "categoryId": "3581"
            },
            {
              "level3TabList": [
                {
                  "categoryUrl": "//www.lazada.co.th/shop-baby-strollers",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//th-live.slatic.net/p/76a3ab91928430d67cc3ee7de6d503e8.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586651.OTHER_5982917493_4874068",
                  "categoryName": "Strollers",
                  "categoryId": "5115"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-car-seats",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//th-live.slatic.net/original/10ddab90ca442d9ad3012da83868466e.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586651.OTHER_5982917494_4874068",
                  "categoryName": "Car Seats",
                  "categoryId": "7027"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-baby-carriers",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//th-live.slatic.net/p/36f9848d81b5375f8abfb46dc6ea93d6.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586651.OTHER_5982917495_4874068",
                  "categoryName": "Backpacks & Carriers",
                  "categoryId": "5084"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-baby-walkers",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//my-live-02.slatic.net/p/a11f9dcdf1cd1e6fc9679e18d2b84965.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586651.OTHER_5982917496_4874068",
                  "categoryName": "Walkers",
                  "categoryId": "5396"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-baby-playards",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//th-live.slatic.net/p/a7230f32b00df6149be2b6c4677624f6.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586651.OTHER_5982917497_4874068",
                  "categoryName": "Playards & Playpens",
                  "categoryId": "5385"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-walkers-bouncers",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//th-live.slatic.net/original/0d7998c8b537b60cdd84ea7352138e69.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586651.OTHER_5982917498_4874068",
                  "categoryName": "Swings, Jumpers & Bouncers",
                  "categoryId": "7990"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-bicycle-child-seats-trailers",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//th-live.slatic.net/p/madamphooh-safety-9728-6651951-1-catalog.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586651.OTHER_5982917499_4874068",
                  "categoryName": "Bicycle Child Seats & Trailers",
                  "categoryId": "5160"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-baby-harnesses-leashes",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//my-live-02.slatic.net/original/4d990680754634095c5d2c64863b97b1.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586651.OTHER_5982917500_4874068",
                  "categoryName": "Harnesses & Leashes",
                  "categoryId": "5162"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-travel-system-car-seats",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//th-live.slatic.net/p/4/brica-nbspihidetm-seat-back-organizer-withtablet-viewer-6007-91290981-242b94ce1d52693618e8af764a46459e-catalog.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586651.OTHER_5982917501_4874068",
                  "categoryName": "Travel Systems",
                  "categoryId": "14211"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-baby-travel-beds",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//my-live-02.slatic.net/p/2459668819a4d5758ae34fe5936f16a5.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586651.OTHER_5982917502_4874068",
                  "categoryName": "Travel Beds",
                  "categoryId": "5389"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-kids-bag-luaggages",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//th-live.slatic.net/original/f75c37704dff94a8e810e18642a10a3e.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586651.OTHER_5982917503_4874068",
                  "categoryName": "Kids Bags & Luggage",
                  "categoryId": "14212"
                }
              ],
              "categoryIcon": "",
              "categoryUrl": "//www.lazada.co.th/shop-baby-gear",
              "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel2TabDTO",
              "categoryName": "Baby Gear",
              "categoryId": "6661"
            },
            {
              "level3TabList": [
                {
                  "categoryUrl": "//www.lazada.co.th/shop-crib-bedding",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//my-live-02.slatic.net/original/a9d50441ed30ee3b5ff19a44c92f1afa.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586651.OTHER_5982917504_4874068",
                  "categoryName": "Baby Mattresses",
                  "categoryId": "5315"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-nursery-blankets",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//my-live-02.slatic.net/original/5fce1341e7200bdef24b20a5fdbcfa9f.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586651.OTHER_5982917505_4874068",
                  "categoryName": "Blankets & Wrappers",
                  "categoryId": "5313"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-cradle-bedding",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//th-live.slatic.net/p/13de899f915c9db118293d9d2f38d7f9.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586651.OTHER_5982917506_4874068",
                  "categoryName": "Cradle Bedding",
                  "categoryId": "5124"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-toddler-bedding",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//th-test-11.slatic.net/p/dcafc0fd54ae3a40d835579336f83c1c.jpg_1000x1000q80.jpg_.webp_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586651.OTHER_5982917507_4874068",
                  "categoryName": "Toddler Bedding",
                  "categoryId": "5326"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-baby-quilts",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//th-live.slatic.net/original/867f1b98740a3514ec86cb032086e550.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586651.OTHER_5982917508_4874068",
                  "categoryName": "Quilts & Bed Covers",
                  "categoryId": "5420"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-baby-pillows-protector-and-cases",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//my-live-02.slatic.net/p/eb1954eb4f76bf7f531be375258cded7.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586651.OTHER_5982917509_4874068",
                  "categoryName": "Pillows Protector & Cases",
                  "categoryId": "4899"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-nursery-baby-furniture",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//th-live.slatic.net/p/3/kakuki-6033-02608303-47f083436a72c488036156036e0d7ae2-catalog.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586651.OTHER_5982917510_4874068",
                  "categoryName": "Baby Furniture",
                  "categoryId": "5107"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-cribs-cots",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//my-live-02.slatic.net/p/7110852b0f750f3863878d83bdb7ff4a.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586651.OTHER_5982917511_4874068",
                  "categoryName": "Cribs",
                  "categoryId": "5143"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-nursery-furniture-cradles",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//th-live.slatic.net/original/d58192c6af47d00018abf61877c846ae.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586651.OTHER_5982917512_4874068",
                  "categoryName": "Cradles",
                  "categoryId": "5140"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-nursery-furniture-chests-dressers",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//my-live-02.slatic.net/p/4f92952fa7f387dee8f8e935316b364e.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586651.OTHER_5982917513_4874068",
                  "categoryName": "Chests & Dressers",
                  "categoryId": "5134"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-nursery-storage-organization",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//th-live.slatic.net/original/6a03165cd7e9b84197460f43ec549680.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586651.OTHER_5982917514_4874068",
                  "categoryName": "Storage & Organization",
                  "categoryId": "5268"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-nursery-decor-gift-sets",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//th-live.slatic.net/p/8fc493f3811057a35a27c271c869158c.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586651.OTHER_5982917515_4874068",
                  "categoryName": "Nursery Décor",
                  "categoryId": "3698"
                }
              ],
              "categoryIcon": "",
              "categoryUrl": "//www.lazada.co.th/shop-nursery",
              "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel2TabDTO",
              "categoryName": "Nursery",
              "categoryId": "5286"
            },
            {
              "level3TabList": [
                {
                  "categoryUrl": "//www.lazada.co.th/baby-detergent",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//th-live.slatic.net/p/b109355090750a25f80dc521d9c644b4.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586651.OTHER_5982917516_4874068",
                  "categoryName": "Baby Detergent",
                  "categoryId": "14447"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-baby-skin-care",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//th-live.slatic.net/original/f0722bceee55e01184b8ccab732abe5e.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586651.OTHER_5982917517_4874068",
                  "categoryName": "Skin Care",
                  "categoryId": "14185"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-baby-shampoos",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//th-live.slatic.net/p/4/mistine-baby-ultracare-head-to-toe-bath-400-1-7127-35128212-2f2ea42c37d19a1c56d8a2f3e5239c5e-catalog.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586651.OTHER_5982917518_4874068",
                  "categoryName": "Shampoo & Conditioners",
                  "categoryId": "14182"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-baby-soaps-cleaners",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//th-live.slatic.net/p/mdc/ebfef5af3368f9d6732a1b6bf07974cc.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586651.OTHER_5982917519_4874068",
                  "categoryName": "Soaps, Cleansers & Bodywash",
                  "categoryId": "14186"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-baby-sun-protection",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//th-live.slatic.net/p/5/sebamed-baby-sun-protection-cream-spf-50-10-ml-3491-64583073-7084cae0385d8f47052fe693498e6e3c-catalog.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586651.OTHER_5982917520_4874068",
                  "categoryName": "Sun Protection",
                  "categoryId": "14191"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-baby-aromatherapy",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//th-live.slatic.net/p/e20aee7963399ade86d44a1e5c07d669.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586651.OTHER_5982917521_4874068",
                  "categoryName": "Aromatherapy",
                  "categoryId": "14179"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-grooming-accessories",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//th-live.slatic.net/p/4/bojia-lookmee-shop-bojia-baby-hairclipper-8271-58675691-15410959d358842f8eed46c3d5b6a552-catalog.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586651.OTHER_5982917522_4874068",
                  "categoryName": "Grooming & Healthcare Kits",
                  "categoryId": "14183"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-baby-oral-care",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//th-live-02.slatic.net/p/4/nuk-training-toothbrush-set-4216-8647789-bf4c41dd2bb3d63e836af9c7ab8785f2-catalog.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586651.OTHER_5982917523_4874068",
                  "categoryName": "Toothbrushes & Toothpaste",
                  "categoryId": "14190"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-baby-bubble-bath",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//th-live.slatic.net/p/4/sebamed-baby-sebamed-baby-bubble-bath-500-ml-x-1-4509-05809869-60ad92af0b1c127f37b6dd7db0c42f6a-catalog.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586651.OTHER_5982917524_4874068",
                  "categoryName": "Bubble Bath",
                  "categoryId": "14181"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-bath-tubs-accessories",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//th-live.slatic.net/p/8cb35659b640099f2db84becc01edd4a.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586651.OTHER_5982917525_4874068",
                  "categoryName": "Bathing Tubs & Seats",
                  "categoryId": "14180"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-baby-non-slip-bath-mats",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//my-live-02.slatic.net/p/640bfba3ec3159ea31df791e1c5570b3.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586651.OTHER_5982917526_4874068",
                  "categoryName": "Non-Slip Bath Mats",
                  "categoryId": "14184"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-baby-towels",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//my-live-02.slatic.net/original/7b4b59ed2adacf80418e47d7e2d50bac.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586651.OTHER_5982917527_4874068",
                  "categoryName": "Washcloths & Towels",
                  "categoryId": "14189"
                }
              ],
              "categoryIcon": "",
              "categoryUrl": "//www.lazada.co.th/shop-bathing-grooming",
              "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel2TabDTO",
              "categoryName": "Baby Personal Care",
              "categoryId": "14170"
            },
            {
              "level3TabList": [
                {
                  "categoryUrl": "//www.lazada.co.th/shop-new-born-baby-clothing-sets",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//th-live.slatic.net/p/d683212bb9fdedf19780b1387842c624.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586651.OTHER_5982917528_4874068",
                  "categoryName": "New Born Set & Packs",
                  "categoryId": "3731"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-new-born-baby-bodysuits-one-piece",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//th-live.slatic.net/p/f95d70067d134277c3515d6d44ced53d.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586651.OTHER_5982917529_4874068",
                  "categoryName": "New Born Body Suits",
                  "categoryId": "3238"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-new-born-baby-clothing-accessories",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//th-live.slatic.net/p/2edd864b63e49445bc58a0fe9c2d6de0.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586651.OTHER_5982917530_4874068",
                  "categoryName": "New Born Accessories",
                  "categoryId": "3804"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-baby-girls-clothing",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//th-live.slatic.net/original/6c9c293124bf302f990fcea629ba325d.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586651.OTHER_5982917531_4874068",
                  "categoryName": "Baby Girls Clothing",
                  "categoryId": "3661"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-baby-girls-dresses",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//th-live.slatic.net/p/433126700b75b0949f4473182eb42904.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586651.OTHER_5982917532_4874068",
                  "categoryName": "Baby Girls Dresses",
                  "categoryId": "7340"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-baby-girls-shoes",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//my-live-02.slatic.net/original/6f23510d2559dd767e3b22695f2b2f4b.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586651.OTHER_5982917533_4874068",
                  "categoryName": "Baby Girls Shoes",
                  "categoryId": "3417"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-baby-girls-clothing-accessories",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//my-live-02.slatic.net/p/f57925628d2c7643a8e9ab8e95536289.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586651.OTHER_5982917534_4874068",
                  "categoryName": "Baby Girls Accessories",
                  "categoryId": "2399"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-baby-girls-swim-wear",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//my-live-02.slatic.net/p/fffe47c42c1d2420c55dfed1e84c6e33.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586651.OTHER_5982917535_4874068",
                  "categoryName": "Baby Girls Swimwear",
                  "categoryId": "2948"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-baby-boys-clothing",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//my-live-02.slatic.net/p/b331f0c6d8bb070589bd3eae7dc57cd8.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586651.OTHER_5982917536_4874068",
                  "categoryName": "Baby Boys Clothing",
                  "categoryId": "6242"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-baby-boys-shoes",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//th-live.slatic.net/original/43e4e64ad3b841689786f0602909305a.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586651.OTHER_5982917537_4874068",
                  "categoryName": "Baby Boys Shoes",
                  "categoryId": "3361"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-baby-boys-clothing-accessories",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//th-live.slatic.net/original/10d30dc788d7b93005f90a28b884ad43.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586651.OTHER_5982917538_4874068",
                  "categoryName": "Baby Boys Accessories",
                  "categoryId": "3348"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-baby-boys-swim-wear",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//my-live-02.slatic.net/p/c99f08483ef6d54741ff1bfdb07335e3.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586651.OTHER_5982917539_4874068",
                  "categoryName": "Baby Boys Swimwear",
                  "categoryId": "8294"
                }
              ],
              "categoryIcon": "",
              "categoryUrl": "//www.lazada.co.th/shop-baby-clothings",
              "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel2TabDTO",
              "categoryName": "Baby Fashion & Accessories",
              "categoryId": "6790"
            },
            {
              "level3TabList": [
                {
                  "categoryUrl": "//www.lazada.co.th/shop-action-figures",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//th-live.slatic.net/p/bandai-lm-hg-eva-01-test-type-4577-5087007-8148ac05d047ce55dde2659912e8a843-catalog.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586651.OTHER_5982917540_4874068",
                  "categoryName": "Action Figures",
                  "categoryId": "3800"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-collectibles",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//th-live.slatic.net/p/af15e7a7f7e4025528531628cb14756b.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586651.OTHER_5982917541_4874068",
                  "categoryName": "Collectibles",
                  "categoryId": "3801"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-mini-action-figures",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//th-live.slatic.net/original/53b5125d9e57c1f34f76b82c4b69c9b7.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586651.OTHER_5982917542_4874068",
                  "categoryName": "Mini - Figures",
                  "categoryId": "3802"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-3-d-puzzles",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//th-live.slatic.net/p/4/omedlh-ai-eflkhwaamkhidsraangsrrkhelech-r-3-miti-kh-ngelnprisnaa-2310-4265485-76e008ce41ae939dde35f41ba6aff6f5-catalog.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586651.OTHER_5982917543_4874068",
                  "categoryName": "Games & Puzzle",
                  "categoryId": "3329"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-board-games",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//th-live.slatic.net/p/mdc/445c817f10a05d0427429de16a7a97f5.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586651.OTHER_5982917544_4874068",
                  "categoryName": "Board Games",
                  "categoryId": "6705"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/Shop-Hobbies-Entertainment",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//th-live.slatic.net/p/9083dab3647b50aa3700fdfcb1663dae.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586651.OTHER_5982917545_4874068",
                  "categoryName": "Hobbies & Entertainment",
                  "categoryId": "42076001"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-blocks-building-toys",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//th-live.slatic.net/p/4/lego-medium-creative-brick-box-10696-6218-90184031-cf027e4437a80fe94960eada60345af0-catalog.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586651.OTHER_5982917546_4874068",
                  "categoryName": "Building Blocks",
                  "categoryId": "7453"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-kids-dress-up",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//th-live.slatic.net/p/3460703551bae1d74838d063c0b65dca.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586651.OTHER_5982917547_4874068",
                  "categoryName": "Pretend Play, Costumes & Party",
                  "categoryId": "3475"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-early-development-toys-2",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//th-live.slatic.net/p/4/lookmeeshop-6-little-joy-box-7219-9912111-72b8e9ba3c9e3940243415acaa6a36e9-catalog.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586651.OTHER_5982917548_4874068",
                  "categoryName": "Learning & Education",
                  "categoryId": "10100004"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-stuffed-toys",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//my-live-02.slatic.net/p/6642d48a3da5f831274d8866d19f442c.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586651.OTHER_5982917549_4874068",
                  "categoryName": "Stuffed Toys",
                  "categoryId": "7998"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-dolls-doll-houses",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//th-live.slatic.net/p/0b540422bc0a4bece9e2d257dfeaa144.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586651.OTHER_5982917550_4874068",
                  "categoryName": "Dolls & Accessories",
                  "categoryId": "6603"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-arts-craft",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//th-live.slatic.net/original/699581664267ee3a30f143f96b561332.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586651.OTHER_5982917551_4874068",
                  "categoryName": "Arts & Crafts",
                  "categoryId": "3236"
                }
              ],
              "categoryIcon": "",
              "categoryUrl": "//www.lazada.co.th/shop-toys-1",
              "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel2TabDTO",
              "categoryName": "Toys & Games",
              "categoryId": "5095"
            },
            {
              "level3TabList": [
                {
                  "categoryUrl": "//www.lazada.co.th/shop-activity-gym-playmats",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//th-live.slatic.net/p/4/product-8528-00220012-60c9b5bc40c6403b5b4efe2063aac2db-catalog.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586651.OTHER_5982917552_4874068",
                  "categoryName": "Activity Gym & Playmats",
                  "categoryId": "4935"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-early-learning-baby-toys",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//th-live.slatic.net/p/285f49a3d7ec67e8e7e3da66832c2a4e.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586651.OTHER_5982917553_4874068",
                  "categoryName": "Early Learning",
                  "categoryId": "5998"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-music-sound-baby-toys",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//th-live.slatic.net/p/4/kids-castle-dancing-ducks-6856-29272544-82c59adbe2b3f0be40473b45e5b91242-catalog.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586651.OTHER_5982917554_4874068",
                  "categoryName": "Music & Sound",
                  "categoryId": "6689"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-blocks-stacks-baby-toys",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//th-live.slatic.net/p/297067-0267-760792-1-catalog.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586651.OTHER_5982917555_4874068",
                  "categoryName": "Blocks",
                  "categoryId": "5994"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-baby-toy-balls",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//th-live.slatic.net/original/9b4848e52dddbb76216956860db183e7.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586651.OTHER_5982917556_4874068",
                  "categoryName": "Balls",
                  "categoryId": "5269"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-baby-rocking-spring-ride-ons",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//th-live-02.slatic.net/original/bae98e011788c683a16efdefc6f74c1f.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586651.OTHER_5982917557_4874068",
                  "categoryName": "Rocking & Spring Ride-Ons",
                  "categoryId": "6739"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-baby-shape-sorter-toys",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//th-live.slatic.net/p/6ee1de75d37afd556c302e3fcd2f433f.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586651.OTHER_5982917558_4874068",
                  "categoryName": "Shape Sorters",
                  "categoryId": "6791"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-baby-rattles",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//my-live-02.slatic.net/original/5b29c772095ae6dda79aed9686c6312c.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586651.OTHER_5982917559_4874068",
                  "categoryName": "Rattles",
                  "categoryId": "6737"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-baby-bath-toys",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//my-live-02.slatic.net/p/503959a3ef30dc442d52ba0a6ac94b67.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586651.OTHER_5982917560_4874068",
                  "categoryName": "Bath Toys",
                  "categoryId": "5867"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-baby-stacking-nesting-toys",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//th-live.slatic.net/p/9b12bad78155fe330991b9d0fcb44bf0.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586651.OTHER_5982917561_4874068",
                  "categoryName": "Stacking & Nesting Toys",
                  "categoryId": "6918"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-baby-spinning-top-toys",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//th-live.slatic.net/p/4/spaceship-top-luukkhaang-yaan-wkaas-1601-26139011-0f92955bff5d4a8be61a7e9e327300ec-catalog.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586651.OTHER_5982917562_4874068",
                  "categoryName": "Spinning Tops",
                  "categoryId": "6914"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-baby-crib-toys",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//th-live.slatic.net/p/4/ombaayphanetiiyng-phanrthekhn-phankhaarchiith-phankh-kkanedk-miiesiiyngdntrii-phueng-5143-08507351-6e891e925084529357c0411df8738274-catalog.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586651.OTHER_5982917563_4874068",
                  "categoryName": "Crib Toys & Attachments",
                  "categoryId": "5996"
                }
              ],
              "categoryIcon": "",
              "categoryUrl": "//www.lazada.co.th/shop-baby-toys",
              "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel2TabDTO",
              "categoryName": "Baby & Toddler Toys",
              "categoryId": "3754"
            },
            {
              "level3TabList": [
                {
                  "categoryUrl": "//www.lazada.co.th/shop-kids-pool",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//th-live.slatic.net/p/4/lookmeeshop-200x150x50cm-giant-rectangular-inflatable-pool-0809-99197939-a34f7ed8d2ffc4255cdf20ddedfc0dc5-catalog.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586651.OTHER_5982917564_4874068",
                  "categoryName": "Pools, Water & Sand Toys",
                  "categoryId": "14274"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-kids-ride-ons",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//th-live.slatic.net/p/cf3cac87fe967a56b4448166961c8b9f.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586651.OTHER_5982917565_4874068",
                  "categoryName": "Ride-on",
                  "categoryId": "7362"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-pedal-cars",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//th-live.slatic.net/p/the-paparin-rthkhaaaith-khaaaithhnaakb-kh-ngelnedk-ruupkaartuunkb-miiesiiyngephlng-9348-6585396-6909c06673c290bdd283196aca1f699d-catalog.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586651.OTHER_5982917566_4874068",
                  "categoryName": "Pedal Cars",
                  "categoryId": "7363"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-kids-tricycles",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//th-live.slatic.net/p/98e0074430c3ce20fe2296d2c5b04bb2.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586651.OTHER_5982917567_4874068",
                  "categoryName": "Kids Tricycles",
                  "categoryId": "6884"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-kids-scooters",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//th-live.slatic.net/p/4196b6d9554420dd96b80ab3bfe35174.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586651.OTHER_5982917568_4874068",
                  "categoryName": "Kids Scooters",
                  "categoryId": "6885"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-kids-outdoor-bikes",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//th-live.slatic.net/original/276e9ba3fc3179ecc38d6bd367768c8f.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586651.OTHER_5982917569_4874068",
                  "categoryName": "Kids Bikes & Accessories",
                  "categoryId": "6905"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-blaster-toys",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//th-live.slatic.net/p/580e6eba0a956670d936d35646975266.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586651.OTHER_5982917570_4874068",
                  "categoryName": "Blaster toys",
                  "categoryId": "4441"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-play-sets-and-playground-equipment",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//th-live.slatic.net/p/mdc/6f00f31bc57bb44beca59d7478b70063.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586651.OTHER_5982917571_4874068",
                  "categoryName": "Play Sets & Playground Equipment",
                  "categoryId": "5752"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-kids-tents",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//th-live.slatic.net/p/4/lookmee-shop-2570-0307387-588f28469371917fe1d6847ae8666a5d-catalog.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586651.OTHER_5982917572_4874068",
                  "categoryName": "Play Tents & Tunnels",
                  "categoryId": "5751"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-ball-pits-and-accessories",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//th-live.slatic.net/original/b46836bf44484452b12cc60dc6616d8a.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586651.OTHER_5982917573_4874068",
                  "categoryName": "Ball Pits & Accessories",
                  "categoryId": "4864"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-lawn-games",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//th-live.slatic.net/original/0d41246bcc3ae4d43e9ac61f0c2423f4.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586651.OTHER_5982917574_4874068",
                  "categoryName": "Lawn Games",
                  "categoryId": "7261"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-flying-toys",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//my-live-02.slatic.net/p/24eb7539fc4ffaf84260964dad798036.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586651.OTHER_5982917575_4874068",
                  "categoryName": "Flying Toys",
                  "categoryId": "3797"
                }
              ],
              "categoryIcon": "",
              "categoryUrl": "//www.lazada.co.th/shop-sports-and-outdoor-play",
              "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel2TabDTO",
              "categoryName": "Sports Toys & Outdoor Play",
              "categoryId": "4086"
            },
            {
              "level3TabList": [
                {
                  "categoryUrl": "//www.lazada.co.th/shop-remote-control-toys",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//th-live.slatic.net/p/253df87aaf128cb3cb7034a1d2d65924.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586651.OTHER_5982917576_4874068",
                  "categoryName": "RC Vehicles & Batteries",
                  "categoryId": "3719"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-remote-control-die-cast-vehicles",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//my-live-02.slatic.net/p/50dd47e298ff8fcde4cd3a510cb61630.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586651.OTHER_5982917577_4874068",
                  "categoryName": "Die-Cast Vehicles",
                  "categoryId": "3695"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-drones-quadcopters",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//my-live-02.slatic.net/original/ebe258f07c8f03c0f50ee8de0d25276a.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586651.OTHER_5982917578_4874068",
                  "categoryName": "Toy Drones",
                  "categoryId": "5328"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-model-railway-and-train-sets",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//th-live.slatic.net/p/4/scale-68-cm-4413-34521806-50faf5f06ef6408626ac3f30fd47a5f6-catalog.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586651.OTHER_5982917579_4874068",
                  "categoryName": "Play Trains & Railway Sets",
                  "categoryId": "6763"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-rc-figures-robots",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//my-live-02.slatic.net/p/4be8e18ee648e1c6c403c7ec0bf48e4d.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586651.OTHER_5982917580_4874068",
                  "categoryName": "RC Figures & Robots",
                  "categoryId": "3379"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-walkie-talkies",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//th-live-02.slatic.net/p/4/avengers-8000-31323269-01783576e375d702588baeb69f77c8f6-catalog.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586651.OTHER_5982917581_4874068",
                  "categoryName": "Walkie Talkies",
                  "categoryId": "3380"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-remote-pull-backs",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//th-live.slatic.net/p/eb67db1f5c17d26ebed63e3c1d645ada.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586651.OTHER_5982917582_4874068",
                  "categoryName": "Pull-Backs",
                  "categoryId": "3742"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-remote-control-vehicles-playsets",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//my-live-02.slatic.net/p/299d4ff59f4039daae6d50a118a64542.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586651.OTHER_5982917583_4874068",
                  "categoryName": "Vehicle Playsets",
                  "categoryId": "3741"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-play-vehicles",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//th-live.slatic.net/p/20e8c00e9b1dadae1c0316e123534cd9.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586651.OTHER_5982917584_4874068",
                  "categoryName": "Vehicles",
                  "categoryId": "3740"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-dance-matt-toys",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//my-live-02.slatic.net/p/529657d01e9f11afe0e21e3311b31e40.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586651.OTHER_5982917585_4874068",
                  "categoryName": "Dance Mats",
                  "categoryId": "3371"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-toy-helipcopter",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//my-live-02.slatic.net/p/0e9b9b5e6d90ae9a6942130176d705bb.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586651.OTHER_5982917586_4874068",
                  "categoryName": "Helicopters",
                  "categoryId": "14220"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-entertainment-and-video-games",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//th-live.slatic.net/p/2/tetris-hand-held-lcd-electronic-game-toys-3699-4903871-2b78a07d74dd28b8bae05c7d72f33c57-catalog.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586651.OTHER_5982917587_4874068",
                  "categoryName": "Entertainment & Video Games",
                  "categoryId": "10100001"
                }
              ],
              "categoryIcon": "",
              "categoryUrl": "//www.lazada.co.th/shop-remote-control-toys-and-play-vehicles",
              "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel2TabDTO",
              "categoryName": "Electronic & Remote Control Toys",
              "categoryId": "3694"
            }
          ],
          "categoryName_zh": "",
          "categoryIcon": "ic-cat-BabiesToys &#xe75a;",
          "id": "6634012",
          "position": "top",
          "childId": "Level_1_Category_No5",
          "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel1TabDTO",
          "categoryName": "Babies & Toys ",
          "level1CategoryId": "6634012"
        },
        {
          "level2TabList": [
            {
              "level3TabList": [
                {
                  "categoryUrl": "//www.lazada.co.th/shop-coffee",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//th-live-02.slatic.net/p/8/dao-coffee-perfect-shape-10-2-1498462438-68778172-420e222963cfa1b405e79e0efe722d02-zoom.jpg",
                  "categoryName": "Coffee",
                  "categoryId": "6895"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-groceries-beverages-soft-drinks",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//laz-img-cdn.alicdn.com/images/ims-web/TB1xlA2XwZC2uNjSZFnXXaxZpXa.jpg",
                  "categoryName": "Soft Drinks",
                  "categoryId": "13652"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-groceries-beverages-uht-milk-milk-powder",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//th-live-03.slatic.net/p/4/honey-stars-300-2-1509355377-8548216-c8833f96a70cda6a770c44f0cc841ab9-zoom.jpg",
                  "categoryName": "UHT, Milk & Milk Powder",
                  "categoryId": "13651"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-tea",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//th-live-03.slatic.net/p/8/x-1-15-1496900004-22772632-4a2d3469b00e716d6b78d14b3282b21c-zoom.jpg",
                  "categoryName": "Tea",
                  "categoryId": "6896"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-groceries-beverages-water",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//th-live-03.slatic.net/p/17/100-3-1508465698-75739865-5e46a4a694fe3ad0ba16aca62070a17d-zoom.jpg",
                  "categoryName": "Water",
                  "categoryId": "13650"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-powdered-drink-mixes",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//th-live-01.slatic.net/p/8/ovaltine-31-33x20-3-60-1496215964-73326422-5509aac45d7d1e6dacf3de7684330f42-zoom.jpg",
                  "categoryName": "Powdered Drink Mixes",
                  "categoryId": "6898"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-groceries-beverages-juices",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//id-live-02.slatic.net/p/16/toffin-syrup-caramel-1473836481-0036949-bd4a5b81d4eb9450cefc480db1a251e7-zoom.jpg",
                  "categoryName": "Juices",
                  "categoryId": "13653"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-groceries-beverages-asian-health-drinks",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//th-live-02.slatic.net/p/8/30-sacha-inchi-inca-peanut-1500291010-78803733-828ab3eaaab9418e9bd9c44aeead0c8a-zoom.jpg",
                  "categoryName": "Asian Drinks",
                  "categoryId": "13654"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-hot-chocolate",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//th-live-01.slatic.net/p/8/dmalt-3in1-33-20-3-60-1499400198-43663303-62f549e8d04004a1a92ad7394646d3fc-zoom.jpg",
                  "categoryName": "Chocolate, Malt & Hot Cereals",
                  "categoryId": "6897"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-Groceries-Beverages-SportsEnergyDrinks",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//vn-live-01.slatic.net/p/5/tra-giam-beo-slimutea-hoc-vien-quan-y-hop-20-goi-1502508673-83357301-6af0ef04aa724eda5473106512bac881-zoom.jpg",
                  "categoryName": "Sports & Energy Drinks",
                  "categoryId": "14513"
                }
              ],
              "categoryIcon": "",
              "categoryUrl": "//www.lazada.co.th/shop-beverages",
              "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel2TabDTO",
              "categoryName": "Drink",
              "categoryId": "6894"
            },
            {
              "level3TabList": [
                {
                  "categoryUrl": "//www.lazada.co.th/shop-bars",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//id-live-02.slatic.net/p/f0a22d36a3841c3c89868de7fb2bc455.jpg",
                  "categoryName": "Bars",
                  "categoryId": "10100548"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-cold-cereals",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//th-live-03.slatic.net/p/4/honey-stars-300-2-1509355377-8548216-c8833f96a70cda6a770c44f0cc841ab9-zoom.jpg",
                  "categoryName": "Breakfast Cereals",
                  "categoryId": "7332"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-groceries-breakfast-jams-honey-spreads",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//th-live-01.slatic.net/p/17/1-1-1503543851-72040393-96a42fa0730bbb00f58e46dd4bb0689b-zoom.jpg",
                  "categoryName": "Jams, Honey & Spreads",
                  "categoryId": "13630"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-oatmeals",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//th-live-01.slatic.net/p/8/1-5-x-16-g-1491320899-93131641-19e26daf1b4e6afaa0ff69568cf4976e-zoom.jpg",
                  "categoryName": "Oatmeals",
                  "categoryId": "7333"
                }
              ],
              "categoryIcon": "",
              "categoryUrl": "//www.lazada.co.th/shop-breakfast",
              "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel2TabDTO",
              "categoryName": "Breakfast Cereals & Spreads",
              "categoryId": "7331"
            },
            {
              "level3TabList": [
                {
                  "categoryUrl": "//www.lazada.co.th/shop-Groceries-FoodStaplesCookingEssentials-CannedFood",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//id-live-02.slatic.net/p/16/abc-sardines-saus-ekstra-pedas-155g-8846-79328696-f7ed577fed17ec699ce08531fbc23b8f-catalog.jpg",
                  "categoryName": "Canned Food",
                  "categoryId": "14548"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-gourmet-food-and-gifts",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//laz-img-cdn.alicdn.com/images/ims-web/TB1yZR8dOjQBKNjSZFnXXa_DpXa.jpg",
                  "categoryName": "Gourmet Food and Gifts",
                  "categoryId": "6281"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-Groceries-FoodStaplesCookingEssentials-CookingSaucesKits",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//laz-img-cdn.alicdn.com/images/ims-web/TB1JPs2XwZC2uNjSZFnXXaxZpXa.jpg",
                  "categoryName": "Cooking Sauces & Kits",
                  "categoryId": "14546"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-Groceries-FoodStaplesCookingEssentials-DriedGoods",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//my-live-01.slatic.net/p/18/organic-blackstrap-molasses-450gm-unsulphured-1495186453-73388853-2e1a2dee6be6b68296dd03dae9d56e98-zoom.jpg",
                  "categoryName": "Dried Goods",
                  "categoryId": "14549"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-Groceries-FoodStaplesCookingEssentials-InstantFoodReadytoEat",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//laz-img-cdn.alicdn.com/images/ims-web/TB19UMEeiAnBKNjSZFvXXaTKXXa.jpg",
                  "categoryName": "Instant Food & Ready to Eat",
                  "categoryId": "14543"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-Groceries-FoodStaplesCookingEssentials-NoodlesVermicelli",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//id-live-02.slatic.net/p/ebdc0460e641febc43d90be1a19c200b.jpg",
                  "categoryName": "Noodles & Vermicelli",
                  "categoryId": "14542"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-Groceries-FoodStaplesCookingEssentials-Oil",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//id-live-02.slatic.net/original/6aa505b7cc20a7a2ce9b038825637bf8.jpg",
                  "categoryName": "Oil",
                  "categoryId": "14551"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-Groceries-FoodStaplesCookingEssentials-Rice",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//id-live-02.slatic.net/p/2/theorganicstop-shirataki-konnyaku-rice-low-carb-diet-keto-diabetes-300-gram-1234-07943987-ca9d6615aa1d483ec3a9c97a025a159f.jpg",
                  "categoryName": "Rice",
                  "categoryId": "14544"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-Groceries-FoodStaplesCookingEssentials-SaltSeasoning",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//id-live-02.slatic.net/p/16/boncabe-original-level-15-50g-8460-88510448-ddd12f7d6017671a8aeb3d18f3687c2d-catalog.jpg",
                  "categoryName": "Salt & Seasoning",
                  "categoryId": "14550"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-Groceries-FoodStaplesCookingEssentials-HomeBakingSugar",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//id-live-02.slatic.net/p/70466b80058d7507d2c2c40e28ae5553.jpg",
                  "categoryName": "Home Baking & Sugar",
                  "categoryId": "14541"
                }
              ],
              "categoryIcon": "",
              "categoryUrl": "//www.lazada.co.th/shop-Groceries-FoodStaplesCookingEssentials",
              "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel2TabDTO",
              "categoryName": "Food Staples & Cooking Essentials",
              "categoryId": "14501"
            },
            {
              "level3TabList": [
                {
                  "categoryUrl": "//www.lazada.co.th/shop-groceries-fresh-produce-fresh-fruit",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//id-live-03.slatic.net/p/4/alldaysmart-mainan-anak-animal-jumping-kuda-02-random-colour-1490012609-48609451-13c63dbefae71ae20d11089a55dcbcfb-zoom.jpg",
                  "categoryName": "Fresh Fruit",
                  "categoryId": "13669"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-groceries-fresh-produce-fresh-vegetables",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//id-live-02.slatic.net/p/007ec0856d55243ed6b8430dd2382ccd.jpg",
                  "categoryName": "Fresh Vegetables",
                  "categoryId": "13667"
                }
              ],
              "categoryIcon": "",
              "categoryUrl": "//www.lazada.co.th/shop-groceries-fresh-produce",
              "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel2TabDTO",
              "categoryName": "Fruit & Vegetables",
              "categoryId": "13549"
            },
            {
              "level3TabList": [
                {
                  "categoryUrl": "//www.lazada.co.th/shop-Groceries-ChocolateSnacksSweets-Biscuits-SweetBiscuits",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//id-live-02.slatic.net/original/b4b7a493c82b16eee892b7dc4a8ad0e0.jpg",
                  "categoryName": "Biscuits & Crackers",
                  "categoryId": "14732"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-Groceries-ChocolateSnacksSweets-Chocolate",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//id-live-02.slatic.net/p/2444d4e0ab3b01a8c273acdc0ca0d88f.jpg",
                  "categoryName": "Chocolate",
                  "categoryId": "14538"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-Groceries-ChocolateSnacksSweets-Mints",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//laz-img-cdn.alicdn.com/images/ims-web/TB1qkg1ekomBKNjSZFqXXXtqVXa.jpg",
                  "categoryName": "Mints",
                  "categoryId": "14539"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-Groceries-ChocolateSnacksSweets-Snacks",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//id-live-02.slatic.net/p/8cd9dc1fba2a7de8f216975ea3dcb2fe.jpg",
                  "categoryName": "Snacks",
                  "categoryId": "14536"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-Groceries-ChocolateSnacksSweets-Sweets",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//id-live-02.slatic.net/p/2a7fde77f8d5a6c5f933f0873b101855.jpg",
                  "categoryName": "Sweets",
                  "categoryId": "14540"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-Groceries-Bakery-Mooncakes",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//laz-img-cdn.alicdn.com/images/ims-web/TB1rfPtflr0gK0jSZFnXXbRRXXa.jpg",
                  "categoryName": "Mooncakes",
                  "categoryId": "14517"
                }
              ],
              "categoryIcon": "",
              "categoryUrl": "//www.lazada.co.th/shop-Groceries-ChocolateSnacksSweets",
              "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel2TabDTO",
              "categoryName": "Chocolate, Snacks & Sweets",
              "categoryId": "14500"
            },
            {
              "level3TabList": [
                {
                  "categoryUrl": "//www.lazada.co.th/shop-aircare-air-fresheners",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//laz-img-cdn.alicdn.com/images/ims-web/TB1fiE1ekomBKNjSZFqXXXtqVXa.jpg",
                  "categoryName": "Air Fresheners",
                  "categoryId": "10100544"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-groceries-laundry-household-dishwashing-hand-dishwashing",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//laz-img-cdn.alicdn.com/images/ims-web/TB15Ok1ekomBKNjSZFqXXXtqVXa.jpg",
                  "categoryName": "Dishwashing Liquid",
                  "categoryId": "13886"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-groceries-laundry-household-cleaning-bathroom",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//laz-img-cdn.alicdn.com/images/ims-web/TB1vhk1ekomBKNjSZFqXXXtqVXa.jpg",
                  "categoryName": "Bathroom & Toilet",
                  "categoryId": "13887"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-facial-tissues-2",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//my-live-03.slatic.net/p/18/royal-gold-luxurious-facial-tissue-4-bxs-x120-sheets-free-1pktofrgold-twin-tone-soft-pack-50s-1493259670-86174782-c27564a685efe091784a096b09c64574-zoom.jpg",
                  "categoryName": "Facial Tissues",
                  "categoryId": "10100541"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-groceries-laundry-household-paper-kitchen-roll",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//laz-img-cdn.alicdn.com/images/ims-web/TB1aaA9eljTBKNjSZFuXXb0HFXa.jpg",
                  "categoryName": "Kitchen Roll",
                  "categoryId": "13879"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-groceries-laundry-household-paper-toilet-paper",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//sg-live-02.slatic.net/p/16/kleenex-ultra-soft-regular-bathroom-tissues-20-rolls-1505452373-62901975-a1e0aab2361eec80b68ce04b7865a887-zoom.jpg",
                  "categoryName": "Toilet Paper",
                  "categoryId": "13881"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-groceries-laundry-household-pest-control-insect-baits",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//laz-img-cdn.alicdn.com/images/ims-web/TB16Hs9eljTBKNjSZFuXXb0HFXa.jpg",
                  "categoryName": "Insect Baits & Traps",
                  "categoryId": "13874"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-groceries-laundry-household-pest-control-insecticide-coil",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//vn-live-02.slatic.net/p/11/binh-xit-muoi-va-con-trung-flyway-chiet-xuat-tu-sa-va-bac-ha-1507176270-01167951-ca8af0f4409d2b96f938212490c87034-zoom.jpg",
                  "categoryName": "Insecticide Coils",
                  "categoryId": "13875"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-groceries-laundry-household-pest-control-insecticide-sprays",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//sg-live-01.slatic.net/p/16/ecomax-insect-spray-400ml-2-bottles-with-1-trigger-foc-1501504407-20895564-920369e5f8512978b0e6ba0e20da348f-zoom.jpg",
                  "categoryName": "Insecticide Sprays",
                  "categoryId": "13877"
                }
              ],
              "categoryIcon": "",
              "categoryUrl": "//www.lazada.co.th/shop-groceries-laundry-household-cleaning",
              "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel2TabDTO",
              "categoryName": "Cleaning Supplies",
              "categoryId": "13626"
            },
            {
              "level3TabList": [
                {
                  "categoryUrl": "//www.lazada.co.th/shop-groceries-laundry-household-laundry-fabric-conditioners",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//laz-img-cdn.alicdn.com/images/ims-web/TB1qWU9eljTBKNjSZFuXXb0HFXa.jpg",
                  "categoryName": "Fabric Conditioner",
                  "categoryId": "13868"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-groceries-laundry-household-laundry-fresheners-ironing",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//laz-img-cdn.alicdn.com/images/ims-web/TB1YW39eljTBKNjSZFuXXb0HFXa.jpg",
                  "categoryName": "Fresheners & Scent Boosters",
                  "categoryId": "13869"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-groceries-laundry-household-laundry-bleach",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//ph-live.slatic.net/p/7fd5e6433d99c84c8e94cddcc62a150d.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586652.OTHER_5967895294_4637318",
                  "categoryName": "Laundry Bleach",
                  "categoryId": "13866"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-groceries-laundry-household-laundry-delicate-care",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//icms-image.slatic.net/images/ims-web/a09a3afd-433e-430c-ba22-3c3cae57aa37.jpg",
                  "categoryName": "Liquid Detergent",
                  "categoryId": "13867"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-groceries-laundry-household-laundry-washing-powder",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//th-live-03.slatic.net/p/8/astonishoxy-plus6-1498649558-17439572-912a472c0227cf8daf8be8e60183ac99-zoom.jpg",
                  "categoryName": "Powder Detergent",
                  "categoryId": "13873"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-groceries-laundry-household-laundry-washing-machine-cleaner",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//ph-live.slatic.net/p/d0262a4a32bba205242898c392c83b50.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586652.OTHER_5967895297_4637318",
                  "categoryName": "Washing Machine Cleaner",
                  "categoryId": "13872"
                }
              ],
              "categoryIcon": "",
              "categoryUrl": "//www.lazada.co.th/shop-groceries-laundry-household-laundry",
              "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel2TabDTO",
              "categoryName": "Laundry Supplies",
              "categoryId": "13621"
            },
            {
              "level3TabList": [
                {
                  "categoryUrl": "//www.lazada.co.th/shop-aquarium-needs",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//laz-img-cdn.alicdn.com/images/ims-web/TB1KZpSdQfb_uJkHFrdXXX2IVXa.jpg",
                  "categoryName": "Aquarium Needs",
                  "categoryId": "10100637"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-dog-beds-mats-houses",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//th-live-03.slatic.net/p/8/mahjeb-l-1506424180-39815664-7627eedef3cff8c17d0bc14dbb9ec8fa-zoom.jpg",
                  "categoryName": "Beds, Mats & Houses",
                  "categoryId": "13576"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-dog-bowls-feeders",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//th-live-02.slatic.net/p/8/petkit-eversweet-3-petkit-1503376536-75098983-5d42e1e891816c19712e912249eea855-zoom.jpg",
                  "categoryName": "Bowls & Feeders",
                  "categoryId": "13579"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-dog-cages-pens-doors",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//th-live-01.slatic.net/p/3/xl-1488047416-0815574-bf2657071c40b476f68e7f4b43664237-zoom.jpg",
                  "categoryName": "Cages, Crates & Doors",
                  "categoryId": "13577"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-dog-carriers-travel",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//ph-live-02.slatic.net/p/4/moonbaby-baby-bed-with-net-bc-1251-pink-1478157666-918253-cf422e50371a90488576a8aadf7f4af3-zoom.jpg",
                  "categoryName": "Carriers & Travels",
                  "categoryId": "13583"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-cat-condo-tree-scratchers",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//th-live-03.slatic.net/p/13/yulapetshop-c160-1-6545160cm-1497881614-23353852-0e085e182edb24298d507563731d92ba-zoom.jpg",
                  "categoryName": "Cat Tree, Condo & Scratchers",
                  "categoryId": "13586"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-dog-clothes",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//laz-img-cdn.alicdn.com/images/ims-web/TB1vhk1ekomBKNjSZFqXXXtqVXa.jpg",
                  "categoryName": "Clothing, Shoes & Accessories",
                  "categoryId": "13578"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/\\N",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//laz-img-cdn.alicdn.com/images/ims-web/TB17LgFeiAnBKNjSZFvXXaTKXXa.jpg",
                  "categoryName": "Others",
                  "categoryId": "13546"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-dog-grooming-supplies",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//th-live-01.slatic.net/p/3/codos-codos-kp-3000-kuku-1463468414-3065446-f78e5352a24631d64eed137bdebcae3a-zoom.jpg",
                  "categoryName": "Grooming",
                  "categoryId": "3428"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-dog-leashes-collars-muzzles",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//th-live-03.slatic.net/p/8/2-intl-1477609854-2798049-dd667a2dd7560e210fcbf733e6cf4f9a-zoom.jpg",
                  "categoryName": "Leashes, Collars & Muzzles",
                  "categoryId": "13580"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-cat-clean-up-toilets",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//laz-img-cdn.alicdn.com/images/ims-web/TB1G3kFebZnBKNjSZFhXXc.oXXa.jpg",
                  "categoryName": "Litter & Toilet",
                  "categoryId": "2253"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-toys",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//ph-live-03.slatic.net/p/8/5pcs-cat-natural-catnip-ball-menthol-flavor-treats-edible-trea-toy-brown-intl-1492510652-93476851-8e026389830e6eccca9ad1cb8a697402-zoom.jpg",
                  "categoryName": "Toys",
                  "categoryId": "10100632"
                }
              ],
              "categoryIcon": "",
              "categoryUrl": "//www.lazada.co.th/shop-pet-accessories",
              "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel2TabDTO",
              "categoryName": "Pet Accessories",
              "categoryId": "10100631"
            },
            {
              "level3TabList": [
                {
                  "categoryUrl": "//www.lazada.co.th/shop-bird-food",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//laz-img-cdn.alicdn.com/images/ims-web/TB1WcE3XwZC2uNjSZFnXXaxZpXa.jpg",
                  "categoryName": "Bird Feed",
                  "categoryId": "13602"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-cat-food",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//th-live-03.slatic.net/p/13/gourmet-golden-80kg-20kg-x-4-1489487471-18362031-efdfa4d15f40febc88f7870ea2d7717b-zoom.jpg",
                  "categoryName": "Cat Food & Treat",
                  "categoryId": "2364"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-dog-food",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//th-live-01.slatic.net/p/8/hill39s-science-diet-acdtive-longevity-adult-7-7-15kg-1477368476-5633919-ad9a7fdfb63511dc69d2b6cecaeaad3e-zoom.jpg",
                  "categoryName": "Dog Food & Treat",
                  "categoryId": "3705"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-fish-food",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//th-live-03.slatic.net/p/8/1-1503650006-03716493-4f74a8f8754551e99168ae89ada2091f-zoom.jpg",
                  "categoryName": "Fish Food",
                  "categoryId": "13600"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-reptile-food",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//laz-img-cdn.alicdn.com/images/ims-web/TB15S.1ekomBKNjSZFqXXXtqVXa.jpg",
                  "categoryName": "Reptile Food",
                  "categoryId": "13605"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-small-pet-food",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//laz-img-cdn.alicdn.com/images/ims-web/TB1oNsFebZnBKNjSZFhXXc.oXXa.jpg",
                  "categoryName": "Small Pet Food",
                  "categoryId": "13596"
                }
              ],
              "categoryIcon": "",
              "categoryUrl": "//www.lazada.co.th/shop-pet-food",
              "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel2TabDTO",
              "categoryName": "Pet Food",
              "categoryId": "10100629"
            },
            {
              "level3TabList": [
                {
                  "categoryUrl": "//www.lazada.co.th/shop-dog-dentalcare",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//laz-img-cdn.alicdn.com/images/ims-web/TB1U2s9eljTBKNjSZFuXXb0HFXa.jpg",
                  "categoryName": "Dental Care",
                  "categoryId": "13763"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-dog-flea-tick",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//th-live-03.slatic.net/p/3/bayer-seresto-8kg-70-1494302416-4835842-b1cf5a39060835428db466b7a66114d2-zoom.jpg",
                  "categoryName": "Fleas & Ticks",
                  "categoryId": "13582"
                }
              ],
              "categoryIcon": "",
              "categoryUrl": "//www.lazada.co.th/shop-pet-healthcare",
              "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel2TabDTO",
              "categoryName": "Pet Healthcare",
              "categoryId": "10100888"
            }
          ],
          "categoryName_zh": "",
          "categoryIcon": "ic-cat-GroceriesPet &#xe755;",
          "id": "6634013",
          "position": "top",
          "childId": "Level_1_Category_No6",
          "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel1TabDTO",
          "categoryName": "Groceries & Pets ",
          "level1CategoryId": "6634013"
        },
        {
          "level2TabList": [
            {
              "level3TabList": [
                {
                  "categoryUrl": "//www.lazada.co.th/shop-bedroom-furniture",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//laz-img-cdn.alicdn.com/images/ims-web/TB1_sJBjrj1gK0jSZFuXXcrHpXa.jpg",
                  "categoryName": "Bedroom Furniture",
                  "categoryId": "11900"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-living-room-furniture",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//th-live-03.slatic.net/p/3/well-ware-6-ag742-black-1450756843-488825-1-zoom.jpg",
                  "categoryName": "Living Room Furniture",
                  "categoryId": "11901"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-kitchen-and-dining-furniture",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//laz-img-cdn.alicdn.com/images/ims-web/TB1lKdzjy_1gK0jSZFqXXcpaXXa.jpg",
                  "categoryName": "Kitchen & Dining Furniture",
                  "categoryId": "11902"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-home-office-furniture",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//laz-img-cdn.alicdn.com/images/ims-web/TB1svXBjBr0gK0jSZFnXXbRRXXa.jpg",
                  "categoryName": "Home Office Furniture",
                  "categoryId": "11904"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-game-room-furniture",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//laz-img-cdn.alicdn.com/images/ims-web/TB1mvJBjBr0gK0jSZFnXXbRRXXa.jpg",
                  "categoryName": "Gaming Furniture",
                  "categoryId": "11906"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-kids-and-baby-furniture",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//laz-img-cdn.alicdn.com/images/ims-web/TB1iMdBjBr0gK0jSZFnXXbRRXXa.jpg",
                  "categoryName": "Kids Furniture",
                  "categoryId": "11903"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-hallway-and-entry-furniture",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//th-live-02.slatic.net/p/3/50-brown-1480396521-65224201-9796c8690b41e7d8b843a966fa0e2e16-zoom.jpg",
                  "categoryName": "Hallway & Entry Furniture",
                  "categoryId": "11905"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-outdoor-furniture",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//laz-img-cdn.alicdn.com/images/ims-web/TB1O5pBjBr0gK0jSZFnXXbRRXXa.jpg",
                  "categoryName": "Outdoor Furniture",
                  "categoryId": "11907"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-clothes-organising",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//laz-img-cdn.alicdn.com/images/ims-web/TB1sRtBjrj1gK0jSZFuXXcrHpXa.jpg",
                  "categoryName": "Wardrobe Organisers",
                  "categoryId": "11912"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-home-storage-bins-baskets",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//laz-img-cdn.alicdn.com/images/ims-web/TB1AzFwjuT2gK0jSZFvXXXnFXXa.jpg",
                  "categoryName": "Storage Bins & Baskets",
                  "categoryId": "11909"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-space-savers",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//laz-img-cdn.alicdn.com/images/ims-web/TB1Fb4yjET1gK0jSZFhXXaAtVXa.jpg",
                  "categoryName": "Space Savers",
                  "categoryId": "11911"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-foldable-shoe-storage",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//laz-img-cdn.alicdn.com/images/ims-web/TB1pC0Bjrj1gK0jSZFuXXcrHpXa.jpg",
                  "categoryName": "Shoe Organisers",
                  "categoryId": "11910"
                }
              ],
              "categoryIcon": "",
              "categoryUrl": "//www.lazada.co.th/shop-furniture-decor",
              "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel2TabDTO",
              "categoryName": "Furniture & Organization",
              "categoryId": "11829"
            },
            {
              "level3TabList": [
                {
                  "categoryUrl": "//www.lazada.co.th/shop-table-lamps",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//th-live-02.slatic.net/p/3/rabia-int-aroma-salt-lamp-2-3kg-1466405313-2951611-529c9e84f0b3180f4f2c76618c23e320-zoom.jpg",
                  "categoryName": "Table Lamps",
                  "categoryId": "11936"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-floor-lamps",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//laz-img-cdn.alicdn.com/images/ims-web/TB1hStzjy_1gK0jSZFqXXcpaXXa.jpg",
                  "categoryName": "Floor Lamps",
                  "categoryId": "11937"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-lampshades",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//laz-img-cdn.alicdn.com/images/ims-web/TB1A9Rzjy_1gK0jSZFqXXcpaXXa.jpg",
                  "categoryName": "Lamp Shades",
                  "categoryId": "11941"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-decorative-ceiling-lights",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//laz-img-cdn.alicdn.com/images/ims-web/TB1j2hyjET1gK0jSZFhXXaAtVXa.jpg",
                  "categoryName": "Ceiling Lights",
                  "categoryId": "11934"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-wall-lights-sconces",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//laz-img-cdn.alicdn.com/images/ims-web/TB1TLFyjET1gK0jSZFhXXaAtVXa.jpg",
                  "categoryName": "Wall Lights",
                  "categoryId": "11935"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-specialty-lights",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//laz-img-cdn.alicdn.com/images/ims-web/TB1UT8zjy_1gK0jSZFqXXcpaXXa.jpg",
                  "categoryName": "Specialty Lighting",
                  "categoryId": "11938"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-fairy-lights",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//laz-img-cdn.alicdn.com/images/ims-web/TB19.xwjuT2gK0jSZFvXXXnFXXa.jpg",
                  "categoryName": "Fairy Lights",
                  "categoryId": "12297"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-night-lights",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//laz-img-cdn.alicdn.com/images/ims-web/TB1q.0zjy_1gK0jSZFqXXcpaXXa.jpg",
                  "categoryName": "Night Lights",
                  "categoryId": "12298"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-seasonal-lights",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//laz-img-cdn.alicdn.com/images/ims-web/TB1SrRAjAL0gK0jSZFxXXXWHVXa.jpg",
                  "categoryName": "Seasonal & Decorative",
                  "categoryId": "12300"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-home-decor-outdoor-lighting",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//laz-img-cdn.alicdn.com/images/ims-web/TB1FXBCjBr0gK0jSZFnXXbRRXXa.jpg",
                  "categoryName": "Outdoor Lighting",
                  "categoryId": "11943"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-light-bulbs",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//laz-img-cdn.alicdn.com/images/ims-web/TB13V0Ajy_1gK0jSZFqXXcpaXXa.jpg",
                  "categoryName": "Light Bulbs",
                  "categoryId": "10100136"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-lighting-fixtures-components",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//laz-img-cdn.alicdn.com/images/ims-web/TB1RylyjET1gK0jSZFhXXaAtVXa.jpg",
                  "categoryName": "Lighting Fixtures & Components",
                  "categoryId": "11940"
                }
              ],
              "categoryIcon": "",
              "categoryUrl": "//www.lazada.co.th/shop-lighting",
              "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel2TabDTO",
              "categoryName": "Lighting",
              "categoryId": "11865"
            },
            {
              "level3TabList": [
                {
                  "categoryUrl": "//www.lazada.co.th/shop-decorative-accents",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//laz-img-cdn.alicdn.com/images/ims-web/TB1czhyjET1gK0jSZFhXXaAtVXa.jpg",
                  "categoryName": "Decorative Accents",
                  "categoryId": "10100089"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-window-treatment-2",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//laz-img-cdn.alicdn.com/images/ims-web/TB1wTFwjpT7gK0jSZFpXXaTkpXa.jpg",
                  "categoryName": "Window Treatment",
                  "categoryId": "10100122"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-wall-stickers",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//laz-img-cdn.alicdn.com/images/ims-web/TB10c8CjBr0gK0jSZFnXXbRRXXa.jpg",
                  "categoryName": "Wall Stickers & Decals",
                  "categoryId": "11920"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-wall-art",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//laz-img-cdn.alicdn.com/images/ims-web/TB141lxjuT2gK0jSZFvXXXnFXXa.jpg",
                  "categoryName": "Wall Décor",
                  "categoryId": "11919"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-picture-frames",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//laz-img-cdn.alicdn.com/images/ims-web/TB1ae8Ajy_1gK0jSZFqXXcpaXXa.jpg",
                  "categoryName": "Pictures, Frames & Art",
                  "categoryId": "11926"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-cushions-and-covers",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//id-live-02.slatic.net/p/3/memory-foam-ring-cushion-surgical-donut-hemorrhoids-piles-pregnancy-pressure-intl-1477421012-3415762-7ea022e5cbd4171cddd79aacccd01dc0-zoom.jpg",
                  "categoryName": "Cushions & Covers",
                  "categoryId": "10100084"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-home-decor-clocks",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//th-live-01.slatic.net/p/3/rhythm-japan-10-cmg434nr03-1486469327-05357611-f0888f57eddadfa099036a09ae2a05e7-zoom.jpg",
                  "categoryName": "Clocks",
                  "categoryId": "11932"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-rugs-and-carpets",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//laz-img-cdn.alicdn.com/images/ims-web/TB1owpAjy_1gK0jSZFqXXcpaXXa.jpg",
                  "categoryName": "Rugs & Carpets",
                  "categoryId": "11918"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-candles-and-candleholders",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//laz-img-cdn.alicdn.com/images/ims-web/TB1KZNxjpT7gK0jSZFpXXaTkpXa.jpg",
                  "categoryName": "Candles & Candleholders",
                  "categoryId": "11927"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-home-fragrance",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//laz-img-cdn.alicdn.com/images/ims-web/TB1KztCjrj1gK0jSZFuXXcrHpXa.jpg",
                  "categoryName": "Aromatherapy & Home Fragrance",
                  "categoryId": "11929"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-artificial-flowers-and-plants",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//laz-img-cdn.alicdn.com/images/ims-web/TB11ilxjuT2gK0jSZFvXXXnFXXa.jpg",
                  "categoryName": "Artificial Flowers & Plants",
                  "categoryId": "11928"
                }
              ],
              "categoryIcon": "",
              "categoryUrl": "//www.lazada.co.th/shop-home-decor",
              "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel2TabDTO",
              "categoryName": "Home Décor",
              "categoryId": "11838"
            },
            {
              "level3TabList": [
                {
                  "categoryUrl": "//www.lazada.co.th/shop-bedding-sets",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//laz-img-cdn.alicdn.com/images/ims-web/TB1nHXzjET1gK0jSZFhXXaAtVXa.jpg",
                  "categoryName": "Bedding Sets",
                  "categoryId": "11896"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-bedsheets",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//th-live-01.slatic.net/p/3/lotus-impression-print-330trd-3539-3-li-037d-1507965099-09270955-4a5eeb4131c8c99a64780ceff2ad46a5-zoom.jpg",
                  "categoryName": "Bed Sheets",
                  "categoryId": "11897"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-pillow-cases",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//laz-img-cdn.alicdn.com/images/ims-web/TB1PPBCjBr0gK0jSZFnXXbRRXXa.jpg",
                  "categoryName": "Pillow Cases",
                  "categoryId": "11892"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-blankets-throws",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//laz-img-cdn.alicdn.com/images/ims-web/TB1UbVzjET1gK0jSZFhXXaAtVXa.jpg",
                  "categoryName": "Blankets",
                  "categoryId": "11888"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-comforters-quilts-duvets",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//laz-img-cdn.alicdn.com/images/ims-web/TB1kgtxjpT7gK0jSZFpXXaTkpXa.jpg",
                  "categoryName": "Quilts, Duvets & Throws",
                  "categoryId": "11889"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-pillows",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//laz-img-cdn.alicdn.com/images/ims-web/TB13ARAjy_1gK0jSZFqXXcpaXXa.jpg",
                  "categoryName": "Pillows & Bolsters",
                  "categoryId": "11891"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-mattresses-protectors",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//th-live-02.slatic.net/p/3/pampp-sheet-6-1502299808-6091831-5a05d88d9e7435f1657a2566c1774a83-zoom.jpg",
                  "categoryName": "Mattress Pads & Toppers",
                  "categoryId": "11899"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-mattress-pads-2",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//laz-img-cdn.alicdn.com/images/ims-web/TB1WlVCjBr0gK0jSZFnXXbRRXXa.jpg",
                  "categoryName": "Mattress Protectors",
                  "categoryId": "11898"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-bedding-accessories-2",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//th-live-01.slatic.net/p/3/triple3shop-1471428360-4078313-1d64102dde130b347182eb553e9d5b28-zoom.jpg",
                  "categoryName": "Bed Runners & Skirts",
                  "categoryId": "11894"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-bedding-accessories",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//laz-img-cdn.alicdn.com/images/ims-web/TB1zm8Ajy_1gK0jSZFqXXcpaXXa.jpg",
                  "categoryName": "Bedding Accessories",
                  "categoryId": "11895"
                }
              ],
              "categoryIcon": "",
              "categoryUrl": "//www.lazada.co.th/shop-bedding",
              "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel2TabDTO",
              "categoryName": "Bedding",
              "categoryId": "11835"
            },
            {
              "level3TabList": [
                {
                  "categoryUrl": "//www.lazada.co.th/shop-bath-towels",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//laz-img-cdn.alicdn.com/images/ims-web/TB1snVCjBr0gK0jSZFnXXbRRXXa.jpg",
                  "categoryName": "Towels",
                  "categoryId": "11883"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-bath-mats",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//laz-img-cdn.alicdn.com/images/ims-web/TB1yaBDjrj1gK0jSZFuXXcrHpXa.jpg",
                  "categoryName": "Bath Mats",
                  "categoryId": "11884"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-bathroom-scales",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//laz-img-cdn.alicdn.com/images/ims-web/TB1CW4Djrj1gK0jSZFuXXcrHpXa.jpg",
                  "categoryName": "Weight Scales",
                  "categoryId": "11877"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-holders-and-dispensers",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//laz-img-cdn.alicdn.com/images/ims-web/TB16g8zjET1gK0jSZFhXXaAtVXa.jpg",
                  "categoryName": "Holders & Dispensers",
                  "categoryId": "10100068"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-shower-holders-hangers",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//laz-img-cdn.alicdn.com/images/ims-web/TB1mXBDjBr0gK0jSZFnXXbRRXXa.jpg",
                  "categoryName": "Shower Caddies & Hangers",
                  "categoryId": "11882"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-bathroom-shelves",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//laz-img-cdn.alicdn.com/images/ims-web/TB1DcpDjrj1gK0jSZFuXXcrHpXa.jpg",
                  "categoryName": "Bathroom Shelving",
                  "categoryId": "11887"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/bathroom-storage",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//laz-img-cdn.alicdn.com/images/ims-web/TB1QGBBjy_1gK0jSZFqXXcpaXXa.jpg",
                  "categoryName": "Bathroom Storage",
                  "categoryId": "11874"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-shower-curtains-and-accessories",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//laz-img-cdn.alicdn.com/images/ims-web/TB1Wq0yjuT2gK0jSZFvXXXnFXXa.jpg",
                  "categoryName": "Shower Curtains",
                  "categoryId": "10100076"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-toilet-covers",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//laz-img-cdn.alicdn.com/images/ims-web/TB1S9tDjAT2gK0jSZFkXXcIQFXa.jpg",
                  "categoryName": "Toilet Covers",
                  "categoryId": "11880"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-towel-rails-and-warmers",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//laz-img-cdn.alicdn.com/images/ims-web/TB1yYJBjy_1gK0jSZFqXXcpaXXa.jpg",
                  "categoryName": "Towel Racks",
                  "categoryId": "11879"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-showerheads",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//laz-img-cdn.alicdn.com/images/ims-web/TB1bj4zjET1gK0jSZFhXXaAtVXa.jpg",
                  "categoryName": "Showerheads",
                  "categoryId": "10100189"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-toilets-and-toilet-parts",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//laz-img-cdn.alicdn.com/images/ims-web/TB1FZByjuT2gK0jSZFvXXXnFXXa.jpg",
                  "categoryName": "Toilets & Toilet Parts",
                  "categoryId": "10100193"
                }
              ],
              "categoryIcon": "",
              "categoryUrl": "//www.lazada.co.th/shop-bath",
              "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel2TabDTO",
              "categoryName": "Bath",
              "categoryId": "11834"
            },
            {
              "level3TabList": [
                {
                  "categoryUrl": "//www.lazada.co.th/shop-cookware",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//laz-img-cdn.alicdn.com/images/ims-web/TB1gLFDjrj1gK0jSZFuXXcrHpXa.jpg",
                  "categoryName": "Cookware",
                  "categoryId": "11855"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-dinnerware",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//laz-img-cdn.alicdn.com/images/ims-web/TB1vJRBjy_1gK0jSZFqXXcpaXXa.jpg",
                  "categoryName": "Dinnerware",
                  "categoryId": "11856"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-cutlery-2",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//laz-img-cdn.alicdn.com/images/ims-web/TB1et8DjBr0gK0jSZFnXXbRRXXa.jpg",
                  "categoryName": "Cutlery",
                  "categoryId": "10100151"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-drinkware-and-glassware",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//laz-img-cdn.alicdn.com/images/ims-web/TB1FKpDjBr0gK0jSZFnXXbRRXXa.jpg",
                  "categoryName": "Drinkware",
                  "categoryId": "11857"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-coffee-tea-kitchenware",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//laz-img-cdn.alicdn.com/images/ims-web/TB10uJDjBr0gK0jSZFnXXbRRXXa.jpeg",
                  "categoryName": "Coffee & Tea",
                  "categoryId": "11859"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-bakeware",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//laz-img-cdn.alicdn.com/images/ims-web/TB1_98zjET1gK0jSZFhXXaAtVXa.jpg",
                  "categoryName": "Bakeware",
                  "categoryId": "11854"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/kitchen-storage",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//laz-img-cdn.alicdn.com/images/ims-web/TB1eLNyjuT2gK0jSZFvXXXnFXXa.jpg",
                  "categoryName": "Kitchen Storage & Accessories",
                  "categoryId": "11862"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-kitchen-tools",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//laz-img-cdn.alicdn.com/images/ims-web/TB1JYhEjAT2gK0jSZFkXXcIQFXa.jpg",
                  "categoryName": "Kitchen Utensils",
                  "categoryId": "11860"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-kitchen-and-table-linen-accessories",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//laz-img-cdn.alicdn.com/images/ims-web/TB10w4Bjy_1gK0jSZFqXXcpaXXa.jpg",
                  "categoryName": "Kitchen & Table Linen",
                  "categoryId": "11861"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-serveware",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//laz-img-cdn.alicdn.com/images/ims-web/TB1Y4tyjuT2gK0jSZFvXXXnFXXa.jpg",
                  "categoryName": "Serveware",
                  "categoryId": "11858"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-disposables",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//laz-img-cdn.alicdn.com/images/ims-web/TB1Rc0EjAT2gK0jSZFkXXcIQFXa.png",
                  "categoryName": "Disposables",
                  "categoryId": "10100180"
                }
              ],
              "categoryIcon": "",
              "categoryUrl": "//www.lazada.co.th/shop-kitchen-and-dining",
              "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel2TabDTO",
              "categoryName": "Kitchen & Dining",
              "categoryId": "11832"
            },
            {
              "level3TabList": [
                {
                  "categoryUrl": "//www.lazada.co.th/shop-school-office-accessories",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//laz-img-cdn.alicdn.com/images/ims-web/TB1diBDjBr0gK0jSZFnXXbRRXXa.jpg",
                  "categoryName": "School & Office Equipment",
                  "categoryId": "11870"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-paper-products",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//laz-img-cdn.alicdn.com/images/ims-web/TB1qAhDjBr0gK0jSZFnXXbRRXXa.jpg",
                  "categoryName": "Paper Products",
                  "categoryId": "11867"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-writing-correction",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//laz-img-cdn.alicdn.com/images/ims-web/TB1tmlDjBr0gK0jSZFnXXbRRXXa.jpg",
                  "categoryName": "Writing & Correction",
                  "categoryId": "11866"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-art-supplies",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//laz-img-cdn.alicdn.com/images/ims-web/TB1FVNEjrj1gK0jSZFuXXcrHpXa.jpg",
                  "categoryName": "Art Supplies",
                  "categoryId": "11869"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-craft-supplies",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//laz-img-cdn.alicdn.com/images/ims-web/TB1XUhDjBr0gK0jSZFnXXbRRXXa.jpg",
                  "categoryName": "Craft Supplies",
                  "categoryId": "11871"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-craft-sewing",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//laz-img-cdn.alicdn.com/images/ims-web/TB1WUFDjBr0gK0jSZFnXXbRRXXa.jpg",
                  "categoryName": "Sewing",
                  "categoryId": "11872"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-gifts-wrapping",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//laz-img-cdn.alicdn.com/images/ims-web/TB1BVXEjBr0gK0jSZFnXXbRRXXa.jpg",
                  "categoryName": "Gifts & Wrapping",
                  "categoryId": "11873"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-packaging-products",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//laz-img-cdn.alicdn.com/images/ims-web/TB1rpJCjy_1gK0jSZFqXXcpaXXa.jpg",
                  "categoryName": "Packaging & Cartons",
                  "categoryId": "11868"
                }
              ],
              "categoryIcon": "",
              "categoryUrl": "//www.lazada.co.th/shop-stationery-craft",
              "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel2TabDTO",
              "categoryName": "Stationery & Office Supplies",
              "categoryId": "11833"
            },
            {
              "level3TabList": [
                {
                  "categoryUrl": "//www.lazada.co.th/shop-brooms-mops-sweepers",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//laz-img-cdn.alicdn.com/images/ims-web/TB1O0REjrj1gK0jSZFuXXcrHpXa.jpg",
                  "categoryName": "Brooms, Mops & Sweepers",
                  "categoryId": "12033"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-trash-cans",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//laz-img-cdn.alicdn.com/images/ims-web/TB1mZFEjBr0gK0jSZFnXXbRRXXa.jpg",
                  "categoryName": "Garbage & Recycling Bins",
                  "categoryId": "12036"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-cleaning-buckets",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//laz-img-cdn.alicdn.com/images/ims-web/TB1t2xEjrj1gK0jSZFuXXcrHpXa.jpg",
                  "categoryName": "Cleaning Buckets & Tubs",
                  "categoryId": "12032"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-drying-racks",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//laz-img-cdn.alicdn.com/images/ims-web/TB1PoF3ebZnBKNjSZFhXXc.oXXa.jpg",
                  "categoryName": "Clothes Line & Drying Racks",
                  "categoryId": "12040"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-hangers",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//laz-img-cdn.alicdn.com/images/ims-web/TB1khxEjrj1gK0jSZFuXXcrHpXa.jpg",
                  "categoryName": "Clothes Hangers & Pegs",
                  "categoryId": "12041"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-ironing-boards",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//laz-img-cdn.alicdn.com/images/ims-web/TB1nIp_eXkoBKNjSZFkXXb4tFXa.jpg",
                  "categoryName": "Ironing Boards",
                  "categoryId": "12042"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-laundry-ironing-tools",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//laz-img-cdn.alicdn.com/images/ims-web/TB1HOXEjrj1gK0jSZFuXXcrHpXa.jpg",
                  "categoryName": "Laundry & Ironing Tools",
                  "categoryId": "12044"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-laundry-baskets",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//laz-img-cdn.alicdn.com/images/ims-web/TB14MlEjBr0gK0jSZFnXXbRRXXa.jpg",
                  "categoryName": "Laundry Baskets & Hampers",
                  "categoryId": "12039"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-laundry-bag-balls",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//laz-img-cdn.alicdn.com/images/ims-web/TB1c3JEjBr0gK0jSZFnXXbRRXXa.jpg",
                  "categoryName": "Laundry Bags & Wash Balls",
                  "categoryId": "12043"
                }
              ],
              "categoryIcon": "",
              "categoryUrl": "//www.lazada.co.th/shop-laundry-cleaning",
              "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel2TabDTO",
              "categoryName": "Laundry & Cleaning",
              "categoryId": "11831"
            },
            {
              "level3TabList": [
                {
                  "categoryUrl": "//www.lazada.co.th/shop-power-tools",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//laz-img-cdn.alicdn.com/images/ims-web/TB1xQlEjrj1gK0jSZFuXXcrHpXa.jpg",
                  "categoryName": "Power Tools",
                  "categoryId": "11851"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-hand-tools",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//laz-img-cdn.alicdn.com/images/ims-web/TB1ocRBjET1gK0jSZFhXXaAtVXa.jpg",
                  "categoryName": "Hand Tools",
                  "categoryId": "11850"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-plumbing",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//laz-img-cdn.alicdn.com/images/ims-web/TB1pRlEjBr0gK0jSZFnXXbRRXXa.jpg",
                  "categoryName": "Fixtures & Plumbing",
                  "categoryId": "11839"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-water-pumps-parts-and-accessories",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//my-live-02.slatic.net/original/007ca10f9e6de16adb85f4c7690ba856.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586653.OTHER_5983911835_4888221",
                  "categoryName": "Water Pumps & Accessories",
                  "categoryId": "10100198"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-home-improvement-electrical",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//th-live-01.slatic.net/p/3/sunkko-787a-mcu-led-pulse-battery-spot-welder-precision-soldering-machine-220v-green-intl-1506254027-70522264-9313806db48b812ce95cbb0b2c53b57d-zoom.jpg",
                  "categoryName": "Electrical",
                  "categoryId": "11846"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-security-system-hardware",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//laz-img-cdn.alicdn.com/images/ims-web/TB1DWVFjBr0gK0jSZFnXXbRRXXa.jpg",
                  "categoryName": "Security",
                  "categoryId": "11843"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-measuring-and-levelling",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//laz-img-cdn.alicdn.com/images/ims-web/TB1TrtFjBr0gK0jSZFnXXbRRXXa.jpg",
                  "categoryName": "Measuring & Levelling",
                  "categoryId": "10100222"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-home-hardware",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//laz-img-cdn.alicdn.com/images/ims-web/TB18H4FjBr0gK0jSZFnXXbRRXXa.jpg",
                  "categoryName": "Hardware",
                  "categoryId": "11841"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-material-handling",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//laz-img-cdn.alicdn.com/images/ims-web/TB1lu0Fjrj1gK0jSZFuXXcrHpXa.jpg",
                  "categoryName": "Material Handling",
                  "categoryId": "10100221"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-painting-decorating",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//laz-img-cdn.alicdn.com/images/ims-web/TB13vBFjrj1gK0jSZFuXXcrHpXa.jpg",
                  "categoryName": "Painting & Decorating",
                  "categoryId": "11840"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-work-safety-equipment",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//laz-img-cdn.alicdn.com/images/ims-web/TB1MeXDjy_1gK0jSZFqXXcpaXXa.jpg",
                  "categoryName": "Protective Clothing &Equipment",
                  "categoryId": "11842"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-tools-and-garage-storage",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//th-live.slatic.net/p/c03c3f567e870fee9bfaa4be9608a885.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586653.OTHER_5983911843_4888221",
                  "categoryName": "Tool Storage & Shelving",
                  "categoryId": "11847"
                }
              ],
              "categoryIcon": "",
              "categoryUrl": "//www.lazada.co.th/shop-home-improvement",
              "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel2TabDTO",
              "categoryName": "Tools&Home Improvement",
              "categoryId": "11830"
            },
            {
              "level3TabList": [
                {
                  "categoryUrl": "//www.lazada.co.th/shop-outdoor-gardening-power-tools",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//id-live-01.slatic.net/p/2/sp-razer-goliathus-mousepad-gaming-mouse-pad-permukaan-lembut-1495267281-93656522-d83f6e76896cdb74624eaa89817426ae-zoom.jpg",
                  "categoryName": "Outdoor & Gardening Power Tools",
                  "categoryId": "12142"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-watering-systems",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//vn-live-01.slatic.net/p/2/vga-asus-strix-gtx1060-dc2o6g-1508380708-81845271-71aef8eae23ab48c15347900bfd87486-zoom.jpg",
                  "categoryName": "Watering Systems & Garden Hoses",
                  "categoryId": "12144"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-outdoor-gardening-tools",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//sg-live.slatic.net/p/3/3-piece-set-mini-garden-shovels-and-claw-tool-with-wooden-handles-6109-9102218-521d8d7886e694696197e41cda659b31-catalog.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586653.OTHER_5983911847_4888221",
                  "categoryName": "Gardening Tools",
                  "categoryId": "12143"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-soils-fertilisers-and-mulches",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//laz-img-cdn.alicdn.com/images/ims-web/TB1CP0Djy_1gK0jSZFqXXcpaXXa.jpg",
                  "categoryName": "Garden Soil & Fertilizers",
                  "categoryId": "12145"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-weed-and-pest-control",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//laz-img-cdn.alicdn.com/images/ims-web/TB1BDBFjrj1gK0jSZFuXXcrHpXa.jpg",
                  "categoryName": "Weeds & Pest Control",
                  "categoryId": "12150"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-plants-and-seeds",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//laz-img-cdn.alicdn.com/images/ims-web/TB1e9lDjy_1gK0jSZFqXXcpaXXa.jpg",
                  "categoryName": "Plant, Seeds and Bulbs",
                  "categoryId": "12149"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-fountains-water-features-and-ponds",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//laz-img-cdn.alicdn.com/images/ims-web/TB15KVCjET1gK0jSZFhXXaAtVXa.jpg",
                  "categoryName": "Ponds & Water Features",
                  "categoryId": "12147"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-sheds-and-greenhouses",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//laz-img-cdn.alicdn.com/images/ims-web/TB1sftCjET1gK0jSZFhXXaAtVXa.jpg",
                  "categoryName": "Garden Shed & Greenhouses",
                  "categoryId": "12152"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-grills-outdoor-entertaining",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//my-live-02.slatic.net/p/9b47f09aebd36c43c4336b909bba04bc.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586653.OTHER_5983911853_4888221",
                  "categoryName": "BBQ & Outdoor Dining",
                  "categoryId": "12284"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-pools-spas",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//laz-img-cdn.alicdn.com/images/ims-web/TB1UU4Djy_1gK0jSZFqXXcpaXXa.jpg",
                  "categoryName": "Pools & Spas",
                  "categoryId": "12293"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-electrical-insect-killers",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//laz-img-cdn.alicdn.com/images/ims-web/TB1hFVGjBr0gK0jSZFnXXbRRXXa.jpg",
                  "categoryName": "Electric Insect Killers",
                  "categoryId": "12141"
                }
              ],
              "categoryIcon": "",
              "categoryUrl": "//www.lazada.co.th/shop-outdoor-and-garden",
              "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel2TabDTO",
              "categoryName": "Outdoor & Garden",
              "categoryId": "10100245"
            },
            {
              "level3TabList": [
                {
                  "categoryUrl": "//www.lazada.co.th/shop-music-guitars",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//th-live-01.slatic.net/p/1/rotating-guitar-knob-1507406439-1466424-65478038b5f9da3aa3cbb4a65bedfd04-zoom.jpg",
                  "categoryName": "Guitars",
                  "categoryId": "7575"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-music-bass-guitars",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//th-live-03.slatic.net/p/1/carols-5-carols-ctb-05bbk-1472460327-4064887-d126f382e660cd9912e648e3eaea38e1-zoom.jpg",
                  "categoryName": "Bass Guitars",
                  "categoryId": "7571"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-drums-percussion",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//th-live-01.slatic.net/p/1/arborea-china-16-b8-16ch-1640cm-bronzecymbal-1497258056-4143365-2aa3b223d872a9945d8f28d6db95def9-zoom.jpg",
                  "categoryName": "Drums & Percussion",
                  "categoryId": "7555"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-music-keyboards-pianos",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//th-live-01.slatic.net/p/1/usb-to-midi-cable-pc-to-music-keyboard-adapter-1494405173-76724881-06652860e271846ad4fed0262ef0e284-zoom.jpg",
                  "categoryName": "Keyboards & Pianos",
                  "categoryId": "7549"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-woodwind",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//th-live-02.slatic.net/p/1/product-1499506479-42571013-cee0aa701b9a183b34692e5b11151c6e-zoom.jpg",
                  "categoryName": "Woodwinds",
                  "categoryId": "7567"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-band-orchestra",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//th-live-02.slatic.net/p/1/suzuki-easy-rider-harmonica-10-c-1483938024-810455-ee9d8f7b1333a0ccef88342b8e5405cd-zoom.jpg",
                  "categoryName": "Band & Orchestra",
                  "categoryId": "7528"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-traditional-instruments",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//th-live-02.slatic.net/p/1/product-1478573899-2297389-163fa8950d3cafa890d6cb91feb1b61b-zoom.jpg",
                  "categoryName": "Traditional Instruments",
                  "categoryId": "7515"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-dj-karaoke-electronic-music",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//th-live-03.slatic.net/p/1/neewer-professional-studio-broadcasting-recording-condensermicrophone-mic-kit-amp-nw-35-adjustable-recording-microphonesuspension-scissor-arm-stand-with-shock-mount-adjustable-suspensionscissor-arm-stand-mounting-clamp-pop-filter-outdoorfree-intl-1500725810-69129643-150831df5d00a3c2f05299afda80c723-zoom.jpg",
                  "categoryName": "DJ, Karaoke & Electronic Music",
                  "categoryId": "7544"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-instrument-accessories",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//th-live-01.slatic.net/p/1/product-1498986108-29118882-67c48a0bfd8d9135e92b26f48e998390-zoom.jpg",
                  "categoryName": "Instrument Accessories",
                  "categoryId": "7517"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-music",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//th-live-03.slatic.net/p/1/wanna-one-1x11-to-be-one-pink-ver-1st-mini-album-cd-folded-poster-free-gift-intl-1502834557-23123483-a3a419da1a57ed772607e5c9e7080ab2-zoom.jpg",
                  "categoryName": "Music",
                  "categoryId": "3016"
                }
              ],
              "categoryIcon": "",
              "categoryUrl": "//www.lazada.co.th/shop-musical-instruments",
              "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel2TabDTO",
              "categoryName": "Music & Instruments",
              "categoryId": "7514"
            },
            {
              "level3TabList": [
                {
                  "categoryUrl": "//www.lazada.co.th/shop-english-books",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//sg-live.slatic.net/p/fdfa54cc478c31c1f227697930a0d53a.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586653.OTHER_5983911868_4888221",
                  "categoryName": "English Books",
                  "categoryId": "7766"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-local-books",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//th-live-01.slatic.net/p/1/archicad-1461926316-3162334-fed3ecf75356e43667b7a5e834e969cf-zoom.jpg",
                  "categoryName": "Local Books",
                  "categoryId": "7799"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-childrens-local-books",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//sg-live.slatic.net/p/88a2da2958bf7156049b31022206908c.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586653.OTHER_5983911870_4888221",
                  "categoryName": "Children's Books",
                  "categoryId": "7822"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-self-help-local-books",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//sg-live.slatic.net/p/8b5c0b53227c248855eca0eef398355c.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586653.OTHER_5983911871_4888221",
                  "categoryName": "Self-Help",
                  "categoryId": "7802"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-study-aid-exam-prep",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//sg-live.slatic.net/p/41a212284d0d9aea18c62400624adce6.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586653.OTHER_5983911872_4888221",
                  "categoryName": "Study Aids & Exam Preparation",
                  "categoryId": "6913"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-education-local-books",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//vn-live-03.slatic.net/p/7/bo-2-doi-gang-tay-chong-nang-ho-ngon-han-quoc-trang-den-1472618719-5790122-1e2250f87e9a4a3b4f160feb518ecefa-zoom.jpg",
                  "categoryName": "Education Books",
                  "categoryId": "7816"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-entertainment-local-books",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//vn-live-03.slatic.net/p/7/that-lung-nu-mac-dam-cat-hoa-lazer-den-kmfashion-1506695525-70601851-a32da09985d715defcca8c15ee7a9876-zoom.jpg",
                  "categoryName": "Entertainment Books",
                  "categoryId": "7813"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-business-local-books",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//sg-live.slatic.net/p/17c85bbfdb8799d40604e01011bb0eb3.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586653.OTHER_5983911875_4888221",
                  "categoryName": "Business Books",
                  "categoryId": "7827"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-english-language-linguistics",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//sg-live.slatic.net/p/fdfa54cc478c31c1f227697930a0d53a.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586653.OTHER_5983911876_4888221",
                  "categoryName": "English Language, Linguistics & Writing",
                  "categoryId": "7356"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-professional-local-books",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//sg-live.slatic.net/p/41a212284d0d9aea18c62400624adce6.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586653.OTHER_5983911877_4888221",
                  "categoryName": "Professional Books",
                  "categoryId": "7806"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-travel-local-books",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//sg-live.slatic.net/p/17c85bbfdb8799d40604e01011bb0eb3.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586653.OTHER_5983911878_4888221",
                  "categoryName": "Travel Books",
                  "categoryId": "7800"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-romance-local-books",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//ph-live-03.slatic.net/p/6/2pcs-alloy-long-skate-board-skateboard-bridge-truck-professional-universal-intl-1504655880-15396263-c06ec5dd0505bbec21053c9cfdace9e9-zoom.jpg",
                  "categoryName": "Romance",
                  "categoryId": "7805"
                }
              ],
              "categoryIcon": "",
              "categoryUrl": "//www.lazada.co.th/books-online",
              "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel2TabDTO",
              "categoryName": "Books",
              "categoryId": "3450"
            }
          ],
          "categoryName_zh": "",
          "categoryIcon": "ic-cat-HomeLifestyl &#xe75c;",
          "id": "6634014",
          "position": "top",
          "childId": "Level_1_Category_No7",
          "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel1TabDTO",
          "categoryName": "Home & Lifestyle ",
          "level1CategoryId": "6634014"
        },
        {
          "level2TabList": [
            {
              "level3TabList": [
                {
                  "categoryUrl": "//www.lazada.co.th/shop-women-t-shirts-tops",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//laz-img-cdn.alicdn.com/images/ims-web/TB1J6L0H8LoK1RjSZFuXXXn0XXa.jpg",
                  "categoryName": "Tops",
                  "categoryId": "6810"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-women-dresses",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//laz-img-cdn.alicdn.com/images/ims-web/TB1WBT5H5rpK1RjSZFhXXXSdXXa.jpg",
                  "categoryName": "Dresses",
                  "categoryId": "6806"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-womens-clothing-pants",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//laz-img-cdn.alicdn.com/images/ims-web/TB1hur5HYvpK1RjSZFqXXcXUVXa.jpg",
                  "categoryName": "Pants & Leggings",
                  "categoryId": "6825"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-women-clothing-jackets-coats",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//laz-img-cdn.alicdn.com/images/ims-web/TB1xMeOH8LoK1RjSZFuXXXn0XXa.jpg",
                  "categoryName": "Jackets & Coats",
                  "categoryId": "6837"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-womens-skirts",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//th-live.slatic.net/p/ab545fdda762ec7a90017911f295a5fc.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586654.OTHER_6053620120_7613798",
                  "categoryName": "Skirts",
                  "categoryId": "6832"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-women-clothing-jeans",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//sg-live.slatic.net/p/7/710-super-skinny-jeans-2588-54019244-7bfb82523de7f2273098ef9871757f3a-catalog.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586654.OTHER_6053620121_7613798",
                  "categoryName": "Jeans",
                  "categoryId": "6800"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-women-overalls-jumpsuits",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//my-live-02.slatic.net/p/fd309f4dc4c6bda0673bcc6237090b88.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586654.OTHER_6053620122_7613798",
                  "categoryName": "Jumpsuits & Playsuits",
                  "categoryId": "13456"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-womens-hoodies-sweatshirts",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//my-live-02.slatic.net/original/abdaad972d56b8773df4e961d2527a41.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586654.OTHER_6053620123_7613798",
                  "categoryName": "Hoodies & Sweatshirts",
                  "categoryId": "13457"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-women-shorts",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//laz-img-cdn.alicdn.com/images/ims-web/TB1q17mixYaK1RjSZFnXXa80pXa.jpg",
                  "categoryName": "Shorts",
                  "categoryId": "6260"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-women-sweaters-cardigans",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//my-live-02.slatic.net/p/4458192111b58fe0014c5eac8a0bcaa4.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586654.OTHER_6053620125_7613798",
                  "categoryName": "Sweaters & Cardigans",
                  "categoryId": "6819"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/invisible-unisex-fashion-4",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//th-live.slatic.net/p/3c1d4720002943477d0e2dbfc987aa76.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586654.OTHER_6053620126_7613798",
                  "categoryName": "Couple & Family Sets",
                  "categoryId": "13465"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-women-muslim-wear",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//icms-image.slatic.net/images/ims-web/4988b5c5-5d33-4297-912a-486032814c8a.jpg",
                  "categoryName": "Muslim Wear",
                  "categoryId": "8046"
                }
              ],
              "categoryIcon": "",
              "categoryUrl": "//www.lazada.co.th/shop-women-clothing",
              "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel2TabDTO",
              "categoryName": "Women's Clothing",
              "categoryId": "6796"
            },
            {
              "level3TabList": [
                {
                  "categoryUrl": "//www.lazada.co.th/shop-womens-sneakers",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//laz-img-cdn.alicdn.com/images/ims-web/TB1sezDi4YaK1RjSZFnXXa80pXa.jpg",
                  "categoryName": "Sneakers",
                  "categoryId": "6718"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-womens-shoes-flip-flops-slides",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//ph-live.slatic.net/p/a6a65a8bb100df246496c19a13742211.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586654.OTHER_6053620129_7613798",
                  "categoryName": "Slides & Flip Flops",
                  "categoryId": "6715"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-womens-flat-shoes",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//icms-image.slatic.net/images/ims-web/5073fa82-1a74-46a1-84e5-5b1a694aed78.jpg",
                  "categoryName": "Flat Shoes",
                  "categoryId": "6678"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-womens-heels",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//icms-image.slatic.net/images/ims-web/1c09f213-e738-46d2-9fd2-f422ac04cbf4.jpg",
                  "categoryName": "Heels",
                  "categoryId": "6697"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-womens-shoes-accessories",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//icms-image.slatic.net/images/ims-web/7848c47f-7d74-44c6-ad10-1fb6b2217b31.jpg",
                  "categoryName": "Shoes Accessories",
                  "categoryId": "6778"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-womens-sandals",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//id-live.slatic.net/p/6d8e10a6b89323043d9b9560d53de355.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586654.OTHER_6053620133_7613798",
                  "categoryName": "Sandals",
                  "categoryId": "6713"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-womens-wedges",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//icms-image.slatic.net/images/ims-web/af4c89be-6a17-4ef6-a7de-5547003d1a9c.jpg",
                  "categoryName": "Wedges",
                  "categoryId": "6722"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-womens-boots",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//icms-image.slatic.net/images/ims-web/fd6d971f-3ed3-4eb6-9aff-e88dc83389cb.jpg",
                  "categoryName": "Boots",
                  "categoryId": "6741"
                }
              ],
              "categoryIcon": "",
              "categoryUrl": "//www.lazada.co.th/shop-women-shoes",
              "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel2TabDTO",
              "categoryName": "Women's Shoes",
              "categoryId": "6675"
            },
            {
              "level3TabList": [
                {
                  "categoryUrl": "//www.lazada.co.th/shop-women-lingerie-bras",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//icms-image.slatic.net/images/ims-web/b46512ba-46db-44d9-aeea-dc1b0d35cb48.jpg",
                  "categoryName": "Bras",
                  "categoryId": "6505"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-women-lingerie-pants-knickers",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//icms-image.slatic.net/images/ims-web/f92ebdb7-52e2-434c-86f7-141955e19c8b.jpg",
                  "categoryName": "Panties",
                  "categoryId": "6506"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-women-lingerie-shapewear",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//icms-image.slatic.net/images/ims-web/2798e31c-7ba8-4e02-9fc0-ecdd8054d9d6.jpg",
                  "categoryName": "Shapewear",
                  "categoryId": "6508"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-women-nightwear",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//th-live.slatic.net/p/0c81efbdb26fb08fd310cb37859522ac.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586654.OTHER_6053620139_7613798",
                  "categoryName": "Sleep & Loungewear",
                  "categoryId": "6509"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-women-lingerie-suspenders",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//sg-live.slatic.net/p/7/avidlove-lingerie-for-women-lace-sheer-sleepwear-dress-hot-underwear-nightwear-black-xl-intl-2834-03722337-91fe5d982e1fd450cf73c6403924c985-catalog.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586654.OTHER_6053620140_7613798",
                  "categoryName": "Sexy Lingerie",
                  "categoryId": "6507"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-womens-lingerie-accessories",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//icms-image.slatic.net/images/ims-web/517ae54d-1265-4c65-ad6c-c4572d3d2e16.jpg",
                  "categoryName": "Accessories",
                  "categoryId": "9633"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-womens-lingerie-sets",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//my-live-02.slatic.net/original/43b4c586461d06cae6c159757213d22b.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586654.OTHER_6053620142_7613798",
                  "categoryName": "Lingerie Sets",
                  "categoryId": "6562"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-women-lingerie-bathrobes",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//my-live.slatic.net/original/4ab7118ae8b2f944774bd9acef57fd23.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586654.OTHER_6053620143_7613798",
                  "categoryName": "Robes",
                  "categoryId": "6510"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-womens-camisoles-slips",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//my-live-02.slatic.net/original/38cac78dd7d63c27dea02bc2eef27a20.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586654.OTHER_6053620144_7613798",
                  "categoryName": "Camisoles & Slips",
                  "categoryId": "6563"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-womens-bodysuits",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//my-live-02.slatic.net/original/2d1b67db2e857329fb92835aaef34a93.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586654.OTHER_6053620145_7613798",
                  "categoryName": "Bodysuits",
                  "categoryId": "8548"
                }
              ],
              "categoryIcon": "",
              "categoryUrl": "//www.lazada.co.th/shop-women-lingerie-nightwear",
              "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel2TabDTO",
              "categoryName": "Lingerie, Sleep & Lounge",
              "categoryId": "5916"
            },
            {
              "level3TabList": [
                {
                  "categoryUrl": "//www.lazada.co.th/shop-womens-swimsuits",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//th-live.slatic.net/p/fbf1de17b8ce4dcf66779799242ad8d9.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586654.OTHER_6053620146_7613798",
                  "categoryName": "Swimsuits",
                  "categoryId": "13520"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-womens-bikinis",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//my-live-02.slatic.net/p/8b97c59f152cab8bb6cc93519107322a.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586654.OTHER_6053620147_7613798",
                  "categoryName": "Bikinis",
                  "categoryId": "6860"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-women-swimwear-beachwear-accessories",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//my-live-02.slatic.net/p/ab3de5b3976e58401c7376332dd22e22.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586654.OTHER_6053620148_7613798",
                  "categoryName": "Beachwear & Accessories",
                  "categoryId": "6863"
                }
              ],
              "categoryIcon": "",
              "categoryUrl": "//www.lazada.co.th/shop-women-swimwear",
              "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel2TabDTO",
              "categoryName": "Swimwear & Beachwear",
              "categoryId": "6859"
            },
            {
              "level3TabList": [
                {
                  "categoryUrl": "//www.lazada.co.th/shop-women-accessories-hats",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//my-live-02.slatic.net/p/71e07cdf170276cfde7fab2cb914fd52.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586654.OTHER_6053620149_7613798",
                  "categoryName": "Hats & Caps",
                  "categoryId": "6941"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-women-accessories-hair-accessories",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//my-live-02.slatic.net/p/df7ffd03a83ba298e2d5ae682f6acf6f.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586654.OTHER_6053620150_7613798",
                  "categoryName": "Hair Accessories",
                  "categoryId": "6942"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-women-accessories-belts",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//my-live-02.slatic.net/p/92e54376dd02b1159fc72d9bf1150f5d.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586654.OTHER_6053620151_7613798",
                  "categoryName": "Belts",
                  "categoryId": "6938"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-women-socks-tights",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//my-live-02.slatic.net/original/13cf15b220e9a81625352dfbdf75a4b7.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586654.OTHER_6053620152_7613798",
                  "categoryName": "Socks & Tights",
                  "categoryId": "6856"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-women-accessories-umbrellas",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//my-live-02.slatic.net/p/cb11a8695ea9f6d535b0a07b48f12b55.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586654.OTHER_6053620153_7613798",
                  "categoryName": "Umbrellas",
                  "categoryId": "6943"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-women-accessories-scarves",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//my-live-02.slatic.net/p/3d8de2189817dc21db057a0a0a865897.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586654.OTHER_6053620154_7613798",
                  "categoryName": "Scarves",
                  "categoryId": "6945"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-women-accessories-gloves",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//my-live-02.slatic.net/original/3493353971b79c1d95413a5a272eb921.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586654.OTHER_6053620155_7613798",
                  "categoryName": "Gloves",
                  "categoryId": "6946"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-fashion-face-mask",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//laz-img-cdn.alicdn.com/images/ims-web/TB1h1g_R8r0gK0jSZFnXXbRRXXa.jpg",
                  "categoryName": "Face mask",
                  "categoryId": "42055002"
                }
              ],
              "categoryIcon": "",
              "categoryUrl": "//www.lazada.co.th/shop-women-accessories",
              "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel2TabDTO",
              "categoryName": "Women's Accessories",
              "categoryId": "6795"
            },
            {
              "level3TabList": [
                {
                  "categoryUrl": "//www.lazada.co.th/shop-women-bags-cross-body-bags",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//id-live.slatic.net/p/f2735c77ecbd22f2ffeb7508405625c2.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586654.OTHER_6053620157_7613798",
                  "categoryName": "Cross Body & Shoulder Bags",
                  "categoryId": "13432"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-women-bags-backpacks",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//id-live.slatic.net/p/f92532691a956d8ef8b2d97265b23e0b.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586654.OTHER_6053620158_7613798",
                  "categoryName": "Backpacks",
                  "categoryId": "13435"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-women-bags-purses",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//id-live.slatic.net/p/2693451bfee21cfa8b859e56bd3c1fab.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586654.OTHER_6053620159_7613798",
                  "categoryName": "Wallets",
                  "categoryId": "13479"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-women-bags-top-handle-bags",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//th-live.slatic.net/p/8a55d198464ab1e9388d0dab4ce329f8.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586654.OTHER_6053620160_7613798",
                  "categoryName": "Top-Handle Bags",
                  "categoryId": "13433"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-women-bags-tote-bags",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//laz-img-cdn.alicdn.com/images/ims-web/TB1dEMmixYaK1RjSZFnXXa80pXa.jpg",
                  "categoryName": "Tote Bags",
                  "categoryId": "13431"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-womens-bag-charms",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//sg-live.slatic.net/p/8/lalang-leather-tassel-pendant-women-bag-charm-key-chain-car-simple-hang-decorations-black-5761-1248876-c235d805dbaca55df2f47555dd609524-catalog.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586654.OTHER_6053620162_7613798",
                  "categoryName": "Bag Accessories",
                  "categoryId": "13478"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-womens-bags-card-holder",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//my-live-02.slatic.net/p/c6e57ec9893d15c6e651a7987592515e.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586654.OTHER_6053620163_7613798",
                  "categoryName": "Card Holders",
                  "categoryId": "13481"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-womens-bags-wristlets",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//id-live.slatic.net/p/f15f19aa271a2efab9ee097c80636f9c.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586654.OTHER_6053620164_7613798",
                  "categoryName": "Wristlets",
                  "categoryId": "13436"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-womens-coin-purses",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//my-live-02.slatic.net/original/92cfe7ee3f6fea92fdd765827b217d0e.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586654.OTHER_6053620165_7613798",
                  "categoryName": "Coin Purses & Pouches",
                  "categoryId": "13480"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-women-bags-clutches",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//laz-img-cdn.alicdn.com/images/ims-web/TB1tx.airvpK1RjSZFqXXcXUVXa.jpg",
                  "categoryName": "Clutches",
                  "categoryId": "13434"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-womens-bags-key-holder",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//id-live.slatic.net/p/bb082af6d1526ffbdb774aa6dfb4a9ad.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586654.OTHER_6053620167_7613798",
                  "categoryName": "Key Holders",
                  "categoryId": "13482"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-travel-luggage-2",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//sg-live.slatic.net/p/mdc/4fbfd788101462b89288aff52bf8e933.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586654.OTHER_6053620168_7613798",
                  "categoryName": "Luggage & Travel",
                  "categoryId": "13425"
                }
              ],
              "categoryIcon": "",
              "categoryUrl": "//www.lazada.co.th/shop-women-bags",
              "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel2TabDTO",
              "categoryName": "Women's Bags",
              "categoryId": "13420"
            },
            {
              "level3TabList": [
                {
                  "categoryUrl": "//www.lazada.co.th/shop-womens-eyeglasses",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//th-live.slatic.net/p/4029234a35617d0bfff01b27b0c3b25a.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586654.OTHER_6053620169_7613798",
                  "categoryName": "Eyesglasses",
                  "categoryId": "12513"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-womens-sunglasses",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//my-live-02.slatic.net/p/8fa9eb7a858cf787f6013580c316fe4b.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586654.OTHER_6053620170_7613798",
                  "categoryName": "Sunglasses",
                  "categoryId": "12512"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-contact-lens",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//laz-img-cdn.alicdn.com/images/ims-web/TB1aaeVHYvpK1RjSZFqXXcXUVXa.jpg",
                  "categoryName": "Contact Lens",
                  "categoryId": "12451"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-eyewear-accessories",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//sg-live.slatic.net/p/6/anti-slip-soft-silicone-spectacle-earhook-sport-ear-muff-grip-lock-tip-holder-neck-strap-glass-eyewear-anti-slip-eye-wear-anti-slip-temple-holder-0504-05089711-26c5730a890ef77e45087d072e0ffff8-catalog.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586654.OTHER_6053620172_7613798",
                  "categoryName": "Accessories",
                  "categoryId": "12452"
                }
              ],
              "categoryIcon": "",
              "categoryUrl": "//www.lazada.co.th/shop-womens-eyeglasses",
              "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel2TabDTO",
              "categoryName": "Women's Eyewear",
              "categoryId": "12515"
            },
            {
              "level3TabList": [
                {
                  "categoryUrl": "//www.lazada.co.th/shop-womens-casual-watches",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//my-live-02.slatic.net/p/e8819e3f1b41da72b1b7a83e7a82e96f.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586654.OTHER_6053620192_7613798",
                  "categoryName": "Casual Watches",
                  "categoryId": "3286"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-luxury-womens-watches",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//my-live-02.slatic.net/p/24f6263fd4397ec1aa7935a0c08487d4.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586654.OTHER_6053620193_7613798",
                  "categoryName": "Luxury Watches",
                  "categoryId": "10100860"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-womens-business-watches",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//my-live-02.slatic.net/p/4a83b863278cee55b4d37397076c5ecc.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586654.OTHER_6053620194_7613798",
                  "categoryName": "Formal Watches",
                  "categoryId": "3287"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-womens-sports-watches",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//sg-live.slatic.net/p/8/casio-standard-digital-dark-blue-resin-strap-watch-lw203-2a-0177-44339817-b1f39d9435e596f75c7ba999e0d9fa99-catalog.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586654.OTHER_6053620195_7613798",
                  "categoryName": "Sports Watches",
                  "categoryId": "3289"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-womenwatches-accessories",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//id-live.slatic.net/p/55105ddd2d440e547727252f26357484.png_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586654.OTHER_6053620196_7613798",
                  "categoryName": "Watch Accessories",
                  "categoryId": "10100892"
                }
              ],
              "categoryIcon": "",
              "categoryUrl": "//www.lazada.co.th/shop-womens-watches",
              "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel2TabDTO",
              "categoryName": "Women's Watches",
              "categoryId": "3285"
            }
          ],
          "categoryName_zh": "",
          "categoryIcon": "ic-cat-WomensFashio &#xe760;",
          "id": "6634015",
          "position": "top",
          "childId": "Level_1_Category_No8",
          "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel1TabDTO",
          "categoryName": "Women's Fashion & Accessories",
          "level1CategoryId": "6634015"
        },
        {
          "level2TabList": [
            {
              "level3TabList": [
                {
                  "categoryUrl": "//www.lazada.co.th/shop-mens-casual-tops",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//laz-img-cdn.alicdn.com/images/ims-web/TB1IFDoi8LoK1RjSZFuXXXn0XXa.jpg",
                  "categoryName": "T-Shirts & Tanks",
                  "categoryId": "7077"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-men-shirts",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//my-live-02.slatic.net/p/9a7cbf667019bcf3141d3ed36e945ff8.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586655.OTHER_6053620215_7613801",
                  "categoryName": "Shirts",
                  "categoryId": "7081"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-men-polo-shirts",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//laz-img-cdn.alicdn.com/images/ims-web/TB1AwMnixYaK1RjSZFnXXa80pXa.jpg",
                  "categoryName": "Polo Shirts",
                  "categoryId": "13459"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-men-pants",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//sg-live.slatic.net/p/a75e75fc86fe93b99320ffb28e73e0ac.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586655.OTHER_6053620217_7613801",
                  "categoryName": "Pants",
                  "categoryId": "7102"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-men-jeans",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//id-live-03.slatic.net/p/7/carvil-jay-50-jeans-pria-dark-brown-1470391988-7318087-967e8eec9e413a32b67ae02714969d0d-zoom.jpg",
                  "categoryName": "Jeans",
                  "categoryId": "7071"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-men-hoodies",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//ph-live-02.slatic.net/p/7b96fdf939dac1d714d771d20f4145ed.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586655.OTHER_6053620219_7613801",
                  "categoryName": "Hoodies & Sweatshirts",
                  "categoryId": "7251"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-men-jackets-coats",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//id-live.slatic.net/original/e0b993dc525165b08ba1a93bf5ef793a.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586655.OTHER_6053620220_7613801",
                  "categoryName": "Jackets & Coats",
                  "categoryId": "7090"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-men-shorts",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//sg-live.slatic.net/p/5ea195b787196ea73d455f1ffcec350a.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586655.OTHER_6053620221_7613801",
                  "categoryName": "Shorts",
                  "categoryId": "7342"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-men-swimwear",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//sg-live.slatic.net/original/de3150ef140da58138377b53d264957f.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586655.OTHER_6053620222_7613801",
                  "categoryName": "Swimwear",
                  "categoryId": "7120"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-men-suits-ties",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//sg-live.slatic.net/original/53b4dc8bf37d4a2f7460f651bb9632cc.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586655.OTHER_6053620223_7613801",
                  "categoryName": "Suits",
                  "categoryId": "7113"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-men-sweaters-cardigans",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//my-live-02.slatic.net/original/66682afb2e120e9e95bf59392383edc5.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586655.OTHER_6053620224_7613801",
                  "categoryName": "Sweaters & Cardigans",
                  "categoryId": "7084"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-men-baju-melayus-cekak-musang",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//id-live.slatic.net/p/798bc840cd2eff900ee6b18fd56594d4.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586655.OTHER_6053620225_7613801",
                  "categoryName": "Muslim Wear",
                  "categoryId": "13461"
                }
              ],
              "categoryIcon": "",
              "categoryUrl": "//www.lazada.co.th/shop-men-clothing",
              "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel2TabDTO",
              "categoryName": "Men's Clothing",
              "categoryId": "7070"
            },
            {
              "level3TabList": [
                {
                  "categoryUrl": "//www.lazada.co.th/shop-mens-sneaker",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//id-live.slatic.net/p/5a078371a2a28675744bbaa7ea2107fc.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586655.OTHER_6053620226_7613801",
                  "categoryName": "Sneakers",
                  "categoryId": "6657"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-mens-flip-flops-sandals",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//th-live.slatic.net/original/4f1dd3cbeb3898c551e7e59e37f8df37.jpg_240x240q80.jpg_.webp?spm=a2o9e.11151479.0.0.3aa5ce739rR8Ea&file=4f1dd3cbeb3898c551e7e59e37f8df37.jpg_240x240q80.jpg_.webp&scm=1003.4.icms-zebra-5000413-2586655.OTHER_6053620227_7613801",
                  "categoryName": "Flip Flops & Sandals",
                  "categoryId": "6663"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-mens-loafers-slip-on-shoes",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//laz-img-cdn.alicdn.com/images/ims-web/TB10GzjdRjTBKNjSZFuXXb0HFXa.jpg",
                  "categoryName": "Slip-Ons & Loafers",
                  "categoryId": "7038"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-mens-shoes-accessories",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//id-live.slatic.net/p/6e5c5f470ff8463f1ffefbcb8da6032e.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586655.OTHER_6053620229_7613801",
                  "categoryName": "Shoes Accessories",
                  "categoryId": "6733"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-mens-formal-shoes",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//id-live.slatic.net/p/f2bbbe7ae7d830069798705792cf751d.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586655.OTHER_6053620230_7613801",
                  "categoryName": "Formal Shoes",
                  "categoryId": "6672"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-mens-boots",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//id-live.slatic.net/p/790e654c177d0922c16f2e0fcce189a2.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586655.OTHER_6053620231_7613801",
                  "categoryName": "Boots",
                  "categoryId": "6665"
                }
              ],
              "categoryIcon": "",
              "categoryUrl": "//www.lazada.co.th/shop-mens-shoes",
              "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel2TabDTO",
              "categoryName": "Men's Shoes",
              "categoryId": "6649"
            },
            {
              "level3TabList": [
                {
                  "categoryUrl": "//www.lazada.co.th/shop-men-clothing-underwear",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//sg-live.slatic.net/original/3a59b833bf22f7dd5700e1f6e05194b4.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586655.OTHER_6053620232_7613801",
                  "categoryName": "Briefs",
                  "categoryId": "7109"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-men-trunks-boxers",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//my-live-02.slatic.net/p/78105edc209b21b43c2c1fbbeefb6cb3.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586655.OTHER_6053620233_7613801",
                  "categoryName": "Trunks & Boxers",
                  "categoryId": "13524"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-men-nightwear",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//my-live-02.slatic.net/p/824ab14be12e69e1b494fd9f443a8230.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586655.OTHER_6053620234_7613801",
                  "categoryName": "Lounge Wear",
                  "categoryId": "7111"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-men-underwear-thongs-others",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//my-live-02.slatic.net/p/224f26ba29924f09a5612f3c34e00f03.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586655.OTHER_6053620235_7613801",
                  "categoryName": "Thongs & Others",
                  "categoryId": "13525"
                }
              ],
              "categoryIcon": "",
              "categoryUrl": "//www.lazada.co.th/shop-mens-clothing-underwear",
              "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel2TabDTO",
              "categoryName": "Men's Underwear",
              "categoryId": "7108"
            },
            {
              "level3TabList": [
                {
                  "categoryUrl": "//www.lazada.co.th/shop-men-accessories-hats",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//sg-live.slatic.net/p/mdc/0be89fdfc6d85727adf29851a96e0413.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586655.OTHER_6053620236_7613801",
                  "categoryName": "Hats & Caps",
                  "categoryId": "7007"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-men-accessories-belts",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//my-live-02.slatic.net/p/d94e51efa9fe22cfa7726b94e9b8b34c.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586655.OTHER_6053620237_7613801",
                  "categoryName": "Belts",
                  "categoryId": "7006"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-men-socks",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//sg-live.slatic.net/p/7/eozy-5-pair-fashion-mens-classic-rhombus-pattern-business-socks-autumn-winter-thick-warm-casual-socks-intl-7729-91583199-1979ee6e25ae32aa1214ded0a6080826-catalog.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586655.OTHER_6053620238_7613801",
                  "categoryName": "Socks",
                  "categoryId": "7252"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-men-accessories-ties",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//sg-live-02.slatic.net/p/7/high-quality-2016-autumn-fashion-business-casual-ties-for-men-5cm-slim-nanofiber-waterproof-tie-silver-dark-stripe-gift-box-silver-2923-4310559-8bed4cc161662e058ff3f67d7bce525b-catalog.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586655.OTHER_6053620239_7613801",
                  "categoryName": "Ties",
                  "categoryId": "6996"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-men-accessories-scarves-gloves-gloves",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//my-live-02.slatic.net/original/3493353971b79c1d95413a5a272eb921.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586655.OTHER_6053620240_7613801",
                  "categoryName": "Gloves",
                  "categoryId": "7009"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-men-accessories-bow-ties",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//sg-live.slatic.net/p/7/whyus-double-layer-solid-color-men-butterfly-cravat-bowtie-neckwear-adjustable-bow-tie-color-wine-red-8149-9234218-9c02fa4556caad63ed1e421ca06bd05c-catalog.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586655.OTHER_6053620241_7613801",
                  "categoryName": "Bow Ties",
                  "categoryId": "6997"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-men-accessories-scarves",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//my-live-02.slatic.net/p/f660916b70f8ce7dde490857e7b47636.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586655.OTHER_6053620242_7613801",
                  "categoryName": "Scarves",
                  "categoryId": "6998"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-fashion-men-accessories-braces",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//my-live-02.slatic.net/p/c62d8edc972b3993da872931b74135a6.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586655.OTHER_6053620243_7613801",
                  "categoryName": "Trouser Braces/Suspenders",
                  "categoryId": "8074"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-men-accessories-umbrellas",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//my-live-02.slatic.net/p/9d99f58598f4a3c8f4a5f255d9c28473.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586655.OTHER_6053620244_7613801",
                  "categoryName": "Umbrellas",
                  "categoryId": "6999"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-men-face-mask",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//laz-img-cdn.alicdn.com/images/ims-web/TB1fEg_R8r0gK0jSZFnXXbRRXXa.jpg",
                  "categoryName": "Face mask",
                  "categoryId": "42055201"
                }
              ],
              "categoryIcon": "",
              "categoryUrl": "//www.lazada.co.th/shop-men-accessories",
              "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel2TabDTO",
              "categoryName": "Men's Accessories",
              "categoryId": "6799"
            },
            {
              "level3TabList": [
                {
                  "categoryUrl": "//www.lazada.co.th/shop-mens-cross-body-bags",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//th-live.slatic.net/p/03cd157d71f0929f3206c69495a32a9b.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586655.OTHER_6053620246_7613801",
                  "categoryName": "Crossbody Bags",
                  "categoryId": "13441"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-mens-backpacks",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//id-live.slatic.net/p/bda99187cc03f990b2076c73a315795a.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586655.OTHER_6053620247_7613801",
                  "categoryName": "Backpacks",
                  "categoryId": "10100762"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-men-wallets",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//id-live.slatic.net/p/390723c70305763f0ac53a9890d145d0.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586655.OTHER_6053620248_7613801",
                  "categoryName": "Wallets",
                  "categoryId": "10100763"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-waist-bags",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//sg-live.slatic.net/original/e0782bd7b17d7bbe12e3cd1284287cbe.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586655.OTHER_6053620249_7613801",
                  "categoryName": "Waist Packs",
                  "categoryId": "13515"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-men-bags-messenger-bags",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//laz-img-cdn.alicdn.com/images/ims-web/TB1oUSHc2uSBuNkHFqDXXXfhVXa.jpg",
                  "categoryName": "Messenger Bags",
                  "categoryId": "13438"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-mens-bags-card-holder",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//my-live-02.slatic.net/p/c6e57ec9893d15c6e651a7987592515e.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586655.OTHER_6053620251_7613801",
                  "categoryName": "Card Holders",
                  "categoryId": "13486"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-mens-bags-key-holder",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//sg-live.slatic.net/p/7/multi-functional-genuine-leather-folding-door-key-electronic-key-holder-bag-credit-card-coins-cash-snap-button-holder-wallet-bag-pouch-coffee-4255-1262039-c0cdb4fa2a28104b25f43512708eb12a-catalog.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586655.OTHER_6053620252_7613801",
                  "categoryName": "Key Holders",
                  "categoryId": "13487"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-men-formal-bags",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//my-live-02.slatic.net/original/84b99d6933dbeb626b697ad8317777f8.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586655.OTHER_6053620253_7613801",
                  "categoryName": "Business Bags",
                  "categoryId": "13439"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-laptop-bags-cases",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//id-live.slatic.net/p/3b2a32d8aa7322d8d5661b127ac67542.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586655.OTHER_6053620254_7613801",
                  "categoryName": "Laptop Bags",
                  "categoryId": "13454"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-mens-money-clips",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//sg-live.slatic.net/original/b7b9aa5c90291dcae6506c4f9fd19456.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586655.OTHER_6053620255_7613801",
                  "categoryName": "Money Clips",
                  "categoryId": "13488"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-mens-tote-bags",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//sg-live.slatic.net/p/01309f298c9badf760e686f5231626e4.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586655.OTHER_6053620256_7613801",
                  "categoryName": "Tote Bags",
                  "categoryId": "13442"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-travel-luggage-2",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//sg-live.slatic.net/p/mdc/4fbfd788101462b89288aff52bf8e933.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586655.OTHER_6053620257_7613801",
                  "categoryName": "Luggage & Travel",
                  "categoryId": "13425"
                }
              ],
              "categoryIcon": "",
              "categoryUrl": "//www.lazada.co.th/shop-men-bags",
              "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel2TabDTO",
              "categoryName": "Men's Bags",
              "categoryId": "13421"
            },
            {
              "level3TabList": [
                {
                  "categoryUrl": "//www.lazada.co.th/shop-mens-eyeglasses",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//th-live.slatic.net/p/1baa0f66e2ab519f776b39342fb1e5a7.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586655.OTHER_6053620258_7613801",
                  "categoryName": "Eyesglasses",
                  "categoryId": "12517"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-mens-sunglasses",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//id-live.slatic.net/p/ce05b496b579677c67c2f97056eec6a2.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586655.OTHER_6053620259_7613801",
                  "categoryName": "Sunglasses",
                  "categoryId": "12511"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-contact-lens",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//laz-img-cdn.alicdn.com/images/ims-web/TB1aaeVHYvpK1RjSZFqXXcXUVXa.jpg",
                  "categoryName": "Contact Lens",
                  "categoryId": "12451"
                }
              ],
              "categoryIcon": "",
              "categoryUrl": "//www.lazada.co.th/shop-mens-eyeglasses",
              "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel2TabDTO",
              "categoryName": "Men's Eyewear",
              "categoryId": "12516"
            },
            {
              "level3TabList": [
                {
                  "categoryUrl": "//www.lazada.co.th/shop-mens-casual-watches",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//my-live-02.slatic.net/p/e8819e3f1b41da72b1b7a83e7a82e96f.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586655.OTHER_6053620271_7613801",
                  "categoryName": "Casual Watches",
                  "categoryId": "5831"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-mens-sports-watches",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//sg-live.slatic.net/p/8/casio-standard-digital-dark-blue-resin-strap-watch-lw203-2a-0177-44339817-b1f39d9435e596f75c7ba999e0d9fa99-catalog.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586655.OTHER_6053620272_7613801",
                  "categoryName": "Sports Watches",
                  "categoryId": "5834"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-mens-business-watches",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//id-live.slatic.net/p/e5579ecc37319d0de6b4cf623f52ec8d.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586655.OTHER_6053620273_7613801",
                  "categoryName": "Formal Watches",
                  "categoryId": "5832"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-mens-watch-accessories",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//id-live.slatic.net/p/54b072d2ca083ee314aacf141b500f63.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586655.OTHER_6053620274_7613801",
                  "categoryName": "Watches Accessories",
                  "categoryId": "5836"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-luxury-mens-watches",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//id-live.slatic.net/p/54cdcb12e4abc3bf3db5b287c2cf0b1f.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586655.OTHER_6053620275_7613801",
                  "categoryName": "Luxury Watches",
                  "categoryId": "10100789"
                }
              ],
              "categoryIcon": "",
              "categoryUrl": "//www.lazada.co.th/shop-mens-watches",
              "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel2TabDTO",
              "categoryName": "Men's Watches",
              "categoryId": "5786"
            }
          ],
          "categoryName_zh": "",
          "categoryIcon": "ic-cat-MensFashion &#xe75f;",
          "id": "6634016",
          "position": "top",
          "childId": "Level_1_Category_No9",
          "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel1TabDTO",
          "categoryName": "Men's Fashion & Accessories",
          "level1CategoryId": "6634016"
        },
        {
          "level2TabList": [
            {
              "level3TabList": [
                {
                  "categoryUrl": "//www.lazada.co.th/shop-fashion-boys-t-shirts-shirts",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//my-live-02.slatic.net/p/85f4fda8f9daade4ff7ee5c795a9c4e3.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586656.OTHER_6053620734_7613840",
                  "categoryName": "T-Shirts & Shirts",
                  "categoryId": "3307"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-underwear",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//my-live-02.slatic.net/p/1e05ba5254d7201eb70980961a7beaa6.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586656.OTHER_6053620735_7613840",
                  "categoryName": "Underwear",
                  "categoryId": "10100761"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-fashion-boys-pants-jeans",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//my-live-02.slatic.net/p/766fd956b8e6cc6c82b7c53fa0f8910a.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586656.OTHER_6053620736_7613840",
                  "categoryName": "Pants & Jeans",
                  "categoryId": "3308"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-boys-shorts",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//my-live-02.slatic.net/p/7871b6546d085a39cc1abca7fb813a36.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586656.OTHER_6053620737_7613840",
                  "categoryName": "Shorts",
                  "categoryId": "3343"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-fashion-boys-jackets-coats",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//my-live-02.slatic.net/p/912642ce164018d50840b656310aeb25.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586656.OTHER_6053620738_7613840",
                  "categoryName": "Jackets & Coats",
                  "categoryId": "3310"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-boys-hoodies",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//my-live-02.slatic.net/p/b2f9f7bb85334a98890d852fb2e26cad.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586656.OTHER_6053620739_7613840",
                  "categoryName": "Hoodies",
                  "categoryId": "7061"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-boys-swimsuits",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//sg-live.slatic.net/p/f70bcc507dd812608fca4d3fc894eca7.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586656.OTHER_6053620740_7613840",
                  "categoryName": "Swimwear",
                  "categoryId": "7066"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-fashion-boys-sleepwear",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//my-live-02.slatic.net/original/d6e38365ad85645776f63b1bf0bc1125.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586656.OTHER_6053620741_7613840",
                  "categoryName": "Sleepwear",
                  "categoryId": "3314"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-socks",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//my-live-02.slatic.net/p/7fa7fae67b7dcebd1014cb8cec96e058.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586656.OTHER_6053620742_7613840",
                  "categoryName": "Socks",
                  "categoryId": "10100760"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-boys-face-mask",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//laz-img-cdn.alicdn.com/images/ims-web/TB1QE0QTRr0gK0jSZFnXXbRRXXa.jpg",
                  "categoryName": "Face mask",
                  "categoryId": "42068201"
                }
              ],
              "categoryIcon": "",
              "categoryUrl": "//www.lazada.co.th/shop-fashion-boys-clothing",
              "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel2TabDTO",
              "categoryName": "Boys' Clothing",
              "categoryId": "3306"
            },
            {
              "level3TabList": [
                {
                  "categoryUrl": "//www.lazada.co.th/shop-fashion-girls-dresses",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//my-live-02.slatic.net/p/8080429126f51ddad613cd41f9bcf60d.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586656.OTHER_6053620744_7613840",
                  "categoryName": "Dresses",
                  "categoryId": "6284"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-fashion-girls-shirts-tops",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//my-live-02.slatic.net/p/d074d17a1fe649da64ef236746531a0c.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586656.OTHER_6053620745_7613840",
                  "categoryName": "Tops",
                  "categoryId": "6278"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-girls-underwear-sleepwear",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//icms-image.slatic.net/images/ims-web/2e3e3a3c-b9c6-43f2-81df-bf02293f6eae.jpg",
                  "categoryName": "Underwear & Sleepwear",
                  "categoryId": "6309"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-girls-clothing-bottoms",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//my-live-02.slatic.net/p/48c8467826b8aa628172352352684b2a.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586656.OTHER_6053620747_7613840",
                  "categoryName": "Bottoms",
                  "categoryId": "6283"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-girls-swimsuits",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//th-live.slatic.net/p/925e539665e3f872efa6b0e6e74566ef.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586656.OTHER_6053620748_7613840",
                  "categoryName": "Swimsuits",
                  "categoryId": "7375"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-girls-socks-tights",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//my-live-02.slatic.net/p/4/smile-ykk-5-pairs-baby-toddler-mixed-winter-3d-cotton-ankle-socks-big-eyes-9239-676290521-1572a89a28bbb640830eb7cacf87edd6-.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586656.OTHER_6053620749_7613840",
                  "categoryName": "Socks & Tights",
                  "categoryId": "7426"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-fashion-girls-caps-hats",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//my-live-02.slatic.net/p/71e07cdf170276cfde7fab2cb914fd52.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586656.OTHER_6053620750_7613840",
                  "categoryName": "Hats & Caps",
                  "categoryId": "6435"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-fashion-girls-jackets-coats",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//my-live-02.slatic.net/p/53ada961912d61b639c43f7a9edc8440.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586656.OTHER_6053620751_7613840",
                  "categoryName": "Jackets & Coats",
                  "categoryId": "6305"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-girls-hair-accories",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//my-live-02.slatic.net/original/f42f0802c52792a65708232baa3ab03b.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586656.OTHER_6053620752_7613840",
                  "categoryName": "Hair Accessories",
                  "categoryId": "7060"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-fashion-girls-belts",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//my-live-02.slatic.net/p/97ece2630bad859ba360d5f47685f162.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586656.OTHER_6053620753_7613840",
                  "categoryName": "Belts",
                  "categoryId": "6434"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-girls-hoodies-2",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//my-live-02.slatic.net/original/abdaad972d56b8773df4e961d2527a41.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586656.OTHER_6053620754_7613840",
                  "categoryName": "Hoodies",
                  "categoryId": "13463"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-fashion-girls-umbrellas-rainwear",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//my-live-02.slatic.net/p/055bb1dc83a8add396a8528ba9c0c3bd.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586656.OTHER_6053620755_7613840",
                  "categoryName": "Umbrellas & Rainwear",
                  "categoryId": "6469"
                }
              ],
              "categoryIcon": "",
              "categoryUrl": "//www.lazada.co.th/shop-fashion-girls-clothing",
              "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel2TabDTO",
              "categoryName": "Girls' Clothing",
              "categoryId": "6302"
            },
            {
              "level3TabList": [
                {
                  "categoryUrl": "//www.lazada.co.th/shop-fashion-boys-sneakers",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//sg-live.slatic.net/p/c0d580af0a2a47e12d5bf8aecfb07428.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586656.OTHER_6053620756_7613840",
                  "categoryName": "Sneakers",
                  "categoryId": "6290"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-boys-flip-flop-slides-sandals",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//th-live.slatic.net/original/4f1dd3cbeb3898c551e7e59e37f8df37.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586656.OTHER_6053620757_7613840",
                  "categoryName": "Flip Flops, Slides & Sandals",
                  "categoryId": "6433"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-boys-formal-shoes",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//th-live.slatic.net/p/b38f2805abef4421dc1d53d9bbfa2329.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586656.OTHER_6053620758_7613840",
                  "categoryName": "Formal Shoes",
                  "categoryId": "6291"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-fashion-boys-slip-ons",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//my-live-02.slatic.net/original/e96796f62e936020dbad4df52d4996d2.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586656.OTHER_6053620759_7613840",
                  "categoryName": "Slip-Ons & Loafers",
                  "categoryId": "6299"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-fashion-boys-boots-wellies",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//my-live-02.slatic.net/p/7e8f613e714eb0ffacbfe7381300b73c.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586656.OTHER_6053620760_7613840",
                  "categoryName": "Boots",
                  "categoryId": "6429"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-fashion-boys-shoes-accessories",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//my-live-02.slatic.net/p/2ec4105f508478f739697cb6c8c62389.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586656.OTHER_6053620761_7613840",
                  "categoryName": "Shoes Accessories",
                  "categoryId": "6430"
                }
              ],
              "categoryIcon": "",
              "categoryUrl": "//www.lazada.co.th/shop-fashion-boys-shoes",
              "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel2TabDTO",
              "categoryName": "Boys' Shoes",
              "categoryId": "6292"
            },
            {
              "level3TabList": [
                {
                  "categoryUrl": "//www.lazada.co.th/shop-girls-flip-flops-slides-sandals",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//my-live-02.slatic.net/p/a4314d88034fdd6958148f3330b781ef.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586656.OTHER_6053620762_7613840",
                  "categoryName": "Flip Flops, Slides & Sandals",
                  "categoryId": "6275"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-fashion-girls-sneakers",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//my-live-02.slatic.net/p/5e1f522fc6508476cf9a703049beaee5.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586656.OTHER_6053620763_7613840",
                  "categoryName": "Sneakers",
                  "categoryId": "6253"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-girls-flats-slip-on-shoes",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//sg-live.slatic.net/p/fc6b506932bad6297e422e40a79d4eae.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586656.OTHER_6053620764_7613840",
                  "categoryName": "Flats & Slip-Ons",
                  "categoryId": "6270"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-girls-formal-shoes",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//my-live-02.slatic.net/p/c5b2d840918036045c74104f98482770.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586656.OTHER_6053620765_7613840",
                  "categoryName": "Formal Shoes",
                  "categoryId": "6256"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-fashion-girls-boots-wellies",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//sg-live.slatic.net/p/158b45135c6e9e43aea762447953e1f4.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586656.OTHER_6053620766_7613840",
                  "categoryName": "Boots",
                  "categoryId": "6272"
                }
              ],
              "categoryIcon": "",
              "categoryUrl": "//www.lazada.co.th/shop-fashion-girls-shoes",
              "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel2TabDTO",
              "categoryName": "Girls' Shoes",
              "categoryId": "6268"
            },
            {
              "level3TabList": [
                {
                  "categoryUrl": "//www.lazada.co.th/shop-boys-watches",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//my-live-02.slatic.net/original/465d9e16effb12683b07b36db28353b1.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586656.OTHER_6053620767_7613840",
                  "categoryName": "Boys Watches",
                  "categoryId": "6523"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-girls-watches",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//my-live-02.slatic.net/p/2ac29e327e64721ab27bdbe9652ec484.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586656.OTHER_6053620768_7613840",
                  "categoryName": "Girls Watches",
                  "categoryId": "6524"
                }
              ],
              "categoryIcon": "",
              "categoryUrl": "//www.lazada.co.th/shop-kids-watches",
              "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel2TabDTO",
              "categoryName": "Kids' Watches",
              "categoryId": "6522"
            },
            {
              "level3TabList": [
                {
                  "categoryUrl": "//www.lazada.co.th/shop-kids-backpack-trolleys",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//id-live-02.slatic.net/original/dfb1af7cd83d683ce13db4d18965431e.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586656.OTHER_6053620769_7613840",
                  "categoryName": "Backpacks Trolley",
                  "categoryId": "13449"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-kids-shoulder-bags",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//my-live-02.slatic.net/p/79bcbbfb6dcdf5c735b812ea073493de.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586656.OTHER_6053620770_7613840",
                  "categoryName": "Bags",
                  "categoryId": "13448"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-kids-travel-accessories",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//my-live-02.slatic.net/p/281040b449680baee17735c4ff090c88.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586656.OTHER_6053620771_7613840",
                  "categoryName": "Accessories",
                  "categoryId": "13451"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-kids-backpacks",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//my-live-02.slatic.net/p/c9dc024ff7100759c034cf2b8b94c07d.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586656.OTHER_6053620772_7613840",
                  "categoryName": "Backpacks",
                  "categoryId": "13450"
                }
              ],
              "categoryIcon": "",
              "categoryUrl": "//www.lazada.co.th/shop-kids-bags",
              "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel2TabDTO",
              "categoryName": "Kids' Bags",
              "categoryId": "13423"
            },
            {
              "level3TabList": [
                {
                  "categoryUrl": "//www.lazada.co.th/shop-kids-eyewear",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//sg-live.slatic.net/p/9675372fa134f18fe08ee4951e7ad7cb.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586656.OTHER_6053620773_7613840",
                  "categoryName": "Kids Eyeglasses",
                  "categoryId": "12518"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-kids-sunglasses",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//my-live.slatic.net/original/66e27c74fa0596d3e66da7b70051d4b8.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586656.OTHER_6053620774_7613840",
                  "categoryName": "Kids Sunglasses",
                  "categoryId": "12514"
                }
              ],
              "categoryIcon": "",
              "categoryUrl": "//www.lazada.co.th/shop-eyeglasses-2",
              "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel2TabDTO",
              "categoryName": "Kids' Eyewear",
              "categoryId": "10100750"
            }
          ],
          "categoryName_zh": "",
          "categoryIcon": "ic-cat-FashionAccess &#xe73f;",
          "id": "6634017",
          "position": "top",
          "childId": "Level_1_Category_No10",
          "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel1TabDTO",
          "categoryName": "Kid's Fashion & Accessories",
          "level1CategoryId": "6634017"
        },
        {
          "level2TabList": [
            {
              "level3TabList": [
                {
                  "categoryUrl": "//www.lazada.co.th/shop-treadmills",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//laz-img-cdn.alicdn.com/images/ims-web/TB11oyvebsrBKNjSZFpXXcXhFXa.jpg",
                  "categoryName": "Treadmills",
                  "categoryId": "6399"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-exercise-bikes",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//laz-img-cdn.alicdn.com/images/ims-web/TB1vLh4ebZnBKNjSZFhXXc.oXXa.jpg",
                  "categoryName": "Exercise Bikes",
                  "categoryId": "6396"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-fitness-yoga-elliptical-trainers",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//sg-live.slatic.net/p/fe6b2eb2be55ca0ad05285bb82e28113.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586657.OTHER_5981320715_4841899",
                  "categoryName": "Elliptical Trainers",
                  "categoryId": "5918"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-strength-training",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//th-live-01.slatic.net/p/6/homefittools-barbell-rack-mb-2-1450609631-1758721-1-zoom.jpg",
                  "categoryName": "Strength Training Equipment",
                  "categoryId": "5923"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-weight-training",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//th-live-03.slatic.net/p/6/olympic-jaw-lock-barbell-weight-2-1501853355-50513073-759808fda1b2c46b761428dabbf4ef48-zoom.jpg",
                  "categoryName": "Weights",
                  "categoryId": "2955"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-boxing-martial-arts-mma",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//my-live-02.slatic.net/original/dd8e37eca533f2ae290a4c781b0ad607.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586657.OTHER_5981320718_4841899",
                  "categoryName": "Boxing, Martial Arts & MMA",
                  "categoryId": "2160"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-yoga",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//th-live-02.slatic.net/p/6/dmall-yoga-foam-roller-massage-blue-1477632616-9873949-6c85fffdcc6e94b50400e346858e62c2-zoom.jpg",
                  "categoryName": "Yoga",
                  "categoryId": "6374"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-pilates",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//th-live-02.slatic.net/p/6/15-1478535301-3923779-fff7c7cec08612e725afd9ac3f2bda80-zoom.jpg",
                  "categoryName": "Pilates",
                  "categoryId": "6384"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-fitness-accessories",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//th-live-03.slatic.net/p/6/sportland-1003-jump-rope-with-spring-spl-cmc9mml305cml-greenblue-1479313213-595768-a4f203d802054fa2f788a54da5ff40e3-zoom.jpg",
                  "categoryName": "Fitness Accessories",
                  "categoryId": "5919"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-running",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//th-live-03.slatic.net/p/6/product-1503056929-65883683-171986b7b2acecc270386b15d92e3206-zoom.jpg",
                  "categoryName": "Running",
                  "categoryId": "12309"
                }
              ],
              "categoryIcon": "",
              "categoryUrl": "//www.lazada.co.th/shop-exercise-fitness",
              "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel2TabDTO",
              "categoryName": "Exercise & Fitness",
              "categoryId": "5801"
            },
            {
              "level3TabList": [
                {
                  "categoryUrl": "//www.lazada.co.th/shop-camping-hiking",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//th-live-03.slatic.net/p/6/quechua-1498287704-83437862-71eb5220fe001a0389cd9b9593a2cff2-zoom.jpg",
                  "categoryName": "Camping & Hiking",
                  "categoryId": "5797"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-bikes",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//laz-img-cdn.alicdn.com/images/ims-web/TB1_amqXwZC2uNjSZFnXXaxZpXa.jpg",
                  "categoryName": "Bikes",
                  "categoryId": "5886"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-scooters",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//th-live-03.slatic.net/p/6/kick-scooter-7xl-200-1464943629-5738186-bcfb92a505dd3437011815231da4c865-zoom.jpg",
                  "categoryName": "Scooters",
                  "categoryId": "5793"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-fishing",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//th-live-03.slatic.net/p/6/nai-khun-4-cm-1503916523-59778793-65f4bf81f8af94afd966fb70f562682a-zoom.jpg",
                  "categoryName": "Fishing",
                  "categoryId": "5789"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-shooting",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//th-live-01.slatic.net/p/6/product-1502613264-16231083-75d2fbc75a31f91e011b6ad9765334e6-zoom.jpg",
                  "categoryName": "Shooting",
                  "categoryId": "2390"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-inline-roller-skates",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//th-live-01.slatic.net/p/6/7pcs-set-of-childrens-protective-equipment-skating-bike-headknee-elbow-pads-black-intl-1499442961-51326703-98cdb84b0b85f7576df6a95f322f78b1-zoom.jpg",
                  "categoryName": "Inline & Roller Skates",
                  "categoryId": "5791"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-skateboarding",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//th-live-01.slatic.net/p/6/24ghz-radio-transmitter-receiver-bind-plug-for-electric-skateboard-1508752988-25290575-6f9c295a2dd572579b8ba6c49354be0f-zoom.jpg",
                  "categoryName": "Skateboarding",
                  "categoryId": "5792"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-outdoor-adventure-climbing",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//th-live-01.slatic.net/p/6/100-ft-army-green-7-strand-core-550-paracord-parachute-cord-lanyardoutdoor-intl-1501111913-34865553-b859926e2776fb1b9bc5eef0b4378f1e-zoom.jpg",
                  "categoryName": "Climbing",
                  "categoryId": "8755"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-golf",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//th-live-03.slatic.net/p/6/2pcs-golf-alignment-sticks-swing-tour-trainer-rod-ball-striking-aidblue-intl-1505948275-76095254-5c9c6be6447422d3811627deb9f9e636-zoom.jpg",
                  "categoryName": "Golf",
                  "categoryId": "3407"
                }
              ],
              "categoryIcon": "",
              "categoryUrl": "//www.lazada.co.th/shop-outdoor-recreation",
              "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel2TabDTO",
              "categoryName": "Outdoor Recreation",
              "categoryId": "5767"
            },
            {
              "level3TabList": [
                {
                  "categoryUrl": "//www.lazada.co.th/shop-sports-men-t-shirts",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//laz-img-cdn.alicdn.com/images/ims-web/TB1ciU0XwZC2uNjSZFnXXaxZpXa.jpg",
                  "categoryName": "T-Shirts & Tops",
                  "categoryId": "9501"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-men-sports-jerseys",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//laz-img-cdn.alicdn.com/images/ims-web/TB17Bo6eljTBKNjSZFuXXb0HFXa.jpg",
                  "categoryName": "Jerseys",
                  "categoryId": "2839"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-men-sports-pants",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//laz-img-cdn.alicdn.com/images/ims-web/TB1ruIZekomBKNjSZFqXXXtqVXa.jpg",
                  "categoryName": "Pants",
                  "categoryId": "9499"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-men-sports-shorts",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//sg-live.slatic.net/p/9b3736ae925a4831945018f129ed1c02.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586657.OTHER_5981320737_4841899",
                  "categoryName": "Shorts",
                  "categoryId": "5430"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-men-uniform-base-layers",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//my-live-02.slatic.net/p/eaa5b074ad5f398ca1d5043c4042aeb2.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586657.OTHER_5981320738_4841899",
                  "categoryName": "Compression",
                  "categoryId": "4138"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-clothing-men-sports-accessories",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//th-live-01.slatic.net/p/6/findbike-polarized-clip-on-black-1463651389-4813646-b2ae00f4cce2e4d7805e34700b2a920b-zoom.jpg",
                  "categoryName": "Accessories",
                  "categoryId": "12337"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-mens-sports-bags",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//th-live-01.slatic.net/p/6/wenhao-sport-baggym-bag-navy-blue-1462945284-0409663-a305c27cf9afe813cd197e3d57d17edf-zoom.jpg",
                  "categoryName": "Bags",
                  "categoryId": "12338"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-men-swim-surf-wear",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//laz-img-cdn.alicdn.com/images/ims-web/TB1MKUZekomBKNjSZFqXXXtqVXa.jpg",
                  "categoryName": "Swimwear",
                  "categoryId": "9504"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-men-sports-socks",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//my-live-02.slatic.net/original/b185f39c61f65e79fe8fe7e1c1de27a1.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586657.OTHER_5981320742_4841899",
                  "categoryName": "Socks",
                  "categoryId": "12416"
                }
              ],
              "categoryIcon": "",
              "categoryUrl": "//www.lazada.co.th/shop-sports-men-clothing",
              "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel2TabDTO",
              "categoryName": "Men's Sports Apparel",
              "categoryId": "10100289"
            },
            {
              "level3TabList": [
                {
                  "categoryUrl": "//www.lazada.co.th/shop-sports-men-football-shoes",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//laz-img-cdn.alicdn.com/images/ims-web/TB10mUCebZnBKNjSZFhXXc.oXXa.jpg",
                  "categoryName": "Football Shoes",
                  "categoryId": "8353"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-mens-sport-sneakers",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//laz-img-cdn.alicdn.com/images/ims-web/TB1QJ.QVNYaK1RjSZFnXXa80pXa.jpg",
                  "categoryName": "Sports Sneakers",
                  "categoryId": "7147"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-sports-men-running-shoes",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//laz-img-cdn.alicdn.com/images/ims-web/TB1gx70XwZC2uNjSZFnXXaxZpXa.jpg",
                  "categoryName": "Running Shoes",
                  "categoryId": "8346"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-sports-men-futsal-shoes",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//my-live-02.slatic.net/p/8041528dd0748acac45d71b47849e293.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586657.OTHER_5981320747_4841899",
                  "categoryName": "Futsal Shoes",
                  "categoryId": "8349"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-sports-men-basketball-shoes",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//id-live-03.slatic.net/p/5/nikita-sandal-akupuntur-kongsui-1483354486-959184-da6e78efc5123d291959c992f9298dc5-zoom.jpg",
                  "categoryName": "Basketball Shoes",
                  "categoryId": "8350"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-men-badminton-shoes",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//laz-img-cdn.alicdn.com/images/ims-web/TB1i23QVNYaK1RjSZFnXXa80pXa.jpg",
                  "categoryName": "Badminton Shoes",
                  "categoryId": "4521"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-sports-men-hiking-shoes",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//laz-img-cdn.alicdn.com/images/ims-web/TB1V2EQVNYaK1RjSZFnXXa80pXa.jpg",
                  "categoryName": "Hiking Shoes",
                  "categoryId": "8356"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-men-sport-sandals",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//laz-img-cdn.alicdn.com/images/ims-web/TB1g3oQVNYaK1RjSZFnXXa80pXa.jpg",
                  "categoryName": "Sports Sandals",
                  "categoryId": "7148"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-sports-men-watersport-shoes",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//laz-img-cdn.alicdn.com/images/ims-web/TB1FMQQVNYaK1RjSZFnXXa80pXa.jpg",
                  "categoryName": "Water Shoes",
                  "categoryId": "8354"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-sports-men-cycling-shoes",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//laz-img-cdn.alicdn.com/images/ims-web/TB1f4cQVNYaK1RjSZFnXXa80pXa.jpg",
                  "categoryName": "Cycling Shoes",
                  "categoryId": "8355"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-sports-men-golf-shoes",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//laz-img-cdn.alicdn.com/images/ims-web/TB1HhwQVNYaK1RjSZFnXXa80pXa.jpg",
                  "categoryName": "Golf Shoes",
                  "categoryId": "8348"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-men-fitness-cross-training-shoes",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//my-live-02.slatic.net/original/ebee023f60c3ebd5d71d42f430ac0990.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586657.OTHER_5981320755_4841899",
                  "categoryName": "Training Shoes",
                  "categoryId": "4928"
                }
              ],
              "categoryIcon": "",
              "categoryUrl": "//www.lazada.co.th/shop-sports-men-shoes-clothing",
              "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel2TabDTO",
              "categoryName": "Men's Sports Shoes",
              "categoryId": "8332"
            },
            {
              "level3TabList": [
                {
                  "categoryUrl": "//www.lazada.co.th/shop-women-sports-tops",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//laz-img-cdn.alicdn.com/images/ims-web/TB1IAw0XwZC2uNjSZFnXXaxZpXa.jpg",
                  "categoryName": "T-Shirts & Tops",
                  "categoryId": "9485"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-women-sport-pants",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//laz-img-cdn.alicdn.com/images/ims-web/TB1OFgDebZnBKNjSZFhXXc.oXXa.jpg",
                  "categoryName": "Pants",
                  "categoryId": "9483"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-women-sports-shorts",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//sg-live.slatic.net/p/5d12c02dbe50141ac3228bf5bd4102fe.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586657.OTHER_5981320759_4841899",
                  "categoryName": "Shorts",
                  "categoryId": "2385"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-women-sports-bras",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//laz-img-cdn.alicdn.com/images/ims-web/TB1lRc0XwZC2uNjSZFnXXaxZpXa.jpg",
                  "categoryName": "Sports Bras",
                  "categoryId": "2384"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-women-sports-jerseys",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//my-live-02.slatic.net/p/756d9e4ba81f389114bf1ed709626a36.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586657.OTHER_5981320761_4841899",
                  "categoryName": "Jerseys",
                  "categoryId": "2958"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-sports-women-dresses-skirts",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//my-live-02.slatic.net/p/33c6be62e3babe43c75d0b20d4f29dd8.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586657.OTHER_5981320762_4841899",
                  "categoryName": "Skirts & Dresses",
                  "categoryId": "2386"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-women-uniform-base-layers",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//sg-live.slatic.net/p/9e615805d18831cd1dcb3eeffca57bb0.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586657.OTHER_5981320763_4841899",
                  "categoryName": "Compression",
                  "categoryId": "2029"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-women-swim-surf-wear",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//laz-img-cdn.alicdn.com/images/ims-web/TB1393CeiAnBKNjSZFvXXaTKXXa.jpg",
                  "categoryName": "Swimwear",
                  "categoryId": "12395"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-sports-women-accessories",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//th-live-03.slatic.net/p/7/nike-speed-headband-performance-22010-bk-690intone-sizeint-one-size-1480492095-58005201-75a3e9c301c7ec4dcb7da5ab5eb1012e-zoom.jpg",
                  "categoryName": "Accessories",
                  "categoryId": "12335"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-womens-sports-bags",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//th-live-01.slatic.net/p/6/wenhao-sport-baggym-bag-navy-blue-1462945284-0409663-a305c27cf9afe813cd197e3d57d17edf-zoom.jpg",
                  "categoryName": "Bags",
                  "categoryId": "12336"
                }
              ],
              "categoryIcon": "",
              "categoryUrl": "//www.lazada.co.th/shop-sports-women-clothing",
              "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel2TabDTO",
              "categoryName": "Women's Sports Apparel",
              "categoryId": "10100287"
            },
            {
              "level3TabList": [
                {
                  "categoryUrl": "//www.lazada.co.th/shop-womens-sport-sneakers",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//laz-img-cdn.alicdn.com/images/ims-web/TB1_.MCebZnBKNjSZFhXXc.oXXa.jpg",
                  "categoryName": "Sports Sneakers",
                  "categoryId": "2356"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-women-running-shoes",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//id-live-03.slatic.net/p/5/happy-green-avocado-oil-cosmetic-grade-80-ml-minyak-alpukat-1472112036-8085198-94e66406652741842f10d75b5d090264-zoom.jpg",
                  "categoryName": "Running Shoes",
                  "categoryId": "8333"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-women-fitness-cross-training-shoes",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//sg-live.slatic.net/p/4cc8a96b05dc842f938a1a450e4c2c69.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586657.OTHER_5981320770_4841899",
                  "categoryName": "Training Shoes",
                  "categoryId": "2353"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-women-futsal-shoes",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//my-live-02.slatic.net/p/c7c3043ebdf7f07bbe3c52291223c95c.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586657.OTHER_5981320771_4841899",
                  "categoryName": "Futsal Shoes",
                  "categoryId": "8336"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-women-football-shoes",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//laz-img-cdn.alicdn.com/images/ims-web/TB1OzMQVNYaK1RjSZFnXXa80pXa.jpg",
                  "categoryName": "Football Shoes",
                  "categoryId": "8340"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-women-basketball-shoes",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//laz-img-cdn.alicdn.com/images/ims-web/TB10CoAVRLoK1RjSZFuXXXn0XXa.jpg",
                  "categoryName": "Basketball Shoes",
                  "categoryId": "8337"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-women-badminton-shoes",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//laz-img-cdn.alicdn.com/images/ims-web/TB1jQwQVNYaK1RjSZFnXXa80pXa.jpg",
                  "categoryName": "Badminton Shoes",
                  "categoryId": "8339"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-women-sport-sandals",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//laz-img-cdn.alicdn.com/images/ims-web/TB1egACVOrpK1RjSZFhXXXSdXXa.jpg",
                  "categoryName": "Sports Sandals",
                  "categoryId": "2357"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-women-hiking-shoes",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//laz-img-cdn.alicdn.com/images/ims-web/TB1dz.QVNYaK1RjSZFnXXa80pXa.jpg",
                  "categoryName": "Hiking Shoes",
                  "categoryId": "8343"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-women-watersport-shoes",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//laz-img-cdn.alicdn.com/images/ims-web/TB1qawDVHvpK1RjSZFqXXcXUVXa.jpg",
                  "categoryName": "Water Shoes",
                  "categoryId": "8341"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-women-cycling-shoes",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//laz-img-cdn.alicdn.com/images/ims-web/TB1JUwAVRLoK1RjSZFuXXXn0XXa.jpg",
                  "categoryName": "Cycling Shoes",
                  "categoryId": "8342"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-women-golf-shoes",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//laz-img-cdn.alicdn.com/images/ims-web/TB1vHcDVHvpK1RjSZFqXXcXUVXa.jpg",
                  "categoryName": "Golf Shoes",
                  "categoryId": "8335"
                }
              ],
              "categoryIcon": "",
              "categoryUrl": "//www.lazada.co.th/shop-sports-women-shoes-clothing",
              "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel2TabDTO",
              "categoryName": "Women's Sports Shoes",
              "categoryId": "8330"
            },
            {
              "level3TabList": [
                {
                  "categoryUrl": "//www.lazada.co.th/shop-cycling",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//th-live-03.slatic.net/p/6/5-ty-566-1506580245-06837011-f343832558da41e733d6f33892bc2298-zoom.jpg",
                  "categoryName": "Cycling",
                  "categoryId": "5795"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-bikes",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//laz-img-cdn.alicdn.com/images/ims-web/TB1_amqXwZC2uNjSZFnXXaxZpXa.jpg",
                  "categoryName": "Bikes",
                  "categoryId": "5886"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-mountain-bikes",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//my-live-02.slatic.net/p/f30e9647ed47c00b1847c2675190db1c.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586657.OTHER_5981320782_4841899",
                  "categoryName": "Mountain Bikes",
                  "categoryId": "8717"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-road-bikes",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//my-live-02.slatic.net/original/051842211fc2da1f6164b277e687c74f.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586657.OTHER_5981320783_4841899",
                  "categoryName": "Road Bikes",
                  "categoryId": "8720"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-folding-bikes",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//sg-live.slatic.net/p/6/hyper-xt-premium-quality-foldable-mountain-sports-bike-with-shimanoparts-high-carbon-steel-pearl-white-7960-61909272-95489a674d7f96c5319d99b62c7f2808-catalog.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586657.OTHER_5981320784_4841899",
                  "categoryName": "Folding Bikes",
                  "categoryId": "8715"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-comfort-cruiser-bikes",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//sg-live.slatic.net/p/c37f89b627e99ba4f14337fa97fbe448.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586657.OTHER_5981320785_4841899",
                  "categoryName": "Comfort & Cruiser Bikes",
                  "categoryId": "8714"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-kids-bikes",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//sg-live.slatic.net/p/6/wimcycle-12-inch-disney-princess-children-bike-kids-bicycle-cycle-gift-toys-outdoor-sports-0858-20105504-50b66729d1a065fbf987af430a7fad08-catalog.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586657.OTHER_5981320786_4841899",
                  "categoryName": "Kids Bikes",
                  "categoryId": "8722"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-electric-bikes",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//sg-live.slatic.net/original/ae08b6534299f89239bab757d46e9e89.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586657.OTHER_5981320787_4841899",
                  "categoryName": "Electric Bikes",
                  "categoryId": "9611"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-cycling-accessories",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//sg-live.slatic.net/p/6/300lm-bicycle-cree-led-lamp-usb-rechargeable-bike-front-light-intl-1748-10221171-c1fa55c2eff0743c3625ca33d3944357-catalog.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586657.OTHER_5981320788_4841899",
                  "categoryName": "Bike Accessories",
                  "categoryId": "5878"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-other-bike-parts",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//sg-live.slatic.net/p/6/reflective-shock-absorbing-hollow-bicycle-saddle-bike-seatred-intl-9500-56161864-bd0065cc93d09e7a715ff632323d38d8-catalog.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586657.OTHER_5981320789_4841899",
                  "categoryName": "Bike Parts",
                  "categoryId": "5877"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-cycling-jersey",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//my-live-02.slatic.net/p/c98fec533edee20b60f5fdb05818f846.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586657.OTHER_5981320790_4841899",
                  "categoryName": "Cycling Clothing",
                  "categoryId": "12330"
                }
              ],
              "categoryIcon": "",
              "categoryUrl": "//www.lazada.co.th/shop-cycling",
              "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel2TabDTO",
              "categoryName": "Cycling",
              "categoryId": "5796"
            },
            {
              "level3TabList": [
                {
                  "categoryUrl": "//www.lazada.co.th/shop-diving-snorkeling",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//th-live-03.slatic.net/p/6/functional-full-dry-swimming-diving-snorkel-with-siliconemouthpiece-black-intl-1491502768-55309441-28e4435ebdbb4c20048b5cb9d6e534f1-zoom.jpg",
                  "categoryName": "Diving & Snorkeling",
                  "categoryId": "2373"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-swimming",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//th-live-02.slatic.net/p/6/swimming-learner-kickboard-floating-plate-eva-swimmer-body-boardspink-intl-1498530796-94811962-f6f3cf1c5d0268c91c6c4ff1c2ba22d2-zoom.jpg",
                  "categoryName": "Swimming",
                  "categoryId": "2312"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-swimming-training-equipment-2",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//laz-img-cdn.alicdn.com/images/ims-web/TB1plZ0XwZC2uNjSZFnXXaxZpXa.jpg",
                  "categoryName": "Training Equipment",
                  "categoryId": "10100293"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-tubes-towables",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//th-live-02.slatic.net/p/6/1x1-hard-pool-cue-stick-carrying-case-billiard-canister-2-holes-1-butt1-shaft-intl-1505988426-12189554-8242e07f09a5347fbd967d604b2260a3-zoom.jpg",
                  "categoryName": "Inflatables",
                  "categoryId": "2394"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-water-sports-boating",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//th-live-01.slatic.net/p/6/cheer-126cm-aluminum-alloy-detachable-float-afloat-oars-fitting-boat-rafting-paddle-black-intl-1503414160-59004093-357d2da950a9f2da678032ce6cb62950-zoom.jpg",
                  "categoryName": "Boating",
                  "categoryId": "2097"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-swimming-accessories-2",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//my-live-02.slatic.net/p/6/1pc-new-children-kids-outdoor-swim-pool-anti-fog-swimming-goggles-glasses-eyewear-accessories-for-boys-girls-with-earplugs-pouch-bag-6111-959937821-70bd125786fa2eb74618b79a2b6fc06c-catalog.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586657.OTHER_5981320797_4841899",
                  "categoryName": "Accessories",
                  "categoryId": "10100292"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-water-sports-dry-bags",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//th-live-03.slatic.net/p/6/cr-seven-waterproof-bag-10-1508466619-06333281-ce6548baf2bab98f8c5505426d4a4b4b-zoom.jpg",
                  "categoryName": "Dry Bags",
                  "categoryId": "2054"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-life-jackets",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//th-live-01.slatic.net/p/6/intl-1463716323-7014974-35b3b26b2687ef8eb57ff105f04995e6-zoom.jpg",
                  "categoryName": "Life Jackets",
                  "categoryId": "4509"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-water-sports-boarding",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//th-live-01.slatic.net/p/6/tpu-surfing-surfboard-leash-super-strong-paddle-board-foot-cord-string-leg-rope-intl-1508837513-25732675-f27718451d7495873a5b937ff608a883-zoom.jpg",
                  "categoryName": "Boarding",
                  "categoryId": "3451"
                }
              ],
              "categoryIcon": "",
              "categoryUrl": "//www.lazada.co.th/shop-water-sports",
              "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel2TabDTO",
              "categoryName": "Water Sports",
              "categoryId": "2381"
            },
            {
              "level3TabList": [
                {
                  "categoryUrl": "//www.lazada.co.th/shop-football",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//th-live-03.slatic.net/p/7/tiebao-soccer-shoes-bluesilver-1050-2-1504865952-88005714-369450a204a2bb371b37717e6317841d-zoom.jpg",
                  "categoryName": "Football",
                  "categoryId": "5811"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-basketball",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//th-live-01.slatic.net/p/6/mikasa-basketball-mks-rb-1000-1478494449-597244-06216b98e3a52f01505a5deb38eea3df-zoom.jpg",
                  "categoryName": "Basketball",
                  "categoryId": "5810"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-volleyball",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//th-live-02.slatic.net/p/6/captain-tsubasa-volleyball-softtouch-1487156497-82827811-8449f30f661d64882310193da00bf1bc-zoom.jpg",
                  "categoryName": "Volleyball",
                  "categoryId": "5809"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-baseball",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//th-live-02.slatic.net/p/6/sa-yanyi-20-inch-aluminum-alloy-baseball-bat-no-handball-andnon-slip-handle-intl-1498597471-86071572-bf631d79d75b35af757b90b7b87718b1-zoom.jpg",
                  "categoryName": "Baseball",
                  "categoryId": "7954"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-sepak-takraw",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//th-live-03.slatic.net/p/6/marathon-mt-101176-1493005088-32469851-b120a2f8df3623380a16cfc056f163b1-zoom.jpg",
                  "categoryName": "Sepak Takraw",
                  "categoryId": "5808"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-gymnastics",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//th-live-03.slatic.net/p/6/4m-gym-dance-ribbon-rhythmic-art-gymnastic-streamer-twirling-rod-stick-intl-1500015623-40657332-ac156244468c2ea60d1ba284ef5cc8fc-zoom.jpg",
                  "categoryName": "Gymnastics",
                  "categoryId": "3214"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-hockey",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//th-live-02.slatic.net/p/6/4-1483627921-9068981-a622924cc8baef69283693102db824a9-zoom.jpg",
                  "categoryName": "Hockey",
                  "categoryId": "2360"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-team-sports-cricket",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//th-live-01.slatic.net/p/6/ac-12-x-copper-dart-darts-needle-flights-steel-tip-for-bar-partyplay-throwing-toy-intl-1491502968-79939441-e2fafda3cf2c08bc295e4c5ff17062cb-zoom.jpg",
                  "categoryName": "Cricket",
                  "categoryId": "8691"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-cheerleading",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//th-live-03.slatic.net/p/6/ah01-fbt-60431-1499068186-48175292-44982307d62ce8c139b2e1802e21ef3f-zoom.jpg",
                  "categoryName": "Cheerleading",
                  "categoryId": "12310"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-sports-fan-shop",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//laz-img-cdn.alicdn.com/images/ims-web/TB1_mQ0XwZC2uNjSZFnXXaxZpXa.jpg",
                  "categoryName": "Fan Shop",
                  "categoryId": "12308"
                }
              ],
              "categoryIcon": "",
              "categoryUrl": "//www.lazada.co.th/shop-team-sports",
              "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel2TabDTO",
              "categoryName": "Team Sports",
              "categoryId": "5769"
            },
            {
              "level3TabList": [
                {
                  "categoryUrl": "//www.lazada.co.th/shop-badminton",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//laz-img-cdn.alicdn.com/images/ims-web/TB1T970XwZC2uNjSZFnXXaxZpXa.jpg",
                  "categoryName": "Badminton",
                  "categoryId": "5805"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-table-tennis",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//laz-img-cdn.alicdn.com/images/ims-web/TB11YMDebZnBKNjSZFhXXc.oXXa.jpg",
                  "categoryName": "Table Tennis",
                  "categoryId": "5806"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-tennis",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//laz-img-cdn.alicdn.com/images/ims-web/TB1sFo7eljTBKNjSZFuXXb0HFXa.jpg",
                  "categoryName": "Tennis",
                  "categoryId": "5807"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-squash",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//th-live-01.slatic.net/p/6/sr700-1504804851-85201214-8a781214ef1e23ebb3823292fc2215cf-zoom.jpg",
                  "categoryName": "Squash",
                  "categoryId": "5799"
                }
              ],
              "categoryIcon": "",
              "categoryUrl": "//www.lazada.co.th/shop-racquet-sports",
              "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel2TabDTO",
              "categoryName": "Racket Sports",
              "categoryId": "5768"
            },
            {
              "level3TabList": [
                {
                  "categoryUrl": "//www.lazada.co.th/shop-sport-outdoors-water-bottles",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//th-live-02.slatic.net/p/6/bbb-bwb-01-comtank-550-ml-blkyellow-1469172753-8541147-f9dc80d63d5abcbd0efc019aa27d1dac-zoom.jpg",
                  "categoryName": "Water Bottles",
                  "categoryId": "9567"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-sport-outdoors-air-pumps",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//th-live-03.slatic.net/p/6/jg-pro-star-co2-inflator-presta-and-schrader-valve-compatible-bicycle-tire-pump-for-road-and-mountain-bikes-with-insulated-sleeve-without-co2-cartridges-intl-1504807579-48501214-821eb673271a9fd27eaef58d0779f9b4-zoom.jpg",
                  "categoryName": "Air Pumps",
                  "categoryId": "9568"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-sports-first-aid",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//th-live-01.slatic.net/p/6/hazyasm-first-aid-kit20-pcs-lightweight-and-durable-medical-traumakit-for-car-sports-hiking-travel-emergency-survival-campinghomered-1491766259-7969499-5b013d4e9af46c254a81b15bf2d81905-zoom.jpg",
                  "categoryName": "First Aid Kits",
                  "categoryId": "12312"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-sports-support-braces",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//th-live-03.slatic.net/p/6/nationman-333-l-1492758702-14064851-bd54d7d87d5a38e723aceebc6828fcb6-zoom.jpg",
                  "categoryName": "Supports & Braces",
                  "categoryId": "12313"
                }
              ],
              "categoryIcon": "",
              "categoryUrl": "//www.lazada.co.th/shop-sport-outdoors-accessories",
              "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel2TabDTO",
              "categoryName": "Sport Accessories",
              "categoryId": "9563"
            },
            {
              "level3TabList": [
                {
                  "categoryUrl": "//www.lazada.co.th/shop-luggage",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//th-live-02.slatic.net/p/8/24-8-360-polycarbonate-gtc02silver-1495164762-95242302-b21b8801d418cdf6e24a842ba12d2715-zoom.jpg",
                  "categoryName": "Luggage",
                  "categoryId": "13452"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-laptop-bags-cases",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//th-live-03.slatic.net/p/8/doraemon-1506411585-39761664-cedb72c14d6b2bad294f5e49b11fa67a-zoom.jpg",
                  "categoryName": "Laptop Bags",
                  "categoryId": "13426"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-travel-accessories",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//th-live-03.slatic.net/p/8/neck-pillow-pl01-1499618261-66183613-55cbddf6fa7c6b493da33ff077c532f2-zoom.jpg",
                  "categoryName": "Travel Accessories",
                  "categoryId": "13453"
                }
              ],
              "categoryIcon": "",
              "categoryUrl": "//www.lazada.co.th/shop-travel-luggage-2",
              "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel2TabDTO",
              "categoryName": "Travel",
              "categoryId": "13424"
            }
          ],
          "categoryName_zh": "",
          "categoryIcon": "ic-cat-SportsOutdoo &#xe761;",
          "id": "6634018",
          "position": "top",
          "childId": "Level_1_Category_No11",
          "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel1TabDTO",
          "categoryName": "Sports & Travel ",
          "level1CategoryId": "6634018"
        },
        {
          "level2TabList": [
            {
              "level3TabList": [
                {
                  "categoryUrl": "//www.lazada.co.th/shop-automotive-oils",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//th-live.slatic.net/p/8/shell-helix-ultra-diesel-0w-40-6-9606-08758039-8ed01d5c463330708295048721947dc6-catalog.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586658.OTHER_6027552120_6548076",
                  "categoryName": "Auto Oils",
                  "categoryId": "12570"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-automotive-cleaners",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//th-live-01.slatic.net/p/8/deepclean-magic-200-ml-1476936360-6859719-614a0fc3caf856d216e083bf9b7c4fe8-zoom.jpg",
                  "categoryName": "Auto Part Cleaners",
                  "categoryId": "12567"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-automotive-transmission-fluids",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//th-live-03.slatic.net/p/8/honda-atf-dw-1-honda-jazz-2012-honda-accord-2012-honda-odyssey-2012-3-08268-p99-z3bt1-1501133834-16769653-2a582cb8baafd80e7667cdeeb5faaecf-zoom.jpg",
                  "categoryName": "Auto Transmission Fluids",
                  "categoryId": "12575"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-automotive-auto-oils-fluids-additives",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//th-live-03.slatic.net/p/8/diesel-purge-1505277093-75745704-f8ed205546e991325a872f6c67805af7-zoom.jpg",
                  "categoryName": "Auto Additives",
                  "categoryId": "12563"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-automotive-radiator-conditioners-protectants",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//th-live-01.slatic.net/p/8/radiator-stop-leak-1509249739-28879793-f714f94981803505718063a7622ba045-zoom.jpg",
                  "categoryName": "Auto Radiator Protectants",
                  "categoryId": "12572"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-automotive-brake-fluids",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//th-live.slatic.net/p/8/shell-dot4-05-3621-10970056-3af3a8e03f52913f5fc3d8567984a8ba-catalog.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586658.OTHER_6027552125_6548076",
                  "categoryName": "Auto Brake Fluids",
                  "categoryId": "12566"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-automotive-greases-lubricants",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//th-live-01.slatic.net/p/8/2-05kg-1508434798-71564765-68e06fd833e7643307cb41333d673b3a-zoom.jpg",
                  "categoryName": "Auto Greases & Lubricants",
                  "categoryId": "12569"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-moto-engine-oils",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//laz-img-cdn.alicdn.com/images/ims-web/TB14qEBfRjTBKNjSZFuXXb0HFXa.jpg",
                  "categoryName": "Motorcycle Engine Oils",
                  "categoryId": "10100722"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-moto-transmission-fluids",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//laz-img-cdn.alicdn.com/images/ims-web/TB1lQkhfQomBKNjSZFqXXXtqVXa.jpg",
                  "categoryName": "Motorcycle Transmission Fluids",
                  "categoryId": "10100723"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-motorcycle-brake-fluid",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//th-live.slatic.net/p/02fa8662f2d61bca8919a8c62dc1a53e.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586658.OTHER_6027552129_6548076",
                  "categoryName": "Motorcycle Brake Fluids",
                  "categoryId": "12706"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-lubricants-and-solvents",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//th-live.slatic.net/original/8ace5a30a371e617143dae9d9fa83ca0.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586658.OTHER_6027552130_6548076",
                  "categoryName": "Motorcycle Lubricants & Solvents",
                  "categoryId": "10100724"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-moto-cleaners",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//th-live.slatic.net/p/f1eb404dd211e6f6a9f575fe43dd27ba.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586658.OTHER_6027552131_6548076",
                  "categoryName": "Motorcycle Cleaners",
                  "categoryId": "10100725"
                }
              ],
              "categoryIcon": "",
              "categoryUrl": "//www.lazada.co.th/shop-oils-fluids",
              "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel2TabDTO",
              "categoryName": "Oils & Fluids",
              "categoryId": "8471"
            },
            {
              "level3TabList": [
                {
                  "categoryUrl": "//www.lazada.co.th/shop-automobiles",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//laz-img-cdn.alicdn.com/images/ims-web/TB1._DFgRr0gK0jSZFnXXbRRXXa.jpg",
                  "categoryName": "Automobiles",
                  "categoryId": "10100672"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-automotive-batteries",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//laz-img-cdn.alicdn.com/images/ims-web/TB13K2sgRr0gK0jSZFnXXbRRXXa.jpg",
                  "categoryName": "Batteries & Accessories",
                  "categoryId": "12534"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-wheels-tires",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//laz-img-cdn.alicdn.com/images/ims-web/TB1G1yqXwZC2uNjSZFnXXaxZpXa.jpg",
                  "categoryName": "Tires & Wheels",
                  "categoryId": "8496"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-oils-fluids",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//laz-img-cdn.alicdn.com/images/ims-web/TB1cDKueljTBKNjSZFuXXb0HFXa.jpg",
                  "categoryName": "Auto Oils & Fluids",
                  "categoryId": "8472"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-auto-parts-spares",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//th-live-01.slatic.net/p/8/full-300-nissannavara-np300-d-2015-1-ans152-1497882941-37794852-1292ece9620d17cd0467fe57b8eb4a55-zoom.jpg",
                  "categoryName": "Parts & Spares",
                  "categoryId": "12461"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-car-audio",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//th-live-02.slatic.net/p/8/5-car-portable-speakers-and-subwoofers-12v220v-high-power-120wuniversal-active-subwoofer-car-audio-with-remote-control-black-intl-1502841846-53263483-af37853a004ffc6b916737c1a4685dbc-zoom.jpg",
                  "categoryName": "Car audio",
                  "categoryId": "12468"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-automotive-tools-equipment",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//th-live-03.slatic.net/p/8/nitro-obd2-performance-chip-tuning-box-works-for-diesel-fuel-carsvehicle-red-intl-1501083111-81560553-439d42e4f3426889fdd88675edc8c859-zoom.jpg",
                  "categoryName": "Tools & Equipment",
                  "categoryId": "8489"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-automotive-hand-tools",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//my-live-02.slatic.net/p/d70aee176c672c28ac8f6ca0ff0d5902.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586658.OTHER_6027552140_6548076",
                  "categoryName": "Hand tools",
                  "categoryId": "8493"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-automotive-batteries-accessories",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//laz-img-cdn.alicdn.com/images/ims-web/TB1NwQ9cAfb_uJjSsD4XXaqiFXa.jpg",
                  "categoryName": "Battery  Accessories",
                  "categoryId": "12462"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-fuel-cards",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//ph-live.slatic.net/p/cbe123e53c015794fa693cd55ed02e84.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586658.OTHER_6027552142_6548076",
                  "categoryName": "Fuel Cards",
                  "categoryId": "10100713"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-automotive-vehicle-insurance",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//laz-img-cdn.alicdn.com/images/ims-web/TB10EHsgHj1gK0jSZFuXXcrHpXa.jpg",
                  "categoryName": "Vehicle Insurance",
                  "categoryId": "12500"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-AutomotiveMotorsportsMerchandise",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//laz-img-cdn.alicdn.com/images/ims-web/TB1VflOQlr0gK0jSZFnXXbRRXXa.png",
                  "categoryName": "Auto Merchandise",
                  "categoryId": "42050401"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-automotive-vehicle-warranty",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//laz-img-cdn.alicdn.com/images/ims-web/TB15VntgHj1gK0jSZFuXXcrHpXa.JPG",
                  "categoryName": "Vehicle Warranty",
                  "categoryId": "12501"
                }
              ],
              "categoryIcon": "",
              "categoryUrl": "//www.lazada.co.th/shop-automotive",
              "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel2TabDTO",
              "categoryName": "Automotive",
              "categoryId": "8429"
            },
            {
              "level3TabList": "",
              "categoryIcon": "",
              "categoryUrl": "//www.lazada.co.th/shop-car-cameras-2",
              "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel2TabDTO",
              "categoryName": "Car Camera",
              "categoryId": "10100463"
            },
            {
              "level3TabList": [
                {
                  "categoryUrl": "//www.lazada.co.th/shop-car-stereos",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//laz-img-cdn.alicdn.com/images/ims-web/TB1iuHwgRr0gK0jSZFnXXbRRXXa.jpg",
                  "categoryName": "Car Stereo Receivers",
                  "categoryId": "12662"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-car-speakers",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//laz-img-cdn.alicdn.com/images/ims-web/TB1Z.2FgRr0gK0jSZFnXXbRRXXa.jpg",
                  "categoryName": "Speakers",
                  "categoryId": "12660"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-car-amplifiers",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//laz-img-cdn.alicdn.com/images/ims-web/TB1__fwgHj1gK0jSZFuXXcrHpXa.jpg",
                  "categoryName": "Amplifiers",
                  "categoryId": "12659"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-car-subwoofers",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//laz-img-cdn.alicdn.com/images/ims-web/TB1ukYsgRr0gK0jSZFnXXbRRXXa.jpg",
                  "categoryName": "Subwoofers",
                  "categoryId": "12661"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-satellite-radio",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//laz-img-cdn.alicdn.com/images/ims-web/TB1F8nsgRr0gK0jSZFnXXbRRXXa.jpg",
                  "categoryName": "Satellite Radio",
                  "categoryId": "12663"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-car-audio-equalizers",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//laz-img-cdn.alicdn.com/images/ims-web/TB1FlPsgRr0gK0jSZFnXXbRRXXa.jpg",
                  "categoryName": "Equalizers",
                  "categoryId": "12664"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-car-digital-media-receivers",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//laz-img-cdn.alicdn.com/images/ims-web/TB1DpYGgRr0gK0jSZFnXXbRRXXa.jpg",
                  "categoryName": "Digital Media Receivers",
                  "categoryId": "12666"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-car-tv-tuners",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//laz-img-cdn.alicdn.com/images/ims-web/TB1VL2tgHj1gK0jSZFuXXcrHpXa.jpg",
                  "categoryName": "TV Tuners",
                  "categoryId": "12676"
                }
              ],
              "categoryIcon": "",
              "categoryUrl": "//www.lazada.co.th/shop-car-audio",
              "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel2TabDTO",
              "categoryName": "Car Audio",
              "categoryId": "12467"
            },
            {
              "level3TabList": [
                {
                  "categoryUrl": "//www.lazada.co.th/shop-vehicle-tires",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//th-live-02.slatic.net/p/8/goodyear-21555r17-assurance-duraplus-2-1470715014-9704057-4666190cd8888047a581fc02d34d1e52-zoom.jpg",
                  "categoryName": "Auto Tires",
                  "categoryId": "2276"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-car-wheels",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//laz-img-cdn.alicdn.com/images/ims-web/TB10nPsgRr0gK0jSZFnXXbRRXXa.jpg",
                  "categoryName": "Auto Wheels",
                  "categoryId": "3456"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-auto-tire-and-wheel-packages",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//laz-img-cdn.alicdn.com/images/ims-web/TB1qrfGgRr0gK0jSZFnXXbRRXXa.JPG",
                  "categoryName": "Auto  Wheel & Tire Packages",
                  "categoryId": "10100671"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-automotive-tire-accessories-parts",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//th-live-03.slatic.net/p/8/hayashi-digital-tire-gauge-red-1502863529-91615483-b841f7df76765510292fe0a51badefe9-zoom.jpg",
                  "categoryName": "Auto Tire Accessories",
                  "categoryId": "12562"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-vehicle-wheel-accessories",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//laz-img-cdn.alicdn.com/images/ims-web/TB18oDpgUT1gK0jSZFhXXaAtVXa.jpg",
                  "categoryName": "Auto Wheel Accessories",
                  "categoryId": "2333"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-wheel-tire-tools",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//laz-img-cdn.alicdn.com/images/ims-web/TB1GpbqgUT1gK0jSZFhXXaAtVXa.jpg",
                  "categoryName": "Auto Tire & Wheel Tools",
                  "categoryId": "7349"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-lug-nuts-accessories",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//th-live.slatic.net/p/17e1e9456bfcc17d75d74f6176206799.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586658.OTHER_6027552163_6548076",
                  "categoryName": "Auto Lug Nuts & Accessories",
                  "categoryId": "3071"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-auto-air-compressors-and-inflators",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//laz-img-cdn.alicdn.com/images/ims-web/TB1l6DogKT2gK0jSZFvXXXnFXXa.JPG",
                  "categoryName": "Air Compressors & Inflators",
                  "categoryId": "10100670"
                }
              ],
              "categoryIcon": "",
              "categoryUrl": "//www.lazada.co.th/shop-wheels-tires",
              "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel2TabDTO",
              "categoryName": "Auto Tires & Wheels",
              "categoryId": "5770"
            },
            {
              "level3TabList": [
                {
                  "categoryUrl": "//www.lazada.co.th/shop-auto-bulbs-leds-and-hids",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//th-live.slatic.net/p/8/phillips-h4-123242-st-c1a-nbsp12v6055whonda-jazz-0231-64499403-1df25fc039d2bf2f293d49aa2c886e31-catalog.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586658.OTHER_6027552166_6548076",
                  "categoryName": "Auto Bulbs, LEDs & HIDs",
                  "categoryId": "12549"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-automotive-engine-parts",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//ph-live-02.slatic.net/original/876f4d0b0df457d8dbe686658bf0a11f.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586658.OTHER_6027552167_6548076",
                  "categoryName": "Engine Parts",
                  "categoryId": "12545"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-automotive-air-filters",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//my-live-02.slatic.net/original/cae6f29de7d5bdc404fcf97838bee0ad.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586658.OTHER_6027552168_6548076",
                  "categoryName": "Air filters",
                  "categoryId": "12915"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-automotive-oil-filters",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//th-live.slatic.net/p/8/full-chudepliiynkr-ng-aiskr-ngnammanechuue-ephling-aiskr-ng-aakaas-aichsamhrab-toyota-vigo-fortuner-commuter-otoytaa-wiiok-f-rcchuunen-r-rthtuukh-mmuuet-r-1-ott540-1-ftt154-1-att584-6838-37662111-ca9b5299d920b1455536083d8069b6a9-catalog.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586658.OTHER_6027552169_6548076",
                  "categoryName": "Oil filters",
                  "categoryId": "12918"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-automotive-batteries-accessories",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//laz-img-cdn.alicdn.com/images/ims-web/TB1NwQ9cAfb_uJjSsD4XXaqiFXa.jpg",
                  "categoryName": "Batteries & Accessories",
                  "categoryId": "12460"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-automotive-shocks-struts-suspension/",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//laz-img-cdn.alicdn.com/images/ims-web/TB1wu6tgRr0gK0jSZFnXXbRRXXa.jpg",
                  "categoryName": "Shocks, Struts & Suspension",
                  "categoryId": "12550"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-automotive-exhaust-emissions",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//th-live.slatic.net/p/a43e783aa4a3acce04b5da97eb20e964.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586658.OTHER_6027552172_6548076",
                  "categoryName": "Exhaust Pipes & Accessories",
                  "categoryId": "12546"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-automotive-windshield-wipers-washers/",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//th-live.slatic.net/original/2030073b4cf113bea41e426a8ac8ebb7.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586658.OTHER_6027552173_6548076",
                  "categoryName": "Windshield Wipers & Washers",
                  "categoryId": "12557"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-automotive-brake-system",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//laz-img-cdn.alicdn.com/images/ims-web/TB1sVvugHj1gK0jSZFuXXcrHpXa.jpg",
                  "categoryName": "Brake System",
                  "categoryId": "12541"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-automotive-body-parts",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//my-live-02.slatic.net/p/920109b30b41b51ecbcbe5a1a5ba1539.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586658.OTHER_6027552175_6548076",
                  "categoryName": "Body Parts",
                  "categoryId": "12539"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-diagnostic-test-tools",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//th-live.slatic.net/p/1eb57af5e95bfb1cbfbd3cff734bf571.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586658.OTHER_6027552176_6548076",
                  "categoryName": "Car Diagnostic & Test Tools",
                  "categoryId": "8490"
                }
              ],
              "categoryIcon": "",
              "categoryUrl": "//www.lazada.co.th/shop-auto-parts-spares",
              "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel2TabDTO",
              "categoryName": "Auto Parts & Spares",
              "categoryId": "12463"
            },
            {
              "level3TabList": [
                {
                  "categoryUrl": "//www.lazada.co.th/shop-interior-accessories",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//th-live-02.slatic.net/p/car-humebll-humekhmkhadnirphay-1541-6101427-e0fc6db93ab167c9e1ce842fb2760c95-catalog.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586658.OTHER_6027552178_6548076",
                  "categoryName": "Interior Accessories",
                  "categoryId": "8442"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-exterior-accessories",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//th-live.slatic.net/p/a98eacf7e63c16df8390946eb254f883.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586658.OTHER_6027552179_6548076",
                  "categoryName": "Exterior Accessories",
                  "categoryId": "8436"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-gps-navigation",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//laz-img-cdn.alicdn.com/images/ims-web/TB1P59oekomBKNjSZFqXXXtqVXa.jpg",
                  "categoryName": "GPS",
                  "categoryId": "12466"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-automotive-electrical-appliances",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//laz-img-cdn.alicdn.com/images/ims-web/TB1doWueljTBKNjSZFuXXb0HFXa.jpg",
                  "categoryName": "Electronic Accessoires",
                  "categoryId": "12650"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-car-air-purifiers",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//laz-img-cdn.alicdn.com/images/ims-web/TB1u4vtgRr0gK0jSZFnXXbRRXXa.jpg",
                  "categoryName": "Air Purifiers",
                  "categoryId": "10100657"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-air-fresheners",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//th-live.slatic.net/p/aa7eac17d0e5626e753c338f58a2efa2.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586658.OTHER_6027552183_6548076",
                  "categoryName": "Air Fresheners",
                  "categoryId": "8443"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-automotive-covers",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//laz-img-cdn.alicdn.com/images/ims-web/TB1VRh4ebZnBKNjSZFhXXc.oXXa.jpg",
                  "categoryName": "Covers",
                  "categoryId": "12649"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-car-seat-covers",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//th-live.slatic.net/p/8/k-rubber-chudhumebaaaaebbswmthab-free-size-chudkhuuhnaa-siidam-daayaedng-5836-2085387-b59ae2a2a2bb790aca9c32b137d72fd8-catalog.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586658.OTHER_6027552185_6548076",
                  "categoryName": "Seat Covers",
                  "categoryId": "10100648"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-automotive-floor-mats-cargo-liners",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//th-live.slatic.net/p/k-rubber-chudthaadyaangr-ngphuuen-samhrabrthkrabaaekhp-chud-5-chin-aethmfrii-maanbangaedd-2-chin-black-5152-3795982-1-catalog.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586658.OTHER_6027552186_6548076",
                  "categoryName": "Floor Mats & Cargo Liners",
                  "categoryId": "12651"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-steering-wheels-accessories",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//my-live.slatic.net/original/64b461ae5bd57b5e30b668dafc1d32a4.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586658.OTHER_6027552187_6548076",
                  "categoryName": "Steering Wheels & Accessories",
                  "categoryId": "8452"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-automotive-key-chains",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//my-live-02.slatic.net/p/5cdd5feca6cd0c73f84b869c4cdfaf12.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586658.OTHER_6027552188_6548076",
                  "categoryName": "Key Chains",
                  "categoryId": "12653"
                }
              ],
              "categoryIcon": "",
              "categoryUrl": "//www.lazada.co.th/shop-exterior-accessories",
              "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel2TabDTO",
              "categoryName": "Auto Accessories",
              "categoryId": "8435"
            },
            {
              "level3TabList": [
                {
                  "categoryUrl": "//www.lazada.co.th/shop-automotive-exterior-vehicle-care",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//th-live.slatic.net/p/52bcad82da284cb472f39d6e78398fc9.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586658.OTHER_6027552190_6548076",
                  "categoryName": "Exterior Vehicle Care",
                  "categoryId": "12464"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-interior-care",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//th-live.slatic.net/p/8/meguiars-g18516-leather-andamp-vinyl-cleaner-eleth-r-ae-nd-aiwnil-khliinen-r-namyaaf-khnangaethaelahnangethiiym-5853-8031058-bec9be891f6390218ef129b6ec836ee2-catalog.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586658.OTHER_6027552191_6548076",
                  "categoryName": "Interior Vehicle Care",
                  "categoryId": "12465"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-automotive-car-polishes-waxes",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//th-live.slatic.net/p/8/3m-paste-wax-0818-4675949-92fa657307db32a3506c5b28015936b0-catalog.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586658.OTHER_6027552192_6548076",
                  "categoryName": "Car Polishes & Waxes",
                  "categoryId": "12578"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-glass-care",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//th-live-01.slatic.net/p/8/soft99-glaco-roll-on-120-1469173364-9582147-a5f9b1670a98898ffde42b2940fa7b16-zoom.jpg",
                  "categoryName": "Glass Care",
                  "categoryId": "12586"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-automotive-paints-primers",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//th-live.slatic.net/original/0553c9107d94ac94a6f981450cf6dfda.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586658.OTHER_6027552194_6548076",
                  "categoryName": "Paints & Primers",
                  "categoryId": "12577"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-automotive-vacuums",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//laz-img-cdn.alicdn.com/images/ims-web/TB1Sw1qXwZC2uNjSZFnXXaxZpXa.jpg",
                  "categoryName": "Car Vacuums",
                  "categoryId": "12593"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-automotive-polishing-waxing-kits",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//my-live-02.slatic.net/p/90c7b981946e888cad9783a9b244b1fb.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586658.OTHER_6027552196_6548076",
                  "categoryName": "Polishing & Waxing Kits",
                  "categoryId": "12581"
                }
              ],
              "categoryIcon": "",
              "categoryUrl": "//www.lazada.co.th/shop-car-care",
              "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel2TabDTO",
              "categoryName": "Car Care",
              "categoryId": "10100702"
            },
            {
              "level3TabList": [
                {
                  "categoryUrl": "//www.lazada.co.th/shop-motorcycles-and-scooters",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//th-live.slatic.net/p/mdc/a19d5fa383d9fa3250e656da78197f59.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586658.OTHER_6027552198_6548076",
                  "categoryName": "Motorcycles",
                  "categoryId": "10100714"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-motorcycle-sportbikes",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//th-live.slatic.net/p/044ce822c89466648c83d737a56a09cc.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586658.OTHER_6027552199_6548076",
                  "categoryName": "Sport Bikes",
                  "categoryId": "12472"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-motorcycle-electric-bikes",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//th-live.slatic.net/p/1435a1211d743c09b67ef3d7b8797da5.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586658.OTHER_6027552200_6548076",
                  "categoryName": "Electric Bikes",
                  "categoryId": "12476"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-motorcycle-scooters",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//th-live.slatic.net/p/53d2943ef26b48ab4ee87828c973a0d3.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586658.OTHER_6027552201_6548076",
                  "categoryName": "Scooters",
                  "categoryId": "12471"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-motorcycle-atvs-utvs",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//th-live.slatic.net/p/a7b68cb260cb8536da3765c41a8bed0e.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586658.OTHER_6027552202_6548076",
                  "categoryName": "ATV & UTV",
                  "categoryId": "12481"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-moto-batteries-accessories",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//th-live-03.slatic.net/p/8/leo-ltz-5-5-1476687524-4712109-92a94fa5fee89d8c7029f11584efc700-zoom.jpg",
                  "categoryName": "Moto Batteries & Accessories",
                  "categoryId": "12483"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-motorcycle-tires-wheels",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//laz-img-cdn.alicdn.com/images/ims-web/TB18YDugHj1gK0jSZFuXXcrHpXa.jpg",
                  "categoryName": "Moto Tires & Wheels",
                  "categoryId": "4007"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-motorcycle-oils-fluids",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//th-live-01.slatic.net/p/8/10w-40-1-1506419322-43304664-768eea6b1c2bb803b2ec6f3177bc0add-zoom.jpg",
                  "categoryName": "Moto Oils & Fluids",
                  "categoryId": "12485"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-motorcycle-parts-spares",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//laz-img-cdn.alicdn.com/images/ims-web/TB19b2ugHj1gK0jSZFuXXcrHpXa.jpg",
                  "categoryName": "Moto Parts & Spares",
                  "categoryId": "12486"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-motorcycle-covers",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//laz-img-cdn.alicdn.com/images/ims-web/TB1CdDrgRr0gK0jSZFnXXbRRXXa.jpg",
                  "categoryName": "Motorcycle Covers",
                  "categoryId": "12722"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-motorcycle-luggage-saddlebags",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//laz-img-cdn.alicdn.com/images/ims-web/TB1jubrgRr0gK0jSZFnXXbRRXXa.jpg",
                  "categoryName": "Luggage & Saddlebags",
                  "categoryId": "12701"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-MotorcycleMotorsportsMerchandise",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//laz-img-cdn.alicdn.com/images/ims-web/TB1RxNOQlr0gK0jSZFnXXbRRXXa.png",
                  "categoryName": "Moto Merchandise",
                  "categoryId": "42050601"
                }
              ],
              "categoryIcon": "",
              "categoryUrl": "//www.lazada.co.th/shop-motorcycle",
              "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel2TabDTO",
              "categoryName": "Motorcycle",
              "categoryId": "7966"
            },
            {
              "level3TabList": [
                {
                  "categoryUrl": "//www.lazada.co.th/shop-motorcycle-tires-tubes",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//th-live.slatic.net/p/934a144322cc390c09a2eb0e6466c595.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586658.OTHER_6027552212_6548076",
                  "categoryName": "Motorcycle Tires & Tubes",
                  "categoryId": "4019"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-motorcycle-wheels-rims",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//ph-live-02.slatic.net/p/8/motor-craze-u-type-safetytire-lockblack-1503996869-44013553-ac5145c3c3700c42c7ba6152a72fdf64-zoom.jpg",
                  "categoryName": "Motorcycle Wheels",
                  "categoryId": "4022"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-motorcycle-wheels-tire-packages",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//ph-live-02.slatic.net/p/8/motor-craze-u-type-safetytire-lockblack-1503996869-44013553-ac5145c3c3700c42c7ba6152a72fdf64-zoom.jpg",
                  "categoryName": "Motorcycle Wheel and Tire Package",
                  "categoryId": "4024"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-motorcycle-wheels-tires-accessories",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//th-live.slatic.net/p/a3db72f0ed2115325221a94277295b95.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586658.OTHER_6027552215_6548076",
                  "categoryName": "Motorcycle Wheels & Tires Accessories",
                  "categoryId": "9214"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-motorcycle-wheel-hub-assemblies",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//th-live.slatic.net/p/e83be9ba4ef49e1310f31c1642b84185.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586658.OTHER_6027552216_6548076",
                  "categoryName": "Motorcycle Wheel Hub Assemblies",
                  "categoryId": "4023"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-motorcycle-valve-caps-stems",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//th-live.slatic.net/p/8/45-degree-motorcycle-tire-valve-stem-extender-intl-8363-03569592-45c81e6eeb6b0b497ad06a7a06af3379-catalog.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586658.OTHER_6027552217_6548076",
                  "categoryName": "Motorcycle Valve Caps & Stems",
                  "categoryId": "4015"
                }
              ],
              "categoryIcon": "",
              "categoryUrl": "//www.lazada.co.th/shop-motorcycle-tires-wheels",
              "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel2TabDTO",
              "categoryName": "Moto Tires & Wheels",
              "categoryId": "4008"
            },
            {
              "level3TabList": [
                {
                  "categoryUrl": "//www.lazada.co.th/shop-motorcycle-exterior-accessories",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//laz-img-cdn.alicdn.com/images/ims-web/TB1klfpgO_1gK0jSZFqXXcpaXXa.jpg",
                  "categoryName": "Exterior Accessories",
                  "categoryId": "12487"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-motorcycle-parts-spares",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//laz-img-cdn.alicdn.com/images/ims-web/TB1zgnrgRr0gK0jSZFnXXbRRXXa.jpg",
                  "categoryName": "Parts & Spares",
                  "categoryId": "12482"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-moto-lighting",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//laz-img-cdn.alicdn.com/images/ims-web/TB1uG2sgHj1gK0jSZFuXXcrHpXa.jpg",
                  "categoryName": "Lighting",
                  "categoryId": "10100718"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-motorcycle-mirrors",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//my-live-02.slatic.net/original/07a656adee57c9eec8d0212c5130bdab.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586658.OTHER_6027552222_6548076",
                  "categoryName": "Mirrors",
                  "categoryId": "12702"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/moto-exhaust-and-accessories",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//laz-img-cdn.alicdn.com/images/ims-web/TB13bHsgHj1gK0jSZFuXXcrHpXa.jpg",
                  "categoryName": "Exhaust Pipes & Accessories",
                  "categoryId": "14458"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-motorcycle-replacements-mounting-harware",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//laz-img-cdn.alicdn.com/images/ims-web/TB1uE6pgO_1gK0jSZFqXXcpaXXa.jpg",
                  "categoryName": "Replacement&Mounting Hardware",
                  "categoryId": "12724"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-motorcycle-body-frame",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//laz-img-cdn.alicdn.com/images/ims-web/TB100HsgHj1gK0jSZFuXXcrHpXa.jpg",
                  "categoryName": "Body & Frame",
                  "categoryId": "12697"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-motorcycle-drivetrain-transmission",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//laz-img-cdn.alicdn.com/images/ims-web/TB1TLrngKT2gK0jSZFvXXXnFXXa.jpg",
                  "categoryName": "Drivetrain & Transmission",
                  "categoryId": "12700"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-motorcycle-fuel-injectors-main-jets",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//laz-img-cdn.alicdn.com/images/ims-web/TB1JMbngKT2gK0jSZFvXXXnFXXa.jpg",
                  "categoryName": "Fuel Delivery & Carburetor",
                  "categoryId": "13158"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-motorcycle-electronics",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//laz-img-cdn.alicdn.com/images/ims-web/TB1P_rrgRr0gK0jSZFnXXbRRXXa.jpg",
                  "categoryName": "Electronics",
                  "categoryId": "12489"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-moto-spark-plugs",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//th-live.slatic.net/p/8/ngk-iridium-cpr7eaix-9-1-honda-pcx-click-i-crf125-made-in-japan-3606-74826936-5a4b7cb3f1a4420b957c4ed8215c4f99-catalog.jpg_240x240q80.jpg_.webp?scm=1003.4.icms-zebra-5000413-2586658.OTHER_6027552229_6548076",
                  "categoryName": "Spark Plugs",
                  "categoryId": "10100716"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-motorcycle-batteries-parts",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//vn-live-01.slatic.net/p/3/can-suc-khoe-dien-tu-cao-cap-imedicare-1500469231-5664638-722a963f76bc587191c493560f47459e-zoom.jpg",
                  "categoryName": "Batteries & Accessories",
                  "categoryId": "12693"
                }
              ],
              "categoryIcon": "",
              "categoryUrl": "//www.lazada.co.th/shop-motorcycle-parts-spares",
              "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel2TabDTO",
              "categoryName": "Moto Parts & Accessories",
              "categoryId": "12484"
            },
            {
              "level3TabList": [
                {
                  "categoryUrl": "//www.lazada.co.th/shop-motorcycle-atv-helmets",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//laz-img-cdn.alicdn.com/images/ims-web/TB1c_2ogUT1gK0jSZFhXXaAtVXa.jpg",
                  "categoryName": "Helmets",
                  "categoryId": "12734"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-motorcycle-bluetooth-headsets",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//laz-img-cdn.alicdn.com/images/ims-web/TB1xyjngKT2gK0jSZFvXXXnFXXa.jpg",
                  "categoryName": "Bluetooth Headsets",
                  "categoryId": "12751"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-motorcycle-riding-gear-helmets-accessories",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//laz-img-cdn.alicdn.com/images/ims-web/TB1hVjsgRr0gK0jSZFnXXbRRXXa.jpg",
                  "categoryName": "Helmet Accessories",
                  "categoryId": "12735"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-motorcycle-riding-gear-gloves",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//laz-img-cdn.alicdn.com/images/ims-web/TB1Z5TsgHj1gK0jSZFuXXcrHpXa.jpg",
                  "categoryName": "Gloves",
                  "categoryId": "12733"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-motorcycle-atv-jackets",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//th-live-01.slatic.net/p/8/mens-multi-pockets-pu-leather-motorcycle-jackets-leisure-intl-1497532012-08834742-8493b84b3a347d2bcd59f0e09b4cb5d4-zoom.jpg",
                  "categoryName": "Jackets & Vests",
                  "categoryId": "12736"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-rainwear",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//laz-img-cdn.alicdn.com/images/ims-web/TB1_ansgRr0gK0jSZFnXXbRRXXa.jpg",
                  "categoryName": "Rain Wear",
                  "categoryId": "10100732"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-motorcycle-riding-gear-eyewear",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//th-live-01.slatic.net/p/8/wisebuy-1482169759-2940244-7c3734b1f35e53e388b76ebede230d93-zoom.jpg",
                  "categoryName": "Eyewear",
                  "categoryId": "12731"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-motorcycle-riding-gear-face-masks",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//laz-img-cdn.alicdn.com/images/ims-web/TB1CqPpgUT1gK0jSZFhXXaAtVXa.jpg",
                  "categoryName": "Face Masks",
                  "categoryId": "12749"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-motorcycle-riding-gear-footwear",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//laz-img-cdn.alicdn.com/images/ims-web/TB1mxbqgO_1gK0jSZFqXXcpaXXa.jpg",
                  "categoryName": "Footwear",
                  "categoryId": "12732"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-motorcycle-atv-protective-gear",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//laz-img-cdn.alicdn.com/images/ims-web/TB11rTpgUT1gK0jSZFhXXaAtVXa.jpg",
                  "categoryName": "Chest & Back Protectors",
                  "categoryId": "12730"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-motorcycle-riding-gear-balaclavas",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//laz-img-cdn.alicdn.com/images/ims-web/TB1GE3ZXwZC2uNjSZFnXXaxZpXa.jpg",
                  "categoryName": "Balaclavas",
                  "categoryId": "12747"
                },
                {
                  "categoryUrl": "//www.lazada.co.th/shop-motorcycle-riding-gear-knee-shin-protection",
                  "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel3TabDTO",
                  "categoryImg": "//th-live-03.slatic.net/p/8/lkn-motorcycle-sports-knee-protection-equipment-covered-black-intl-1505484346-46006044-44f9dcbb102e2e4b08d41db767dc50d3-zoom.jpg",
                  "categoryName": "Knee & Shin Protection",
                  "categoryId": "12739"
                }
              ],
              "categoryIcon": "",
              "categoryUrl": "//www.lazada.co.th/shop-motorcycle-riding-gear",
              "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel2TabDTO",
              "categoryName": "Motorcycle Riding Gear",
              "categoryId": "12488"
            }
          ],

          
          "categoryName_zh": "",
          "categoryIcon": "ic-cat-Motors &#xe75d;",
          "id": "6634019",
          "position": "top",
          "childId": "Level_1_Category_No12",
          "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel1TabDTO",
          "categoryName": "Automotive & Motorcycles",
          "level1CategoryId": "6634019"
        },
        {
          "level2TabList": [
            {
              "level3TabList": "",
              "categoryIcon": "",
              "categoryUrl": "//my-m.lazada.co.th/mobilerecharge?wh_weex=true",
              "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel2TabDTO",
              "categoryName": "Mobile Top-Up",
              "categoryId": "14456"
            },
            {
              "level3TabList": "",
              "categoryIcon": "",
              "categoryUrl": "//www.lazada.co.th/shop-food-beverage-vouchers",
              "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel2TabDTO",
              "categoryName": "Food & Beverage Deals",
              "categoryId": "14224"
            },
            {
              "level3TabList": "",
              "categoryIcon": "",
              "categoryUrl": "//www.lazada.co.th/shop-beauty-wellness-vouchers",
              "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel2TabDTO",
              "categoryName": "Beauty & Wellness Deals",
              "categoryId": "14225"
            },
            {
              "level3TabList": "",
              "categoryIcon": "",
              "categoryUrl": "//www.lazada.co.th/shop-travel-vouchers",
              "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel2TabDTO",
              "categoryName": "Travel Deals",
              "categoryId": "14227"
            },
            {
              "level3TabList": "",
              "categoryIcon": "",
              "categoryUrl": "//www.lazada.co.th/shop-activities-entertainment-vouchers",
              "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel2TabDTO",
              "categoryName": "Activity & Entertainment Deals",
              "categoryId": "14226"
            },
            {
              "level3TabList": "",
              "categoryIcon": "",
              "categoryUrl": "//www.lazada.co.th/shop-home-digital-vouchers",
              "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel2TabDTO",
              "categoryName": "Home",
              "categoryId": "10100041"
            }
          ],
          "categoryName_zh": "",
          "categoryIcon": "ic-DigitalProduct &#xe610;",
          "id": "6634020",
          "position": "top",
          "childId": "Level_1_Category_No13",
          "class": "com.lazada.guidedshopping.categories.constants.CategoryLevel1TabDTO",
          "categoryName": "Digital Goods ",
          "level1CategoryId": "6634020"
        }
      ]
    }
}

# count = len(api_data['3887232320']["categoriesLpMultiFloor"][])
# print(count);

# print(api_data['3887232320']["categoriesLpMultiFloor"][0]["level2TabList"][0]['level3TabList'][0]['categoryUrl'])
data_link  = {
    0: 'อุปกรณ์-อิเล็กทรอนิกส์',
    1: 'อุปกรณ์เสริม-อิเล็กทรอนิกส์', 
    2: 'ทีวีและเครื่องใช้ในบ้าน', 
    3: 'สุขภาพและความงาม', 
    4: 'ทารกและของเล่น', 
    5: 'ของชำและสัตว์เลี้ยง', 
    6: 'บ้านและไลฟ์สไตล์', 
    7: 'แฟชั่นและเครื่องประดับผู้หญิง',
    8: 'แฟชั่นและเครื่องประดับผู้ชาย',
    9: 'กีฬาและการเดินทาง',
    10: 'ยานยนต์และรถจักรยานยนต์'}
# Invert ข้อมูล (สลับ key กับ value)
def get_in_json(json_file_path):
     with open(json_file_path, 'w', encoding='utf-8') as new_json_file:
        json.dump(existing_data, new_json_file, ensure_ascii=False, indent=2)
        print(f'ข้อมูลถูกเติมลงในไฟล์ JSON ใหม่ที่ {json_file_path}') 
# เติมข้อมูลใหม่
path_here = os.getcwd();
json_file_path = path_here+'\data_link_all.json';
print(json_file_path)
with open(json_file_path, 'r', encoding='utf-8') as json_file:
    existing_data = json.load(json_file)

d=0;
for c in range(len(api_data['3887232320']["categoriesLpMultiFloor"])):
  
  if(c<12):
    print("\n<======>",c+1,"<======>\n");
    data_link_1=[];
    for data in range(len(api_data['3887232320']["categoriesLpMultiFloor"][c]["level2TabList"])):
        
        data_link_1.append(api_data['3887232320']["categoriesLpMultiFloor"][c]["level2TabList"][data]["categoryUrl"]);
        if(len(api_data['3887232320']["categoriesLpMultiFloor"][c]["level2TabList"][data]["level3TabList"])!=1):
          for i in range(len(api_data['3887232320']["categoriesLpMultiFloor"][c]["level2TabList"][data]["level3TabList"])):
              data_link_1.append(api_data['3887232320']["categoriesLpMultiFloor"][c]["level2TabList"][data]["level3TabList"][i]["categoryUrl"]);
    if(c==9):
        existing_data[data_link[4]]["lazada"]=data_link_1
        get_in_json(json_file_path);
        d-=1;
    else:
        existing_data[data_link[d]]["lazada"] = [] 
        get_in_json(json_file_path);
        existing_data[data_link[d]]["lazada"]=data_link_1
        get_in_json(json_file_path);
    d+=1;

# 4 9 อยู่ด้วยกัน