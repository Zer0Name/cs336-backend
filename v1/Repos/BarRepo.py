import v1.Repos.SQL as SQL


from v1.DTO.BarTopBeerBrandDTO import BarTopBeerBrandDTO

class BarRepo(SQL.SQL_table):
	
	def __init__(self):
		super(DrinkerRepo, self).__init__()

    
'''
SELECT manf, SUM(quantity) AS quantity
FROM Beer b RIGHT JOIN 
(SELECT t.item AS item, SUM(t.quantity) AS quantity
FROM (SELECT *
FROM Bills b
WHERE b.bar = "Armed Pudding Bar" and b.day = "Thursday") b, Transactions t
WHERE b.bill_id = t.bill_id AND type = "beer"
GROUP BY t.item) q ON q.item = b.name
GROUP BY manf
ORDER BY quantity DESC
LIMIT 10;

'''
    def getbarTopBeerBrand(self,bar,dayOfWeek):
		sql = "SELECT manf, SUM(quantity) AS quantity \
                FROM Beer b RIGHT JOIN \
                (SELECT t.item AS item, SUM(t.quantity) AS quantity\
                FROM (SELECT * \
                FROM Bills b \
                WHERE b.bar = \""+str(bar)+"\" and b.day = \""+str(dayOfWeek)+"\") b, Transactions t \
                WHERE b.bill_id = t.bill_id AND type = \""+str(beer)+"\" \
                GROUP BY t.item) q ON q.item = b.name \
                GROUP BY manf \
                ORDER BY quantity DESC \
                LIMIT 10;"
		items = self.query(sql)
		result = []
		for item in items:
			barTopBeerBrandDTO = BarTopBeerBrandDTO()
			barTopBeerBrandDTO.map(item)
			result.append(barTopBeerBrandDTO)
		self.close()
		return result

