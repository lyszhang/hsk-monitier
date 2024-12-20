import requests
import datetime

def get_hsk_block_height(target_date):
    """
    根据起始区块高度和日期计算目标日期的区块高度。

    :param start_block: 起始区块高度（如0xCB41）
    :param interval_blocks: 每天的区块间隔数量
    :param target_date: 目标日期，格式为"YYYY-MM-DD"
    :return: 目标日期起始区块高度和结束区块高度
    """
    start_block = "0xCB41"  # 2024-12-18 00:00 的区块高度
    interval_blocks = 0xA8C0  # 每天的区块间隔
    base_date = datetime.datetime(2024, 12, 18)
    target_datetime = datetime.datetime.strptime(target_date, "%Y-%m-%d")

    # 计算相差的天数
    days_diff = (target_datetime - base_date).days

    # 计算区块高度
    start_block_height = int(start_block, 16) + days_diff * interval_blocks
    end_block_height = start_block_height + interval_blocks - 1

    return hex(start_block_height), hex(end_block_height)

def get_balance(rpc_url, address, block_height):
    """
    查询指定地址在指定区块高度的余额。

    :param rpc_url: RPC接口地址
    :param address: 查询的地址
    :param block_height: 区块高度（十六进制）
    :return: 余额（十进制，单位为HSK）
    """
    payload = {
        "method": "eth_getBalance",
        "params": [address, block_height],
        "id": 1,
        "jsonrpc": "2.0"
    }
    response = requests.post(rpc_url, json=payload)

    if response.status_code == 200:
        hex_balance = response.json().get("result", "0x0")
        # 转为十进制并除以 10^18
        return int(hex_balance, 16) / 10**18
    else:
        raise Exception(f"RPC request failed with status code {response.status_code}: {response.text}")

def get_fee_income_info(target_date):
    rpc_url = "https://mainnet.hsk.xyz"
    # rpc_url = "https://hashkeychain-mainnet.alt.technology"

    addresses = [
        "0x4200000000000000000000000000000000000011",
        "0x4200000000000000000000000000000000000019",
        "0x420000000000000000000000000000000000001a",
    ]

    try:
        # 获取费用数据
        start_height, end_height = get_hsk_block_height(target_date)

        print(f"*****日期 {target_date} 的区块高度范围: {start_height} - {end_height}")

        total_income = 0
        for address in addresses:
            start_balance = get_balance(rpc_url, address, start_height)
            end_balance = get_balance(rpc_url, address, end_height)

            print(f"*****地址 {address}:")
            print(f"  *****起始余额 (区块 {start_height}): {start_balance} HSK")
            print(f"  *****结束余额 (区块 {end_height}): {end_balance} HSK")

            total_income = total_income + (end_balance - start_balance)
        return total_income

    except Exception as e:
        print(f"查询过程中出错: {e}")