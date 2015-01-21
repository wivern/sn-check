import web, pymssql, serial

# db = web.database(dbn='mssql', host='sql-srv.pentar.ru', db='products', user='WebUser', pw='WebUser')
db = pymssql.connect(host='sql-srv.pentar.ru', user='WebUser', password='WebUser', database='Products',
                     charset='cp1251', as_dict=True)


def get_serial_numbers(serial):
    #	return db.query("""select sn.ID as serialID, p.Code as code, p.Name as name, sn.SerialNum as serialNum from dbo.SerialNum sn join
    #		Product p on p.ID = sn.ProductID
    #		where sn.SerialNum = $sn""", vars={'sn':serial})
    cur = db.cursor()
    cur.execute("""select sn.ID as SerialID, p.Code, p.Name, sn.SerialNum from dbo.SerialNum sn join
		Product p on p.ID = sn.ProductID
		where sn.SerialNum = '%s' order by p.Code""" % (serial,))
    rs = []
    for row in cur:
        rs.append(serial.SerialNum(row['Code'], row['Name'], row['SerialNum']))
    db.close()
    return rs