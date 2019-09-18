import json


def load_data(filepath):
    with open(filepath, "r", encoding='UTF-8') as f:
        data = json.load(f)
        pretty = (json.dumps(data, indent=4, sort_keys=True, ensure_ascii=False))
        return pretty

    
print(load_data(r"C:\Users\A&A\Desktop\Python\4_json\als.json"))

# Честно, не понял - зачем 2 функции? Первая должна просто открывать файл? а вторая именно приводить его в читаемый вид?
# Сейчас, на функцию подается путь до файла json, далее она его открывает и приводит в читаемый вид.
# И что обычно пишется в "if __name__ == '__main__':"?
