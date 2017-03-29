import sqlite3

# items.dbとつなぐ（なければ作られる）
conn = sqlite3.connect('items.db')
c = conn.cursor()

# テーブルの作成
c.execute("create table items(id, name)")

# 3行追加
c.execute("insert into items values(1, 'りんご')")
c.execute("insert into items values(2, 'ぱなま')")
c.execute("insert into items values(3, 'すいか')")

# 確定
conn.commit()

# clone ばいばい
conn.close()
