import requests
import time
from config.headers import get_default_headers
from dicts.font_map import FONT_MAP
# 全局定义请求头
HEADERS=get_default_headers()

"""通用 HTML 请求函数，支持自动重试。"""
def get_html(url, retries=3, timeout=10, verbose=True):
    for attempt in range(1, retries + 1):
        try:
            response = requests.get(url, headers=HEADERS, timeout=timeout)
            if response.status_code == 200:
                return response.text
            else:
                if verbose:
                    print(f"[!] 第 {attempt} 次请求返回状态码: {response.status_code}")
        except requests.RequestException as e:
            if verbose:
                print(f"[!] 第 {attempt} 次请求异常：{e}")
        time.sleep(1)
    if verbose:
        print(f"[x] 请求失败：共重试 {retries} 次，未成功获取 {url}")
    return None

"""解密章节文本"""
def decrypt_text(content):
    decrypted_chars = []
    for char in content:
        try:
            unicode_code = str(ord(char))  # 将字符转换为十进制的 Unicode 编码（字符串）
            real_char = FONT_MAP.get(unicode_code, char)  # 如果查不到，保留原字符
        except Exception:
            real_char = char  # 极少数异常字符安全兜底
        decrypted_chars.append(real_char)
    return ''.join(decrypted_chars)