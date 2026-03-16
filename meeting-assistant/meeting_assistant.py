#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
📋 Meeting Assistant - 会议助手
功能：会议纪要、待办事项、日程安排
"""

import json
from pathlib import Path
from datetime import datetime

DATA_DIR = Path(__file__).parent
MEETINGS_FILE = DATA_DIR / "meetings.json"


def load_meetings():
    """加载会议记录"""
    if MEETINGS_FILE.exists():
        with open(MEETINGS_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return {"meetings": []}


def save_meetings(data):
    """保存会议记录"""
    with open(MEETINGS_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


def generate_minutes(title, attendees, notes):
    """生成会议纪要"""
    meeting = {
        "title": title,
        "date": datetime.now().strftime("%Y-%m-%d %H:%M"),
        "attendees": attendees,
        "notes": notes,
        "action_items": []
    }
    
    meetings = load_meetings()
    meetings["meetings"].append(meeting)
    save_meetings(meetings)
    
    return meeting


def extract_action_items(text):
    """提取待办事项"""
    # 简单实现：查找包含"待办"、"需要"、"负责"的句子
    action_items = []
    lines = text.split('\n')
    
    for line in lines:
        if any(kw in line for kw in ['待办', '需要', '负责', '完成', '截止']):
            action_items.append(line.strip())
    
    return action_items


def format_meeting(meeting):
    """格式化会议输出"""
    response = f"📋 **会议纪要** - {meeting['title']}\n"
    response += f"📅 {meeting['date']}\n"
    response += f"👥 参会：{', '.join(meeting['attendees'])}\n\n"
    
    response += "📝 **讨论要点**\n"
    response += meeting['notes'] + "\n\n"
    
    if meeting.get('action_items'):
        response += "✅ **待办事项**\n"
        for item in meeting['action_items']:
            response += f"- [ ] {item}\n"
    
    return response


def main(query):
    """主函数"""
    query = query.strip()
    
    if "纪要" in query or "会议" in query:
        # 简单实现：返回模板
        return """📋 会议纪要模板

**会议主题：** [填写]
**会议时间：** [填写]
**参会人员：** [填写]

**讨论要点：**
1. [要点 1]
2. [要点 2]

**待办事项：**
- [ ] [任务 1] - [负责人] - [截止日期]
- [ ] [任务 2] - [负责人] - [截止日期]

**下次会议：** [填写]

把会议内容发给我，我帮你整理！👻"""
    
    # 默认回复
    return """📋 会议助手

**功能**：
1. 会议纪要 - "整理会议纪要"
2. 待办提取 - "提取待办事项"
3. 日程安排 - "安排下周会议"

发送会议内容，我帮你整理！👻"""


if __name__ == "__main__":
    import sys
    sys.stdout.reconfigure(encoding='utf-8')
    print(main("整理会议纪要"))
