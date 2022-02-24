"""
https://syncwith.com/api/pancakeswap/get/api-v2-tokens-address
"""

import requests

ETH = "0x2170ed0880ac9a755fd29b2688956bd959f933f8"


def get_current_coin_value(contract):
    result = requests.get(
        f"https://api.pancakeswap.info/api/v2/tokens/{contract}")
    print(result.json())


get_current_coin_value(ETH)
