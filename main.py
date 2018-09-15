
import tkinter as tk
import secrets
import string 

# メインウィンドウ作成
root = tk.Tk()

#メインウィンドウのタイトルを変更
root.title("Password Generator")

#メインウィンドウを640x480にする
root.geometry("640x480")

#ラベルを追加
label = tk.Label(root, text="下のボタンを押すとパスワードを生成します。")
#表示
label.grid()

#commandに関数を指定するとクリックしたときにその関数を呼び出せる
def pass_gen(size=8):
    password = ''.join([secrets.choice(string.ascii_letters + string.digits) for i in range(size)])
    #生成したパスワードを表示
    label2 = tk.Label(root, text=password)
    label2.grid()

#ボタンの表示
button = tk.Button(root, text="パスワードを生成", command= lambda : pass_gen())
button.grid()

#rootを表示し無限ループ
root.mainloop()