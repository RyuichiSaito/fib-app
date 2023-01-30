# Fib App

フィボナッチ数を返すAPIです。

# Features

- フィボナッチ数列のn番目の数を返すAPIです。

ディレクトリ構成は以下の通りです。

```bash
.
├── README.md
├── app
│   ├── __init__.py
│   ├── main.py　# APIのエンドポイントを記載
│   ├── fib.py # フィボナッチ数列を計算する関数を記載
│   └── unit_test.py # テストコードを記載
└── requirements.txt
```

* フィボナッチ数について

フィボナッチ数列は以下のように定義されます。

```math
F_0 = 0, F_1 = 1, F_n = F_{n-1} + F_{n-2} (n \geq 2)
```

一般的には、フィボナッチ数列のn番目の数を計算する際には、以下のように再帰的に計算します。

```python
def fib(n: int) -> int:
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)
```

しかし、再帰な計算方法であると計算量が多くなるため、計算量を抑えるために、以下のように一般項を用いて計算しました。

```math
F_n = \frac{1}{\sqrt{5}}\left(\frac{1+\sqrt{5}}{2}\right)^n - \frac{1}{\sqrt{5}}\left(\frac{1-\sqrt{5}}{2}\right)^n
```


一般項を用いて計算する際に、浮動小数点演算の誤差が発生するため、誤差を抑えるために、`sympy.fibonacci` を用いています。

```python
from sympy import fibonacci

def fib(n: int) -> int:
    return fibonacci(n)
```



# Requirement

このAPIサービスは、`Python 3.9.13 + FastAPI 0.70.0` で動作します。

# Installation

`requirements.txt` に必要なライブラリが記載されています。

```bash
pip install -r requirements.txt
```

# Usage

### ローカルでの実行

```bash
uvicorn app.main:app --reload
```

`http://127.0.0.1:8000/fib?n=10` にアクセスすると、フィボナッチ数列の10番目の数が返ってきます。


### ローカルでのテスト

`pytest` を使ってテストを実行します。テストコードは `app/unit_test.py` に記載されています。

```bash
pytest
```
