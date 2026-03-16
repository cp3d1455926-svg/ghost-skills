#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
📧 Email Helper - 邮件助手
功能：邮件草稿、回复建议、邮件模板
"""

import json
from pathlib import Path
from datetime import datetime

DATA_DIR = Path(__file__).parent
TEMPLATES_FILE = DATA_DIR / "templates.json"

# 邮件模板库
EMAIL_TEMPLATES = {
    "请假": """
主题：请假申请 - {name} - {date}

尊敬的{leader}：

您好！

因{reason}，我需要在{start_date}至{end_date}期间请假{days}天。

请假期间的工作已安排如下：
1. {handover1}
2. {handover2}

如有紧急情况，可通过{contact}联系我。

恳请批准，谢谢！

此致
敬礼

{name}
{date}
""",
    
    "商务合作": """
主题：商务合作洽谈 - {company}

尊敬的{recipient}：

您好！

我是{company}的{position}{name}。我们专注于{business}...

希望能与贵方探讨合作机会...

期待您的回复！

祝好，
{name}
{company}
{contact}
""",
    
    "感谢": """
主题：感谢 - {topic}

尊敬的{recipient}：

您好！

非常感谢您{reason}...

您的帮助对我非常重要...

再次感谢！

祝好，
{name}
{date}
""",
    
    "求职": """
主题：应聘{position} - {name}

尊敬的招聘负责人：

您好！

我在{channel}看到贵公司正在招聘{position}...

我的优势：
1. {skill1}
2. {skill2}

期待有机会加入贵公司！

此致
敬礼

{name}
{contact}
"""
}


def generate_email(template_name, **kwargs):
    """生成邮件"""
    if template_name not in EMAIL_TEMPLATES:
        return None
    
    template = EMAIL_TEMPLATES[template_name]
    
    # 填充默认值
    defaults = {
        "name": "[你的名字]",
        "date": datetime.now().strftime("%Y-%m-%d"),
        "recipient": "[收件人]",
        "company": "[公司名]",
        "position": "[职位]",
        "contact": "[联系方式]"
    }
    
    defaults.update(kwargs)
    
    return template.format(**defaults)


def main(query):
    """主函数"""
    query = query.lower()
    
    # 请假邮件
    if "请假" in query:
        return generate_email("请假")
    
    # 商务邮件
    if "商务" in query or "合作" in query:
        return generate_email("商务合作")
    
    # 感谢邮件
    if "感谢" in query or "谢谢" in query:
        return generate_email("感谢")
    
    # 求职邮件
    if "求职" in query or "应聘" in query:
        return generate_email("求职")
    
    # 默认回复
    return """📧 邮件助手

**支持模板**：
1. 请假申请 - "帮我写请假邮件"
2. 商务合作 - "写合作邮件"
3. 感谢信 - "写感谢邮件"
4. 求职信 - "写求职邮件"

告诉我你需要写什么邮件？👻"""


if __name__ == "__main__":
    import sys
    sys.stdout.reconfigure(encoding='utf-8')
    print(main("帮我写请假邮件"))
