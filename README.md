

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
        "beer": String,
        "quantity": String
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
        "beer": "Southside Strong",
        "quantity": "5"
    },
    {
        "beer": "Dry Stout",
        "quantity": "3"
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
        "bar": String,
        "total_price": String
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
        "bar": "Interesting Trumpet Inn",
        "total_price": "51.31"
    },
    {
        "bar": "Iron Library Tavern",
        "total_price": "23.53"
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




