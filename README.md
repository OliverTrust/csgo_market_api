## Python CS:GO Market API (market.csgo.com)

A simple python module for interacting with various parts of market.csgo.com

Documentation: https://market.csgo.com/docs-v2

### Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install

```bash
python -m pip install csgo_market_api
```
Or you can install from source with:
```bash
python -m pip install git+https://github.com/OliverTrust/csgo_market_api.git
```
### Usage

Get Balance
```python
from csgo_market_api import CSGOMarket

market = CSGOMarket(api_key='')
balance = market.get_money()
print(balance)  
# {'money': 980, 'currency': 'RUB', 'success': True}
```

Sale item
```python
from csgo_market_api import CSGOMarket

market = CSGOMarket(api_key='')
# price (1 USD=1000, 1 RUB=100, 1 EUR=1000)
res = market.add_to_sale(item_id=136285662, price=10000, currency='RUB')
print(res)
# {"success": True, "item_id": 136285662 }
```

Get items info
```python
from csgo_market_api import CSGOMarket

market = CSGOMarket(api_key='')
list_hash_name = ['2020 RMR Challengers']
item_info = market.get_list_items_info(list_hash_name=list_hash_name)
print(item_info)
# {'success': True, 'currency': 'RUB', 'data': {'2020 RMR Challengers': {'max': 19, 'min': 13, 'average': 15.962, 'history': [[1620673328, 14], [1620673323, 14], [1620673318, 14], [1620673309, 14], [1620673305, 14], [1620673301, 14], [1620673208, 16.99], [1620673146, 14], [1620673145, 14], [1620672997, 16.99], [1620672969, 16.99], [1620672950, 16.99], [1620672948, 16.99], [1620672946, 16.99], [1620672945, 16.99], [1620672944, 16.99], [1620672941, 16.99], [1620672939, 16.99], [1620672938, 16.99], [1620672933, 16.99], [1620672932, 16.99], [1620672930, 16.99], [1620672926, 16.99], [1620672851, 16.99], [1620672786, 16.99], [1620672729, 16.99], [1620672719, 16.99], [1620672701, 16.99], [1620672694, 16.99], [1620672688, 16.99], [1620672678, 16.99], [1620672659, 16.99], [1620672528, 16.99], [1620672272, 16.99], [1620672131, 16], [1620671822, 15.9], [1620671604, 18.9], [1620671352, 19], [1620671300, 17.57], [1620671144, 14], [1620671141, 14], [1620670857, 13], [1620670031, 14], [1620670028, 14], [1620670027, 14], [1620670026, 14], [1620670024, 14], [1620670022, 14], [1620669809, 16], [1620669793, 16]]}}}
```
More info here https://market.csgo.com/docs-v2
