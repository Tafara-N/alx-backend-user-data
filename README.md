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
- [What Is PII, non-PII, and Personal Data?](https://intranet.alxswe.com/rltoken/jf71oYqiETchcVhPzQVnyg)
- [logging documentation](https://intranet.alxswe.com/rltoken/W2JiHD6cbJY1scJORyLqnw)
- [bcrypt package](https://intranet.alxswe.com/rltoken/41oaQXfzwnF1i-wT8W0vHw)
- [Logging to Files, Setting Levels, and Formatting](https://intranet.alxswe.com/rltoken/XCpI9uvguxlTCsAeRCW6SA)

# Learning Objectives
At the end of this project, you are expected to be able to [explain to anyone](https://intranet.alxswe.com/rltoken/yiowzem5NkzxawDmImXy8Q), **without the help of Google:**

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

In the industry, you should **not** implement your own Basic authentication system and use a module or framework that doing it for you (like in Python-Flask: [Flask-HTTPAuth](https://intranet.alxswe.com/rltoken/rpsPy0M3_FJuCLGNPUbmvg)). Here, for the learning purpose, we will walk through each step of this mechanism to understand it by doing.

![Authentication Failed! You shall not pass!](authentication.png)

# Resources

**Read or watch:**
- [REST API Authentication Mechanisms](https://intranet.alxswe.com/rltoken/ssg5umgsMk5jKM8WRHk2Ug)
- [Base64 in Python](https://intranet.alxswe.com/rltoken/RpaPRyKx1rdHgRSUyuPfeg)
- [HTTP header Authorization](https://intranet.alxswe.com/rltoken/WlARq8tQPUGQq5VphLKM4w)
- [Flask](https://intranet.alxswe.com/rltoken/HG5WXgSja5kMa29fbMd9Aw)
- [Base64 - concept](https://intranet.alxswe.com/rltoken/br6Rp4iMaOce6EAC-JQnOw)

# Learning Objectives
At the end of this project, you are expected to be able to [explain to anyone](https://intranet.alxswe.com/rltoken/swiIZazfz7mspY1vjuy_Zg), **without the help of Google:**

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

## Author

**Tafara Nyamhunga - [Github](https://github.com/tafara-n) / [Twitter](https://twitter.com/tafaranyamhunga)**
