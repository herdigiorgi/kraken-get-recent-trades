# Kraken get-recent-trades

This script generates a CSV like this:

```csv
Price,Volume,Time,Buy/Sell,Market/Limit,Miscellaneous
10328.40000,0.00663860,1568563492.5675,b,m,
10327.80000,0.01668070,1568563521.4269,b,m,
10328.00000,0.00998403,1568563521.4357,b,m,
10328.00000,0.00001594,1568563521.4379,b,m,
10328.00000,0.00000003,1568563521.44,b,m,
10328.60000,1.97331930,1568563521.4428,b,m,
...
```

What you need to run this script is to create a `.env` file in the same directory with the API's key and secret. The `.env` file should look very similar to this:

```
KEY=Lr8KIIPGcZFaYsYtBeaoQoKyJ8XqP1WC
SECRET=cdPo8ODiBlGber2oWVuzmSKHz0m4fPGQp8sxf68gXP1WSwCREJRl7AaFZmcwwLRD
```

Then to execute the script simply:
```
$ pipenv install
$ python main.py
```

You need [`pipev`](https://github.com/pypa/pipenv) and python 3 installed for this script to work.