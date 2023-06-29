const fs = require('fs');

// コマンドライン引数からJSONファイルのパスと検索キーを取得する
const filePath = process.argv[2];
const searchKey = process.argv[3];
// const replaceKey = process.argv[4];
// JSONファイルを読み込む
fs.readFile(filePath, 'utf8', (err, data) => {
  if (err) {
    console.error('Failed to read JSON file:', err);
    return;
  }

  try {
    const json = JSON.parse(data);
    const valueData = getValueByKey(json, searchKey);
    if (valueData !== undefined) {
        // 値が見つかった場合、値をコピーして新しいキーとして追加します
        json.a.newvalue = JSON.parse(JSON.stringify(valueData));
        // 変更後のJSONデータを表示する
        console.log(JSON.stringify(json, null, 2));
        // JSONファイルに書き込む
      fs.writeFile(filePath, JSON.stringify(json, null, 2), 'utf8', (err) => {
        if (err) {
          console.error('Failed to write JSON file:', err);
        }
      });
    } else {
      console.log(`Key "${searchKey}" not found in the JSON data.`);
    }
  } catch (err) {
    console.error('Failed to parse JSON data:', err);
  }
});

function getValueByKey(obj, key) {
  const keys = key.split('.');
  let value = obj;
  for (const k of keys) {
    if (value.hasOwnProperty(k)) {
      value = value[k];
    } else {
      return undefined;
    }
  }
  return value;
}


