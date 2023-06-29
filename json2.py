import json
import sys
# JSONファイルのパスを指定する
file_path =  sys.argv[1]
# '/home/senoo/git/json/example.json'

replace = sys.argv[2].split(":")

# JSONファイルを読み込む
with open(file_path, 'r') as file:
    json_data = json.load(file)

# "a"の値を取得する
value_a = json_data["a"]

# "a"の値をコピーして"？"のキーとして追加する
json_data[replace[0]] = value_a

# "？"の値の一部を指定した文字列で置換する
json_data[replace[0]] = json_data[replace[0]].replace(replace[1], replace[2])

# 変更後のJSONデータを表示する
print(json.dumps(json_data, indent='\t'))

# JSONファイルに書き込む
with open(file_path, 'w') as file:
    json.dump(json_data, file, indent='\t')
