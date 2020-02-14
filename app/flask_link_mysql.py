# coding: utf-8
from sqlalchemy import create_engine, Table, Column, Integer, String, MetaData, DateTime, ForeignKey
import datetime

# 建立引擎連接資料庫
#create_engine("資料庫類型+資料庫驅動://資料庫用戶名:資料庫密碼@IP:資料庫名稱"，其他參數)
#使用pysql驅動
engine = create_engine('mysql+pymysql://root:465x225x490mm@localhost:3306/flask_user', encoding='utf8', echo=True)

print(engine)

#建立元資料
metadata = MetaData(engine)


#Table()方法用来建立table，第一參數:table名，第二參數元資料，後面使用Column()設定資料庫中每一column參數。
user = Table('user', metadata,
                Column('id', Integer, primary_key=True),
                Column('username', String(80), unique=True, nullable=False),
                Column('password', String(80), nullable=False),
                Column('email', String(120), unique=True, nullable=False),
                Column('avatar_img', String(120), nullable=False)
            )

post = Table('post', metadata,
                Column('id', Integer, primary_key=True),
                Column('body', String(500), nullable=False),
                Column('timestamp', DateTime, default=datetime.datetime.utcnow()),
                Column('user_id', ForeignKey('user.id'), nullable=False)
              )

# 建立資料表，如果資料表存在，則忽視
metadata.create_all(engine)