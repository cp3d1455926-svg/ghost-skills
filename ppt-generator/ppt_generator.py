#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
📊 PPT Generator - PPT 生成助手
功能：PPT 大纲生成、内容填充、配图建议
"""

import json
from pathlib import Path
from datetime import datetime

DATA_DIR = Path(__file__).parent
PRESENTATIONS_FILE = DATA_DIR / "presentations.json"

# PPT 模板库
PPT_TEMPLATES = {
    "产品介绍": [
        {"slide": 1, "title": "封面", "content": ["[产品名称]", "[Slogan]", "[日期]"]},
        {"slide": 2, "title": "目录", "content": ["产品概述", "核心功能", "技术优势", "应用场景", "客户案例", "价格方案"]},
        {"slide": 3, "title": "产品概述", "content": ["产品定位", "目标用户", "核心价值"]},
        {"slide": 4, "title": "核心功能", "content": ["功能 1", "功能 2", "功能 3"]},
        {"slide": 5, "title": "技术优势", "content": ["技术亮点 1", "技术亮点 2"]},
        {"slide": 6, "title": "应用场景", "content": ["场景 1", "场景 2", "场景 3"]},
        {"slide": 7, "title": "客户案例", "content": ["客户 A", "客户 B"]},
        {"slide": 8, "title": "价格方案", "content": ["基础版", "专业版", "企业版"]},
        {"slide": 9, "title": "谢谢", "content": ["Q&A", "[联系方式]"]}
    ],
    
    "项目汇报": [
        {"slide": 1, "title": "封面", "content": ["[项目名称]", "汇报人：[姓名]", "[日期]"]},
        {"slide": 2, "title": "项目背景", "content": ["项目目标", "项目范围"]},
        {"slide": 3, "title": "当前进度", "content": ["已完成", "进行中", "待开始"]},
        {"slide": 4, "title": "问题与挑战", "content": ["问题 1", "问题 2"]},
        {"slide": 5, "title": "下一步计划", "content": ["计划 1", "计划 2"]},
        {"slide": 6, "title": "需要支持", "content": ["资源需求", "人员需求"]}
    ],
    
    "培训课件": [
        {"slide": 1, "title": "封面", "content": ["[培训主题]", "讲师：[姓名]", "[日期]"]},
        {"slide": 2, "title": "目录", "content": ["课程目标", "课程内容", "实践练习", "总结"]},
        {"slide": 3, "title": "课程目标", "content": ["学习目标 1", "学习目标 2"]},
        {"slide": 4, "title": "课程内容", "content": ["知识点 1", "知识点 2", "知识点 3"]},
        {"slide": 5, "title": "实践练习", "content": ["练习 1", "练习 2"]},
        {"slide": 6, "title": "总结", "content": ["重点回顾", "Q&A"]}
    ]
}


def generate_outline(template_name):
    """生成 PPT 大纲"""
    if template_name not in PPT_TEMPLATES:
        return None
    return PPT_TEMPLATES[template_name]


def format_outline(outline, title):
    """格式化大纲输出"""
    response = f"📊 **PPT 大纲** - {title}\n"
    response += f"📄 建议页数：{len(outline)}页\n\n"
    
    for slide in outline:
        response += f"**Slide {slide['slide']}: {slide['title']}**\n"
        for content in slide['content']:
            response += f"- {content}\n"
        response += "\n"
    
    return response


def main(query):
    """主函数"""
    query = query.lower()
    
    # 产品介绍 PPT
    if "产品" in query and "ppt" in query:
        outline = generate_outline("产品介绍")
        return format_outline(outline, "产品介绍")
    
    # 项目汇报 PPT
    if "项目" in query or "汇报" in query:
        outline = generate_outline("项目汇报")
        return format_outline(outline, "项目汇报")
    
    # 培训 PPT
    if "培训" in query or "课件" in query:
        outline = generate_outline("培训课件")
        return format_outline(outline, "培训课件")
    
    # 默认回复
    return """📊 PPT 生成助手

**支持模板**：
1. 产品介绍 - "生成产品介绍 PPT"
2. 项目汇报 - "项目汇报 PPT"
3. 培训课件 - "培训 PPT"

告诉我你需要什么类型的 PPT？👻"""


if __name__ == "__main__":
    import sys
    sys.stdout.reconfigure(encoding='utf-8')
    print(main("生成产品介绍 PPT"))
