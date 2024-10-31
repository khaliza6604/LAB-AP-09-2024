import random

print("welcome to blackjack!")

def ambil_kartu():    
    cards = random.randint(1, 11)
    return cards


def calculate_total(cards):
    total = sum(cards)
    return total


def blackjack_game():
    pemain = [ambil_kartu()]
    dealer = [ambil_kartu()]

    print(f"kartu anda sekarang adalah {pemain[0]} ")

    while True:

        pilihan = input("Apakah masih akan mengambil kartu?(y/n): ").lower()
        if pilihan == "y":
            pemain.append(ambil_kartu())
            p_total = calculate_total(pemain)
            print(f"Kartu anda sekarang adalah: {p_total}")
            if p_total > 21:
                print("Anda kalah, kartu anda melebihi 21")
                return

        elif pilihan == "n":
            break
        else:
            print("pilihan tidak valid, masukkan 'y' atau 'n'.")

    print(f"Kartu dealer sekarang {dealer[0]}")
    while calculate_total(dealer) < 17:
        dealer.append(ambil_kartu())
        d_total = calculate_total(dealer)
        print(f"Kartu dealer sekarang adalah: {d_total}")
        if d_total > 21:
            print("Anda menang!")
            return
        #jika tak ada yg melebihi 21
    p_total = calculate_total(pemain)
    d_total = calculate_total(dealer)
    if p_total > d_total:
        print("Anda menang!")
    elif p_total == d_total:
        print("Seri!")
    else:
        print("Dealer menang!")
print(blackjack_game())

    