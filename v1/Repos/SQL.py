import mysql.connector

from v1.Exceptions.Error import Error

class SQL_table(object):
	def __init__(self):
		self.mydb = self.getConnection()
		self.cursor = self.mydb.cursor()

		
	def close(self):
		self.cursor.close()
		self.mydb.close()

	
	def getConnection(self):
		mydb = mysql.connector.connect(
		# host="pro-336.cuyc1x8g0d0t.us-east-1.rds.amazonaws.com",
		host="testing-server.cuyc1x8g0d0t.us-east-1.rds.amazonaws.com",
		user="student",
		passwd="Database123",
		database = "project336",
		connection_timeout = 10000
		)
		return mydb


	def query(self,sql_query,Obj):
		try:
			self.cursor.execute(sql_query)
			myresult = self.cursor.fetchall()
		except mysql.connector.Error as err:
			self.close()
			raise Error(err.msg)
		result = []
		columns = tuple( [d[0].decode('utf8') for d in self.cursor.description] )
		for row in myresult:
			result.append(dict(zip(columns, row)))
		final_results = []
		for item in result:
			obj = Obj()
			obj.map(item)
			final_results.append(obj)
		self.close()
		return final_results

	def insert(self,sql,vals):
		try:
			self.cursor.execute(sql,vals)
		except mysql.connector.Error as err:
			self.close()
			raise Error(err.msg)
		self.mydb.commit()
		self.close()
		return "Success"


	def update(self,sql,vals):
		try:
			self.cursor.execute(sql,vals)
		except mysql.connector.Error as err:
			self.close()
			raise Error(err.msg)
		self.mydb.commit()
		self.close()
		return "Success"


	def delete(self,sql,vals):
		try:
			self.cursor.execute(sql,vals)
		except mysql.connector.Error as err:
			self.close()
			raise Error(err.msg)
		self.mydb.commit()
		self.close()
		return "Success"

	def insertWithoutClose(self,sql,vals):
		try:
			self.cursor.execute(sql,vals)
		except mysql.connector.Error as err:
			self.close()
			raise Error(err.msg)
		self.mydb.commit()
		return "Success"
		

