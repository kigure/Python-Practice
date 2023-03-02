# 自動販売機
# 投入した金額がジュースの値段以下の場合にtrue それ以外はfalse
# trueの場合はジュースが出て、falseはジュースは出ずに足りない金額を告知
# ジュースの値段より多く金額が投入された場合は、ジュースが出てかつ money - JUICE の値が出力


def vending_machine():

    import random

    lucky = random.randint(1, 3)

    JUICE = 150
    money = input("いくら入れますか?:")
    money = int(money)

    if money > JUICE and lucky == 1:
        print("ジュースゲット！当たりです！" + str(money - JUICE) + "円のお釣りです")
    elif money > JUICE:
        print("ジュースゲット" + str(money - JUICE) + "円のお釣りです")
    elif money == JUICE and lucky == 1:
        print("ジュースゲットお釣りなし" + "当たりです")
    elif money == JUICE:
        print("ジュースゲットお釣りなし")
    else:
        print("ジュースは出ません" + str(JUICE - money) + "円足りません")


vending_machine()

# 追加したい機能
# 辞書型かリスト型を使って、いろんな種類のドリンクを購入できるようにする
# ドリンクひとつひとつに値(値段)を設定する
# 消費税を追加する 標準税率は10%だけどドリンクは生活必需品になるから軽減税率が適用されるため、税率は8%だ。
# 消費税 = 商品価格 * 0.08  税込価格 = 商品価格 + 消費税
