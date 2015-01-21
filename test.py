# -*- coding: utf-8 -*-

import pymssql

db = pymssql.connect(host='sql-srv.pentar.ru', user='WebUser', password='WebUser', database='Products')

cur = db.cursor()
#cur.execute("""select sn.ID as SerialID, p.Code, p.Name, sn.SerialNum from dbo.SerialNum sn join
#		Product p on p.ID = sn.ProductID
#		where sn.SerialNum = %s order by p.Code""", 'WD14107099')
cur.execute("select * from SerialNum where SerialNum=%s", 'WD14107099')
print cur.fetchall()
#for row in cur:
#	print row
db.close()
