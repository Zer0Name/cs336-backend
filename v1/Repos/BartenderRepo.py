import v1.Repos.SQL as SQL
from v1.Entity.Bartender import Bartender
from v1.DTO.ShiftsDTO import ShiftsDTO
from v1.DTO.QuantityDTO import QuantityDTO

class BartenderRepo(SQL.SQL_table):
	
	def __init__(self):
		super(BartenderRepo, self).__init__()
	
	def getAllBartenders(self):
		sql = "Select * from Bartender"
		items = self.query(sql,Bartender)
		return items
	
	#need to add dates to shifts table and include here
	def getAllPastShifts(self,bartender,bar):
		sql = "SELECT day, start, end \
		FROM Shifts \
		WHERE bartender = \""+str(bartender)+"\" AND bar = \""+str(bar)+"\""
		items = self.query(sql,ShiftsDTO)
		return items
	
	def getNumberOfEachBeerBrandSold(self,bartender,bar):
		sql = "SELECT manf AS name, SUM(s.quantity) AS amount \
				FROM (SELECT b.bill_id AS bill_id, t.item AS item, t.quantity AS quantity \
				FROM (SELECT * \
				FROM Bills \
				WHERE bartender = \""+str(bartender)+"\" AND bar = \""+str(bar)+"\") b,Transactions t \
				WHERE b.bill_id = t.bill_id and type = \""+str("beer")+"\") s \
				JOIN Beer ON s.item = name \
				GROUP BY manf;"
		items = self.query(sql,QuantityDTO)
		return items
	
	def rankByNumberOfBeersSold(self, startTime, endTime, day, bar):
		sql = "SELECT b1.bartender AS name, SUM(t.quantity) AS amount \
				FROM (SELECT b.bartender, b.bill_id \
				FROM (SELECT bar, bartender, day \
				FROM Shifts \
				WHERE start <= \""+str(startTime)+"\" AND end >= \""+str(endTime)+"\") s, Bills b \
				WHERE s.bar = \""+str(bar)+"\" AND s.day = \""+str(day)+"\" \
				AND b.bartender = s.bartender AND b.day = s.day AND b.bar = s.bar \
				AND b.time >= \""+str(startTime)+"\" AND b.time <= \""+str(endTime)+"\") b1, \
				Transactions t \
				WHERE b1.bill_id = t.bill_id and t.type = \""+str("beer")+"\" \
				GROUP BY b1.bartender \
				ORDER BY amount DESC;"
		items = self.query(sql,QuantityDTO)
		return items