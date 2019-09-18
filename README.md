# Prettify JSON

Скрипт, приводящий в читабельный вид сплошную информацию находящуюся в JSON. 

# Quickstart

Example of script launch on Linux, Python 3.5:

```bash
$ python pprint_json.py <path to file>
```

```python
import json
with open(r"C:\Users\860159\Documents\GitHub\4_json\als.json", "r", encoding='UTF-8') as filepath:
    data = json.load(filepath)


def pretty_print_json(data):
    print(json.dumps(data, indent=4, sort_keys=True, ensure_ascii=False))
```
# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
