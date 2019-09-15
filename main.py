from settings import KEY, SECRET
import numpy as np
from pandas import DataFrame
import krakenex


def select_pairs():
    pairs = ['XXBTZUSD', 'XETHZUSD', 'XETHXXBT', 'XDAOXXBT']
    print("pairs")
    for i, pair in enumerate(pairs):
        print(f"    {i}) {pair}")
    i = int(input("    selection: "))
    return pairs[i] 


def store_recent(pair):
    k = krakenex.API(KEY, SECRET)
    r = k.query_public('Trades', {'pair': pair})
    error = r.get('error')
    if error:
        raise RuntimeError(error)
    data = np.array(r['result'][pair])
    columns = ["Price", "Volume", "Time", "Buy/Sell", "Market/Limit", "Miscellaneous"]
    dataFrame = DataFrame(data, columns=columns)
    fileName = f"{pair}.csv"
    dataFrame.to_csv(fileName,index=False)
    print(f"{fileName} generated")


store_recent(select_pairs())
