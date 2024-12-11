import psutil
import socket

from datetime import datetime

# 현재 시간 가져오기
current_time = datetime.now()

# 포맷에 맞춰 출력
formatted_time = current_time.strftime("%Y-%m-%d %H:%M:%S")


def check_network_status():
    # 네트워크 인터페이스 상태 확인
    net_status = psutil.net_if_stats()
    active_interfaces = [iface for iface, stats in net_status.items() if stats.isup]
    
    if active_interfaces:
        print("인터넷 연결 상태: 연결됨")
        print(f"활성화된 네트워크 인터페이스: {', '.join(active_interfaces)}")
        get_local_ip()
    else:
        get_local_ip()
        print("인터넷 연결 상태: 연결되지 않음")

def get_local_ip():
    try:
        # 로컬 머신의 IP 주소 확인
        host_name = socket.gethostname()
        local_ip = socket.gethostbyname(host_name)
        return f"로컬 IP 주소: {local_ip}"
    except socket.error as e:
        return f"IP 주소를 가져오는 중 오류 발생: {e}"

check_network_status()
