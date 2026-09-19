"""9 月 17 日练习：读取 JSON 文件并生成设备报告。

练习顺序：
1. 完成 load_devices，读取并解析 devices.json。
2. 完成 validate_device，检查必要字段和数据类型。
3. 完成 build_report，生成统计结果。
4. 在 main 中添加异常处理和当前时间。

先完成第一关，不要一次性填写全部 TODO。
"""

from __future__ import annotations

import json
from datetime import datetime
from pathlib import Path
from typing import Any


DATA_FILE = Path(__file__).with_name("devices.json")


def load_devices(path: Path) -> list[dict[str, Any]]:
    """读取 JSON 文件，返回设备字典组成的列表。"""
    # TODO 第一关：
    # 1. 使用 path.open 打开文件，模式是 "r"，编码是 "utf-8"。
    # 2. 使用 json.load 读取已经打开的文件。
    # 3. 返回读取结果。
    return []


def validate_device(device: dict[str, Any]) -> bool:
    """检查一条设备记录是否包含今天需要的字段。"""
    required_fields = {"name", "ip", "online", "latency_ms"}

    # TODO 第二关：判断 required_fields 是否都存在于 device 中。
    return False


def build_report(device_list: list[dict[str, Any]]) -> dict[str, Any]:
    """根据合法设备记录生成汇总报告。"""
    # TODO 第三关：生成 total、online、offline 和 slow_devices。
    return {}


def main() -> None:
    print("===== JSON 设备报告 =====")

    # 第一关完成后，这里应该读取到 4 台设备。
    devices = load_devices(DATA_FILE)
    print("读取文件：", DATA_FILE.name)
    print("设备数量：", len(devices))

    # TODO 第四关：
    # 1. 使用 try/except 处理文件不存在和 JSON 格式错误。
    # 2. 调用 validate_device 和 build_report。
    # 3. 使用 datetime.now() 输出报告生成时间。


if __name__ == "__main__":
    main()
