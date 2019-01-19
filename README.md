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
