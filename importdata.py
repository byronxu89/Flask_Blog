import json
import sqlite3
from datetime import datetime

conn = sqlite3.connect('./flaskblog/site.db')
with open ('posts.json') as json_data:
	fewdata = json.load(json_data)
	cur = conn.cursor()
	timenow = datetime.now().strftime("%Y-%m-%d")
	sql = '''INSERT INTO post(title, date_posted, content, user_id ) VALUES (?,?,?,?)'''
	for i in fewdata:
		try:
			cur.execute(sql, (i['title'], timenow, i['content'], 1))
		except sqlite3.IntegrityError as e:
			print(e)
	conn.commit()
	conn.close()