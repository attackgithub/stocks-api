import requests

def get_info(quote):
    x = requests.get("https://web.tmxmoney.com/quote.php?qm_symbol=%s&local=EN" % (quote)).text
    price = float(x.split('<div class="quote-price priceLarge">')[1].split('</span>')[0].split('<span>')[1])
    prevclose = float(x.split('<td class="">Prev. Close:</td>')[1].split('<td class="">')[1].split('</td>')[0])
    changejuan = x.split('<div class="quote-change')[1].split('</div>')[0].split('<br />')[1].split('\t\t\t\t\t\t\t\t\t\t\t\t\t\t')[1].split('\r\n\t\t\t\t\t\t\t')
    changeval = float(changejuan[0])
    changeperc = changejuan[1].encode().strip('\r\n')
    daylow = x.split('<strong>Day Low</strong>')[1].split('</div>')[0].encode().split('\r\n\t\t\t')[1].split('\t\t\t')[0]
    dayhigh = x.split('<strong>Day High</strong>')[1].split('</div>')[0].encode().split('\r\n\t\t\t')[1].split('\t\t\t')[0]
    week52low = float(x.split('<div class="lowHighBar" title="52 Week Low:')[1].split('\n')[0].split('<br>')[0])
    week52high = float(x.split('<div class="lowHighBar" title="52 Week Low:')[1].split('\n')[0].split('52 Week High: ')[1].split(' ')[0])
    return(daylow, dayhigh, price, prevclose, changeval, changeperc, week52low, week52high)
