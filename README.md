# Patriks-Chiffer-Script
En automatisk lösning på uppgiften.

Använding:
------
### Cryptera medelande
OBS: Man kan inte ha mellandrum i medelande eller nyckel!
```
python crypt.py --encrypt [msg] [key]
```

### Dekryptera medelande
```
python crypt.py --decrypt [msg] [key]
```

### Bruteforce på medelande
```
python crypt.py --bruteforce [msg] ([minkey] [maxkey] [--scan-mode])
```
**minkey = minsta nyckeln den kommer att försöka med. (default: 100).**

**maxkey = när den kommer sluta. (default: 100000).**

**--scan-mode = kommer göra så att den hoppar över svar som inte innehåller ord ifrån en lista i programmet.**


För att lösa uppgifterna:
------

#### Övning 4
```
python crypt.py --encrypt Hejjagflyttarrunt 2310
```
**Svar:** jjeHflgatatyunrrxxxt

#### Övning 5
```
python crypt.py --decrypt aaveldtetödg 352140
```
**Svar:** devalagöttde

#### Övning 6
```
python crypt.py --bruteforce kirgitvstxrå 205 215
```
**Svar:** 210 : riktigtsvårx *(540 - 543 ger samma svar men om man krypterar deras svar med samma nyckel så blir det fel)*

#### Övning X
```
python crypt.py --bruteforce äurntesdtuflirdövgva 2125 2135
```
**Svar:** 2130 : nuärdetslutföridagvv *(Ceasar key: 2)*


