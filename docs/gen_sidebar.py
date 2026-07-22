#!/usr/bin/env python3
"""
根据 docs/ 目录下的 md 文件自动生成 _sidebar.md
- 扫描所有 .md 文件（排除 _sidebar.md, _coverpage.md 等以下划线开头的文件）
- 提取每个文件的第一个 # 标题作为显示名称
- README.md 作为首页，链接指向 /
- 其他文件链接指向自身文件名
"""

import os
import re
import sys

def extract_title(filepath):
    """从 md 文件中提取第一个 # 标题"""
    with open(filepath, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            match = re.match(r'^#\s+(.+)$', line)
            if match:
                return match.group(1).strip()
    return None

def generate_sidebar(docs_dir):
    """扫描目录，生成 _sidebar.md 内容"""
    entries = []

    # 排序优先级：README.md 第一，guide.md 第二，features.md 第三，其余按字母序
    PRIORITY = ['README.md', 'guide.md', 'features.md']
    def sort_key(fname):
        if fname in PRIORITY:
            return (0, PRIORITY.index(fname))
        return (1, fname)

    # 收集所有 md 文件（排除下划线开头和非文档文件）
    md_files = []
    EXCLUDE = {'DEPLOY.md'}
    for fname in os.listdir(docs_dir):
        if not fname.endswith('.md'):
            continue
        if fname.startswith('_'):
            continue
        if fname in EXCLUDE:
            continue
        md_files.append(fname)

    md_files.sort(key=sort_key)

    # 为每个文件生成侧边栏条目
    for fname in md_files:
        fpath = os.path.join(docs_dir, fname)
        title = extract_title(fpath)

        if fname == 'README.md':
            display = '首页'
            link = '/'
        else:
            display = title if title else fname.replace('.md', '')
            link = fname

        entries.append(f'- [{display}]({link})')

    # 加上分类分隔
    content = '\n'.join(entries) + '\n'
    return content

def main():
    docs_dir = sys.argv[1] if len(sys.argv) > 1 else '/workspace/docs'
    sidebar_content = generate_sidebar(docs_dir)

    sidebar_path = os.path.join(docs_dir, '_sidebar.md')
    with open(sidebar_path, 'w', encoding='utf-8') as f:
        f.write(sidebar_content)

    print(f'✅ 已生成: {sidebar_path}')
    print(f'--- 内容 ---')
    print(sidebar_content)

if __name__ == '__main__':
    main()
