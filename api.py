import requests
import datetime

def get_number_of_accounts_daily(api_base, target_date):
    """
    获取指定日期的账户总数。

    :param api_url: API接口地址
    :param target_date: 目标日期，格式为"YYYY-MM-DD"
    :return: 账户总数
    """
    api_url = api_base + "/accountsGrowth"
    params = {
        "from": target_date,
        "to": target_date,
        "resolution": "DAY"
    }
    response = requests.get(api_url, params=params)

    if response.status_code == 200:
        data = response.json()
        return int(data.get("chart", [{}])[0].get("value", 0))
    else:
        raise Exception(f"API request failed with status code {response.status_code}: {response.text}")

def get_active_accounts_daily(api_base, target_date):
    """
    获取指定日期活跃账户数。

    :param api_url: API接口地址
    :param target_date: 目标日期，格式为"YYYY-MM-DD"
    :return: 活跃账户数量
    """
    api_url = api_base + "/activeAccounts"
    params = {
        "from": target_date,
        "to": target_date,
        "resolution": "DAY"
    }
    response = requests.get(api_url, params=params)

    if response.status_code == 200:
        data = response.json()
        return int(data.get("chart", [{}])[0].get("value", 0))
    else:
        raise Exception(f"API request failed with status code {response.status_code}: {response.text}")

def get_new_accounts_daily(api_base, target_date):
    """
    获取指定日期新增的账户数量。

    :param api_url: API接口地址
    :param target_date: 目标日期，格式为"YYYY-MM-DD"
    :return: 新增账户数量
    """
    api_url = api_base + "/newAccounts"
    params = {
        "from": target_date,
        "to": target_date,
        "resolution": "DAY"
    }
    response = requests.get(api_url, params=params)

    if response.status_code == 200:
        data = response.json()
        return int(data.get("chart", [{}])[0].get("value", 0))
    else:
        raise Exception(f"API request failed with status code {response.status_code}: {response.text}")

def get_number_of_contracts_daily(api_base, target_date):
    """
    获取指定日期的合约数。

    :param api_url: API接口地址
    :param target_date: 目标日期，格式为"YYYY-MM-DD"
    :return: 合约数量
    """
    api_url = api_base + "/contractsGrowth"
    params = {
        "from": target_date,
        "to": target_date,
        "resolution": "DAY"
    }
    response = requests.get(api_url, params=params)

    if response.status_code == 200:
        data = response.json()
        return int(data.get("chart", [{}])[0].get("value", 0))
    else:
        raise Exception(f"API request failed with status code {response.status_code}: {response.text}")

def get_new_contracts_daily(api_base, target_date):
    """
    获取指定日期新增的合约数。

    :param api_url: API接口地址
    :param target_date: 目标日期，格式为"YYYY-MM-DD"
    :return: 新增合约数量
    """
    api_url = api_base + "/newContracts"
    params = {
        "from": target_date,
        "to": target_date,
        "resolution": "DAY"
    }
    response = requests.get(api_url, params=params)

    if response.status_code == 200:
        data = response.json()
        return int(data.get("chart", [{}])[0].get("value", 0))
    else:
        raise Exception(f"API request failed with status code {response.status_code}: {response.text}")

def get_number_of_txs_daily(api_base, target_date):
    """
    获取指定日期的交易数。

    :param api_url: API接口地址
    :param target_date: 目标日期，格式为"YYYY-MM-DD"
    :return: 交易数量
    """
    api_url = api_base + "/newTxns"
    params = {
        "from": target_date,
        "to": target_date,
        "resolution": "DAY"
    }
    response = requests.get(api_url, params=params)

    if response.status_code == 200:
        data = response.json()
        return int(data.get("chart", [{}])[0].get("value", 0))
    else:
        raise Exception(f"API request failed with status code {response.status_code}: {response.text}")

def get_txs_success_rate_daily(api_base, target_date):
    """
    获取指定日期的交易成功率。

    :param api_url: API接口地址
    :param target_date: 目标日期，格式为"YYYY-MM-DD"
    :return: 交易数量
    """
    api_url = api_base + "/txnsSuccessRate"
    params = {
        "from": target_date,
        "to": target_date,
        "resolution": "DAY"
    }
    response = requests.get(api_url, params=params)

    if response.status_code == 200:
        data = response.json()
        return data.get("chart", [{}])[0].get("value", 0)
    else:
        raise Exception(f"API request failed with status code {response.status_code}: {response.text}")

def get_ethereum_block_height(target_date):
    """
    根据起始区块高度和日期计算目标日期的区块高度。

    :param target_date: 目标日期，格式为"YYYY-MM-DD"
    :return: 目标日期起始区块高度和结束区块高度
    """
    start_block = "0x146E4CE"  # 2024-12-18 00:00 的区块高度
    interval_blocks = 0x1BF4  # 每天的区块间隔
    base_date = datetime.datetime(2024, 12, 18)
    target_datetime = datetime.datetime.strptime(target_date, "%Y-%m-%d")

    # 计算相差的天数
    days_diff = (target_datetime - base_date).days

    # 计算区块高度
    start_block_height = int(start_block, 16) + days_diff * interval_blocks
    end_block_height = start_block_height + interval_blocks - 1

    return start_block_height, end_block_height

def get_account_fee_in_ethereum_daily(api_base, target_date, sender_address, receiver_address):
    """
    获取指定日期对应账户的以太坊交易费支出。

    :param api_url: API接口地址
    :param target_date: 目标日期，格式为"YYYY-MM-DD"
    :return: 交易数量
    """
    api_url = api_base
    start_height, end_height = get_ethereum_block_height(target_date)
    params = {
        "chainid": 1,
        "module": "account",
        "action": "txlist",
        "address": sender_address,
        "startblock": start_height,
        "endblock": end_height,
        "sort": "asc",
        "apikey": "EPVRT2D6HAHUFM5H2IHXGSYZT377B7866N"
    }
    response = requests.get(api_url, params=params)

    if response.status_code == 200:
        txlist = response.json().get("result")
        fee_total = 0
        for tx in txlist:
            if tx.get("to").lower() == receiver_address.lower():
                tx_fee_in_ether = int(tx.get("gasPrice"))*int(tx.get("gasUsed"))/1e18
                fee_total = fee_total + tx_fee_in_ether 
                # print(tx.get("hash"))
                # print(tx_fee_in_ether)
            
        return fee_total
    else:
        raise Exception(f"API request failed with status code {response.status_code}: {response.text}")

def get_spot_price(api_url, currency_pair): 
    """
    获取指定交易对最近的价格。

    :param api_base: API接口地址
    :return: 交易对最近的价格
    """
    params = {
        "currency_pair": currency_pair,
        "limit": 1
    }
    response = requests.get(api_url, params=params)

    if response.status_code == 200:
        data = response.json()
        return float(data[0].get("price"))
    else:
        raise Exception(f"API request failed with status code {response.status_code}: {response.text}")

def get_eth_and_hsk_price(api_base):
    """
    获取ETH、HSK最近的价格。

    :param api_base: API接口地址
    :return: ETH、HSK最近的价格
    """
    api_url = api_base + "/spot/trades"
    
    eth_price = get_spot_price(api_url, "ETH_USDT")
    hsk_price = get_spot_price(api_url, "HSK_USDT")
    return eth_price, hsk_price