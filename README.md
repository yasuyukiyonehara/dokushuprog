# 独学プログラマーでPythonを覚える

## Pythonのインストール

    Pythonは公式版のインストールを行う。
    Anacondaも後々使用したいので
    切り替え方法を習得する。
    
### 公式Pythonのインストール

    2022年11月23日の時点の最新版である`3.11`をインストールする。

    https://www.python.org/downloads/

#### Pyenvのインストール

    HomeBrewでインストールをする

    ```
    brew update
    ```
    ```
    brew install pyenv
    ```

    ```
    brew install pyenv
    ```



インストール前
    
```
yonehara@yonehara-no-MacBook-Pro Dokushuprog % python --version
Python 2.7.16
```

インストール後
```

```

### Githubとのコネクション

ローカルに.sshディレクトりを作成し.sshディレクトリで鍵を作る
```
/Users/User/.ssh
```

ローカルにsshKeyを作成
```
ssh-keygen -t rsa -C "メールアドレス"
```

- 保存先の設定。（.ssh内なのでEnterでOK）
- パスワードの設定

ssh-agent（認証鍵を保存するプログラム）に、生成した鍵を追加する
```
ssh-add ~/.ssh/id_rsa
```

鍵をコピーする
```
pbcopy < ~/.ssh/id_rsa.pub
```

確認テスト
```
ssh -T git@github.com
```
