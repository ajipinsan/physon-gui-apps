import tkinter as tk
import random


# ランダムに単語を選ぶ関数
def choose_word():
    return random.choice(words)


# 単語リスト
words = [
    "python",
    "java",
    "ruby",
    "javascript",
    "html",
    "css",
    "php",
    "swift",
    "cplusplus",
    "typescript",
]
# 初期設定
window = tk.Tk()
window.title("タイピング")
window.geometry("400x300")
window.configure(bg="#333333")
# ラベル表示のための変数
current_word = tk.StringVar()
current_word.set(choose_word())
# ラベル作成
label_word = tk.Label(
    window,
    textvariable=current_word,
    font=("Helvetica", 24),
    bg="#333333",
    fg="#FFFFFF",
)
label_word.pack(pady=30)
# ユーザー入力のためのエントリー
entry_user_input = tk.Entry(window, font=("Helvetica", 16), bg="#FFFFFF", fg="#333333")
entry_user_input.pack(pady=10)


# 正誤判定のための関数
def check_word():
    user_input = entry_user_input.get().strip()
    if user_input == current_word.get():
        current_word.set(choose_word())
    entry_user_input.delete(0, tk.END)


button_check = tk.Button(window, text="OK", font=("Helvetica", 14), command=check_word)
button_check.pack(pady=20)
# ↓↓↓ お約束のコード ↓↓↓
window.mainloop()
# ↑↑↑ お約束のコード ↑↑↑
