# API-Exercise I
Using flask to develop a API for sum, minus, multiply, and divide two parameters.

## How to use
URI: /sum, /minus, /multiply, /divide
Parameters: value1, value2

Request: http://127.0.0.1:5000/sum?value1=1&value2=1
Response: 2

Request: http://127.0.0.1:5000/minus?value1=10&value2=1
Response: 9

Request: http://127.0.0.1:5000/multiply?value1=1&value2=5
Response: 5

Request: http://127.0.0.1:5000/divide?value1=1&value2=1
Response: 1.0

## How to Install Flash module
$ pip install Flask

$ pip show flask


# API-Exercise II

Task

Learning test framework of flask API. Adding test cases of APIs. Test cases must be including:

Correct case (ex. /sum?value1=1&value2=1 result: 2)
Missing values (ex. /sum?value1=1 result: 406 Error)
Invalid values (ex. /sum?value1=a&value=2 result: 406 error)