# P2HACKS2023 アピールシート 

<img src="https://github.com/p2hacks2023/post-06/assets/55681988/137802ca-09e5-49b8-9ef1-dacb2ed0ba3e" height="50%" width="50%" />

## プロダクト名  
おやじチョップ！！

## コンセプト  
チョップオヤジとクイズで冷え冷えバスター

## 対象ユーザ  
おやじギャグを言いたいおやじとその周りの人

## 利用の流れ  
おやじギャグボットと突っ込みマシンが空気を温めてくれてます．  
おやじがおやじギャグを言っても，冷えることはありません. 
でもおやじがギャグを言わないと突っ込みマシンがひんやりしてしまいます.
それももう大丈夫、なぜなら今は相棒のおやじギャグボットがいるから！
ただ，おやじギャグボットと突っ込みマシンの様子を見て，おやじはさみしい気持ちになりました．  
おやじの気持ちが冷えないように，アプリもあるよ！  

## 推しポイント  
おやじギャグのセンスの高さ．おやじの顔面のあご落としの芸術性．

## スクリーンショット(任意)  
![oyaji gag quiz demo](https://github.com/p2hacks2023/post-06/assets/49859718/d44f3054-34e0-473a-b475-7b8970a7dcf4)

<img width="897" alt="overall" src="https://github.com/p2hacks2023/post-06/assets/55681988/f2434c3c-6d9c-459f-bd40-56e47d71e284">


## 開発体制  

役割分担  
* あとり(M1) : サーバサイドとクイズアプリ
* こーき(M2) : つっこみの御手手と動作，御手手のAPI
* しんご(M1) : おやじギャグの画像生成
* りょう(M1) : 音声認識
* はやと(B4) : おやじの顔面とあごを落とす処理


開発における工夫した点  
- ブランチ名
  - [feature/hotfix/refactor]/what-you-did 
- 基本的な命名規則はpythonの命名規則に準拠
  - [参考](https://qiita.com/naomi7325/items/4eb1d2a40277361e898b)

| 対象 | ルール | 例 |
| ---- | ---- | ---- |
| パッケージ | 全小文字 なるべく短くアンダースコア非推奨 | tqdm, requests ... |
| モジュール | 全小文字 なるべく短くアンダースコア可 | sys, os,... |
| クラス | 最初大文字 + 大文字区切り | MyFavoriteClass |
| 例外 | 最初大文字 + 大文字区切り | MyFuckingError |
| 型変数 | 最初大文字 + 大文字区切り | MyFavoriteType |
| メソッド | 全小文字 + アンダースコア区切り | my_favorite_method |
| 関数 | 全小文字 + アンダースコア区切り | my_favorite_funcion |
| 変数 | 全小文字 + アンダースコア区切り | my_favorite_instance |
| 定数 | 全大文字 + アンダースコア区切り | MY_FAVORITE_CONST |

* Monorepo管理しました．  
以下各ディレクトリの説明．  
  * 3dprinter  →  3Dプリンタで印刷する.stlファイルを管理
  * boke       →  おやじギャグを生成・発言させるファイルを管理
  * chop       →  突っ込みを入れる御手手の処理・ラズパイのサーバファイルを管理
  * oyaji      →  顎を落とす処理のファイルを管理
  * quiz       →  Flutterのアプリを作成するファイルを管理
  * tukkomi    →  突っ込みを入れるおやじギャグの判定処理を管理

## 開発技術 

### 利用したプログラミング言語  
Python, Dart, Arduino言語

### 利用したフレームワーク・ライブラリ  
Flutter, Fast API, LangChain, Servo

### その他開発に使用したツール・サービス
Raspberry Pi 3B+, Arduino Leonardo, 3Dプリンタ, 直流安定化電源, Fusion360, ChatGPT, OpenAI API
