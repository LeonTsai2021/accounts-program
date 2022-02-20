from fileinput import filename
import os  # os的權限

def read_file(filename):
    products = []
    with open(filename, 'r', encoding='utf-8')as f:
        for line in f:
            if'name,price' in line:
                continue
            name, price = line.strip().split(',')
            products.append([name, price])
    return products  # 回傳products裝有內容的清單
# 讓使用者輸入
def user_input(products):
    while True:
        name = input('請輸入商品名稱: ')
        if name == 'q':
            break
        price = input('請輸入商品價格: ')
        products.append([name, price])
    return products
# 印出使用者輸入的資料
def print_products(products):
    for product in products:
        print(product[0], '價格是:', product[1])
# 寫入檔案
def write_file(filename,products):
    with open(filename, 'w', encoding='utf-8')as f:
        f.write('name,price\n')
        for p in products:
            f.write(p[0] + ',' + p[1] + '\n')
    print('成功把資料輸入至檔案')

def main():
    filename = 'products.csv'
    products=[]
    if os.path.isfile(filename):
        products = read_file(filename)
        print('找到該記帳檔案')
        products = user_input(products)
        print_products(products)
        write_file('products.csv',products)
    else:
        print('找不到該檔案，為您建製新的記帳excel檔案')
        products = user_input(products)
        print_products(products)
        write_file('products.csv',products)

main()