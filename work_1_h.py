import tkinter as tk

# ↓↓↓ お約束のコード ↓↓↓
window = tk.Tk()
window.title("GUI App")
window.geometry("600x400")
bg_color = "#333333"  # ダークグレー
fg_color = "#FFFFFF"  # 白
window.configure(bg=bg_color)
# ↑↑↑ お約束のコード ↑↑↑

"""
変数
    データを入れておく箱

データ型
    変数は決まったデータ型を持つ
    int: 数値型 ex) 1, 2, 3
    str: 文字列型 ex) "Hello", "World", "0", "123", ""

四則演算
    + - * /

関数
    処理をまとめたもの

フォーマット文字リテラル
    f"文字列 {変数名} 文字列"

"""


def button_action1():  # 関数の定義 ※ボタンが押されたときの動き
    user_input = entry1.get()  # 入力値を取得
    user_input2 = entry2.get()
    X = int(user_input) + int(user_input2)
    label1.config(text=f"{user_input} + {user_input2} = {X}")


def button_action2():  # 関数の定義 ※ボタンが押されたときの動き
    user_input = entry1.get()  # 入力値を取得
    user_input2 = entry2.get()
    X = int(user_input) - int(user_input2)
    label1.config(text=f"{user_input} - {user_input2} = {X}")


def button_action3():  # 関数の定義 ※ボタンが押されたときの動き
    user_input = entry1.get()  # 入力値を取得
    user_input2 = entry2.get()
    X = int(user_input) * int(user_input2)
    label1.config(text=f"{user_input} * {user_input2} = {X}")


def button_action4():  # 関数の定義 ※ボタンが押されたときの動き
    user_input = entry1.get()  # 入力値を取得
    user_input2 = entry2.get()
    X = int(user_input) / int(user_input2)
    label1.config(text=f"{user_input} / {user_input2} = {X}")


# 入力フィールドの作成
entry1 = tk.Entry(window, bg=fg_color, fg=bg_color)
entry1.pack(pady=10)

entry2 = tk.Entry(window, bg=fg_color, fg=bg_color)
entry2.pack(pady=10)

# ボタンの作成
button1 = tk.Button(window, text="＋", command=button_action1)
button1.pack(pady=10)
button2 = tk.Button(window, text="-", command=button_action2)
button2.pack(pady=10)
button3 = tk.Button(window, text="×", command=button_action3)
button3.pack(pady=10)
button4 = tk.Button(window, text="÷", command=button_action4)
button4.pack(pady=10)

# 出力ラベルの作成
label1 = tk.Label(window, text="", bg=bg_color, fg=fg_color)
label1.pack(pady=10)

# ↓↓↓ お約束のコード ↓↓↓
window.mainloop()
# ↑↑↑ お約束のコード ↑↑↑
