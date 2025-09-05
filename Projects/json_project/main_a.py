import json

# ngebuka dan ngebaca file json
p = r"data.json"

def bagianA(path=p):
    with open(path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    print("Daftar Hafalan Santri:")
    for i in data['santri']:
        print(f"- {i['nama']:<7} : {i['hafalan']}")

