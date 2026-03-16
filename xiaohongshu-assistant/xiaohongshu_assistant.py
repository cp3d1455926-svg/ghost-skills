#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
📕 Xiaohongshu Assistant - 小红书助手
功能：文案生成、标题优化、话题推荐
"""

import json
from pathlib import Path
from datetime import datetime

DATA_DIR = Path(__file__).parent
POSTS_FILE = DATA_DIR / "posts.json"

# 标题模板
TITLE_TEMPLATES = [
    "救命！XXX 真的太好用了吧！",
    "XXX 是一种什么样的体验？",
    "后悔没早买！XXX 真香",
    "XXX 避雷指南，千万别踩坑",
    "学生党必看！XXX 平价替代",
    "打工人必备！XXX 提升幸福感",
    "XXX 测评｜值不值得买？",
    "我宣布！XXX 是年度最佳",
]

# emoji 库
EMOJIS = {
    "开心": ["😄", "🤣", "😆", "😊"],
    "惊讶": ["😱", "😲", "🤯", "😮"],
    "喜欢": ["❤️", "💕", "💖", "💗"],
    "推荐": ["👍", "👏", "💯", "✅"],
    "警告": ["⚠️", "❌", "🚫", "⛔"],
    "购物": ["🛍️", "🛒", "💰", "🏷️"],
    "美食": ["🍔", "🍕", "🍰", "🍵"],
    "美妆": ["💄", "💅", "🧴", "✨"],
    "旅行": ["✈️", "🏖️", "📸", "🗺️"],
}

# 话题标签
HASHTAGS = {
    "美妆": ["#美妆", "#护肤", "#彩妆", "#美妆分享", "#护肤心得"],
    "美食": ["#美食", "#美食日常", "#美食分享", "#吃货", "#美食探店"],
    "旅行": ["#旅行", "#旅游", "#旅行攻略", "#旅行日记", "#说走就走"],
    "穿搭": ["#穿搭", "#每日穿搭", "#穿搭分享", "#时尚", "#OOTD"],
    "学习": ["#学习", "#学习打卡", "#自律", "#成长", "#提升自己"],
    "生活": ["#生活", "#生活碎片", "#记录生活", "#日常", "#plog"],
    "购物": ["#购物", "#购物分享", "#好物分享", "#种草", "#拔草"],
    "职场": ["#职场", "#打工人", "#职场日常", "#工作", "#升职加薪"],
}


def load_posts():
    """加载笔记"""
    if POSTS_FILE.exists():
        with open(POSTS_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return {"posts": []}


def save_posts(data):
    """保存笔记"""
    with open(POSTS_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


def generate_title(topic, style="推荐"):
    """生成标题"""
    import random
    
    templates = TITLE_TEMPLATES[:5] if style == "推荐" else TITLE_TEMPLATES[5:]
    template = random.choice(templates)
    
    # 添加 emoji
    emoji = random.choice(EMOJIS.get("喜欢", ["✨"]))
    
    title = f"{emoji} {template.replace('XXX', topic)}"
    
    return title


def generate_hashtags(category, count=5):
    """生成话题标签"""
    tags = HASHTAGS.get(category, HASHTAGS["生活"])
    import random
    return random.sample(tags, min(count, len(tags)))


def generate_content(topic, category="生活"):
    """生成文案"""
    import random
    
    # 开头
    openings = [
        f"姐妹们！今天必须给你们安利{topic}！",
        f"真的绝了！{topic}我用了一次就爱上了！",
        f"救命！{topic}怎么这么好用？！",
        f"说实话，{topic}比我想象中还香！",
    ]
    
    # 正文模板
    body = f"""
{random.choice(openings)}

✨ 使用感受：
用了一周，真的惊艳到我了！
{topic}的{random.choice(['效果', '质量', '性价比'])}真的很不错～

💡 亮点：
1. {random.choice(['颜值高', '效果好', '性价比高', '使用方便'])}
2. {random.choice(['设计贴心', '功能强大', '材质好', '服务棒'])}
3. {random.choice(['物流快', '包装好', '客服好', '售后好'])}

⚠️ 注意事项：
{random.choice(['敏感肌先试用', '理性消费', '按需购买', '货比三家'])}

总的来说，{topic}还是值得入手的！
推荐指数：⭐⭐⭐⭐⭐
"""
    
    # 添加 emoji
    emojis = random.sample(EMOJIS.get(category, EMOJIS["生活"]), 3)
    body = body.replace("✨", emojis[0] + " ")
    body = body.replace("💡", emojis[1] + " ")
    body = body.replace("⚠️", emojis[2] + " ")
    
    # 添加话题
    hashtags = generate_hashtags(category)
    body += "\n" + " ".join(hashtags)
    
    return body


def create_post(title, content, category="生活"):
    """创建笔记"""
    data = load_posts()
    
    post = {
        "title": title,
        "content": content,
        "category": category,
        "created": datetime.now().isoformat(),
        "likes": 0,
        "comments": 0,
        "status": "draft"
    }
    
    data["posts"].append(post)
    save_posts(data)
    
    return post


def format_post(post):
    """格式化笔记"""
    response = f"📕 **{post['title']}**\n\n"
    response += f"📂 分类：{post['category']}\n"
    response += f"📅 创建：{post['created'][:10]}\n"
    response += f"❤️ 点赞：{post['likes']}\n"
    response += f"💬 评论：{post['comments']}\n"
    response += f"📊 状态：{post['status']}\n\n"
    response += "---\n\n"
    response += post['content'][:300] + "...\n"
    
    return response


def main(query):
    """主函数"""
    query = query.lower()
    
    # 生成标题
    if "标题" in query or "起名" in query:
        topic = "好物"  # 默认
        title = generate_title(topic)
        return f"""📕 **标题建议**

{title}

💡 告诉我你的主题，我帮你生成更精准的标题！"""
    
    # 生成文案
    if "文案" in query or "写笔记" in query:
        topic = "好物分享"
        content = generate_content(topic)
        return f"""📕 **文案示例**

{content}

💡 告诉我你想写什么，我帮你生成专属文案！"""
    
    # 生成话题
    if "话题" in query or "标签" in query:
        category = "生活"
        tags = generate_hashtags(category)
        response = "🏷️ **话题推荐**：\n\n"
        for tag in tags:
            response += f"{tag} "
        return response
    
    # 创建笔记
    if "创建" in query or "保存" in query:
        title = "新笔记"
        content = generate_content("好物")
        post = create_post(title, content)
        return f"✅ 笔记已创建！\n\n{format_post(post)}"
    
    # 查看笔记列表
    if "笔记" in query and "列表" in query:
        data = load_posts()
        if not data["posts"]:
            return "📕 暂无笔记"
        
        response = "📕 **笔记列表**：\n\n"
        for p in data["posts"][-5:]:
            response += f"📝 {p['title']} ({p['created'][:10]})\n"
        
        return response
    
    # 默认回复
    return """📕 小红书助手

**功能**：
1. 标题生成 - "帮我想个标题"
2. 文案生成 - "写一篇好物分享"
3. 话题推荐 - "推荐话题标签"
4. 笔记管理 - "查看笔记列表"

**特色**：
- 爆款标题，吸引点击
- emoji 丰富，更生动
- 话题精准，流量高

告诉我你想写什么？👻"""


if __name__ == "__main__":
    import sys
    sys.stdout.reconfigure(encoding='utf-8')
    print(main("写一篇好物分享"))
