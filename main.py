import requests
import datetime
from fee import get_fee_income_info
from batch import get_accounts_info_daily, get_contract_info_daily, get_tx_info_daily

def main():
    blockscout_url = "https://explorer.hsk.xyz/api/v1/lines"
    etherscan_url = "https://api.etherscan.io/v2/api"
    gateio_market_url = "https://api.gateio.ws/api/v4"

    # 替换为预定义日期，避免使用 input
    # 使用昨天的日期作为目标日期
    # print("HashKey Chain日常活动扫描")
    # target_date = (datetime.datetime.now() - datetime.timedelta(days=1)).strftime("%Y-%m-%d")
    # # target_date = "2024-12-21"  # 示例日期
    # print("扫描日期:",target_date)

    # # work, work
    # get_accounts_info_daily(blockscout_url, target_date)
    # get_tx_info_daily(blockscout_url, etherscan_url, gateio_market_url, target_date)
    # get_contract_info_daily(blockscout_url, target_date)

    # 设置起始日期和结束日期
    start_date = datetime.datetime(2024, 12, 16)
    end_date = datetime.datetime(2025, 1, 22)

    # 初始化当前日期
    current_date = start_date

    # 循环打印日期，直到结束日期
    while current_date <= end_date:
        current_date_str = current_date.strftime("%Y-%m-%d")
        get_tx_info_daily(blockscout_url, etherscan_url, gateio_market_url, current_date_str)
        current_date += datetime.timedelta(days=1)

if __name__ == "__main__":
    main()
