import os
import parsel
from utils.common_tools import get_html, decrypt_text

"""解析小说主页，提取基本信息和章节目录"""
def parse_main_page(url):
    html = get_html(url)
    if not html:
        print("[x] 主页面请求失败")
        return None, [], []
    selector = parsel.Selector(html)
    # 提取基本信息
    book_title = selector.css('.info-name h1::text').get(default='未知标题').strip()
    author_name = selector.css('.author-name-text::text').get(default='未知作者').strip()
    chapter_count = selector.css('.page-directory-header h3::text').get(default='0').strip()
    # word_count_info = selector.css('.info-count-word span::text').getall() # 小说字数
    # book_description = selector.css('.page-abstract-content p::text').get(default='').strip() # 小说简介
    tags = selector.css('.info-label span::text').getall()
    # 提取章节信息
    chapter_titles = selector.css('.chapter-item-title::text').getall()
    chapter_hrefs = selector.css('.chapter-item-title::attr(href)').getall()
    # 提取最近更新信息
    last_update_title = selector.css('.info-last-title::text').getall()[1]
    last_update_time = selector.css('.info-last-time::text').get(default='').strip()
    # 输出摘要信息
    print(f"📘 小说：《{book_title}》 by {author_name}")
    print(f"📖 共 {chapter_count} 章；标签：{'、'.join(tags)}")
    print(f"🕘 最近更新：{last_update_title} · {last_update_time}")
    return book_title, chapter_titles, chapter_hrefs[1:]  # 可选跳过第一个（如为引导/目录）


"""下载并解密章节"""
def download_chapters(book_title, titles, urls):
    output_dir = "output"
    os.makedirs(output_dir, exist_ok=True)  # 确保输出目录存在
    file_path = os.path.join(output_dir, f"{book_title}.txt")
    print(f"🎁 开始下载小说《{book_title}》")
    with open(file_path, "w", encoding="utf-8") as f:
        for title, link in zip(titles, urls):
            full_url = 'https://fanqienovel.com' + link
            html = get_html(full_url)
            if not html:
                print(f"[x] 章节《{title}》请求失败，已跳过")
                continue
            selector = parsel.Selector(html)
            print(selector)
            print(full_url)
            content_list = selector.css('.muye-reader-content-16 p::text').getall()
            raw_text = '\n'.join(content_list)
            decrypted_text = decrypt_text(raw_text)
            f.write(f"\n\n{title}\n\n")
            f.write(decrypted_text)
            print(f"✅ 已下载：{title}")
    print(f"🎉 已保存至：{file_path}")


if __name__ == "__main__":
    book_id= input("请输入小说ID：").strip()
    # ✅ 设置小说主页面 URL
    novel_url = f"https://fanqienovel.com/page/{book_id}"
    # ✅ 解析主页面，提取章节信息
    result = parse_main_page(novel_url)
    # 判断小说页面是否解析成功
    if not result:
        print("[x] 小说页面解析失败，程序终止。")
    else:
        book_title, chapter_titles, chapter_urls = result
        for i, (title, url) in enumerate(zip(chapter_titles, chapter_urls), start=1):
            print(f"{i}. {title} - {url}")
        while True:
            user_input = input("请输入要下载的章节范围（如 1-220 或 all）：").strip().lower()
            if user_input == "all":
                download_chapters(book_title, chapter_titles, chapter_urls)
                break
            elif "-" in user_input:
                try:
                    start_str, end_str = user_input.split("-")
                    start_idx = int(start_str) - 1  # 转换为列表下标
                    end_idx = int(end_str)  # 包含该章节

                    if 0 <= start_idx < end_idx <= len(chapter_urls):
                        selected_titles = chapter_titles[start_idx:end_idx]
                        selected_urls = chapter_urls[start_idx:end_idx]
                        download_chapters(book_title, selected_titles, selected_urls)
                        break
                    else:
                        print(f"请输入有效范围（1-{len(chapter_urls)}）")
                except ValueError:
                    print("格式错误，请输入类似 '1-220' 的范围")
            else:
                print("输入无效，请输入 '1-220' 或 'all'")

    input("按任意键结束...")
