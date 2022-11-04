import cek_stok
import clear
import payment

daftar_menu = cek_stok.get_all_stok()
daftar_belanja = []

# fungsi untuk nge print daftar item
def tampilan():
    # Judul
    print("======================================================")
    print("||           Selamat Datang di Sistem USER          ||")
    print("======================================================")

    print("||" + "Daftar Item".center(50) + "||")

    for x in daftar_menu:
        print("||" + str('\t'+x).expandtabs(2).ljust(8) + '|' + str('\t'+daftar_menu[x]['nama']).expandtabs(3).ljust(25) + '|' +  str('\t' + "Rp{:,.1f}".format(daftar_menu[x]['harga'])).expandtabs(3).ljust(15) + "||")

    print("======================================================")

def show_daftar_belanja():
    clear.cls()
    # Judul
    print("=====================================================")
    print("||                 Daftar Belanja                  ||")
    print("=====================================================")

    i = 1
    for x in daftar_belanja:
        print("||" +
        str('\t'+str(i)).expandtabs(2).ljust(4) +
        '|' +
        str('\t'+x[0]).expandtabs(3).ljust(22) +
        '|' +
        str('\t' + str(x[1])).expandtabs(2).ljust(4) +
        '|' + '\t'.expandtabs(3) +
        'Rp{:,.1f}'.format(x[2]).ljust(13) +
        "||")
        i += 1

    print("=====================================================")

def kamera():
    import cv2
    from pyzbar.pyzbar import decode

    cap = cv2.VideoCapture(0)

    if (cap.isOpened() == False):
        print("Unable to read camera feed!")
    
    isi_barcode = ''
    type_barcode = ''
    while(True):
        ret, frame = cap.read()

        if ret == True:
            detectedBarcodes = decode(frame)

            for barcode in detectedBarcodes:
                (x, y, w, h) = barcode.rect
                cv2.rectangle(frame, (x-10, y-10), (x+w+10, y + h+10), (255,0,0), 2)
                isi_barcode = barcode.data
                type_barcode = barcode.type
                # frame = cv2.flip(frame, 1)
            cv2.imshow('frame', frame)
            if isi_barcode != '':
                break

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        else:
            break
    # print(isi_barcode, type_barcode)
    cap.release()
    cv2.destroyAllWindows()
    isi_barcode = str(isi_barcode)
    isi_barcode = isi_barcode[2:len(isi_barcode)-2]
    print(isi_barcode)
    return isi_barcode

def terima_masukan():
    clear.cls()
    tampilan()

    scan = input("Scan barcode? y/n: ")
    if scan == "y" or scan == 1:
        print("Masukkan kode item: ", end=" ")
        id = kamera()
        id = id[8:12]
        print(id)
        if id == '':
            id = input("Masukkan kode item: ")
    else:
        id = input("Masukkan kode item: ")
    
    while True:
        try:
            qty = int(input("Masukkan jumlah: "))
            while qty == 0:
                qty = int(input("Masukkan jumlah: "))
            diskon = float(input("Masukkan diskon item: "))
            break
        except:
            print("Tolong Masukkan Angka")
            continue

    # input("Press enter to continue...")
    # while True:
    #     try:
    #         id = input("Masukkan kode item: ")
    #         qty = int(input("Masukkan jumlah: "))
    #         diskon = float(input("Masukkan diskon item: "))
    #         break
    #     except:
    #         print("Tolong Masukkan angka")
    #         continue
        

    hasil_cek = cek_stok.cek_stok(id, qty)

    if hasil_cek[0]:
        daftar_belanja.append([daftar_menu[id]['nama'], qty, daftar_menu[id]['harga'] * qty * (100 - diskon)/100, str(id)])
    else:
        if hasil_cek[1] == 0:
            print("Maaf stok saat ini kosong")
        else:
            print("Maaf stok saat ini tidak mencukupi permintaan")
        input("Press Enter to continue...")
        terima_masukan()

# Fungsi untuk ngecek ada tambahan atau tidak
def tambahan():
    next = input("Ada tambahan? y / n: ")
    if next == 'y':
        return True
    elif next == 'n':
        return False
    else:
        tambahan()

def belanjaan_fix():
    check = input('Apakah belanjaan sudah benar? y / n: ')
    if check == 'y':
        return True
    elif check == 'n':
        return False

def list_del():
    idx_del = int(input("No item yang di delete: "))
    daftar_belanja.pop(idx_del-1)

def Total_harga():
    sum = 0
    for x in daftar_belanja:
        sum += x[2]
    return sum

# Fungsi untuk menjalankan sistem user
def sistem_user():

    isRun = True
    while isRun:
        terima_masukan()

        if tambahan():
            continue
        else:
            isRun = False
    

    isRun = True
    while isRun:
        # Print daftar belanja
        show_daftar_belanja()
        if belanjaan_fix():
            isRun = False
        else:
            add_or_del = input("Mau delete atau tambah? add / del : ")
            if add_or_del == 'add':
                terima_masukan()
            else:
                list_del()
    
    clear.cls()
    show_daftar_belanja()
    total_harga = Total_harga()
    print(f"Total harga: " + "Rp{:,.1f}".format(total_harga))

    print("masukkan diskon: ")
    diskon = float(input("> "))
    clear.cls()
    show_daftar_belanja()
    total_harga = total_harga * (100-diskon)/100
    print(f"Total harga: " + ("Rp{:,.1f}").format(total_harga))

    # payment gateway
    print("Pilih metode pembayaran:\n1. Cash\n2. Kartu\n3. E-money")
    metode = input("> ")

    if metode == '1':
        print("Masukkan jumlah uang")
        uang = float(input("> "))
        while uang < total_harga:
            print("Masukkan jumlah uang dengan benar")
            uang = float(input("> "))

        # cetak struk
        payment.receipt(daftar_belanja, diskon, total_harga, uang)
        cek_stok.update_stok(daftar_belanja)
    elif metode == '2' or metode == '3':
        payment.payment_card(daftar_belanja, diskon, total_harga)
        cek_stok.update_stok(daftar_belanja)