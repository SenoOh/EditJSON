import json
import sys

# JSONファイルのパスを指定する
file_path =  sys.argv[1]
# '/home/senoo/git/json/example.json'

# コマンドライン引数からキーを取得する
keys = sys.argv[2:]

# JSONファイルを読み込む
with open(file_path, 'r') as file:
    json_data = json.load(file)

# キーをJSONデータに追加する
for key in keys:
    if key not in json_data:
        value = input(f"Enter the value for key '{key}': ")
        json_data[key] = value

# 拡張されたJSONデータを表示する
print(json.dumps(json_data, indent='\t'))

# JSONファイルに書き込む
with open(file_path, 'w') as file:
    json.dump(json_data, file, indent='\t')

