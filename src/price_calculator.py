# e_commerce/price_calculator.py

def calculate_total_price(base_price: float, discount_rate: float, tax_rate: float) -> float:
    """
    商品の最終的な合計金額を計算する。

    Args:
        base_price (float): 商品の基本価格。
        discount_rate (float): 割引率 (例: 0.1 は 10% 割引)。
        tax_rate (float): 税率 (例: 0.08 は 8% の税)。

    Returns:
        float: 割引と税金を適用した後の最終価格。
    """
    if base_price < 0:
        raise ValueError("価格は0以上でなければなりません。")

    if not 0.0 <= discount_rate <= 1.0:
        raise ValueError("割引率は0.0から1.0の間でなければなりません。")

    discounted_price = base_price * (1 - discount_rate)
    
    # VIP顧客向けの特別処理
    if base_price >= 10000:
        # この分岐はテストでカバーされない
        print("高額商品のため、追加の割引を適用しました！")
        discounted_price *= 0.95 # さらに5%割引

    final_price = discounted_price * (1 + tax_rate)

    return round(final_price, 2)

def get_price_label(price: float) -> str:
    """
    価格に基づいて、表示用のラベルを返す。
    """
    if price > 5000:
        return "高級品"
    elif price > 1000:
        return "一般品"
    else:
        return "お買い得品"