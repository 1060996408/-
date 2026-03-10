#!/usr/bin/env python3
"""
华为健康数据手动导出解析器
支持 CSV 和 JSON 格式
"""

import json
import csv
import os
from datetime import datetime
from pathlib import Path

def parse_huawei_csv(csv_file):
    """解析华为健康导出的 CSV 文件"""
    data = {
        'steps': [],
        'heart_rate': [],
        'sleep': [],
        'weight': []
    }
    
    with open(csv_file, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            # 根据数据类型分类
            data_type = row.get('类型', row.get('type', ''))
            
            if '步数' in data_type or 'step' in data_type.lower():
                data['steps'].append({
                    'date': row.get('日期', row.get('date', '')),
                    'value': int(row.get('数值', row.get('value', 0)))
                })
            
            elif '心率' in data_type or 'heart' in data_type.lower():
                data['heart_rate'].append({
                    'date': row.get('日期', row.get('date', '')),
                    'value': int(row.get('数值', row.get('value', 0)))
                })
            
            elif '睡眠' in data_type or 'sleep' in data_type.lower():
                data['sleep'].append({
                    'date': row.get('日期', row.get('date', '')),
                    'duration': row.get('时长', row.get('duration', '')),
                    'quality': row.get('质量', row.get('quality', ''))
                })
            
            elif '体重' in data_type or 'weight' in data_type.lower():
                data['weight'].append({
                    'date': row.get('日期', row.get('date', '')),
                    'value': float(row.get('数值', row.get('value', 0)))
                })
    
    return data

def parse_huawei_json(json_file):
    """解析华为健康导出的 JSON 文件"""
    with open(json_file, 'r', encoding='utf-8') as f:
        raw_data = json.load(f)
    
    # 根据实际 JSON 结构调整
    data = {
        'steps': raw_data.get('steps', []),
        'heart_rate': raw_data.get('heartRate', []),
        'sleep': raw_data.get('sleep', []),
        'weight': raw_data.get('weight', [])
    }
    
    return data

def save_to_memory(data, source='huawei-manual'):
    """保存到 OpenClaw memory"""
    today = datetime.now().strftime("%Y-%m-%d")
    memory_dir = Path.home() / '.openclaw' / 'workspace' / 'memory'
    memory_dir.mkdir(parents=True, exist_ok=True)
    
    memory_file = memory_dir / f'health-{today}.json'
    
    output = {
        'date': datetime.now().isoformat(),
        'source': source,
        'data': data
    }
    
    with open(memory_file, 'w', encoding='utf-8') as f:
        json.dump(output, f, indent=2, ensure_ascii=False)
    
    print(f"✅ 数据已保存到: {memory_file}")
    return memory_file

def main():
    import sys
    
    if len(sys.argv) < 2:
        print("用法: python3 parse_huawei.py <导出文件路径>")
        print("支持格式: CSV, JSON")
        sys.exit(1)
    
    file_path = sys.argv[1]
    
    if not os.path.exists(file_path):
        print(f"❌ 文件不存在: {file_path}")
        sys.exit(1)
    
    print(f"📂 正在解析: {file_path}")
    
    # 根据文件扩展名选择解析器
    if file_path.endswith('.csv'):
        data = parse_huawei_csv(file_path)
    elif file_path.endswith('.json'):
        data = parse_huawei_json(file_path)
    else:
        print("❌ 不支持的文件格式,请使用 CSV 或 JSON")
        sys.exit(1)
    
    # 统计
    print(f"\n📊 数据统计:")
    print(f"  步数记录: {len(data['steps'])} 条")
    print(f"  心率记录: {len(data['heart_rate'])} 条")
    print(f"  睡眠记录: {len(data['sleep'])} 条")
    print(f"  体重记录: {len(data['weight'])} 条")
    
    # 保存
    memory_file = save_to_memory(data)
    print(f"\n✅ 导入完成!")
    print(f"查看数据: cat {memory_file}")

if __name__ == '__main__':
    main()
