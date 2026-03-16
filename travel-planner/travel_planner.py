#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
✈️ Travel Planner - 旅行规划助手
功能：行程规划、景点推荐、预算估算
"""

import json
from pathlib import Path
from datetime import datetime

DATA_DIR = Path(__file__).parent
TRIPS_FILE = DATA_DIR / "trips.json"

# 示例景点数据库
DESTINATIONS = {
    "北京": {
        "attractions": [
            {"name": "故宫", "time": "4 小时", "price": 60, "area": "东城"},
            {"name": "天安门广场", "time": "2 小时", "price": 0, "area": "东城"},
            {"name": "颐和园", "time": "4 小时", "price": 30, "area": "海淀"},
            {"name": "八达岭长城", "time": "6 小时", "price": 40, "area": "延庆"},
            {"name": "天坛", "time": "3 小时", "price": 15, "area": "东城"},
        ],
        "food_cost": 150,
        "hotel_cost": 300
    },
    "上海": {
        "attractions": [
            {"name": "外滩", "time": "2 小时", "price": 0, "area": "黄浦"},
            {"name": "东方明珠", "time": "3 小时", "price": 220, "area": "浦东"},
            {"name": "迪士尼", "time": "8 小时", "price": 400, "area": "浦东"},
            {"name": "豫园", "time": "2 小时", "price": 40, "area": "黄浦"},
        ],
        "food_cost": 200,
        "hotel_cost": 400
    },
    "杭州": {
        "attractions": [
            {"name": "西湖", "time": "4 小时", "price": 0, "area": "西湖"},
            {"name": "灵隐寺", "time": "3 小时", "price": 75, "area": "西湖"},
            {"name": "千岛湖", "time": "6 小时", "price": 180, "area": "淳安"},
        ],
        "food_cost": 120,
        "hotel_cost": 250
    }
}


def plan_itinerary(destination, days):
    """规划行程"""
    if destination not in DESTINATIONS:
        return f"抱歉，暂时没有{destination}的旅游攻略~"
    
    dest_info = DESTINATIONS[destination]
    attractions = dest_info["attractions"]
    
    itinerary = []
    for day in range(1, days + 1):
        day_plan = {
            "day": day,
            "attractions": attractions[(day-1)*2:(day-1)*2+2] if (day-1)*2 < len(attractions) else []
        }
        itinerary.append(day_plan)
    
    return itinerary


def estimate_budget(destination, days):
    """估算预算"""
    if destination not in DESTINATIONS:
        return None
    
    dest_info = DESTINATIONS[destination]
    
    food = dest_info["food_cost"] * days
    hotel = dest_info["hotel_cost"] * (days - 1)
    tickets = sum([a["price"] for a in dest_info["attractions"][:days*2]])
    transport = 200  # 市内交通估算
    
    total = food + hotel + tickets + transport
    
    return {
        "food": food,
        "hotel": hotel,
        "tickets": tickets,
        "transport": transport,
        "total": total
    }


def format_itinerary(itinerary, destination, budget):
    """格式化行程输出"""
    response = f"✈️ **{destination} {len(itinerary)}日游**\n\n"
    
    for day_plan in itinerary:
        response += f"📅 **Day {day_plan['day']}**\n"
        if day_plan['attractions']:
            for attr in day_plan['attractions']:
                response += f"- {attr['name']} ({attr['time']}, ¥{attr['price']})\n"
        else:
            response += "- 自由活动时间\n"
        response += "\n"
    
    if budget:
        response += "💰 **预算估算**（人均）\n"
        response += f"- 餐饮：¥{budget['food']}\n"
        response += f"- 住宿：¥{budget['hotel']}\n"
        response += f"- 门票：¥{budget['tickets']}\n"
        response += f"- 交通：¥{budget['transport']}\n"
        response += f"- **总计：¥{budget['total']}**\n"
    
    return response


def main(query):
    """主函数"""
    query = query.lower()
    
    # 检测目的地
    for dest in DESTINATIONS.keys():
        if dest in query:
            # 检测天数
            import re
            days_match = re.search(r'(\d+) 天', query)
            days = int(days_match.group(1)) if days_match else 3
            
            itinerary = plan_itinerary(dest, days)
            budget = estimate_budget(dest, days)
            
            return format_itinerary(itinerary, dest, budget)
    
    # 默认回复
    return """✈️ 旅行规划助手

**功能**：
1. 行程规划 - "帮我规划 3 天的北京旅行"
2. 预算估算 - "去上海玩 5 天要多少钱"
3. 景点推荐 - "杭州有哪些好玩的"

**支持目的地**：北京、上海、杭州

告诉我你想去哪里玩？👻"""


if __name__ == "__main__":
    import sys
    sys.stdout.reconfigure(encoding='utf-8')
    print(main("帮我规划 3 天的北京旅行"))
