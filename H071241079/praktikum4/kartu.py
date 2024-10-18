import random

def ambil_kartu():
    return random.randint(1, 10)
def main():
    print("Welcome to blackjack!")

    kartu_pemain = ambil_kartu()
    kartu_dealer = ambil_kartu()
    print(f"Kartu anda sekarang adalah: {kartu_pemain}")

    while True: 
        ambil = input("Apakah masih akan mengambil kartu? (y/n): ").lower()
        if ambil == 'y':
            kartu_pemain += ambil_kartu()
            print(f"Kartu anda sekarang adalah: {kartu_pemain}")
            if kartu_pemain > 21:
                print("Anda kalah1 Total kartu anda melebihi 21.")
                return
            else:
                break
            while kartu_dealer < 17:
                kartu_dealer  += ambil_kartu()
                print(f"Kartu dealer sekarang adalah:{kartu_dealer}")
                if kartu_dealer > 21:
                    print("Anda menang! Dealer melebihi 21.")
                elif kartu_pemain > kartu_dealer:
                    print(f"Anda menang!")
                elif kartu_pemain == kartu_dealer:
                    print("Seri!")
                else:
                    print("Dealer menang!") 

main()

        
