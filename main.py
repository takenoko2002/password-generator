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

#パスワードの文字列を指定
#エントリー
EditBox = tk.Entry()
EditBox.insert(tk.END,"10")
EditBox.grid()

label2 = tk.Label(root,text ='')
label2.grid()

#commandに関数を指定するとクリックしたときにその関数を呼び出せる
#パスワードを生成
def pass_gen(pass_string = string.ascii_letters + string.digits,size=8):
    password = ''.join([secrets.choice(pass_string) for i in range(size)])
    ##ラベルを更新
    global label2
    label2["text"] = password

#ボタンの表示(パスワード生成ボタン)
button = tk.Button(root, text="パスワードを生成", command= lambda : pass_gen('abcdefghijklmn123456789',int(EditBox.get())))
button.grid()

#rootを表示し無限ループ
root.mainloop()
