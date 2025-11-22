# 题目1（购物程序）

# 商品价格列表
products = {
    '01':{'名称':'苹果','价格':3},
    '02':{'名称':'梨','价格':4},
    '03':{'名称':'笔','价格':1.5},
    '04':{'名称':'笔记本','价格':5},
    '05':{'名称':'短袖上衣','价格':30},
    '06':{'名称':'裙子','价格':25},
}

total = 0 # 总金额

print("===欢迎来到“应有尽有”杂货店===")

# 显示商品列表
print("商品列表：")
for num, product_info in products.items():
    name = product_info['名称']
    price = product_info['价格']
    print(f"{num}.{name} - ${price}")

# 购物中......
while True:
    choice = input("\n请选择商品编号（01-06），输入0结束购物：")

    # 条件判断
    if choice == '0':
        break
    elif choice in products:
        product_name = products[choice]['名称']
        price = products[choice]['价格']
        total += price
        print(f"添加了{product_name}，当前总计：${total:.1f}")
    else:
        print("输入错误，请选择01-06的商品编号")

# 购物结束
print(f"\n购物结束，总金额：${total:.1f}")
print("谢谢光临！！！")
