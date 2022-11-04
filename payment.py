import datetime
import clear
import daily_retail

def check_balance(total_harga):
    balance = 500000
    if total_harga <= balance:
        return True
    return False

def check_credential(id, pw):
    if id == '1234' and pw == '1234':
        return True
    return False
        
def payment_card(daftar_belanja, diskon, total_harga):
    id = input("Masukkan no kartu: ")
    pin = input("Masukkan pin: ")

    if check_credential(id, pin):
        if check_balance(total_harga):
            print("Terima kasih sudah belanja bersama kami")
            receipt(daftar_belanja, diskon, total_harga, total_harga)
        else:
            print("Maaf saldo anda tidak mencukupi")
    else:
        print("Maaf pin anda salah")
        input("Press Enter to continue...")
        payment_card(daftar_belanja, diskon, total_harga)



def receipt(arr, diskon, tot, uang):
    kembalian = uang - tot - diskon
    clear.cls()
    daily_retail.save_data(arr, diskon, tot)
    # Judul
    date = datetime.datetime.now()
    print("=====================================================")
    print("||                  Struk Belanja                  ||")
    print("||-------------------------------------------------||")
    print(f"||            {date}           ||")
    print("=====================================================")

    i = 1
    for x in arr:
        print("||" + str('\t' + str(i)).expandtabs(2).ljust(4) + '|' +
              str('\t' + x[0]).expandtabs(3).ljust(24) + '|' +
              str('\t' + str(x[1])).expandtabs(2).ljust(4) + '|' +
              str('\t' + 'Rp' + str(x[2])).expandtabs(2).ljust(14) + "||")
        i += 1

    print("=====================================================")
    print(f"||  Total Harga :                        {tot + diskon}")
    print(f"||  Diskon      :                        {diskon}")
    print(f"||  Tunai       :                        {uang}")
    print(f"||  Kembalian   :                        {kembalian}\n\n")
