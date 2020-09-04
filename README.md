# SimplePasswordGenerator
Thinking about save passwords is rather hard. This is why passwords are often chosen to be simple to remember like 123456 or ones date of birth. However, these passwords can be found out very easily.  

To help a friend to generate save passwords, I tried to implement a kind of password generator where it is up to the user to define the total length and the kind of characters used.  
Find out for yourself if this generator scripts works for you!

## How to use it 
The general usage of this script is as following:
```sh
$ python pw_generator.py <total length> <lower case> <upper case> <special chars> <digits>
```
- `<total length>`: total number of characters of the password  
- `<lower case>`: number of lower case letters  
- `<upper case>`: number of upper case letters  
- `<special chars>`: number of special characters  
- `<digits>`: number of digits  

Run for example 
```sh
$ python pw_generator.py 10 4 3 2 1
```
to get a password of total length 10, which contains 4 lower case letters, 3 upper letter, 2 special characters and 1 number. 
