import v1.Repos.SQL as SQL
from v1.DTO.TrueFalseDTO import TrueFalseDTO



class PatternRepo(SQL.SQL_table):
	
	def __init__(self):
		super(PatternRepo, self).__init__()
	
	def pattern_1(self):
		sql = "SELECT NOT EXISTS (SELECT * FROM Bills b \
				WHERE NOT EXISTS (SELECT *  \
				FROM Operates o \
				WHERE b.bar = o.bar AND b.date = o.date AND (o.start <= b.time AND o.end >= b.time))\
				GROUP BY b.date \
				ORDER BY b.date) AS value"
		items = self.query(sql,TrueFalseDTO)
		if int(items[0].value) == 1:
			return True
		return False


	def pattern_2(self):
		sql = "SELECT NOT EXISTS \
				(SELECT *  \
				FROM Frequents f, Bar b, Drinker d \
				WHERE d.name = f.drinker AND f.bar = b.name AND b.state <> d.state) \
				AS value;"
		items = self.query(sql,TrueFalseDTO)
		if int(items[0].value) == 1:
			return True
		return False

	def pattern_3(self):
		sql = "SELECT NOT EXISTS (SELECT *\
				FROM\
				(SELECT s1.beername AS beer1, s1.barname AS bar, s1.price AS price1,\
				s2.beername AS beer2, s2.price AS price2\
				FROM SellsBeer s1, SellsBeer s2\
				WHERE s1.beername <> s2.beername AND s1.barname = s2.barname) s, \
				(SELECT s3.beername AS beer3, s3.barname AS bar, s3.price AS price3,\
				s4.beername AS beer4, s4.price AS price4\
				FROM SellsBeer s3, SellsBeer s4\
				WHERE s3.beername <> s4.beername AND s3.barname = s4.barname) s5\
				WHERE s.bar <> s5.bar AND s.beer1 = s5.beer3 AND s.beer2 = s5.beer4\
				AND ((s.price1 <= s.price2 AND s5.price3 > s5.price4) OR\
				(s.price1 >= s.price2 AND s5.price3 < s5.price4))) AS value;"
		items = self.query(sql,TrueFalseDTO)
		if int(items[0].value) == 1:
			return True
		return False

	def pattern_4(self):
		sql = "SELECT NOT EXISTS (SELECT * FROM (SELECT SUM(t.quantity) AS quantity_in_transactions, (b1.startquantity - b1.endquantity) AS num_sold \
		FROM (SELECT b.bill_id AS bill_id, i.beer AS beer, b.bar AS bar, b.date AS date, i.startquantity AS startquantity, i.endquantity AS endquantity \
		FROM Inventory i, Bills b WHERE i.bar = b.bar AND i.date = b.date) b1, Transactions t WHERE t.type = \""+ str("beer")+ "\" AND b1.bill_id = t.bill_id AND t.item = b1.beer \
		GROUP BY b1.beer, b1.bar, b1.date) c WHERE c.num_sold < c.quantity_in_transactions) AS value;"
		items = self.query(sql,TrueFalseDTO)
		if int(items[0].value) == 1:
			return True
		return False

	def pattern_5(self):
		sql = "SELECT NOT EXISTS( \
			SELECT COUNT(*) AS number_of_shifts_a_day\
			FROM Shifts s\
			GROUP BY s.bartender, s.date\
			HAVING number_of_shifts_a_day <> 1) AS value;"
		items = self.query(sql,TrueFalseDTO)
		if int(items[0].value) == 1:
			return True
		return False