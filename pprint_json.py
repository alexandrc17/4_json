import json
with open(r"C:\Users\860159\Documents\GitHub\4_json\als.json", "r", encoding='UTF-8') as filepath:
    data = json.load(filepath)


def pretty_print_json(data):
    print(json.dumps(data, indent=4, sort_keys=True, ensure_ascii=False))


if __name__ == '__main__':
     pass
