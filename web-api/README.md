# Path of Web Site/API
## Goals

1. Knowing how to develop a web site
2. Knowing how to develop a web api
3. Familar with major web frameworks

## Exercise
### API-Exercise I
#### Task

Using flask to develop a API for sum, minus, multiply, and divide two parameters.

**URI**: /sum, /minus, /multiply, /divide

**Parameters**: value1, value2

**Example**:

Request:

```
http://127.0.0.1/sum?value1=1&value2=1
```

Response:

```
2
```

### API-Exercise II

#### Task

Learning test framework of flask API. Adding test cases of APIs.
Test cases must be including:

1. Correct case (ex. /sum?value1=1&value2=1 result: 2)
2. Missing values (ex. /sum?value1=1 result: 406 Error)
3. Invalid values (ex. /sum?value1=a&value=2 result: 406 error)

### Website-Exercise I

#### Task

Learning how to built a single webpage with template. Using flask to develop a webpage for sum, minus, multiply, and divide two parameters.

**URI**: /count

**Parameters**: op, value1, value2

**Example**

Request:

```
http://127.0.0.1/count?op=add&value=1&value=2
```

Response:

```
The Answer of 1 + 1 is 2
```

#### Requirement

You must use the template when rendering Reponse.
