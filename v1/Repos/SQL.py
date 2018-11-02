import mysql.connector


class SQL_table(object):
	def __init__(self):
		self.mydb = self.getConnection()
		self.cursor = self.mydb.cursor()

		
	def close(self):
		self.cursor.close()
		self.mydb.close()

	
	def getConnection(self):
		mydb = mysql.connector.connect(
		host="project336.cuyc1x8g0d0t.us-east-1.rds.amazonaws.com",
		user="student",
		passwd="Database123",
		database="project336"
		)
		return mydb


	def query(self,sql_query):
		self.cursor.execute(sql_query)
		myresult = self.cursor.fetchall()
		result = []
		columns = tuple( [d[0].decode('utf8') for d in self.cursor.description] )
		for row in myresult:
			result.append(dict(zip(columns, row)))
		return result

		

