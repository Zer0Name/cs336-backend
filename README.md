

**Base url: https://xja36rg9of.execute-api.us-east-1.amazonaws.com/dev**

---
**URL: /v1/drinker**

- Description: Will return all drinkers that are found in the drinker table
- request type: GET

### Request: 
```
{
}
```
### Response: 
```
[
  {
        "name": String,
        "phone": String,
        "state": String
    }
]
```

### Example request: 
```
{
}
```
### Example response: 
```
[
    {
        "name": "Aaron Adkins",
        "phone": "213-064-6450",
        "state": "AR"
    },
    {
        "name": "Aaron Betancourt",
        "phone": "653-222-8871",
        "state": "TN"
    }
]
```

---

**URL: /v1/drinker/transactions**

- Description: Get all transactions for a given drinker
- request type: GET

### Request: 
```
params:
    drinker = "name of drinker"
```

### Response: 
```
[
    {
        "bar": String,
        "bill_id": String,
        "date": String,
        "item": String,
        "quantity": String,
        "time": String,
        "total_item_price": String
    }
]
```

### Example request: 
```
baseURL/v1/drinker/transactions?drinker=Aaron Adkins
```
### Example response: 
```
[
    {
        "bar": "Busy Bachelor Bar",
        "bill_id": "55ed03e6-d719-11e8-a205-acde48001122",
        "date": "2018-10-22",
        "item": "Dry Stout",
        "quantity": "3",
        "time": "13:35",
        "total_item_price": "29.97"
    },
    {
        "bar": "Blue City",
        "bill_id": "55874454-d719-11e8-b0ab-acde48001122",
        "date": "2018-10-20",
        "item": "Welsh Honey Bitter",
        "quantity": "1",
        "time": "18:58",
        "total_item_price": "7.70"
    }
]
```

---

**URL: /v1/drinker/beer/top**

- Description: Get the top 10 beers the drinker orders the most
- request type: GET

### Request: 
```
params:
    drinker = "name of drinker"
```

### Response: 
```
[
     {
        "name": String,
        "total": String
    }
]
```

### Example request: 
```
baseURL/v1/drinker/beer/top?drinker=Aaron Adkins
```
### Example response: 
```
[
    {
        "name": "Southside Strong",
        "total": "5"
    },
    {
        "name": "Dry Stout",
        "total": "3"
    }
]
```

---

**URL: /v1/drinker/bar/spent**

- Description: Get the amount the drinker spent at each bar 
- request type: GET

### Request: 
```
params:
    drinker = "name of drinker"
```

### Response: 
```
[
    {
        "name": String,
        "total": String
    }
]
```

### Example request: 
```
baseURL/v1/drinker/bar/spent?drinker=Aaron Butler
```
### Example response: 
```
[
    {
        "name": "Interesting Trumpet Inn",
        "total": "51.31"
    },
    {
        "name": "Iron Library Tavern",
        "total": "23.53"
    }
]
```

---

**URL: /v1/drinker/spent/day**

- Description: Get the amount the drinker spent each day 
- request type: GET

### Request: 
```
params:
    drinker = "name of drinker"
```

### Response: 
```
[
    {
        "period": String,
        "total_price": String
    }
]
```

### Example request: 
```
baseURL/v1/drinker/spent/day?drinker=Aaron Butler
```
### Example response: 
```
[
    {
        "period": "2018-10-10",
        "total_price": "23.55"
    },
    {
        "period": "2018-10-12",
        "total_price": "13.49"
    }
]
```

---

**URL: /v1/drinker/spent/week**

- Description: Get the amount the drinker spent each week
- request type: GET

### Request: 
```
params:
    drinker = "name of drinker"
```

### Response: 
```
[
    {
        "period": String,
        "total_price": String
    }
]
```

### Example request: 
```
baseURL/v1/drinker/spent/week?drinker=Aaron Butler
```
### Example response: 
```
[
   {
        "period": "40",
        "total_price": "43.31"
    },
    {
        "period": "41",
        "total_price": "31.55"
    }
]
```
---

**URL: /v1/drinker/spent/month**

- Description: Get the amount the drinker spent each month
- request type: GET

### Request: 
```
params:
    drinker = "name of drinker"
```

### Response: 
```
[
    {
        "period": String,
        "total_price": String
    }
]
```

### Example request: 
```
baseURL/v1/drinker/spent/month?drinker=Aaron Butler
```
### Example response: 
```
[
    {
        "period": "October",
        "total_price": "98.39"
    }
]
```

---
**URL: /v1/bar**

- Description: Will return all bars that are found in the bar table
- request type: GET

### Request: 
```
{
}
```
### Response: 
```
[
    {
        "name": String,
        "state": String
    }
]
```

### Example request: 
```
{
}
```
### Example response: 
```
[
    {
        "name": "Absent Snow",
        "state": "AL"
    },
    {
        "name": "Admiral Benbow Inn",
        "state": "AL"
    }
]
```

---

---
**URL: /v1/bar/operates**

- Description: Will return all the operating hours for a given bar
- request type: GET

### Request: 
```
params:
    bar = "name of bar"
```
### Response: 
```
[
    {
        "bar": String,
        "day": String,
        "end": String,
        "start": String
    }
]
```

### Example request: 
```
baseURL/v1/bar/operates?bar=Latino Magpie
```
### Example response: 
```
[
    {
        "bar": "Latino Magpie",
        "day": "Monday",
        "end": "23:15",
        "start": "08:00"
    },
    {
        "bar": "Latino Magpie",
        "day": "Tuesday",
        "end": "22:15",
        "start": "11:00"
    }
]
```

---

---
**URL: /v1/bar/rank/sales/manf**

- Description: Will return the top 10 bars based on their sales (number of beers sold) of a given brand of beer (manufacturer)
- request type: GET

### Request: 
```
params:
    manf = "name of manufacturer"
```
### Response: 
```
[
    {
        "name": String,
        "total": String
    }
]
```

### Example request: 
```
baseURL/v1/bar/rank/sales/manf?manf=kirin
```
### Example response: 
```
[
    {
        "name": "Purple Pint Bar and Grille",
        "total": "706"
    },
    {
        "name": "Courageous Melon",
        "total": "523"
    }
]
```

---

---
**URL: /v1/bar/rank/sales/day**

- Description: Will return the top 10 bars based on the total sales (number of beers sold) on a given day of the week
- request type: GET

### Request: 
```
params:
    day = "day of the week"
```
### Response: 
```
[
    {
        "name": String,
        "total": String
    }
]
```

### Example request: 
```
baseURL/v1/bar/rank/sales/day?day=Monday
```
### Example response: 
```
[
    {
        "name": "Spicy Cats Tavern",
        "total": "262"
    },
    {
        "name": "Brave Olive Pub",
        "total": "260"
    }
]
```

---

---
**URL: /v1/bar/inventory/fraction**

- Description: Will return the average fraction of inventory sold for a given bar for each day of the week
- request type: GET

### Request: 
```
params:
    bar = "name of bar"
```
### Response: 
```
[
    {
        "name": String,
        "total": String
    }
]
```

### Example request: 
```
baseURL/v1/bar/inventory/fraction?bar=Latino Magpie
```
### Example response: 
```
[
    {
        "name": "Sunday",
        "total": "0.03360000"
    },
    {
        "name": "Monday",
        "total": "0.03305000"
    }
]
```

---

---
**URL: /v1/bar/beer/top**

- Description: Will return the top 10 beer brands (manufacturers) that are most popular in a specified bar on a specified day
- request type: GET

### Request: 
```
params:
    bar = "name of bar"
    day_of_week = "name of the day of the week"
```
### Response: 
```
[
    {
        "name": String,
        "total": String
    }
]
```

### Example request: 
```
baseURL/v1/bar/beer/top?bar=Armed Pudding Bar&day_of_week=Thursday
```
### Example response: 
```
[
    {
        "name": "Asahi",
        "total": "28"
    },
    {
        "name": "Tsingtao Brewery Group",
        "total": "25"
    }
]
```

---

---
**URL: /v1/bar/top/spenders**

- Description: Will return the top 10 drinkers who are the largest spenders at a specified bar
- request type: GET

### Request: 
```
params:
    bar = "name of bar"
```
### Response: 
```
[
    {
        "name": String,
        "total": String
    }
]
```

### Example request: 
```
baseURL/v1/bar/top/spenders?bar=Armed Pudding Bar
```
### Example response: 
```
[
    {
        "name": "Keith Morales",
        "total": "375.28"
    },
    {
        "name": "Sheila Sloan",
        "total": "254.53"
    }
]
```

---

---
**URL: /v1/bar/sale/distribution/days**

- Description: Time distributions of sales (average number of items sold) to indicate busiest periods of the day
- request type: GET

### Request: 
```
params:
    bar = "name of bar"
```
### Response: 
```
[
    {
        "period": String,
        "total": String
    }
]
```

### Example request: 
```
baseURL/v1/bar/sale/distribution/days?bar=Armed Pudding Bar
```
### Example response: 
```
[
    {
        "period": "Sunday",
        "total": "85"
    },
    {
        "period": "Monday",
        "total": "80"
    }
]
```

---

---
**URL: /v1/bar/sale/distribution/days**

- Description: Time distributions of sales (average number of items sold) to indicate busiest periods of the week (busiest days of the week)
- request type: GET

### Request: 
```
params:
    bar = "name of bar"
```
### Response: 
```
[
    {
        "period": String,
        "total": String
    }
]
```

### Example request: 
```
baseURL/v1/bar/sale/distribution/days?bar=Armed Pudding Bar
```
### Example response: 
```
[
    {
        "period": "Sunday",
        "total": "128.0000"
    },
    {
        "period": "Monday",
        "total": "128.5000"
    }
]
```

---

---
**URL: /v1/bar/sale/time/distribution**

- Description: Time distributions of sales (average number of items sold) to indicate busiest periods of the day (morning 8:00-12:00, afternoon 12:00-16:00, evening 16:00-20:00, night 20:00-24:00)
- request type: GET

### Request: 
```
params:
    bar = "name of bar"
```
### Response: 
```
[
  {
        "afternoon_avg_sold": String,
        "evening_avg_sold": String,
        "morning_avg_sold": String,
        "night_avg_sold": String
    }
]
```

### Example request: 
```
baseURL/v1/bar/sale/time/distribution?bar=Armed Pudding Bar
```
### Example response: 
```
[
    {
        "afternoon_avg_sold": "31.0714",
        "evening_avg_sold": "45.9286",
        "morning_avg_sold": "13.9286",
        "night_avg_sold": "47.6429"
    }
]
```

---

---
**URL: /v1/beer**

- Description: Will return all beers that are found in the beer table
- request type: GET

### Request: 
```
{
}
```
### Response: 
```
[
    {
        "manf": String,
        "name": String
    }
]
```

### Example request: 
```
{
}
```
### Example response: 
```
[
    {
        "manf": "Groupe Castel",
        "name": "Amstel Bock"
    },
    {
        "manf": "China Resources Snow Breweries",
        "name": "Amstel Bright"
    }
]
```

---

---
**URL: /v1/beer/biggest/consumers**

- Description: Show the (top 10) bars where this beer sells the most
- request type: GET

### Request: 
```
params:
    beer = "name of bar"
```
### Response: 
```
[
    {
        "name": String,
        "total": String
    }
]
```

### Example request: 
```
baseURL/v1/beer/biggest/consumers?beer=Code Blue
```
### Example response: 
```
[
    {
        "name": "Juan Brechbiel",
        "total": "14"
    },
    {
        "name": "Jarrod Sharpe",
        "total": "13"
    }
]
```

---

---
**URL: /v1/beer/sold/most**

- Description: (Top 10) Drinkers who are the biggest consumers of the beer
- request type: GET

### Request: 
```
params:
    beer = "name of bar"
```
### Response: 
```
[
    {
        "name": String,
        "total": String
    }
]
```

### Example request: 
```
baseURL/v1/beer/sold/most?beer=Code Blue
```
### Example response: 
```
[
    {
        "name": "Chubby Badger Pub",
        "total": "165"
    },
    {
        "name": "Natural Squash Tavern",
        "total": "166"
    }
]
```

---

---
**URL: /v1/beer/sale/time/distribution**

- Description: Time distribution of when this beer sells the most (morning 8:00-12:00, afternoon 12:00-16:00, evening 16:00-20:00, night 20:00-24:00)
- request type: GET

### Request: 
```
params:
    beer = "name of beer"
```
### Response: 
```
[
    {
        "afternoon_avg_sold": String,
        "evening_avg_sold": String,
        "morning_avg_sold": String,
        "night_avg_sold": String
    }
]
```

### Example request: 
```
baseURL/v1/beer/sale/time/distribution?beer=Code Blue
```
### Example response: 
```
[
    {
        "afternoon_avg_sold": "45.2857",
        "evening_avg_sold": "69.0000",
        "morning_avg_sold": "22.1429",
        "night_avg_sold": "52.6429"
    }
]
```

---

---
**URL: /v1/bartender**

- Description: Will return all bartenders that are found in the bartender table
- request type: GET

### Request: 
```
{
}
```
### Response: 
```
[
  {
        "name": String,
        "phone": String,
        "state": String
    }
]
```

### Example request: 
```
{
}
```
### Example response: 
```
[
    {
        "name": "Aaron Allen",
        "phone": "883-576-1442",
        "state": "FL"
    },
    {
        "name": "Aaron Bundy",
        "phone": "775-363-1039",
        "state": "NJ"
    }
]
```

---

---
**URL: /v1/bartender/works**

- Description: Will return all bars that a given bartender works at
- request type: GET

### Request: 
```
params:
    bartender = "name of bartender"

```
### Response: 
```
[
    {
        "name": String,
        "state": String
    }
]
```

### Example request: 
```
baseURL/v1/bartender/works?bartender=Aaron Allen
```
### Example response: 
```
[
    {
        "name": "Deep Glass Bar",
        "state": "FL"
    }
]
```

---

---
**URL: /v1/bartender/shifts/past**

- Description: Gets all shifts a given bartender has had in the past at a given bar
- request type: GET

### Request: 
```
params:
    bartender = "name of bartender"
    bar = "name of bar"
```
### Response: 
```
[
    {
        "date": String,
        "day": String,
        "end": String,
        "start": String
    }
]
```

### Example request: 
```
baseURL/v1/bartender/shifts/past?bartender=Alice Fico&bar=Latino Magpie
```
### Example response: 
```
[
    {
        "date": "2018-10-15"
        "day": "Monday",
        "end": "23:15",
        "start": "15:00"
    },
    {
        "date": "2018-10-09"
        "day": "Tuesday",
        "end": "14:50",
        "start": "11:00"
    }
]
```

---

---
**URL: /v1/bartender/sold/beer/brands**

- Description: Gets how many beers of each brand/manufacturer a given bartender sold at a given bar
- request type: GET

### Request: 
```
params:
    bartender = "name of bartender"
    bar = "name of bar"
```
### Response: 
```
[
    {
        "name": String,
        "total": String
    }
]
```

### Example request: 
```
baseURL/v1/bartender/sold/beer/brands?bartender=Alice Fico&bar=Latino Magpie
```
### Example response: 
```
[
   {
        "name": "Carlsberg",
        "total": "44"
    },
    {
        "name": "China Resources Snow Breweries",
        "total": "21"
    }
]
```

---

---
**URL: /v1/bartender/rank/sold/beers**

- Description: Ranks the bartenders at a given bar by total number of beers sold on a given day of the week and a given shift. The bartender must be working for the entirety of the shift to be included.
- request type: GET

### Request: 
```
params:
    startTime = "time when the shift starts"
    endTime = "time when the shift ends"
    day = "day of the week"
    bar = "name of bar"
```
### Response: 
```
[
    {
        "name": String,
        "total": String
    }
]
```

### Example request: 
```
baseURL/v1/bartender/rank/sold/beers?bar=Latino Magpie&day=Monday&startTime=20:00&endTime=22:00
```
### Example response: 
```
[
    {
        "name": "Alice Fico",
        "total": "11"
    },
    {
        "name": "Cindy Laso",
        "total": "7"
    }
]
```

---

---
**URL: /v1/manufacturer**

- Description: Will return all manufacturers that are found in the beer table
- request type: GET

### Request: 
```
{
}
```
### Response: 
```
[
    {
        "name": String
    }
]
```

### Example request: 
```
{
}
```
### Example response: 
```
[
    {
        "name": "Groupe Castel"
    },
    {
        "name": "China Resources Snow Breweries"
    }
]
```

---

---
**URL: /v1/manufacturer/beers**

- Description: Will return all beers that are made by a given manufacturer
- request type: GET

### Request: 
```
params:
    manf = "name of manufacturer"
```
### Response: 
```
[
    {
        "name": String
    }
]
```

### Example request: 
```
baseURL/v1/manufacturer/beers?manf=kirin
```
### Example response: 
```
[
    {
        "name": "Amstel Lager"
    },
    {
        "name": "Amstel Lentebock"
    }
]
```

---

---
**URL: /v1/manufacturer/sales/lastweek/top/states**

- Description: Will return the top 10 states where a given manufacturer had the highest sales (sold largest number of their beers) in the last week
- request type: GET

### Request: 
```
params:
    manf = "name of manufacturer"
```
### Response: 
```
[
    {
        "name": String,
        "total": String
    }
]
```

### Example request: 
```
baseURL/v1/manufacturer/sales/lastweek/top/states?manf=kirin
```
### Example response: 
```
[
    {
        "name": "CO",
        "total": "604"
    },
    {
        "name": "ND",
        "total": "601"
    }
]
```

---

---
**URL: /v1/manufacturer/liked/top/states**

- Description: Will return the top 10 states where the beers of a given manufacturer are liked the most
- request type: GET

### Request: 
```
params:
    manf = "name of manufacturer"
```
### Response: 
```
[
    {
        "name": String,
        "total": String
    }
]
```

### Example request: 
```
baseURL/v1/manufacturer/liked/top/states?manf=kirin
```
### Example response: 
```
[
    {
        "name": "AK",
        "total": "76"
    },
    {
        "name": "WI",
        "total": "70"
    }
]
```

---

---
**URL: /v1/modification/barfood**

- Description: Will return all bar food that are found in the BarFood table
- request type: GET

### Request: 
```
{
}
```
### Response: 
```
[
  {
        "name": String
    }
]
```

### Example request: 
```
{
}
```
### Example response: 
```
[
    {
        "name": "Blooming Onion"
    },
    {
        "name": "Buffalo Wings"
    }
]
```

---

---
**URL: /v1/modification/day**

- Description: Will return all day that are found in the Day table
- request type: GET

### Request: 
```
{
}
```
### Response: 
```
[
  {
        "name": String
    }
]
```

### Example request: 
```
{
}
```
### Example response: 
```
[
    {
        "name": "Friday"
    },
    {
        "name": "Monday"
    }
]
```

---

---
**URL: /v1/modification/frequents**

- Description: Will return all tuples that are found in the Frequents table
- request type: GET

### Request: 
```
{
}
```
### Response: 
```
[
    {
        "bar": String,
        "drinker": String
    }
]
```

### Example request: 
```
{
}
```
### Example response: 
```
[
    {
        "bar": "Brave Olive Pub",
        "drinker": "Aaron Adkins"
    },
    {
        "bar": "Spicy Cats Tavern",
        "drinker": "Aaron Betancourt"
    }
]
```

---

---
**URL: /v1/modification/likes**

- Description: Will return all tuples that are found in the Likes table
- request type: GET

### Request: 
```
{
}
```
### Response: 
```
[
    {
        "beer": String,
        "drinker": String
    }
]
```

### Example request: 
```
{
}
```
### Example response: 
```
[
    {
        "beer": "Amstel Lager",
        "drinker": "Aaron Adkins"
    },
    {
        "beer": "Cauldron Brew",
        "drinker": "Aaron Adkins"
    }
]
```

---

---
**URL: /v1/modification/inventory**

- Description: Will return all tuples that are found in the Inventory table
- request type: GET

### Request: 
```
{
}
```
### Response: 
```
[
    {
        "bar": String,
        "beer": String,
        "date": String,
        "endquantity": String,
        "startquantity": String
    }
]
```

### Example request: 
```
{
}
```
### Example response: 
```
[
     {
        "bar": "Fluffy Husband",
        "beer": "Hibiscus Ginger Beer",
        "date": "2018-10-11",
        "endquantity": "113",
        "startquantity": "127"
    },
    {
        "bar": "Discreet Elderberry Pub",
        "beer": "Lawnmower Lager",
        "date": "2018-10-13",
        "endquantity": "169",
        "startquantity": "183"
    }
]
```

---

---
**URL: /v1/modification/operates**

- Description: Will return all tuples that are found in the Operates table
- request type: GET

### Request: 
```
{
}
```
### Response: 
```
[
    {
        "bar": String,
        "date": String,
        "day": String,
        "end": String,
        "start": String
    }
]
```

### Example request: 
```
{
}
```
### Example response: 
```
[
    {
        "bar": "Absent Snow",
        "date": "2018-10-15",
        "day": "Monday",
        "end": "23:45",
        "start": "12:00"
    },
    {
        "bar": "Absent Snow",
        "date": "2018-10-09",
        "day": "Tuesday",
        "end": "22:00",
        "start": "09:00"
    }
]
```

---

---
**URL: /v1/modification/sellsbeer**

- Description: Will return all tuples that are found in the SellsBeer table
- request type: GET

### Request: 
```
{
}
```
### Response: 
```
[
    {
        "barname": String,
        "beername": String,
        "price": String
    }
]
```

### Example request: 
```
{
}
```
### Example response: 
```
[
    {
        "barname": "Absent Snow",
        "beername": "North Beach Ale",
        "price": "4.40"
    },
    {
        "barname": "Absent Snow",
        "beername": "Dry Stout",
        "price": "9.99"
    }
]
```

---

---
**URL: /v1/modification/sellsfood**

- Description: Will return all tuples that are found in the SellsFood table
- request type: GET

### Request: 
```
{
}
```
### Response: 
```
[
    {
        "barname": String,
        "foodname": String,
        "price": String
    }
]
```

### Example request: 
```
{
}
```
### Example response: 
```
[
    {
        "barname": "Absent Snow",
        "foodname": "Waffle Fries",
        "price": "4.74"
    },
    {
        "barname": "Absent Snow",
        "foodname": "Blooming Onion",
        "price": "8.89"
    }
]
```

---

---
**URL: /v1/modification/shifts**

- Description: Will return all tuples that are found in the Shifts table
- request type: GET

### Request: 
```
{
}
```
### Response: 
```
[
    {
        "bar": String,
        "bartender": String,
        "date": String,
        "day": String,
        "end": String,
        "start": String
    }
]
```

### Example request: 
```
{
}
```
### Example response: 
```
[
    {
        "bar": "Absent Snow",
        "bartender": "Carolyn Norman",
        "date": "2018-10-15",
        "day": "Monday",
        "end": "23:45",
        "start": "15:00"
    },
    {
        "bar": "Absent Snow",
        "bartender": "Brandon Campbell",
        "date": "2018-10-15",
        "day": "Monday",
        "end": "23:45",
        "start": "15:00"
    }
]
```

---