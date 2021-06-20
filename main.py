# https://daeudaeu.com/python_tkinter/#label

# This is a sample Python script.
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

# -*- coding:utf-8 -*-
import tkinter

import MySQLdb

def db_sample():
    #事前にデータベース作成
    #sudo mysql
    #mysql>create database sample;
    #mysql>create user 'devuesr'@'%' identified by 'dbpasswd';
    #mysql>grant all on *.* to 'devuser'@'%';
    #接続

    con = MySQLdb.connect(
        user='devuser',
        passwd='dbpasswd',
        host='localhost',
        db='sample',
        charset='utf8')

    #カーソルを取得
    cur = con.cursor()

    #クリエを実行
    sql = "show databases;"
    cur.execute(sql)

    #実行結果をすべて取得する
    rows = cur.fetchall()

    # 一行ずつ表示する
    for row in rows:
        print(row)

    cur.close()
    con.close()



# マウスボタンが押されていているかどうかの判断用
press = False

def print_hi(name):
    db_sample()


    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

    # アプリの作成
    app = tkinter.Tk()

    # アプリの画面設定
    app.geometry(
        "400x400"  # アプリ画面のサイズ
    )
    app.title(
        "アプリのタイトル"  # アプリのタイトル
    )
    # キャンバスの作成
    canvas = tkinter.Canvas(
        app,  # キャンバスの作成先アプリ
        width=300,  # キャンバスの横サイズ
        height=300,  # キャンバスの縦サイズ
        bg="black"  # キャンバスの色
    )

    # キャンバスの配置
    canvas.place(
        x=50,  # キャンバスの配置先座標x
        y=50  # キャンバスの配置先座標y
    )

    # ラベルを作成
    global label
    label = tkinter.Label(
        app,  # ラベルの作成先アプリ
        font=("System", 20),  # ラベルのフォント
        text="ラベルです"  # ラベルに表示するテキスト
    )
    label.place(
        x=50,  # ラベルの配置先座標x
        y=5,  # ラベルの配置先座標y
    )

    # ボタンを作成
    button = tkinter.Button(
        app,  # ボタンの作成先アプリ
        text="ボタン",  # ボタンに表示するテキスト
        command = click_func #ボタンをクリック時に実行する関数
    )
    # ボタンの配置
    button.place(
        x=300,  # ボタンの配置先座標x
        y=5,  # ボタンの配置先座標y
    )
    app.bind(
        "<Key>",  # 受付けるイベント
        press_key_func  # そのイベント時に実行する関数
    )
    app.bind(
        "<KeyRelease>",  # 受付けるイベント
        release_key_func  # そのイベント時に実行する関数
    )

    #マウスボタンのクリックイベントの受付
    app.bind(
        "<Motion>",         # 受付けるイベント
        mouse_move_func     # そのイベント時に実行する関数
    )
    app.bind(
        "<ButtonPress>",    # 受付けるイベント
        mouse_click_func    # そのイベント時に実行する関数
    )
    app.bind(
        "<ButtonRelease>",  # 受付けるイベント
        mouse_release_func  # そのイベント時に実行する関数
    )

    # アプリの待機
    app.mainloop()

def mouse_click_func(event):
    global press

    # マウスボタンが押された
    press = True

def mouse_release_func(event):
    global press

    # マウスボタンが離された
    press = False
    # 現在のマウスの位置
    x = event.x
    y = event.y
    print("x = %d, y = %d  " % (x, y))



def mouse_move_func(event):
    global canvas



#キーボード押し下げ時に実行する関
def press_key_func(event):
    global label
    # 入力されたキーを取得
    key = event.keysym

    # 入力されたキーに応じてラベルを変更
    if key == "Left":
        label[ "text" ] = "左が押されました"
    elif key == "Right":
        label[ "text" ] = "右が押されました"

#キーボード Release 時に実行する関
def release_key_func(event):
    global label
    # 入力されたキーを取得
    key = event.keysym
    # 入力されたキーに応じてラベルを変更
    if key == "Left":
        label[ "text" ] = "左が離されました"
    elif key == "Right":
        label[ "text" ] = "右が離されました"

#ボタンをクリック時に実行する関数
def click_func():
    global label
    label["text"] = "クリックされました。"

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
