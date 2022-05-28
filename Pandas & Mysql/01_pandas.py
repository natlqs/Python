import pandas as pd
url = 'http://vip.stock.finance.sina.com.cn/q/go.php/vInvestConsult/kind/dzjy/index.phtml'
table = pd.read_html(url)[0]
print(table)