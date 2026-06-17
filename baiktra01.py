products = [

    {
        "id": "SP001",
        "name": "Chuot",
        "price": 25000,
        "stock": 15,
        "safety_stock": 20,
        "total_price": 3750000,
        "state": "canh bao"
    }
]

def menu():
    print("="*60)
    print("MENU")
    print("="*60)
    print("1. Hien thi danh sach kho hang")
    print("2. Khai bao san pham moi")
    print("3. Cap nhap so luong va gia von")
    print("4. Xoa san pham khoi danh muc")
    print("5. Tim kiem san pham")
    print("6. Thong ke trang thao kho hang")
    print("7. Phan loai trang thai tu dong")
    print("8. Thoat chuong trinh")
    print("="*60)

def display_product():
    print("\nHIEN THI DANH SACH KHO HANG\n")
    if not products:
        print("Kho hang khong co san pham!")
        return
    print("-"*100)
    print(f"{"Ma SP":^10} | {"Ten SP":^20} | {"Gia Von":^10} | {"So Luong":^10} | {"Dinh Muc":^10} | {"Tong Gia":^10} | {"Trang Thai":^10}")
    print("-"*100)
    for table in products:
        print(f"{table["id"]:^10} | {table["name"]:^20} | {table["price"]:^10,} | {table["stock"]:^10,} | {table["safety_stock"]:^10,} | {table["total_price"]:^10,} | {table["state"]:^10}")
    print("-"*100)


def value_input(value_name):
    while True:
        try:

            raw_value = input(f"Nhap {value_name}: ").strip()
            if raw_value == "":
                print("Gia tri khong duoc de rong!")
                continue
            fixed_value = int(raw_value)
            if fixed_value < 0:
                print("Gia tri khong duoc nho hon 0")
                continue

            break
        except ValueError:
            print("Sai kieu du lieu!")
            continue
    return fixed_value

def adjust_product(title = "add"):
    while True:
        try:
            raw_id = input("Nhap id: ").strip()
            if raw_id == '':
                print("id khong duoc de trong!")
                continue
            if not raw_id.startswith("SP"):
                print("ID bat dau phai la SP!")
                continue
            if not raw_id[2:].isdigit():
                print("id sau SP phai la so nguyen!!")
                continue
            
            found_id = False
            for table in products:
                if table["id"] == raw_id:
                    found_id = True
                    if title == "update":
                        print("Da tim thay id can thay doi!")
                        break
                    else:
                        print("ID da ton tai!")
                        break
            if not found_id:
                if title == "update":
                    print("Khong tim thay id!")
                    return
                else:
                    break
            else:
                if title == "update":
                    break
                continue

        except ValueError:
            print("Sai kieu du lieu!")
            continue


    while True:
        raw_name = input("Nhap ten: ").strip()
        if raw_name == "":
            print("Ten khong duoc de rong!")
            continue
        break

    p_id = raw_id
    p_name = raw_name
    p_price = value_input("Don gia von")
    p_stock = value_input("So luong ton dau ky")
    p_safety_stock = value_input("Dinh muc toi thieu")
    p_total_price = p_price * p_stock
    p_state = "Het hang"

    if p_safety_stock == 0:
        p_state = "Het hang"
    elif p_stock < p_safety_stock:
        p_state = "Canh bao"
    elif p_stock >= p_safety_stock and p_stock <= p_safety_stock*3:
        p_state = "An toan"
    elif p_stock > p_safety_stock*3:
        p_state = "Qua tai"
    if title == "add":
        products.append({
            "id": p_id,
            "name": p_name,
            "price": p_price,
            "stock": p_stock,
            "safety_stock": p_safety_stock,
            "total_price": p_total_price,
            "state": p_state


        })
        print("Them thanh cong!")
    elif title == "update":
        for table in products:
            if table["id"] == p_id:
                table["id"] = p_id
                table["name"] = p_name
                table["price"] = p_price
                table["stock"] = p_stock
                table["safety_stock"] = p_safety_stock
                table["total_price"] = p_total_price
                table["state"] = p_state
                print("Cap nhap thanh cong!")
                break
    else:
        print("Sth WRONG!!")
def delete_product():
    print("\nXOA SAN PHAM\n")
    delete_id = input("Nhap id muon xoa: ").strip()
    found_id = False
    for table in products:
        if table["id"] == delete_id:
            found_id = True
            while True:
                p_choice = input("Ban co chac muon xoa san pham khoi danh muc khong?(Y/N): ").strip().upper()
                if p_choice == "Y":
                    products.remove(table)
                    print("Xoa thanh cong!")
                    break
                elif p_choice == "N":
                    break
                else:
                    print("Lua chon sai moi nhap lai!")
            break

    if not found_id:
        print("Khong tim thay id!")

def find_product():
    while True:
        print("\nTIM KIEM SAN PHAM\n")
        print("1. theo ma")
        print("2. Theo ten")
        p_choice = input("Chon (1-2):")
        match p_choice:
            case '1':
                found_id = False
                find_by_id = input("Nhap id san pham muon tim: ").strip()
                for table in products:
                    if table["id"] == find_by_id:
                        found_id = True
                        print(f"{table["id"]:^10} | {table["name"]:^20} | {table["price"]:^10,} | {table["stock"]:^10,} | {table["safety_stock"]:^10,} | {table["total_price"]:^10,} | {table["state"]:^10}")
                        break
                if not found_id:
                    print("Khong tim that sp!")
                break
            case '2':
                found_id = False
                find_by_name = input("Nhap ten san pham muon tim: ").strip().upper()
                for table in products:
                    if str(table["name"]).upper() == find_by_name:
                        found_id = True
                        print(f"{table["id"]:^10} | {table["name"]:^20} | {table["price"]:^10,} | {table["stock"]:^10,} | {table["safety_stock"]:^10,} | {table["total_price"]:^10,} | {table["state"]:^10}")
                        break
                if not found_id:
                    print("Khong tim that sp!")
                break
            case _:
                print("Lua chon sai moi nhap lai!")

def main():
    while True:
        menu()
        p_choice = input("Nhap lua chon(1-8): ")
        match p_choice:
            case '1':
                display_product()
            case '2':
                adjust_product("add")
            case '3':
                adjust_product("update")
            case '4':
                delete_product()
            case '5':
                find_product()
            case '6':
                print("Hi")
            case '7':
                print("Hi")
            case '8':
                print("Thoat chuong trinh!")
                break
            case _:
                print("Nhap sai moi nhap lai!")





if __name__ == "__main__":
    main()