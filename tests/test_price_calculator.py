# tests/test_price_calculator.py

import pytest
from src.price_calculator import calculate_total_price, get_price_label

def test_calculate_total_price_normal_case():
    """通常の割引と税金が正しく計算されるかテスト"""
    # 1000円の商品に10%の割引と8%の税金
    # 1000 * 0.9 = 900
    # 900 * 1.08 = 972
    assert calculate_total_price(base_price=1000.0, discount_rate=0.1, tax_rate=0.08) == 972.00

def test_calculate_total_price_no_discount():
    """割引がない場合の計算をテスト"""
    # 500円の商品に割引なし、10%の税金
    # 500 * 1.10 = 550
    assert calculate_total_price(base_price=500.0, discount_rate=0.0, tax_rate=0.10) == 550.00

def test_calculate_total_price_with_invalid_discount_rate():
    """不正な割引率で例外が発生するかテスト"""
    with pytest.raises(ValueError, match="割引率は0.0から1.0の間でなければなりません。"):
        calculate_total_price(base_price=100.0, discount_rate=1.1, tax_rate=0.10)
        
def test_calculate_total_price_with_minus_base_price():
    """base_priceがマイナスの場合に例外が発生するかテスト"""
    with pytest.raises(ValueError, match="価格は0以上でなければなりません。"):
        calculate_total_price(base_price=-100.0, discount_rate=0.1, tax_rate=0.10)    

# -----------------
# 意図的に不足しているテストケース
# -----------------
# - base_priceがマイナスの場合のテストがない
# - base_priceが高額商品の場合のテストがない
# -----------------


def test_get_price_label_luxury():
    """価格ラベルが「高級品」になるかテスト"""
    assert get_price_label(price=6000) == "高級品"

def test_get_price_label_normal():
    """価格ラベルが「一般品」になるかテスト"""
    assert get_price_label(price=1500) == "一般品"

def test_get_price_label_budget():
    """価格ラベルが「お買い得品」になるかテスト"""
    # このテストケースはカバレッジを100%にしないために意図的に不足している
    assert get_price_label(price=800) == "お買い得品"