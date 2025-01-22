import requests
import datetime
from api import *
from fee import get_fee_income_info

def get_accounts_info_daily(api_base, target_date):
    """
    获取指定日期的账户信息。

    :param api_url: API接口地址
    :param target_date: 目标日期，格式为"YYYY-MM-DD"
    :return: 账户总数、今日活跃账户数、新增账户数
    """
    total = get_number_of_accounts_daily(api_base, target_date)
    activeAccounts = get_active_accounts_daily(api_base, target_date)
    newAccounts = get_new_accounts_daily(api_base, target_date)

    print(f"账户情况:")
    print(f"  链上账户总数 {total}")
    print(f"  今日活跃账户数 {activeAccounts}")
    print(f"  今日新增账户数 {newAccounts}")

    return total, activeAccounts, newAccounts

def get_tx_info_daily(api_base, etherscan_url, gate_url, target_date):
    """
    获取指定日期的交易信息。

    :param api_url: API接口地址
    :param target_date: 目标日期，格式为"YYYY-MM-DD"
    :return: 今日交易数、交易成功率、总收入-HSK、以太坊交易费用-eth、净收益
    """
    txs_daily = get_number_of_txs_daily(api_base, target_date) - 43200
    txs_success_rate = get_txs_success_rate_daily(api_base, target_date)

    # 每日统计
    target_date_begin_datetime = datetime.datetime.strptime(target_date, "%Y-%m-%d")
    target_date_end_datetime = (target_date_begin_datetime + datetime.timedelta(days=1))
    fee_income = get_fee_income_info(target_date_begin_datetime,target_date_end_datetime)

    # dispute
    dispute_game_sender = "0x66b8F8425ecB610239e79E3517feFddCf85Af41a"
    dispute_game_factory = "0x04Ec030f362CE5A0b5Fe2d4B4219f287C2EBDE50"
    # batch
    batch_sender = "0x9391791f7CB74F8BFDA65edc0749efd964311b55"
    batch = "0x0004cb44C80b6Fbf8ceb1d80AF688C9f7C0b2aB5"
    dispute_fee = get_account_fee_in_ethereum_daily(etherscan_url, target_date_begin_datetime, target_date_end_datetime, dispute_game_sender, dispute_game_factory)
    batcher_fee = get_account_fee_in_ethereum_daily(etherscan_url, target_date_begin_datetime, target_date_end_datetime, batch_sender, batch)
    l1_fee_total = dispute_fee + batcher_fee

    # price 
    eth_price, hsk_price = get_eth_and_hsk_price(gate_url)
    profit = fee_income* hsk_price - l1_fee_total * eth_price

    print(f"交易情况:")
    print(f"  今日交易数 {txs_daily}")
    print(f"  交易成功率 {float(txs_success_rate):.2%}")
    print(f"  总交易费用(收入) {fee_income}")
    print(f"  以太坊交易费(支出) {l1_fee_total} ETH, dispute Game fee: {dispute_fee} ETH, batcher fee: {batcher_fee} ETH")
    print(f"  今日币价   ETH: {eth_price} USD, HSK: {hsk_price} USD")
    print(f"  净收益: {profit} USD")

    return

def get_contract_info_daily(api_base, target_date):
    """
    获取指定日期的合约信息。

    :param api_url: API接口地址
    :param target_date: 目标日期，格式为"YYYY-MM-DD"
    :return: 总合约数、新增合约数
    """
    total = get_number_of_contracts_daily(api_base, target_date)
    newContracts = get_new_contracts_daily(api_base, target_date)

    print(f"合约:")
    print(f"  总合约数 {total}")
    print(f"  今日新增合约数 {newContracts}")
    return total, newContracts

