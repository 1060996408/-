#!/usr/bin/env python3
"""
华为健康数据分析脚本
自动生成健康报告
"""

import json
import os
from glob import glob
from datetime import datetime, timedelta
from pathlib import Path

def load_health_data():
    """加载所有健康数据"""
    memory_dir = Path.home() / '.openclaw' / 'workspace' / 'memory'
    files = glob(str(memory_dir / 'health-*.json'))
    
    all_data = {
        'steps': [],
        'heart_rate': [],
        'sleep': [],
        'weight': []
    }
    
    for file in sorted(files):
        try:
            with open(file, 'r', encoding='utf-8') as f:
                data = json.load(f)
                health_data = data.get('data', {})
                
                all_data['steps'].extend(health_data.get('steps', []))
                all_data['heart_rate'].extend(health_data.get('heart_rate', []))
                all_data['sleep'].extend(health_data.get('sleep', []))
                all_data['weight'].extend(health_data.get('weight', []))
        except Exception as e:
            print(f"⚠️ 读取文件失败: {file} - {e}")
    
    return all_data

def analyze_steps(steps):
    """分析步数数据"""
    if not steps:
        return None
    
    total = sum(s['value'] for s in steps)
    avg = total / len(steps)
    max_steps = max(steps, key=lambda x: x['value'])
    min_steps = min(steps, key=lambda x: x['value'])
    
    # 达标天数 (>8000步)
    target_days = sum(1 for s in steps if s['value'] >= 8000)
    
    return {
        'total': total,
        'average': avg,
        'max': max_steps,
        'min': min_steps,
        'target_days': target_days,
        'target_rate': target_days / len(steps) * 100
    }

def analyze_heart_rate(heart_rates):
    """分析心率数据"""
    if not heart_rates:
        return None
    
    values = [hr['value'] for hr in heart_rates]
    avg = sum(values) / len(values)
    max_hr = max(values)
    min_hr = min(values)
    
    # 静息心率 (假设最低值)
    resting_hr = min_hr
    
    return {
        'average': avg,
        'max': max_hr,
        'min': min_hr,
        'resting': resting_hr,
        'count': len(values)
    }

def analyze_sleep(sleep_data):
    """分析睡眠数据"""
    if not sleep_data:
        return None
    
    # 解析睡眠时长 (假设格式: "7h 32m")
    total_minutes = 0
    for sleep in sleep_data:
        duration = sleep.get('duration', '0h 0m')
        try:
            parts = duration.replace('h', '').replace('m', '').split()
            hours = int(parts[0]) if len(parts) > 0 else 0
            minutes = int(parts[1]) if len(parts) > 1 else 0
            total_minutes += hours * 60 + minutes
        except:
            pass
    
    if total_minutes == 0:
        return None
    
    avg_hours = total_minutes / len(sleep_data) / 60
    
    # 睡眠质量统计
    quality_count = {}
    for sleep in sleep_data:
        quality = sleep.get('quality', '未知')
        quality_count[quality] = quality_count.get(quality, 0) + 1
    
    return {
        'average_hours': avg_hours,
        'total_nights': len(sleep_data),
        'quality_distribution': quality_count
    }

def analyze_weight(weight_data):
    """分析体重数据"""
    if not weight_data:
        return None
    
    values = [w['value'] for w in weight_data]
    latest = weight_data[-1] if weight_data else None
    earliest = weight_data[0] if weight_data else None
    
    change = latest['value'] - earliest['value'] if latest and earliest else 0
    
    return {
        'latest': latest,
        'earliest': earliest,
        'change': change,
        'average': sum(values) / len(values)
    }

def generate_report(data):
    """生成健康报告"""
    steps_analysis = analyze_steps(data['steps'])
    hr_analysis = analyze_heart_rate(data['heart_rate'])
    sleep_analysis = analyze_sleep(data['sleep'])
    weight_analysis = analyze_weight(data['weight'])
    
    report = []
    report.append("=" * 50)
    report.append("📊 健康数据分析报告")
    report.append(f"生成时间: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    report.append("=" * 50)
    report.append("")
    
    # 步数分析
    if steps_analysis:
        report.append("🚶 步数统计")
        report.append(f"  总步数: {steps_analysis['total']:,} 步")
        report.append(f"  日均步数: {steps_analysis['average']:.0f} 步")
        report.append(f"  最高记录: {steps_analysis['max']['value']:,} 步 ({steps_analysis['max']['date']})")
        report.append(f"  最低记录: {steps_analysis['min']['value']:,} 步 ({steps_analysis['min']['date']})")
        report.append(f"  达标天数: {steps_analysis['target_days']} 天 ({steps_analysis['target_rate']:.1f}%)")
        report.append("")
    
    # 心率分析
    if hr_analysis:
        report.append("❤️ 心率统计")
        report.append(f"  平均心率: {hr_analysis['average']:.1f} bpm")
        report.append(f"  静息心率: {hr_analysis['resting']} bpm")
        report.append(f"  最高心率: {hr_analysis['max']} bpm")
        report.append(f"  最低心率: {hr_analysis['min']} bpm")
        report.append(f"  测量次数: {hr_analysis['count']} 次")
        report.append("")
    
    # 睡眠分析
    if sleep_analysis:
        report.append("😴 睡眠统计")
        report.append(f"  平均睡眠: {sleep_analysis['average_hours']:.1f} 小时/天")
        report.append(f"  记录天数: {sleep_analysis['total_nights']} 天")
        report.append(f"  睡眠质量分布:")
        for quality, count in sleep_analysis['quality_distribution'].items():
            report.append(f"    {quality}: {count} 天")
        report.append("")
    
    # 体重分析
    if weight_analysis and weight_analysis['latest']:
        report.append("⚖️ 体重统计")
        report.append(f"  当前体重: {weight_analysis['latest']['value']} kg ({weight_analysis['latest']['date']})")
        if weight_analysis['earliest']:
            report.append(f"  初始体重: {weight_analysis['earliest']['value']} kg ({weight_analysis['earliest']['date']})")
            change = weight_analysis['change']
            change_str = f"+{change:.1f}" if change > 0 else f"{change:.1f}"
            report.append(f"  体重变化: {change_str} kg")
        report.append(f"  平均体重: {weight_analysis['average']:.1f} kg")
        report.append("")
    
    report.append("=" * 50)
    
    return "\n".join(report)

def save_report(report):
    """保存报告"""
    today = datetime.now().strftime("%Y-%m-%d")
    report_dir = Path.home() / '.openclaw' / 'workspace' / 'docs' / 'reports'
    report_dir.mkdir(parents=True, exist_ok=True)
    
    report_file = report_dir / f'health-report-{today}.txt'
    
    with open(report_file, 'w', encoding='utf-8') as f:
        f.write(report)
    
    return report_file

def main():
    print("📊 正在分析健康数据...")
    
    data = load_health_data()
    
    if not any([data['steps'], data['heart_rate'], data['sleep'], data['weight']]):
        print("❌ 没有找到健康数据")
        print("请先导入数据: python3 parse_huawei.py <数据文件>")
        return
    
    report = generate_report(data)
    print(report)
    
    report_file = save_report(report)
    print(f"\n✅ 报告已保存到: {report_file}")

if __name__ == '__main__':
    main()
