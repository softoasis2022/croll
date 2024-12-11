import psutil
import platform

from datetime import datetime

# 현재 시간 가져오기
current_time = datetime.now()

# 포맷에 맞춰 출력
formatted_time = current_time.strftime("%Y-%m-%d %H:%M:%S")

def check_system_status():
    # OS 정보 확인
    os_info = platform.uname()
    print("\n[시스템 정보]")
    print(f"시스템: {os_info.system}")
    print(f"노드 이름: {os_info.node}")
    print(f"버전: {os_info.version}")
    print(f"머신: {os_info.machine}")
    print(f"프로세서: {os_info.processor}")

    # CPU 사용률 확인
    cpu_usage = psutil.cpu_percent(interval=1)
    print(f"\n[CPU 상태]")
    print(f"CPU 사용률: {cpu_usage}%")

    # 메모리 사용량 확인
    memory = psutil.virtual_memory()
    print(f"\n[메모리 상태]")
    print(f"전체 메모리: {round(memory.total / (1024**3), 2)} GB")
    print(f"사용 중 메모리: {round(memory.used / (1024**3), 2)} GB")
    print(f"메모리 사용률: {memory.percent}%")

    # 디스크 사용량 확인
    disk = psutil.disk_usage('/')
    print(f"\n[디스크 상태]")
    print(f"디스크 전체 용량: {round(disk.total / (1024**3), 2)} GB")
    print(f"디스크 사용 중: {round(disk.used / (1024**3), 2)} GB")
    print(f"디스크 사용률: {disk.percent}%")