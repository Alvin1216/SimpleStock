from tkinter import *
import twstock
import time

#超簡單看盤by Alvin
#使用twstock
#放入你想看的股票代碼在stock_code中
stock_code=['5255','1101','1437','2302','2303','2311','2325','2230']
stock_time=[]#時間
stock_name=[]#公司名
latest_trade_price=[]#最近成交價
accumulate_trade_volume	=[]#累積成交量
best_bid_price=[]#買進
best_ask_price=[]#賣出
open=[]#開盤
high=[]#最高
low=[]#最低
upperson=[]

blank_width=12
background_color='black'
text_color='white'

#從twstock拿即時的資料
#from證券交易所
def stock_up():
    for i in stock_code:
        stock = twstock.realtime.get(i)
        stock_name.append(stock['info']['name'])
        stock_time.append(stock['info']['time'])
        latest_trade_price.append(stock['realtime']['latest_trade_price'])
        accumulate_trade_volume.append(stock['realtime']['accumulate_trade_volume'])
        best_bid_price.append(stock['realtime']['best_bid_price'][0])
        best_ask_price.append(stock['realtime']['best_ask_price'][0])
        open.append(stock['realtime']['open'])
        high.append(stock['realtime']['high'])
        low.append(stock['realtime']['low'])

        a = float(stock['realtime']['latest_trade_price'])
        b = float(stock['realtime']['open'])
        upperson.append(format(a - b, '.2f'))

#ui更新
def ui_up():
    titles = ['股票代碼', '公司名稱', '最近成交價', '漲跌', '累績成交量', '買進', '賣出', '開盤', '最高', '最低']
    r = 0
    for t in range(0, len(titles)):
        Label(root,text=titles[t], relief=GROOVE, width=blank_width, font=("微軟正黑體", 16),background=background_color,fg=text_color).grid(row=0, column=r)
        r = r + 1
    for p in range(0, len(stock_code)):
        Label(root,text=stock_code[p], relief=GROOVE, width=blank_width, font=("微軟正黑體", 16),background=background_color,fg=text_color).grid(row=p + 1, column=0)
        Label(root,text=stock_name[p], relief=GROOVE, width=blank_width, font=("微軟正黑體", 16),background=background_color,fg=text_color).grid(row=p + 1, column=1)
        if (float(upperson[p]) > 0):
            Label(root,text=latest_trade_price[p], relief=GROOVE, fg="red", width=blank_width, font=("微軟正黑體", 16),background=background_color).grid(row=p + 1, column=2)
            Label(root,text=upperson[p], relief=GROOVE, width=blank_width, fg="red", font=("微軟正黑體", 16),background=background_color).grid(row=p + 1, column=3)
        elif (float(upperson[p]) < 0):
            Label(root,text=latest_trade_price[p], relief=GROOVE, fg="green", width=blank_width, font=("微軟正黑體", 16),background=background_color).grid(row=p + 1, column=2)
            Label(root,text=upperson[p], relief=GROOVE, width=blank_width, fg="green", font=("微軟正黑體", 16),background=background_color).grid(row=p + 1,column=3)
        else:
            Label(root,text=latest_trade_price[p], relief=GROOVE, width=blank_width, font=("微軟正黑體", 16),background=background_color,fg=text_color).grid(row=p + 1, column=2)
            Label(root,text=upperson[p], relief=GROOVE, width=blank_width, font=("微軟正黑體", 16),background=background_color,fg=text_color).grid(row=p + 1, column=3)
        Label(root,text=accumulate_trade_volume[p], relief=GROOVE, width=blank_width, font=("微軟正黑體", 16),background=background_color,fg=text_color).grid(row=p + 1,column=4)
        Label(root,text=best_bid_price[p], relief=GROOVE, width=blank_width, font=("微軟正黑體", 16),background=background_color,fg=text_color).grid(row=p + 1, column=5)
        Label(root,text=best_ask_price[p], relief=GROOVE, width=blank_width, font=("微軟正黑體", 16),background=background_color,fg=text_color).grid(row=p + 1, column=6)
        Label(root,text=open[p], relief=GROOVE, width=blank_width, font=("微軟正黑體", 16),background=background_color,fg=text_color).grid(row=p + 1, column=7)
        Label(root,text=high[p], relief=GROOVE, width=blank_width, font=("微軟正黑體", 16),background=background_color,fg=text_color).grid(row=p + 1, column=8)
        Label(root,text=low[p], relief=GROOVE, width=blank_width, font=("微軟正黑體", 16),background=background_color,fg=text_color).grid(row=p + 1, column=9)

    Label(root,text=stock_time[0][2:16], relief=FLAT, width=blank_width, font=("Arial", 12)).grid(row=len(stock_code) + 1,column=9)
    Label(root,text=time.strftime("%H:%M", time.localtime()), relief=FLAT, width=blank_width, font=("Arial", 12)).grid(row=len(stock_code) + 1, column=8)

#每次拿資料前把list徹底清空
def clear():
    stock_time.clear()
    stock_name.clear()
    latest_trade_price.clear()
    accumulate_trade_volume.clear()
    best_bid_price.clear()
    best_ask_price.clear()
    open.clear()
    high.clear()
    low.clear()
    upperson.clear()

#更新(再跑一次)
def update():
    clear()
    stock_up()
    ui_up()
    #print(time.strftime("%H:%M:%S", time.localtime()))
    root.after(60000, update)
    #一分鐘更新一次
root = Tk()
root.title("看股票嚕")
root.after(100, update)
#update()
root.mainloop()
