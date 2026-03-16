#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
🎯 Habit Tracker - 习惯养成助手
功能：习惯打卡、统计分析、提醒督促
"""

import json
from pathlib import Path
from datetime import datetime

DATA_DIR = Path(__file__).parent
HABITS_FILE = DATA_DIR / "habits.json"


def load_habits():
    """加载习惯数据"""
    if HABITS_FILE.exists():
        with open(HABITS_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return {"habits": []}


def save_habits(data):
    """保存习惯数据"""
    with open(HABITS_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


def create_habit(name, reminder_time="21:00"):
    """创建习惯"""
    habits = load_habits()
    
    habit = {
        "name": name,
        "created_date": datetime.now().strftime("%Y-%m-%d"),
        "reminder_time": reminder_time,
        "streak": 0,
        "checkins": []
    }
    
    habits["habits"].append(habit)
    save_habits(habits)
    
    return habit


def checkin(habit_name):
    """打卡"""
    habits = load_habits()
    
    for habit in habits["habits"]:
        if habit_name in habit["name"]:
            today = datetime.now().strftime("%Y-%m-%d")
            
            # 检查是否已打卡
            if today in habit["checkins"]:
                return {"error": "今天已经打卡过了~"}
            
            habit["checkins"].append(today)
            habit["streak"] += 1
            
            save_habits(habits)
            
            return {
                "success": True,
                "name": habit["name"],
                "streak": habit["streak"],
                "total": len(habit["checkins"])
            }
    
    return {"error": "未找到该习惯"}


def get_stats():
    """获取统计"""
    habits = load_habits()
    
    stats = []
    for habit in habits["habits"]:
        stats.append({
            "name": habit["name"],
            "streak": habit["streak"],
            "total": len(habit["checkins"])
        })
    
    return stats


def main(query):
    """主函数"""
    query = query.lower()
    
    # 创建习惯
    if "创建" in query or "开始" in query:
        if "读书" in query:
            habit = create_habit("每天读书")
            return f"✅ 习惯已创建：{habit['name']}\n⏰ 提醒时间：{habit['reminder_time']}\n\n回复\"打卡读书\"开始打卡！"
        elif "运动" in query:
            habit = create_habit("每天运动")
            return f"✅ 习惯已创建：{habit['name']}\n⏰ 提醒时间：{habit['reminder_time']}"
    
    # 打卡
    if "打卡" in query:
        if "读书" in query:
            result = checkin("读书")
            if result.get("error"):
                return f"❌ {result['error']}"
            return f"""✅ 打卡成功！

📚 每天读书
🔥 连续打卡：{result['streak']}天
📊 总打卡：{result['total']}次

💪 加油！坚持就是胜利！"""
    
    # 统计
    if "统计" in query or "查看" in query:
        stats = get_stats()
        if not stats:
            return "📊 暂无习惯数据，先创建一个习惯吧~"
        
        response = "📊 **习惯统计**\n\n"
        for s in stats:
            response += f"📚 {s['name']}\n"
            response += f"   🔥 连续：{s['streak']}天\n"
            response += f"   📊 总计：{s['total']}次\n\n"
        
        return response
    
    # 默认回复
    return """🎯 习惯养成助手

**功能**：
1. 创建习惯 - "我想养成读书的习惯"
2. 每日打卡 - "打卡读书"
3. 查看统计 - "查看习惯统计"

**示例习惯**：
- 每天读书
- 每天运动
- 早睡早起

告诉我你想养成什么习惯？👻"""


if __name__ == "__main__":
    import sys
    sys.stdout.reconfigure(encoding='utf-8')
    print(main("查看习惯统计"))
