print("======================")
harga_baju     = int(input("masukkan harga baju"))

potongan_harga = harga_baju * 10/100


if harga_baju > 100000 :
    potongan_harga = harga_baju * 10/100

total_harga = harga_baju - potongan_harga
