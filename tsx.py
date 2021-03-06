# Python3
import requests,sqlite3

def get_info(quote):
    try:
        x = requests.get("https://web.tmxmoney.com/quote.php?qm_symbol=%s&local=EN" % (quote)).content
        companyname = str(x.split(b'<div class="quote-name">')[1].split(b'<h2>')[1].split(b'</h2>')[0].decode())
        price = float(x.split(b'<div class="quote-price priceLarge">')[1].split(b'</span>')[0].split(b'<span>')[1])
        prevclose = float(x.split(b'<td class="">Prev. Close:</td>')[1].split(b'<td class="">')[1].split(b'</td>')[0])
        openprice = float(x.split(b'<td class="">Open:</td>')[1].split(b'<td class="">')[1].split(b'</td>')[0])
        changejuan = x.split(b'<div class="quote-change')[1].split(b'</div>')[0].split(b'<br />')[1].split(b'\t\t\t\t\t\t\t\t\t\t\t\t\t\t')[1].split(b'\r\n\t\t\t\t\t\t\t')
        changeval = float(changejuan[0])
        changeperc = changejuan[1].strip(b'\r\n').decode()
        daylow = x.split(b'<strong>Day Low</strong>')[1].split(b'</div>')[0].split(b'\r\n\t\t\t')[1].split(b'\t\t\t')[0].decode()
        dayhigh = x.split(b'<strong>Day High</strong>')[1].split(b'</div>')[0].split(b'\r\n\t\t\t')[1].split(b'\t\t\t')[0].decode()
        week52low = float(x.split(b'<div class="lowHighBar" title="52 Week Low:')[1].split(b'\n')[0].split(b'<br>')[0])
        week52high = float(x.split(b'<div class="lowHighBar" title="52 Week Low:')[1].split(b'\n')[0].split(b'52 Week High: ')[1].split(b' ')[0])

        frmtReturn = {
            quote.upper():{
                "companyName":str(companyname),
                "lastPrice":float(price),
                "prevClose":float(prevclose),
                "openPrice":float(openprice),
                "Change24Hr":str(str(changeval)+' '+changeperc),
                "DayHigh":float(dayhigh),
                "DayLow":float(daylow),
                "YrHigh":float(week52high),
                "YrLow":float(week52low)
                }
            }
        return(frmtReturn)
    except:
        return("Invalid Quote")
