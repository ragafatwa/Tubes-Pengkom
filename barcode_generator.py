from barcode import EAN13

from barcode import ImageWriter

import cek_stok

cek_stok.init_object()

print(cek_stok.item_list)

for x in cek_stok.item_list:
    number = '00001111' + str(x)

    my_code = EAN13(number, writer=ImageWriter())
    my_code.save(f'barcodes/barcode_{x}')