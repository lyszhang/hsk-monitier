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

def get_ethereum_block_height2(target_date_begin_datetime, target_date_end_datetime):
    """
    直接通过接口查询指定日期或月份的起始日期

    :param target_date: 目标日期，格式为"YYYY-MM-DD"
    :return: 目标日期起始区块高度和结束区块高度
    """
    blockscout_url = "https://coins.llama.fi/block/ethereum/"

    # target_date_begin_datetime = datetime.datetime.strptime(target_date, "%Y-%m-%d")
    # target_date_end_datetime = datetime.datetime.strptime(end_date, "%Y-%m-%d")
    #target_date_end_datetime = (target_date_begin_datetime + datetime.timedelta(days=1))
    target_date_begin = int((target_date_begin_datetime-datetime.timedelta(hours=8)).timestamp())
    target_date_end = int((target_date_end_datetime-datetime.timedelta(hours=8)).timestamp())

    response_date_begin = requests.get(blockscout_url+str(target_date_begin))
    response_date_end = requests.get(blockscout_url+str(target_date_end))

    if response_date_begin.status_code == 200 & response_date_end.status_code == 200:
        start_block_height = response_date_begin.json().get("height", "0x0")
        end_block_height = response_date_end.json().get("height", "0x0")
        return start_block_height, end_block_height
    else:
        raise Exception(f"RPC request failed with status code {response_date_begin.status_code}: {response_date_begin.text}")

def get_account_fee_in_ethereum_daily(api_base, target_date, end_date, sender_address, receiver_address):
    """
    获取指定日期对应账户的以太坊交易费支出。

    :param api_url: API接口地址
    :param target_date: 目标日期，格式为"YYYY-MM-DD"
    :return: 交易数量
    """
    api_url = api_base
    start_height, end_height = get_ethereum_block_height2(target_date, end_date)
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
                # print(tx.get("hash"))
                # print(tx_fee_in_ether)

                # 获取交易的详细信息（transaction receipt）
                txhash = tx.get("hash")
                receipt_params = {
                    "chainid": 1,
                    "module": "proxy",
                    "action": "eth_getTransactionReceipt",
                    "txhash": txhash,
                    "apikey": "EPVRT2D6HAHUFM5H2IHXGSYZT377B7866N"
                }
                receipt_response = requests.get(api_url, params=receipt_params)

                 # 检查交易收据的响应状态码
                if receipt_response.status_code != 200:
                    raise Exception(f"get_account_fee_in_ethereum_daily Failed to get receipt for tx {txhash}. Status code: {receipt_response.status_code}")

                receipt_data = receipt_response.json().get("result")
                blob_fee = 0
                # 如果 receipt_data 中有 blobGasPrice 和 blobGasUsed，计算 blob_fee
                if "blobGasPrice" in receipt_data and "blobGasUsed" in receipt_data:
                    blob_fee = int(receipt_data.get("blobGasPrice"), 16) * int(receipt_data.get("blobGasUsed"), 16) / 1e18

                tx_fee_total = tx_fee_in_ether + blob_fee
                print(f"tx Hash: {txhash}, tx fee total:{tx_fee_total}")

                fee_total = fee_total + tx_fee_total

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

if __name__ == "__main__":
    target_date = "2024-12-19"  
    print(get_ethereum_block_height(target_date))
    print(get_ethereum_block_height2(target_date))