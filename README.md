# Introduction to Backend User Data: with Python.

## Table of Content
- [Author](#author)
- [Description](#description)
___

- [Basic Authentication](0x01-Basic_authentication/README.md)
- [Personal Data](0x00-personal_data/README.md)
- [Session Authentication](0x02-Session_authentication/README.md)
- [User Authentication Service](0x03-user_authentication_service/README.md)
___

# Description

1. # Personal Data

![Information about myself](info.png)

# Resources

**Read or watch:**
- [What Is PII, non-PII, and Personal Data?](https://piwik.pro/blog/what-is-pii-personal-data/)
- [logging documentation](https://docs.python.org/3/library/logging.html)
- [bcrypt package](https://github.com/pyca/bcrypt/)
- [Logging to Files, Setting Levels, and Formatting](https://www.youtube.com/watch?v=-ARI4Cz-awo)

# Learning Objectives
At the end of this project, you are expected to be able to [explain to anyone](https://fs.blog/feynman-learning-technique/) **without the help of Google:**

- Examples of Personally Identifiable Information (PII)
- How to implement a log filter that will obfuscate PII fields
- How to encrypt a password and check the validity of an input password
- How to authenticate to a database using environment variables

# Requirements
- All your files will be interpreted/compiled on Ubuntu 18.04 LTS using `python3` (version `3.7`)
- All your files should end with a new line
- The first line of all your files should be exactly `#!/usr/bin/env python3`
- A `README.md` file, at the root of the folder of the project, is mandatory
- Your code should use the `pycodestyle` style (version `2.5`)
- All your files must be executable
- The length of your files will be tested using `wc`
- All your modules should have a documentation (`python3 -c 'print(__import__("my_module").__doc__)'`)
- All your classes should have a documentation (`python3 -c 'print(__import__("my_module").MyClass.__doc__)'`)
- All your functions (inside and outside a class) should have a documentation (`python3 -c 'print(__import__("my_module").my_function.__doc__)'` and `python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'`)
- A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class or method (the length of it will be verified)
- All your functions should be type annotated

2. # Basic Authentication

# Background Context

In this project, you will learn what the authentication process means and implement a **Basic Authentication** on a simple API.

In the industry, you should **not** implement your own Basic authentication system and use a module or framework that doing it for you (like in Python-Flask: [Flask-HTTPAuth](https://flask-httpauth.readthedocs.io/en/latest/)). Here, for the learning purpose, we will walk through each step of this mechanism to understand it by doing.

![Authentication Failed! You shall not pass!](https://github.com/Tafara-N/alx-backend-user-data/blob/main/0x01-Basic_authentication/authentication.png)

# Resources

**Read or watch:**
- [REST API Authentication Mechanisms](https://www.youtube.com/watch?v=501dpx2IjGY)
- [Base64 in Python](https://docs.python.org/3.7/library/base64.html)
- [HTTP header Authorization](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Authorization)
- [Flask](https://palletsprojects.com/projects/flask/)
- [Base64 - concept](https://en.wikipedia.org/wiki/Base64)

# Learning Objectives
At the end of this project, you are expected to be able to [explain to anyone](https://fs.blog/feynman-learning-technique/), **without the help of Google:**

## General
- What authentication means
- What Base64 is
- How to encode a string in Base64
- What Basic authentication means
- How to send the Authorization header

# Requirements

## Python Scripts
- All your files will be interpreted/compiled on Ubuntu 18.04 LTS using `python3` (version `3.7`)
- All your files should end with a new line
- The first line of all your files should be exactly `#!/usr/bin/env python3`
- A `README.md` file, at the root of the folder of the project, is mandatory
- Your code should use the `pycodestyle` style (version `2.5`)
- All your files must be executable
- The length of your files will be tested using `wc`
- All your modules should have a documentation ( `python3 -c 'print(__import__("my_module").__doc__)'` )
- All your classes should have a documentation ( `python3 -c 'print(__import__("my_module").MyClass.__doc__)'` )
- All your functions (inside and outside a class) should have a documentation ( `python3 -c 'print(__import__("my_module").my_function.__doc__)'` and `python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'` )
- A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class or method (the length of it will be verified)

3. # Session Authentication

# Background Context

In this project, you will implement a **Session Authentication**. You are not allowed to install any other module.

In the industry, you should **not** implement your own Session authentication system and use a module or framework that doing it for you (like in Python-Flask: [Flask-HTTPAuth](https://flask-httpauth.readthedocs.io/en/latest/)). Here, for the learning purpose, we will walk through each step of this mechanism to understand it by doing.

# Resources

**Read or watch:**
- [REST API Authentication Mechanisms - Only the session auth part](https://www.youtube.com/watch?v=501dpx2IjGY)
- [HTTP Cookie](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Cookie)
- [Flask](https://palletsprojects.com/projects/flask/)
- [Flask Cookie](https://flask.palletsprojects.com/en/1.1.x/quickstart/#cookies)

# Learning Objectives
At the end of this project, you are expected to be able to [explain to anyone](https://fs.blog/feynman-learning-technique/), **without the help of Google:**

## General
- What authentication means
- What session authentication means
- What Cookies are
- How to send Cookies
- How to parse Cookies

# Requirements

## Python Scripts
- All your files will be interpreted/compiled on Ubuntu 18.04 LTS using `python3` (version `3.7`)
- All your files should end with a new line
- The first line of all your files should be exactly `#!/usr/bin/env python3`
- A `README.md` file, at the root of the folder of the project, is mandatory
- Your code should use the `pycodestyle` style (version `2.5`)
- All your files must be executable
- The length of your files will be tested using `wc`
- All your modules should have a documentation (`python3 -c 'print(__import__("my_module").__doc__)'`)
- All your classes should have a documentation (`python3 -c 'print(__import__("my_module").MyClass.__doc__)'`)
- All your functions (inside and outside a class) should have a documentation (`python3 -c 'print(__import__("my_module").my_function.__doc__)'` and `python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'`)
- A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class or method (the length of it will be verified)

4. # User Authentication Service

![Changed password](https://github.com/Tafara-N/alx-backend-user-data/blob/main/0x03-user_authentication_service/incorrect_password.jpg)

In the industry, you should not implement your own authentication system and use a module or framework that doing it for you (like in Python-Flask: [Flask-User](https://intranet.alxswe.com/rltoken/9nVfotMI_1zpEzihMzBeTA)). Here, for the learning purpose, we will walk through each step of this mechanism to understand it by doing.

# Resources

**Read or watch:**
- [Flask documentation](https://intranet.alxswe.com/rltoken/lKExyvivrrW4eh0eI8UV6A)
- [Requests module](https://intranet.alxswe.com/rltoken/py7LuuD1u2MUwcaf8wnDzQ)
- [HTTP status codes](https://intranet.alxswe.com/rltoken/cj-mc5ZHp_KyXn1yikHC0A)

# Learning Objectives
At the end of this project, you are expected to be able to [explain to anyone](https://intranet.alxswe.com/rltoken/oAqmZmipBdjCcfI5QqyFXA), **without the help of Google:**

- How to declare API routes in a Flask app
- How to get and set cookies
- How to retrieve request form data
- How to return various HTTP status codes

# Requirements
- Allowed editors: `vi`, `vim`, `emacs`
- All your files will be interpreted/compiled on Ubuntu 18.04 LTS using `python3` (version `3.7`)
- All your files should end with a new line
- The first line of all your files should be exactly `#!/usr/bin/env python3`
- A `README.md` file, at the root of the folder of the project, is mandatory
- Your code should use the `pycodestyle` style (version `2.5`)
- You should use `SQLAlchemy` 1.3.x
- All your files must be executable
- The length of your files will be tested using `wc`
- All your modules should have a documentation (`python3 -c 'print(__import__("my_module").__doc__)'`)
- All your classes should have a documentation (`python3 -c 'print(__import__("my_module").MyClass.__doc__)'`)
- All your functions (inside and outside a class) should have a documentation (`python3 -c 'print(__import__("my_module").my_function.__doc__)'` and `python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'`)
- A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class or method (the length of it will be verified)
- All your functions should be type annotated
- The flask app should only interact with `Auth` and never with `DB` directly.
- Only public methods of `Auth` and `DB` should be used outside these classes

## Author

**Tafara Nyamhunga - [Github](https://github.com/tafara-n) / [Twitter](https://twitter.com/tafaranyamhunga)**
