"""9 月 16 日练习：Python 基础与网络设备状态统计。

练习顺序：
1. 先直接运行本文件，确认可以打印四台设备。
2. 完成 count_online。
3. 完成 calculate_average_latency。
4. 完成 get_alerts。
5. 取消 main 中相应代码的注释，逐项验证。

今天先追求正确、易读，不需要追求一行代码解决问题。
"""


devices = [
    {"name": "router-01", "online": True, "latency_ms": 25},
    {"name": "switch-01", "online": True, "latency_ms": 83},
    {"name": "server-01", "online": False, "latency_ms": None},
    {"name": "gateway-01", "online": True, "latency_ms": 135},
]


def show_devices(device_list):
    """打印每台设备的名称和状态。这个函数已经完成，先读懂它。"""
    for device in device_list:
        if device["online"]:
            status = "在线"
        else:
            status = "离线"

        print(device["name"], status)


def count_online(device_list):
    """返回在线设备数量。"""
    count = 0

    # TODO 1：遍历 device_list。
    # TODO 2：如果设备的 online 为 True，就让 count 增加 1。

    for device in device_list:
        if device["online"]:
            count = count+1

    return count


def calculate_average_latency(device_list):
    """返回在线设备的平均延迟；没有有效数据时返回 None。"""
    total = 0
    count = 0

    # TODO 1：遍历所有设备。
    # TODO 2：只统计在线且 latency_ms 不是 None 的设备。
    # TODO 3：把延迟累加到 total，并让 count 增加 1。
    # TODO 4：count 为 0 时返回 None，否则返回 total / count。

    for device in device_list:
        if device["online"] and device["latency_ms"] is not None:
            total = total + device["latency_ms"]
            count = count + 1
    if count == 0:
        return None
    
    return total / count



def get_alerts(device_list):
    """返回所有告警文字组成的列表。"""
    alerts = []
    
    # 告警规则：
    # 1. 设备离线：添加“设备名：设备离线”。
    # 2. 设备在线，但延迟超过 100 ms：添加“设备名：延迟过高”。
    # 提示：使用 alerts.append("告警内容") 添加一条告警。
    for device in device_list:
        if not device["online"]:
            alerts.append(f'{device["name"]}：设备离线')

        elif device["latency_ms"] is not None and device["latency_ms"] > 100:
            alerts.append(f'{device["name"]}:延迟过高')


    return alerts


def main():
    print("===== 第一关：设备列表 =====")
    show_devices(devices)

    # 完成 count_online 后，取消下面两行开头的 #。
    online_count = count_online(devices)
    print("在线设备数量：", online_count)

    # 完成 calculate_average_latency 后，取消下面三行开头的 #。
    average = calculate_average_latency(devices)
    print("在线设备平均延迟：", round(average, 1), "ms")

    # 完成 get_alerts 后，取消下面三行开头的 #。
    print("告警信息：")
    for alert in get_alerts(devices):
        print("-", alert)


if __name__ == "__main__":
    main()
