#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
📚 Book Recommender - 书籍推荐助手
功能：书籍推荐、豆瓣评分、读书笔记
"""

import json
from pathlib import Path
from datetime import datetime

DATA_DIR = Path(__file__).parent
LIBRARY_FILE = DATA_DIR / "library.json"

# 示例书籍数据库
BOOKS_DB = {
    "小说": [
        {"title": "活着", "author": "余华", "rating": 9.4, "desc": "讲述一个人一生的苦难与坚强"},
        {"title": "百年孤独", "author": "马尔克斯", "rating": 9.3, "desc": "布恩迪亚家族七代人的传奇故事"},
        {"title": "追风筝的人", "author": "卡勒德·胡赛尼", "rating": 9.2, "desc": "关于救赎与成长的感人故事"},
        {"title": "三体", "author": "刘慈欣", "rating": 9.5, "desc": "地球文明与三体文明的生死较量"},
    ],
    "商业": [
        {"title": "穷查理宝典", "author": "查理·芒格", "rating": 9.3, "desc": "投资大师的智慧箴言"},
        {"title": "原则", "author": "瑞·达利欧", "rating": 9.0, "desc": "桥水基金创始人的生活和工作原则"},
    ],
    "成长": [
        {"title": "被讨厌的勇气", "author": "岸见一郎", "rating": 9.1, "desc": "阿德勒心理学入门"},
        {"title": "原子习惯", "author": "詹姆斯·克利尔", "rating": 9.2, "desc": "细微改变带来巨大成就"},
    ],
    "历史": [
        {"title": "明朝那些事儿", "author": "当年明月", "rating": 9.5, "desc": "幽默风趣的明朝历史"},
        {"title": "人类简史", "author": "尤瓦尔·赫拉利", "rating": 9.3, "desc": "从动物到上帝的人类历程"},
    ]
}


def recommend_books(category, limit=5):
    """推荐书籍"""
    if category in BOOKS_DB:
        return BOOKS_DB[category][:limit]
    
    # 搜索
    results = []
    for cat, books in BOOKS_DB.items():
        for book in books:
            if category in book['title'] or category in book['author']:
                results.append(book)
    
    return results[:limit]


def format_book(book):
    """格式化书籍信息"""
    return f"📖 《{book['title']}》- {book['author']} ⭐{book['rating']}\n   📝 {book['desc']}"


def main(query):
    """主函数"""
    query = query.lower()
    
    # 推荐小说
    if "小说" in query:
        books = recommend_books("小说")
        response = "📚 **小说推荐**\n\n"
        for book in books:
            response += format_book(book) + "\n\n"
        return response
    
    # 推荐商业书
    if "商业" in query or "投资" in query:
        books = recommend_books("商业")
        response = "💼 **商业书籍推荐**\n\n"
        for book in books:
            response += format_book(book) + "\n\n"
        return response
    
    # 推荐成长书
    if "成长" in query or "心理" in query:
        books = recommend_books("成长")
        response = "🌱 **成长书籍推荐**\n\n"
        for book in books:
            response += format_book(book) + "\n\n"
        return response
    
    # 搜索书籍
    if "三体" in query:
        return """📖 《三体》- 刘慈欣

⭐ 豆瓣评分：9.5 (50 万人评分)
📝 简介：地球文明与三体文明的生死较量
🏆 奖项：雨果奖最佳长篇小说
📚 系列：三体三部曲第一部"""
    
    # 默认回复
    return """📚 书籍推荐助手

**功能**：
1. 书籍推荐 - "推荐小说"
2. 评分查询 - "查三体的评分"
3. 读书笔记 - "记录读书笔记"

**分类**：小说、商业、成长、历史

告诉我你想看什么类型的书？👻"""


if __name__ == "__main__":
    import sys
    sys.stdout.reconfigure(encoding='utf-8')
    print(main("推荐小说"))
