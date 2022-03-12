#ひとり用
import random
import re

# 半角数字判定用関数
def ishalfnum(s):
    if re.fullmatch("[0-9]+", s):
        return True
    else:
        return False


# 桁数 (0 < Digit < 11)
print("桁数を入力してください:",end="")
Digit = int(input())

while  Digit < 1 or Digit > 10: 
    print ("2~11で入力してください")
    print("桁数を入力してください:",end="")
    Digit = int(input())

# 正解の数字を一桁ずつランダムに決定
# 配列要素はint型
Ans_list = []
for _ in range(Digit):
    n = random.randint(0,9)
    # 既に選ばれている数字の場合、選びなおし
    while(n in Ans_list):
        n = random.randint(0,9)
    Ans_list.append(n)

# 正解の数字リストを一つに連結　str型
Ans = "".join(map(str, Ans_list))

# -----ゲームスタート-----
print("スタート")

for i in range(1,11):

    # Good,Greatを定義
    eat = 0
    bite = 0

    print(i,"回目のチャレンジ！")
    print(Digit,"桁の数値を入力してください:", end="")
    A = input()

    # ---ここからエラーの処理----
    # 桁数が多い/少ない    
    # 半角数字以外が入っている
    # 同じ数字が入っている 重複時dup>Digit
    dup = 0
    while len(A) != Digit or ishalfnum(A) == False or dup != Digit  :

        if len(A) != Digit or ishalfnum(A) == False:
            print("※ 半角数字",Digit,"桁で入力してください")

        dup = 0
        for a in range(len(A)):
            for b in range(len(A)):
                if A[a] == A[b]:
                    dup = dup+1

        if dup != Digit:
            print("※ 一つの数字につき、一度まで使用できます。")
        else:
            break
        
        #再度入力
        print(Digit,"桁の数値を入力してください:", end="")
        A = input()


    # ---ここまでエラーの処理---
    
    # bite,eatの換算
    for y in range(0,Digit):
        if(int(A[y]) == Ans_list[y]):
            eat = eat+1
        elif(int(A[y]) in Ans_list):
            bite = bite+1

    # if →（不正解時）10回目までは繰り返し , else →（正解時）ゲーム終了
    if eat != Digit:
        print("eat:",eat)
        print("bite:",bite)
    else:
        print("正解です！")
        break


if eat != Digit:
    print("残念！答えは",Ans,"です。")