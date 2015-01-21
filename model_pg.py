# -*- coding: utf-8 -*-
__author__ = 'kvw'

import serial, psycopg2
import psycopg2.extensions
psycopg2.extensions.register_type(psycopg2.extensions.UNICODE)
psycopg2.extensions.register_type(psycopg2.extensions.UNICODEARRAY)

db = psycopg2.connect("host='10.10.10.142' dbname='all-pentar-upp' user='user' password='user00'")
db.set_client_encoding('UTF8')

def get_serial_numbers(serial):
    cursor = db.cursor()
    cursor.execute("""
        select sn._Fld27955 as SerialNum,
	p._Fld2918 as Code,
	p._Description as Name
    from _InfoRg27953 sn join _Reference162 p on
	p._IDRRef = sn._Fld27954RRef where sn._Fld27955=%s
    """, (serial,))
    rs = []
    for row in cursor:
        rs.append(serial.SerialNum(row['Code'].decode("utf-8"), row['Name'].decode("utf-8"), row['SerialNum'].decode("utf-8")))
    db.close()
    return rs