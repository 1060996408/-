from googleapiclient.discovery import build
from datetime import datetime, timedelta
import pickle
import json
import os

def get_fitness_service():
    with open('token.pickle', 'rb') as token:
        creds = pickle.load(token)
    return build('fitness', 'v1', credentials=creds)

def get_steps(service, days=7):
    end_time = int(datetime.now().timestamp() * 1000000000)
    start_time = int((datetime.now() - timedelta(days=days)).timestamp() * 1000000000)
    dataset = f"{start_time}-{end_time}"
    
    try:
        response = service.users().dataSources().datasets().get(
            userId='me',
            dataSourceId='derived:com.google.step_count.delta:com.google.android.gms:estimated_steps',
            datasetId=dataset
        ).execute()
        
        steps = []
        for point in response.get('point', []):
            steps.append({
                'date': datetime.fromtimestamp(int(point['startTimeNanos']) / 1000000000).isoformat(),
                'value': point['value'][0]['intVal']
            })
        return steps
    except Exception as e:
        print(f"获取步数失败: {e}")
        return []

def get_heart_rate(service, days=7):
    end_time = int(datetime.now().timestamp() * 1000000000)
    start_time = int((datetime.now() - timedelta(days=days)).timestamp() * 1000000000)
    dataset = f"{start_time}-{end_time}"
    
    try:
        response = service.users().dataSources().datasets().get(
            userId='me',
            dataSourceId='derived:com.google.heart_rate.bpm:com.google.android.gms:merge_heart_rate_bpm',
            datasetId=dataset
        ).execute()
        
        heart_rate = []
        for point in response.get('point', []):
            heart_rate.append({
                'date': datetime.fromtimestamp(int(point['startTimeNanos']) / 1000000000).isoformat(),
                'value': round(point['value'][0]['fpVal'], 1)
            })
        return heart_rate
    except Exception as e:
        print(f"获取心率失败: {e}")
        return []

def save_to_memory(data):
    today = datetime.now().strftime("%Y-%m-%d")
    memory_file = os.path.expanduser(f"~/.openclaw/workspace/memory/health-{today}.json")
    
    with open(memory_file, 'w') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    
    print(f"✅ 数据已保存到 {memory_file}")

if __name__ == '__main__':
    service = get_fitness_service()
    
    print("正在获取健康数据...")
    data = {
        'date': datetime.now().isoformat(),
        'source': 'google-fit',
        'steps': get_steps(service),
        'heart_rate': get_heart_rate(service)
    }
    
    save_to_memory(data)
    print(f"\n📊 数据统计:")
    print(f"  步数记录: {len(data['steps'])} 条")
    print(f"  心率记录: {len(data['heart_rate'])} 条")
