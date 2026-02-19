import os

def generate_contents_html(target_dir="."):
    """
    지정된 디렉토리의 폴더와 html 파일 리스트를 추출하여 contents.html을 생성합니다.
    """
    # 1. 파일 및 디렉토리 리스트 수집
    items = os.listdir(target_dir)
    
    # 제외할 항목 (숨김 파일, 자기 자신 등)
    exclude_list = ['.git', '.github', 'contents.html', 'update_contents.py']
    
    filtered_items = [
        item for item in items 
        if item not in exclude_list and (os.path.isdir(item) or item.endswith('.html'))
    ]
    
    # 이름 순으로 정렬 (폴더 우선)
    filtered_items.sort(key=lambda x: (not os.path.isdir(x), x.lower()))

    # 2. HTML 템플릿 작성
    html_start = """<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <title>강의 자료 목차</title>
    <style>
        body { font-family: sans-serif; padding: 40px; line-height: 1.8; }
        h1 { color: #2c3e50; border-bottom: 2px solid #3498db; display: inline-block; }
        ul { list-style: none; padding-left: 0; }
        li { margin-bottom: 8px; border-bottom: 1px dotted #ccc; }
        .dir { font-weight: bold; color: #e67e22; }
        .file { color: #34495e; }
        a { text-decoration: none; color: inherit; }
        a:hover { text-decoration: underline; color: #3498db; }
        .icon { margin-right: 10px; }
    </style>
</head>
<body>
    <h1>📂 저장소 콘텐츠 목록</h1>
    <ul>
"""

    html_end = """    </ul>
    <p style="margin-top:30px; font-size: 0.8em; color: #7f8c8d;">
        마지막 업데이트: {update_time}
    </p>
</body>
</html>
"""

    # 3. 리스트 항목 생성
    import datetime
    content_list = ""
    for item in filtered_items:
        is_dir = os.path.isdir(item)
        icon = "📁" if is_dir else "📄"
        class_name = "dir" if is_dir else "file"
        display_name = f"{item}/" if is_dir else item
        
        content_list += f'        <li><span class="icon">{icon}</span><a href="./{item}" class="{class_name}">{display_name}</a></li>\n'

    # 4. 파일 쓰기
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    full_html = html_start + content_list + html_end.format(update_time=now)

    with open("contents.html", "w", encoding="utf-8") as f:
        f.write(full_html)
    
    print(f"성공: contents.html 파일이 업데이트되었습니다. ({now})")

if __name__ == "__main__":
    generate_contents_html()
