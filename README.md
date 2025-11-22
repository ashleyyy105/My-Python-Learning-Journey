# My-Python-Learning-Journey
这是我写过的最满意的Python程序的代码，用来记录我的Python学习历程。

## 项目内容
- **【购物程序】**(`题目1购物程序.py`)
  - 功能：统计商品价格
 
## 运行指南
1. 安装Python
2. 复制本仓库至本地：
   ```bash
   git clone https://github.com/[ashleyyy105]/My-Python-Learning-Journey.git
   ```
3. 运行程序：
   ```bash
   cd My-Python-Learning-Journey
   题目1购物程序.py
   ```
## 核心代码
```python
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

**学习心得与规划**
1. 浏览了GitHub上其他优秀项目后，我发现应该清晰的README、规范的代码结构是非常重要的。这让我意识到代码不只是给机器运行，更是写给人看的。这让我学会了如何系统地组织和管理一个个人项目，并从优秀的项目中获益良多。
2. 透过GitHub这个网站，我可以非常直观的了解到我的编程能力、学习轨迹和项目经验，这对于我后续学习和未来求职也是非常有帮助的。
