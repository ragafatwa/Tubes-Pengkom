import os
# Struktur item_lisit

'''

item_id: {
    nama: ,
    harga: ,
    stok: 
},
item_id: {
    ...
}
...

'''

item_list = {}

rerun = []

# Translate dari txt jadi object
def init_object():
    f = open('list_barang.txt', 'r+')
    i = 0
    init = []
    for x in f:
        temp = x.split(',')
        rerun.append(temp)
        if i == 0:
            init = temp
        else:
            temp[-1] = int(temp[-1])
            temp[-2] = int(temp[-2])
            args = {
                init[1]: temp[1],
                init[2]: temp[2],
                init[3]: temp[3]
            }
            item_list.update({temp[0]: args})
        i += 1
    if os.stat("list_barang.txt").st_size == 0:
        f.write('item_id,nama,harga,stok,')
    f.close()

# Fungsi untuk nge cek 1 item ada atau habis
def cek_stok(item_id, qty):
    try:
        if item_list[item_id]['stok'] > 0 and item_list[item_id]['stok'] - qty >= 0:
            return [True, item_list[item_id]['stok']]
        else:
            return [False, item_list[item_id]['stok']]
    except:
        print("Maaf barang tidak tersedia")
        return False

# Fungsi untuk nge print semua stok yang ada
def get_all_stok():

    return item_list

# Fungsi Translate dari Object ke List
def obj_to_list():
    ans = []
    if len(rerun) > 0:
        ans = [','.join(rerun[0])]
    else:
        ans = ['item_id,nama,harga,stok,\n']

    for val in item_list:
        temp = [val,item_list[val]['nama'],str(item_list[val]['harga']),str(item_list[val]['stok'])]
        temp = ','.join(temp) + '\n'
        ans.append(temp)
    # print('ini ans',ans)
    temp = ans[0]
    ans.pop(0)
    ans.sort()
    ans = [temp] + ans
    return ''.join(ans)

# Fungsi untuk update dan tambah item
def update_item(item_id, args):
    for key, val in args.items():

        if item_list.get(item_id):
            item_list[item_id].update({key: val})
        else:
            item_list.update({item_id: {}})
            item_list[item_id].update({key: val})
    
    # tulis kembali ke file txt
    f = open('list_barang.txt', 'w')
    ans = obj_to_list()
    f.write(ans)
    f.close()

def update_stok(arr):
    for x in arr:
        item_list[x[3]]['stok'] -= x[1]
    
    f = open('list_barang.txt', 'w')
    ans = obj_to_list()
    f.write(ans)
    f.close()
