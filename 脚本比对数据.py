# coding = utf-8
import pymysql
import mysql.connector as msq
import psycopg2
import pandas as pd
import sqlalchemy

# lep_report
c = pymysql.connect(host='10.0.7.21',
                    user='lepower',
                    password='Lepower123',
                    database='lep_report',
                    port=3306)
b = c.cursor()
sql = """select * from erp_day_settle_stockout where sku = 'QPCNY0004CPD-BUEU' """
b.execute(sql)
d = b.fetchall()

sql2 = """select ware_code from erp_day_settle_stockout where sku_name = 'HDMI切换器' and sku = 'QPCNY0004CPD-BUEU'"""
b.execute(sql2)
d2 = b.fetchall()
print(d2)
da = pd.read_sql(sql, c)
print(da)

# c = pymysql.connect(host='10.0.7.21',
#                     user='lepower',
#                     password='Lepower123',
#                     database='lep_report',
#                     port=3306)
# b = c.cursor()
# sql = """select * from erp_day_settle_stockout where sku = 'QPCNY0004CPD-BUEU' """
# b.execute(sql)
# d2 = b.fetchall()
# da = pd.read_sql(sql, con=b)
#
# print(da)