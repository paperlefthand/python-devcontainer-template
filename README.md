# python-devcontainer-template

[Visual Studio Code Dev Containers](https://code.visualstudio.com/docs/devcontainers/containers)で管理する

## memo

- 必要な拡張機能は`devcontainer.json`に記載
- コードチェックツール  
  VSCodeの利用を前提としているため, CLIではなくVSCodeの拡張機能を利用する.
  - formatter: `black`
  - linter: `ruff`
  - static type checker: `Pylance(Pyright)`
- `pip install`は`Dockerfile`に記述することでコンテナリビルド時にキャッシュを効かせる
- VSCodeの設定は, `devcontainer.json`に記載することで, コンテナ上のユーザスペースに反映させる.
  ワークスペース固有の設定がしたい場合は`.vscode/settings.json`に記載
- `autoDocstring`でGoogleスタイルを指定.
- テストフレームワークは`pytest`. テストコードは`tests`ディレクトリに置く.
- コンテナビルド時にPylanceのloadエラーが発生し, Window Reloadしないとblackが効かない件(why?)
