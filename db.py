# -*- coding:utf-8 -*-
import MySQLdb
OperationalError = MySQLdb.OperationalError
class MySQL:
    def __init__(self):
        try:
            self.conn=MySQLdb.connect(host='127.0.0.1',port=3306,user='root',passwd='',db='xieebaike')
            self.conn.autocommit(False)
            self.conn.set_character_set(charset="utf8")
            self.cur=self.conn.cursor()
        except MySQLdb.Error as e:
            print("Mysql Error %d: %s" % (e.args[0], e.args[1]))

    def __del__(self):
        print '关闭数据库连接'
        self.close()

    def query(self,sql):
        try:
            n=self.cur.execute(sql)
            return n
        except MySQLdb.Error as e:
            print("Mysql Error:%s\nSQL:%s" %(e,sql))

    def fetchRow(self):
        result = self.cur.fetchone()
        return result

    def fetchAll(self):
        result=self.cur.fetchall()
        desc =self.cur.description
        d = []
        for inv in result:
            _d = {}
            for i in range(0,len(inv)):
                _d[desc[i][0]] = str(inv[i])
                d.append(_d)
        return d

    def insert(self,table_name,data):
        columns=data.keys()
        _prefix="".join(['INSERT INTO `',table_name,'`'])
        _fields=",".join(["".join(['`',column,'`']) for column in columns])
        _values=",".join(["%s" for i in range(len(columns))])
        _sql="".join([_prefix,"(",_fields,") VALUES (",_values,")"])
        _params=[data[key] for key in columns]
        return self.cur.execute(_sql,tuple(_params))

    def update(self,tbname,data,condition):
        _fields=[]
        _prefix="".join(['UPDATE `',tbname,'`','SET'])
        for key in data.keys():
            _fields.append("%s = %s" % (key,data[key]))
        _sql="".join([_prefix ,_fields, "WHERE", condition ])

        return self.cur.execute(_sql)

    def delete(self,tbname,condition):
        _prefix="".join(['DELETE FROM  `',tbname,'`','WHERE'])
        _sql="".join([_prefix,condition])
        return self.cur.execute(_sql)

    def getLastInsertId(self):
        return self.cur.lastrowid

    def rowcount(self):
        return self.cur.rowcount

    def commit(self):
        self.conn.commit()

    def rollback(self):
        self.conn.rollback()

    def close(self):
        self.cur.close()
        self.conn.close()
