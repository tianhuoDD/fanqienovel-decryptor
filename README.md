# fanqienovel-decryptor

> 本工具基于 [RChow](https://www.cnblogs.com/ruichow/p/18209338) 大佬的博客内容，在其思路基础上进行了优化和扩展，适配更多场景，提升了使用体验。

## 🧿 说明

该项目已完成字体解密工作，但由于番茄小说网站的限制（验证码、无法阅读全文）等原因，无法下载全部章节，拥有番茄SVIP除外。这也是为什么大多数相关工具需要API的原因。

关于后续扩展，考虑去抓取番茄小说APP的API，通过手机端获得小说内容，尽情期待。

## 📘 项目简介

`fanqienovel-decryptor` 是一个用于**解密并下载番茄小说内容**的 Python 工具。  
通过逆向番茄小说的字体加密机制，提取真实章节文本，并支持通过小说 ID 批量下载为 `.txt` 格式。

---

## 🔧 功能特点

- ✅ 自动解析并解密字体映射（反反爬机制）
- ✅ 支持通过输入小说章节选择要下载的内容
- ✅ 输出为纯文本 `.txt` 文件
- ⬜ 通过API聚合输出

---

## 📥 使用方式

### ✨ 项目结构

```python
fanqie_novel_spider/
│
├── .gitignore               # git忽略文件
├── README.md                # 项目说明文档
├── requirements.txt         # 依赖列表
├── run.py                   # 主运行脚本
│
├── config/                  # 配置文件
│   └── headers.py           # 请求头、Cookie 等配置
│
├── dicts/                   # 存放映射字典文件
│   └── font_map.py          # 解密字体映射字典
│    
└── utils/
    └── common_tools.py      # 公共的通用方法
```



---

## 🙏 致谢

特别感谢 [RChow](https://www.cnblogs.com/ruichow/p/18209338) 的技术分享，为本项目的实现提供了关键思路。

---