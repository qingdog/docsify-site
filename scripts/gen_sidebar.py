#!/usr/bin/env python3
"""
根据 docs/ 目录下的 md 文件自动生成 _sidebar.md

用法:
  python3 scripts/gen_sidebar.py

功能:
  - 扫描 docs/ 目录下所有 .md 文件
  - 提取每个文件的第一个 # 标题作为侧边栏显示名
  - README.md 作为首页，链接指向 /
  - 其余文件按配置的优先级和字母序排列
  - 自动排除 _sidebar.md、_coverpage.md 等下划线开头的文件
"""

import os
import re

# ====== 配置 ======
DOCS_DIR = os.environ.get('DOCS_DIR', 'docs')
OUTPUT = os.path.join(DOCS_DIR, '_sidebar.md')

# 排序优先级：排在前面的
PRIORITY = ['README.md', 'guide.md', 'features.md']

# 排除的文件（除了下划线开头的）
EXCLUDE = {'DEPLOY.md'}


def extract_title(filepath):
    """从 md 文件中提取第一个 # 标题"""
    with open(filepath, 'r', encoding='utf-8') as f:
        for line in f:
            match = re.match(r'^#\s+(.+)$', line.strip())
            if match:
                return match.group(1).strip()
    return None


def collect_md_files(docs_dir):
    """收集并排序 md 文件"""
    md_files = []
    for fname in os.listdir(docs_dir):
        if not fname.endswith('.md'):
            continue
        if fname.startswith('_'):
            continue
        if fname in EXCLUDE:
            continue
        md_files.append(fname)

    md_files.sort(key=lambda f: (0, PRIORITY.index(f)) if f in PRIORITY else (1, f))
    return md_files


def generate_sidebar(docs_dir):
    """生成 _sidebar.md 内容"""
    md_files = collect_md_files(docs_dir)
    lines = []

    for fname in md_files:
        fpath = os.path.join(docs_dir, fname)
        title = extract_title(fpath)

        if fname == 'README.md':
            display = '首页'
            link = '/'
        else:
            display = title if title else fname.replace('.md', '')
            link = fname

        lines.append(f'- [{display}]({link})')

    return '\n'.join(lines) + '\n'


def main():
    content = generate_sidebar(DOCS_DIR)
    with open(OUTPUT, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f'✅ 已生成: {OUTPUT}')
    print(f'--- 内容 ---')
    print(content)


if __name__ == '__main__':
    main()
