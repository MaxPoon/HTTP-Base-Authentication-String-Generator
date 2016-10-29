# HTTP-Base-Authentication-String-Generator
Module for python 2 and python 3 to generate the hashed string of user id and time based one-time password for HTTP base authentication.

## API
Import module HTTP_Base_Auth2 for python 2.x and HTTP_Base_Auth3 for python 3.x.

To generate the string:
```
HTTP_Base_Auth2.HTTP_Basic_string (user_id, secret, t0, timestep, password_digits, alg)
```
Default value:

t0 = 0

timestep = 30

password_digits = 10

alg = hashlib.sha1
