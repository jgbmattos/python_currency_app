# Currency transaction

Currency transaction is a simple project intend to convert an amount of money of some chosen currency to  USD. It relies on [Open Exchange Rates](https://openexchangerates.org/) to get current rate of the chosen currency.

## Features
### Stack:
* Flask
* SQLAlchemy
* Alembic
* Redis
* Elasticsearch (APM)
* React JS

### API's:

This  project exposes two API's: 
* POST /api/currency-transact
* GET /api/currency-transactions/last?limit=1&currency=USD&page=1
  * Query parameters are optional

For saving and retrieving data respectively.


## Installation

On project root execute the following command:

```bash
docker-compose up -d
```
Note: The backend takes almost a minute to boot up in order to guarantee that MySQL is up and running.

This project uses the following ports:
* 5601, 8200, 9200, 5601, 6379, 8080 and 3000.

Those ports must available in order to run the project.


## Usage
### Curl

#### Save a transaction:
```commandline
curl --location --request POST 'http://0.0.0.0:8080/api/currency-transaction' \
--header 'Content-Type: application/json' \
--data-raw '{
    "amount": 0.25567801,
    "currency": "BTC"
}'
```
#### Retrieve Nth transaction:
```commandline
curl --location --request GET 'http://0.0.0.0:8080/api/currency-transactions/last?currency=USD&limit=1&page=1' 
```
#### Frontend:
Access http://localhost:3000


#### Using kibana 

In order to see APM error logs it's necessary to configure elastic index, follow the steps bellow:
1. Open kibana ([localhost:5601](http://localhost:5601))
2. Click  in discovery on left-side menu
3. Kibana will redirect you to index creation.
4. Type in "index pattern" "apm*" and click "next step"
5. Select @timestaamp as date filter, click "create index". Now you're ready to go to discovery.