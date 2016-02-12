# Website-Exercise I
## Task

Learning how to built a single webpage with template. Using flask to develop a webpage for sum, minus, multiply, and divide two parameters.

**URI**: /count

**Parameters**: op, value1, value2

**Example**

Request:

```
http://127.0.0.1/count?op=sum&value1=1&value2=1
```

Response:

```
The Answer of 1 + 1 is 2
```

## Requirement

You must use the template when rendering Response.

# Website-Exercise II
## Task

Learning how build a website with login mechanism.

**WebPage**: /hello

Show "hello, {username}". If user had not logged-in yet, redirect to "login" page.

**WebPage**: /login

Login form with 'username'(textfield) & 'password' (passwordfield) and 'login' button.

After user logged-in, redirect to '/hello'.

Note: Please use the model.py in database exercise as your backend. You will need to create the user before you login.
