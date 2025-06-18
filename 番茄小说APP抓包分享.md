## 说明

本文档简要的说明`番茄小说APP`如何进行抓包，以及部分的API；但由于技术原因，API无法实现通用性，即无法通过更改`book_id`就实现小说内容抓取，往往需要同时修改其他字段信息。

## 部分API

### 1.获取书籍详情（听书）

```python
import requests
params = {
    'book_id': '6982529841564224526', # 更改此处可更改小说
    'source': '5',
    'aid': '1967',
}

response = requests.get('https://api5-normal-sinfonlineb.fqnovel.com/reading/reader/book/recommend_data_plan/v',params=params)
print(response.json())
```

### 2.获取小说的目录信息

```python
import requests

url = "https://api5-normal-sinfonlineb.fqnovel.com/reading/bookapi/directory/all_items/v?book_type=0&item_data_list_md5&catalog_data_md5&book_id=7087872099557051400&book_info_md5&need_version=true&iid=1408906374261642&device_id=1408906374257546&ac=wifi&channel=49786187a&aid=1967&app_name=novelapp&version_code=67532&version_name=6.7.5.32&device_platform=android&os=android&ssmix=a&device_type=ASUS_I005DA&device_brand=Asus&language=zh&os_api=28&os_version=9&manifest_version_code=67532&resolution=800*1280&dpi=240&update_version_code=67532&_rticket=1749715124712&host_abi=arm64-v8a&dragon_device_type=pad&pv_player=67532&compliance_status=4&need_personal_recommend=0&player_so_load=1&is_android_pad_screen=1&rom_version=Asus-user+9.0.0+20171130.276299+release-keys&cdid=56ab0923-ba18-450b-87ff-b6ca7589ac68"

headers = {
'x-tt-store-region': 'cn-yn',
'x-argus': 's4hKaA==',
'x-helios': 'boLxPagH896HUmgApcg/oqBUQP4IZUFD94+m6qvcR28qJobn',
'x-medusa': 't4hKaKHnyh1VDfheC2POopFDCYAe2AABL5uWra9ZAQQhGqke2zLbtqSzV7+eipB7M5jvjP5xA6rYJXrpZK7Waf8mQCcVbxtES3sh5WRDRCueHYgp0i5swggGz7GZT2YhizKmihiVxpw2v/tY5XUV0Zsqd8b/2UBYjsD1UTmS+C/HV7RZLRjDz2v1qW+tLvq69adOuzns+X/yRQQyqoip7sgJePdZmLU8dMdpJb+RUHV83wUY+baaJZDMfZeKVhfvBl+qb/CKM7Bgj7sp58dI3pDcESuG4iCQbu3GvlBvPmHSJiSMxbvMp823GU4dsE9zqqD8druNZ1dTk3wBomEuyzLnN3+PpIx3k6dlD8dcP9TnbBgAVCg2W0JiSplHyMAR+7o2NlQNgBym6NfaRjgvDjmgfd0KuG+DHw+kh5roFk+mFF920DRiqkpwYrpjGHxOQGWEtuqvQZBUHv+HHNdXvZLci62BH2/uQgaNEYLdAjacVotEsNLwM7RLBCfeyl9KCN6VPI88tyIGdlnn+sTqOwojILJYCLI+8H735XGmYBLfdQhuNjdZJIr3ApgEEIMxDfzdX/RIVW2eRFc1/poHCW0s0b8Gf+IPh146qo5GN5cuw2Mo+QdB0A0XLV1Pvh0XxBOR8I5XKe2Xwqr+4QyjNu9MDiGz8q58rpQDHTdczK2OvIPuab3tR+VL5FCJFIUPBBRQyk4rRz54W8+i0oHisyQB+DXtoi4CmpV+UgvC5fQrDVIsbgV+657CkUI6UCBB+awtSujSQHO2u1P2P0F8AQTIwpcv9wCUyPobv5EslZp2rG3N6UPv7HZUjbUYKGJTMQPKGhPikxZnkxSMSJkcIFEPjJSIdHwSCzc3Wgmaff1Dzbqsez5LgpiSqtMQVqprUt7k/ctkefVh+gCOnEnubhkz0i5X/RlsvCEyOGmkt+mQ2OgS9oihsljjhxILG5UAhE0+QdCYyHmAnxqDrjImu/PRoCGhI1WZG8SFsRn6B01VQlRQSG9w/CxT4plj6XFfL/NL8HiacGlfPf/6vz3/+r+obw==',
}

response = requests.get(url, headers=headers)
# 将 response.text 写入文件
with open('番茄小说抓包测试/py_目录抓包.txt', 'w', encoding='utf-8') as file:
    file.write(response.text)
```

### 3.获取小说内容信息

```python
import requests

url = "https://api5-normal-sinfonlineb.fqnovel.com/reading/bookapi/detail/v?without_video=false&book_id=7087872099557051400&iid=1408906374261642&device_id=1408906374257546&ac=wifi&channel=49786187a&aid=1967&app_name=novelapp&version_code=67532&version_name=6.7.5.32&device_platform=android&os=android&ssmix=a&device_type=ASUS_I005DA&device_brand=Asus&language=zh&os_api=28&os_version=9&manifest_version_code=67532&resolution=800*1280&dpi=240&update_version_code=67532&_rticket=1749715124701&host_abi=arm64-v8a&dragon_device_type=pad&pv_player=67532&compliance_status=4&need_personal_recommend=0&player_so_load=1&is_android_pad_screen=1&rom_version=Asus-user+9.0.0+20171130.276299+release-keys&cdid=56ab0923-ba18-450b-87ff-b6ca7589ac68"

headers = {
'Host': 'api5-normal-sinfonlineb.fqnovel.com',
'accept-encoding': 'gzip',
'accept': 'application/json; charset=utf-8,application/x-protobuf',
'x-xs-from-web': '0',
'x-ss-req-ticket': '1749715124705',
'x-reading-request': '1749715124705-2019704209',
'x-vc-bdturing-sdk-version': '3.7.2.cn',
'lc': '101',
'sdk-version': '2',
'passport-sdk-version': '50564',
'x-tt-store-region': 'cn-yn',
'x-tt-store-region-src': 'did',
'user-agent': 'com.dragon.read/67532 (Linux; U; Android 9; zh_CN; ASUS_I005DA; Build/PI;tt-ok/3.12.13.4-tiktok)',
'x-ladon': 'aEqIsw==',
'x-khronos': '1749715123',
'x-soter': 'AAEAAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA',
'x-argus': 's4hKaA==',
'x-gorgon': '8404c05b00006604d8aafcf7928eff884d13b2f8e8102f89ef67',
'x-helios': 'mR6bAP/kc8SiVagw03Lx3fvOpHfk3gdRCR1oIri407ptY7m2',
'x-medusa': 't4hKaKHnyh1VDfheC2POopFDCYAqHAABNJlNk+UxAU8tGPd2PiMU/bG5G1s1XYsRU2g1cMYKbsCG9XI1lg8dQkwMWQdFSWd/xgNCLSUDuiqCL35qkONQ83qVCgttMDXcl0NER6iVQR48Wp3Pm6c12L8gfnz/o9qc3Zkn5NrsJkHpyVtLBkHcbPHqXvzizJwtX5eg3Z/Rz8k5/tLAmlmtQ7QbPrG/N2JpXuc8kwDSs3KIxOgVjzohqlTKmtW7+2X9xEVT3ty81vakofUT6mfy1KrNGFJwtjDT681JxKi/SFniGM5WwheIf/MDo4jV9SHx0HGTW/EAf4jVG1fZEz4ys71QVBZSN5PE8AfiNb3wHoL8rbZRk02tnUdfJXpI+oCy2I+/Augafq2GUbH9JyrM0CQrTRJFGTs7Q3gGIBlb3zMdOOYZgl4U6D36ohRJha+AXJK8HCSVST2jgQdCTwKN4WN8NO7gHSg2g6PK504eprVWDqi0WbNHgw4h9jYz8WQr8W1KbFcE5yw6UsscK2+ndYFcuzRMALgqhcjOvDpLS+prGcIHTUdPf+eqzgIDaCEAnMJkv65oOrUIM8moUVSh3X1dk3nPmep3NjRtTVoJtd/A8w+HisGyhhzE/S0d8sCBcal2SqfKfzP1UA0uJSwIj5EfE5+aTIX0wQ7DMh8IlsiVggwSRNU+Bhwe9qfDo5xx+44iNqe7G0uPLEgElOboBWQG/+6p+Z6BSs1jl1cXxlX0x0alYL7DrEkgSpCqnc1QXOez48bBoGfgUqHB+d4WEHFJ8upapH2ZQTYtUXaDAcGqUI1vGXT76AKy2bK9FqDs9Jmtj8QbvQkBQc2f+MesqKGh4C7JHpk8fwOPDuNLDwvElm7UrKoRHzdfzqDovueG4zXXSvHar+ru1rXCov4bkd5TVX3+Z22ePziiS2bPstXgHLWzWlinAVO13y2a/D3P8DAuKcM6w3BAx5Nzcf5AMwERUe0WwNidKXpPuk17ohzudbO8bIDjvC3cVq7ZG3SW+FvACGg4V4krbv/4F27/+Bf9aw==',
'cookie': 'store-region=cn-yn; store-region-src=did; install_id=1408906374261642; ttreq=1$2a0bde343119a958ac8c99709f728953b499ccea; odin_tt=f693e06644c6018656c87642668ed589769ad96574a56b8d1a10df97f6cf337faa77eca258dd8d9a4bbe81e462434e2c43202d8eaad98c5493cfd4fb4797533fd672f40ec14c293e394529efe3b7ac52; passport_csrf_token=40ef3528b447c66518506eb19a38f25d; passport_csrf_token_default=40ef3528b447c66518506eb19a38f25d',

}

response = requests.get(url, headers=headers)
print(response.text)
# # 将 response.text 写入文件
# with open('番茄小说抓包测试/py_目录抓包.txt', 'w', encoding='utf-8') as file:
#     file.write(response.text)
```

### 抓包思路

> Android抓包工具：[HTTPCanary(小黄鸟)](https://blog.csdn.net/weixin_53891182/article/details/124739048)   Android模块安装：[逍遥模拟器安装Magisk和EDXPosed教程](https://www.duokaiya.com/1443.html)   Android模块：[解除抓包无网络限制-TrustMeAlready模块](https://www.bilibili.com/video/BV1wD421p74N/?vd_source=24008413d06e0afa2b9aacaae9bdb6dc)
>
> 下载所有工具：[蓝奏云-密码: romcere](https://wwvh.lanzouu.com/b00l20lbfc)

​	安卓抓包首要条件是选择抓包工具，常用的有`Fiddler`、`Wireshark`、`BurpSuite`、`r0capture`、`HTTPCanary`。其中[`r0capture`](https://github.com/r0ysue/r0capture)也非常推荐，它抓包很简单，无需root及配置模块，但分析日志具有一定难度（[r0capture使用教程](https://blog.csdn.net/yi_rui_jie/article/details/122667368)）。我这里使用的是`HTTPCanary`，需要root，推荐模拟器运行。

​	下载完`HTTPCanary`后，根据[逍遥模拟器安装Magisk和EDXPosed教程](https://www.duokaiya.com/1443.html)安装模块工具，接着安装[解除抓包无网络限制-TrustMeAlready模块](https://www.bilibili.com/video/BV1wD421p74N/?vd_source=24008413d06e0afa2b9aacaae9bdb6dc)即可进行抓包。



































