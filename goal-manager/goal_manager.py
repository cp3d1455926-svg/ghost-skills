#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
🎯 Goal Manager - 目标管理助手
功能：目标设定、进度跟踪、复盘总结
"""

import json
from pathlib import Path
from datetime import datetime

DATA_DIR = Path(__file__).parent
GOALS_FILE = DATA_DIR / "goals.json"


def load_goals():
    """加载目标数据"""
    if GOALS_FILE.exists():
        with open(GOALS_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return {"yearly_goals": [], "monthly_goals": [], "reviews": []}


def save_goals(data):
    """保存目标数据"""
    with open(GOALS_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


def set_yearly_goals():
    """设定年度目标"""
    goals = {
        "year": 2026,
        "objectives": [
            {
                "title": "职业发展",
                "key_results": [
                    {"desc": "完成 3 个重要项目", "progress": 0},
                    {"desc": "学习 2 项新技能", "progress": 0},
                    {"desc": "晋升到高级工程师", "progress": 0}
                ]
            },
            {
                "title": "健康生活",
                "key_results": [
                    {"desc": "每周运动 3 次", "progress": 0},
                    {"desc": "体重控制在 70kg", "progress": 0},
                    {"desc": "每天睡眠 7 小时", "progress": 0}
                ]
            },
            {
                "title": "个人成长",
                "key_results": [
                    {"desc": "阅读 24 本书", "progress": 0},
                    {"desc": "学习一门新语言", "progress": 0},
                    {"desc": "旅行 3 个城市", "progress": 0}
                ]
            }
        ]
    }
    
    data = load_goals()
    data["yearly_goals"].append(goals)
    save_goals(data)
    
    return goals


def format_goals(goals):
    """格式化目标输出"""
    response = f"🎯 **{goals['year']}年度目标**\n\n"
    
    for obj in goals["objectives"]:
        response += f"**O: {obj['title']}**\n"
        for i, kr in enumerate(obj["key_results"], 1):
            progress_bar = "█" * int(kr["progress"] / 10) + "░" * (10 - int(kr["progress"] / 10))
            response += f"- KR{i}: {kr['desc']} [{progress_bar}] {kr['progress']}%\n"
        response += "\n"
    
    return response


def review_template():
    """复盘模板"""
    return """📋 **月度复盘报告**

✅ **完成的目标**
- [ ] [目标 1]
- [ ] [目标 2]

⏳ **进行中的目标**
- [ ] [目标 3] (50%)
- [ ] [目标 4] (30%)

❌ **未完成的目标**
- [ ] [目标 5]

💡 **改进建议**
- [建议 1]
- [建议 2]

🎯 **下月目标**
- [目标 1]
- [目标 2]"""


def main(query):
    """主函数"""
    query = query.lower()
    
    # 设定目标
    if "设定" in query or "目标" in query:
        goals = set_yearly_goals()
        return format_goals(goals)
    
    # 复盘
    if "复盘" in query or "总结" in query:
        return review_template()
    
    # 默认回复
    return """🎯 目标管理助手

**功能**：
1. 目标设定 - "帮我设定 2026 年的目标"
2. 进度跟踪 - "更新目标进度"
3. 复盘总结 - "做月度复盘"

**OKR 框架**：
- O (Objective): 目标
- KR (Key Results): 关键结果

告诉我你想设定什么目标？👻"""


if __name__ == "__main__":
    import sys
    sys.stdout.reconfigure(encoding='utf-8')
    print(main("帮我设定 2026 年的目标"))
