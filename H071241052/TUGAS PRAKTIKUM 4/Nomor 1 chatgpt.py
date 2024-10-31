import random

# Fungsi untuk mengambil satu kartu
def draw_card():
    # Menghasilkan angka kartu dari 2-10 dan Jack, Queen, King yang bernilai 10, dan Ace yang bernilai 11
    cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]
    return random.choice(cards)

# Fungsi untuk menghitung total nilai kartu
def calculate_total(cards):
    total = sum(cards)
    return total

# Fungsi untuk memulai permainan Blackjack
def blackjack_game():
    print("Welcome to Blackjack!")
    
    # Inisialisasi kartu pemain dan dealer
    player_cards = [draw_card()]
    dealer_cards = [draw_card()]
    
    print(f"Kartu anda sekarang adalah: {player_cards[0]}")
    print(f"Kartu dealer adalah: {dealer_cards[0]}")
    
    # Pemain menarik kartu
    while True:
        choice = input("Apakah masih akan mengambil kartu? (y/n): ").lower()
        if choice == 'y':
            player_cards.append(draw_card())
            player_total = calculate_total(player_cards)
            print(f"Kartu anda sekarang adalah: {player_total}")
            
            # Pemain kalah jika total kartu lebih dari 21
            if player_total > 21:
                print("Anda kalah, kartu anda melebihi 21.")
                return
        elif choice == 'n':
            break
        else:
            print("Pilihan tidak valid, masukkan 'y' atau 'n'.")

    # Dealer menarik kartu hingga mencapai total 17 atau lebih
    print(f"Kartu dealer sekarang adalah: {dealer_cards[0]}")
    while calculate_total(dealer_cards) < 17:
        dealer_cards.append(draw_card())
        dealer_total = calculate_total(dealer_cards)
        print(f"Kartu dealer sekarang adalah: {dealer_total}")
        
        if dealer_total > 21:
            print("Anda menang, dealer melebihi 21.")
            return

    # Menentukan hasil akhir permainan
    player_total = calculate_total(player_cards)
    dealer_total = calculate_total(dealer_cards)

    if player_total > dealer_total:
        print("Anda menang!")
    elif player_total == dealer_total:
        print("Seri!")
    else:
        print("Dealer menang!")

# Memulai permainan Blackjack
blackjack_game()
