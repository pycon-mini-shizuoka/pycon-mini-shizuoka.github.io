## Pycon mini Shizuoka 公式フロントページ Pelican Project

## 推奨作業環境

- Python 3.8
- Pelican 4.5.6

詳しくは Pipfileを参照してください。

## 構築方法

pelicanをインストールします。

`pipenv install`

pelican-themesのリポジトリをcloneします

操作位置 => `/home/[username]/` を想定

`git clone --recursive https://github.com/getpelican/pelican-themes ~/pelican-themes`

pelicanテーマをインストールします

`pelican-themes -i ~/pelican-themes/`

サイトの生成を確認します。

`pipenv run make devserver`