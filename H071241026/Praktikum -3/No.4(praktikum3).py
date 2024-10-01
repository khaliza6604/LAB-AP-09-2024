total_harga = int(input("Masukkan Total harga: Rp. "))
uang_diberikan = int(input("Masukkan uang yang diberikan:Rp.  "))
pecahan_uang = [100000, 50000, 20000, 10000, 5000, 2000, 1000]
kembalian = uang_diberikan - total_harga

for i in pecahan_uang:
    if kembalian >= i:
        lembar_uang = kembalian //i
        kembalian -= lembar_uang *i
        print(f"{lembar_uang} lembar Rp {i:,}")
    