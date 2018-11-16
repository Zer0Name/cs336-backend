Drinker:

baseurl/v1/modification/drinker/insert
baseurl/v1/modification/drinker/update
baseurl/v1/modification/drinker/delete

{
	"name"  :  "",
	"phone" :  "",
	"state" :   "",
    "old_name" : ""
}

BarFood:

baseurl/v1/modification/barFood/insert
baseurl/v1/modification/barFood/update
baseurl/v1/modification/barFood/delete

{
	"name"  :  "",
    "old_name" : ""
}

Bar:

baseurl/v1/modification/bar/insert
baseurl/v1/modification/bar/update
baseurl/v1/modification/bar/delete

{
	"name"  :  "",
	"state" :   "",
    "old_name" : ""
}

Bartender:

baseurl/v1/modification/bartender/insert
baseurl/v1/modification/bartender/update
baseurl/v1/modification/bartender/delete

{
	"name"  :  "",
	"phone" :  "",
	"state" :   "",
    "old_name" : ""
}

Beer:

baseurl/v1/modification/beer/insert
baseurl/v1/modification/beer/update
baseurl/v1/modification/beer/delete

{
	"name"  :  "",
	"manf" :  "",
    "old_name" : ""
}

Bills:

baseurl/v1/modification/bills/insert
baseurl/v1/modification/bills/update
baseurl/v1/modification/bills/delete


{
	"bill_id"  :  "",
	"bar" :  "",
	"date" :  "",
	"drinker" :  "",
	"items_price" :  "",
	"tax_price" :  "",
	"tip" :  "",
	"total_price" : "",
	"time" :  "",
	"bartender" : "",
	"day" :  "",
    "old_bill_id": ""
}

Day:
baseurl/v1/modification/day/insert
baseurl/v1/modification/day/update
baseurl/v1/modification/day/delete

{
	"name"  :  "",
    "old_name" : ""
}

Frequents:
baseurl/v1/modification/frequents/insert
baseurl/v1/modification/frequents/update
baseurl/v1/modification/frequents/delete

{
	"bar"  :  "",
    "drinker": "",
    "old_bar": "",
    "old_drinker" : ""
}

Likes:
baseurl/v1/modification/likes/insert
baseurl/v1/modification/likes/update
baseurl/v1/modification/likes/delete

{
	"beer"  :  "",
    "drinker": "",
    "old_beer": "",
    "old_drinker" : ""
}


Inventory:
baseurl/v1/modification/inventory/insert
baseurl/v1/modification/inventory/update
baseurl/v1/modification/inventory/delete

{
	"beer"  :  "",
	"bar"  :  "",
	"date"  :  "",
	"startquantity"  :  "",
	"endquantity"  :  "",
    "old_beer": "",
    "old_bar": "",
    "old_date": ""
}


Operates:
baseurl/v1/modification/operates/insert
baseurl/v1/modification/operates/update
baseurl/v1/modification/operates/delete

{
	"bar"  :  "",
	"day"  :  "",
	"start"  :  "",
	"end"  :  "",
	"date" : "",
    "old_bar": "",
    "old_date": ""
}

SellsBeer:
baseurl/v1/modification/sellsbeer/insert
baseurl/v1/modification/sellsbeer/update
baseurl/v1/modification/sellsbeer/delete

{
	"beername"  :  "",
	"barname"  :  "",
	"price"  :  "",
    "old_bar": "",
    "old_beer": ""
	"start_quantity": ""
}

SellsFood:
baseurl/v1/modification/sellsfood/insert
baseurl/v1/modification/sellsfood/update
baseurl/v1/modification/sellsfood/delete

{
	"foodname"  :  "",
	"barname"  :  "",
	"price"  :  "",
    "old_bar": "",
    "old_food": ""
}

Shifts:
baseurl/v1/modification/shifts/insert
baseurl/v1/modification/shifts/update
baseurl/v1/modification/shifts/delete

{
	"bar"  :  "",
	"bartender"  :  "",
	"day"  :  "",
	"start"  :  "",
	"end"  :  "",
	"date" :  "",
    "old_bartender": "",
    "old_bar": "",
    "old_date": ""
}

Transactions:
baseurl/v1/modification/transactions/insert
baseurl/v1/modification/transactions/update
baseurl/v1/modification/transactions/delete

{
	"bill_id"  :  "",
	"quantity" :  "",
	"item" :  "",
	"item_type" :  "",
	"price" :  "",
    "old_bill_id": "",
    "old_item": ""
}