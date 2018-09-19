import os, csv, sqlite3

with open('mig_report.csv', 'r') as csvfile:
    exchange = []
    fullname = []
    ticker = []
    sector = []

    readCSV = csv.reader(csvfile)
    for row in readCSV:
        exrow = row[0]
        namerow = row[1]
        tickerow = row[2]
        sectorow = row[6]

        db = sqlite3.connect('quotes.db')
        dbcursor = db.cursor()
        insertvar = [tickerow,namerow,sectorow,exrow]
        dbcursor.execute('INSERT INTO tsx VALUES (?,?,?,?)', insertvar)
        db.commit()

        exchange.append(exrow)
        fullname.append(namerow)
        ticker.append(tickerow)
        sector.append(sectorow)

print(fullname)
print(len(ticker))
'''
db = sqlite3.connect('quotes.db')
dbcursor = db.cursor()
insertvar = [ticker,fullname,sector,exchange]
dbcursor.execute('INSERT INTO tsx VALUES (?,?,?,?)', insertvar)
db.commit()
'''
