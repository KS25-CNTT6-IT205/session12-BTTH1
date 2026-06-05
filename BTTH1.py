cart_items = [
         {
         	"id": "P001", 
         	"name": "Dien thoai iPhone 15",
         	"number": 1,
         	"price": 25000000
         },
         {
         	"id": "P002",
         	"name": "Op lung Silicon", 
         	"number": 2, 
         	"price": 150000
         }
]

while True:
    print("="*50)
    print("SHOPEE CART MANGEMENT SYSTEM".center(50))
    print("="*50)
    print("1. Xem chi tiết giỏ hàng & Tính tổng tiền\n"
          "2. Thêm sản phẩm mới / Cộng dông số lượng\n"
          "3. Cập nhật số lượng của một sản phẩm\n"
          "4. Xóa sản phẩm khởi giỏ hàng\n"
          "5. Thoát chương trình")
    print("="*50)
    choice = input("Mời bạn chọn chức năng (1-5): ").strip()

    match choice:
        case '1':
            if (len(cart_items) == 0):
                print("Hiện tại trong giỏ hàng không có sản phẩm nào!!")
                continue
            total_price = 0
            count_item = 0
            print()
            print("___ CHI TIẾT GIỎ HÀNG ___")
            print(f"{"STT":<5}|{"Mã SP":^7}|{"Tên Sản Phẩm":<40}|{"SL":<5}|{"Đơn giá":<21}|{"Thành tiền":<21}")
            print("="*104)
            for index, item in enumerate(cart_items, 1):
                print(f"{index:<5}|{item.get("id"):^7}|{item.get("name"):<40}|{item.get("number"):<5}|{item.get("price"):<20,}đ|{item.get("number")*item.get("price"):<20,}đ")
                total_price += item.get("number")*item.get("price")
                count_item += item.get("number")
            print("="*104)
            print("=> Tổng số lượng sản phẩm trong giỏ:", count_item)
            print(f"=> TỔNG TIỀN THANH TOÁN {total_price:,}đ")
            print()
        case '2':
            print()
            print("___ THÊM SẢN PHẨM MỚI HOẶC TĂNG SỐ LƯỢNG ___")
            input_pro_id = input("Nhập mã sản phẩm: ").upper()
            input_pro_name = input("nhập tến sản phẩm: ")

            while True:
                input_pro_number = input("nhập số lượng sản phẩm: ")
                if input_pro_number.isdigit():
                    input_pro_number = int(input_pro_number)
                    break
                else:
                    print("Bạn nhập số lượng không phải là số hoặc giá trị âm!!\nNhập lại")
            while True:
                input_pro_price = input("nhập giá của sản phẩm: ")
                if input_pro_price.isdigit():
                    input_pro_price = int(input_pro_price)
                    break
                else:
                    print("Bạn nhập giá tiền không phải là số hoặc giá trị âm!!\nNhập lại")
            flag = False
            for item in cart_items:
                if item.get("id") == input_pro_id:
                    print("Đã tìm thấy mã sản phẩm tồn tại trong giỏ hàng\n"
                    "Tiến hành cập nhật")
                    flag = True
                    item["number"] += input_pro_number
                    print("Thành công thêm số lượng cho sản phẩm")
                    break
            if not flag:
                print("Không tìm thấy mã sản phẩm trong giỏ hàng\n"
                "Tiến hành thêm đơn hàng vào giỏ")
                cart_items.append({
                    "id": input_pro_id, 
                    "name": input_pro_name,
                    "number": input_pro_number,
                    "price": input_pro_price
                })
                print("Thành công thêm sản phẩm cho sản phẩm")
            print()
        case '3':
            if (len(cart_items) == 0):
                print("Hiện tại trong giỏ hàng không có sản phẩm nào!!")
                continue
            print()
            print("___ CẬP NHẬT SỐ LƯỢNG SẢN PHẨM ___")
            input_pro_id = input("Nhập mã sản phẩm: ").upper()

            while True:
                input_pro_number = input("nhập số lượng sản phẩm: ")
                if input_pro_number.isdigit():
                    input_pro_number = int(input_pro_number)
                    break
                else:
                    print("Bạn nhập số lượng không phải là số hoặc giá trị âm!!\nNhập lại")
            flag = False
            for item in cart_items:
                if item.get("id") == input_pro_id:
                    print("Đã tìm thấy mã sản phẩm tồn tại trong giỏ hàng\n"
                    "Tiến hành cập nhật giá trị mới")
                    flag = True
                    item["number"] = input_pro_number
                    print("Thành công cập nhật số lượng mới cho sản phẩm")
                    break
            if not flag:
                print("Mã sản phẩm không tồn tại trong giỏ hàng của bạn!!")
            print()
        case '4':
            if (len(cart_items) == 0):
                print("Hiện tại trong giỏ hàng không có sản phẩm nào!!")
                continue
            print()
            print("___ XÓA SẢN PHẨM KHỎI GIỎ HÀNG ___")
            input_pro_id = input("Nhập mã sản phẩm: ").upper()

            flag = False
            for index, item in enumerate(cart_items):
                if item.get("id") == input_pro_id:
                    print("Đã tìm thấy mã sản phẩm tồn tại trong giỏ hàng\n"
                    "Tiến hành xóa sản phẩm khỏi giỏ hàng")
                    flag = True
                    del cart_items[index]
                    print("Thành công xóa sản phẩm")
                    break
            if not flag:
                print("Mã sản phẩm không tồn tại trong giỏ hàng của bạn!!")
            print()
            print()
        case '5':
            print()
            print("Thoát chương trình!")
            break
        case _:
            print("Bạn chọn chức năng không hợp lệ!!")