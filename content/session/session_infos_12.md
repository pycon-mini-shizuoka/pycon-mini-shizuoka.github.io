Title: unittest.mockを使ってテストを書こう 〜モックオブジェクトを使ってより単体テストの目的に沿ったテストに〜
date:2020-01-04 20:00
Author: mizzsugar0425
speaker_name: みずき
level:Advanced: 経験者向け
session_category: プログラミングノウハウ
twittername: mizzsugar0425
self_intro: 昼間はデータマネジメントをしていますが、夜と休日はPythonでWEB開発しています。運用業務に携わってから開発者になった経験から、ずっとテストに関心があります。
website:
session_number:12


<meta http-equiv="refresh" content="1; URL=https://shizuoka.pycon.jp/2020/session/mizzsugar0425/">
<link rel="canonical" href="https://shizuoka.pycon.jp/2020/session/mizzsugar0425/">

<!-- 
こちらのページは2020年開催時のリンクです。新しいページへリダイレクトされます


単体テストを書く上で、モックオブジェクトという手法があります。モックオブジェクトがどんな役割を果たすか、どのように使うかを知っていると、外部的な要因でテストが落ちなくなったり、テストしたいところだけテストできるようになって便利です。このトークでは、Pythonの標準モジュールunittest.mockを使ってモックオブジェクトを扱う方法について話します。


### 対象となる人：
* unittest.mockの存在は知っているけれどもイマイチ使いどころが分かっていない人
* assertTrueやassertEqualなどの基本的なテストコードの文法は知っているけれど、何のためにテストを書くかをじっくり考えたことがない人

※基本的なテストコードの文法や使い方を手短に説明します。単体テストを書いたことがなくてもこの話を聞けるように配慮します。


### トークの目的：
* 「なんとなくテスト書いた方がいい」から目的を持ったテストを書くように意識づける
* 単体テストを書く目的を達成するためにモックを使うべき場面で使えるようになる
* unittest.mockの使い方/ハマりポイントの対応策を知ってもらう


### 話さないこと
* テスト実行に便利なツールの紹介(coverageなど)
* pytestの紹介及びunittestとの比較
* E2Eテスト、結合テストの話


### 話すこと

#### 単体テストの目的(3-5分)
* 単体テストの目的
* 単体テストを書くメリット
* 単体テストを書いて修正や機能追加をした例。(飲食店での購入合計金額を算出する関数を例に。既存の消費税が1.08に統一されていた頃の関数から軽減税率導入後の関数に変更する例を使います)
    - assertEqualやassertTrueなどの基本的なアサーションメソッドの文法
    - テストを実行するコマンド
    - テストが落ちてからテストを通す道程
    - テストを書くとどこまで関数の振る舞いを保証しているかわかるというメリット


####  単体テストでモックオブジェクトを使う理由(5-8分)

* モックオブジェクトの説明

* 単体テストは下記の条件が揃っているべきである
    - 速く実行される
    - 常に同じ条件下で同じことがテストされる
    - 外的要因を排除する
    - 1つのテストメソッドで1つのことのみ確認でないとならない
    - テスト対象の関数の振る舞いを担保する

* 単体テストでモックオブジェクトを使うメリット

####  Pythonのunittest.mockの基本的な使い方(5-8分)
* 簡単なサンプルコードを使って説明(ランダムに運勢が出力されるおみくじを表現する関数を例に)
    - unittest.mockを使わないテストコードで失敗する例
    - unittest.mockの基本的な文法
    - どのような考え方でこの例ではunittest.mockを使ったのか

unittest.mockモジュールを使って困った点とその対策(5-8分)

* unittest.mock.patchが当たらない
* assert_called_onceなど、関数が呼ばれたことをアサートする方法
* APIのレスポンスをモックすることで、(外部)APIを呼び出す関数の振る舞いをテストする
* datetime.datetime.nowをモックオブジェクトに置き換えられない場合datetime.datetime.nowを引数に持たせるかPythonの3rdパーティライブラリ「freezegun」を使ってテストする


--- -->