import random
import time

# Ödül merdiveni (TL)
# "Kim Milyoner Olmak İster?" ödül yapısı.
# 5. ve 10. sorular garanti puandır.
PRIZE_LADDER = [
    1000,    # Soru 1
    2000,    # Soru 2
    3000,    # Soru 3
    5000,    # Soru 4
    7500,    # Soru 5 (Garanti)
    10000,   # Soru 6
    15000,   # Soru 7
    30000,   # Soru 8
    50000,   # Soru 9
    100000,  # Soru 10 (Garanti)
    200000,  # Soru 11
    300000,  # Soru 12
    500000,  # Soru 13 
    1000000, # Soru 14
    5000000  # Soru 15 (Büyük Ödül)
]

GUARANTEE_LEVELS = [4, 9] 

# Sorular: Soruların listesi.
# 'q': soru metni
# 'o': seçenekler listesi
# 'a': Doğru seçenek harfi (A, B, C, D)

QUESTIONS = [
    {
        'q': "Türkiye'nin başkenti neresidir?",
        'o': ["İstanbul", "Ankara", "İzmir", "Bursa"],
        'a': "B"
    },
    {
        'q': "Hangi renk trafik ışıklarında 'dur' anlamına gelir?",
        'o': ["Yeşil", "Sarı", "Kırmızı", "Mavi"],
        'a': "C"
    },
    {
        'q': "Bir yılda kaç mevsim vardır?",
        'o': ["2", "3", "4", "5"],
        'a': "C"
    },
    {
        'q': "Mustafa Kemal Atatürk'ün anıt mezarı hangi şehirdedir?",
        'o': ["İstanbul", "Samsun", "Ankara", "İzmir"],
        'a': "C"
    },
    {
        'q': "Hangi gezegen 'Kızıl Gezegen' olarak bilinir?", # 5. Soru - Garanti
        'o': ["Venüs", "Mars", "Jüpiter", "Satürn"],
        'a': "B"
    },
    {
        'q': "Dünyanın en yüksek dağı hangisidir?",
        'o': ["K2", "Kangchenjunga", "Everest", "Lhotse"],
        'a': "C"
    },
    {
        'q': "Leonardo da Vinci'nin ünlü tablosu Mona Lisa hangi müzede sergilenmektedir?",
        'o': ["British Museum, Londra", "Prado Müzesi, Madrid", "Louvre Müzesi, Paris", "Uffizi Galerisi, Floransa"],
        'a': "C"
    },
    {
        'q': "Hangi elementin kimyasal sembolü 'O' dur?",
        'o': ["Osmiyum", "Oksijen", "Altın (Aurum)", "Azot (Nitrogen)"],
        'a': "B"
    },
    {
        'q': "Futbolda bir takımda kaç oyuncu sahada yer alır?",
        'o': ["9", "10", "11", "12"],
        'a': "C"
    },
    {
        'q': "Nobel Barış Ödülü hangi şehirde verilir?", # 10. Soru - Garanti
        'o': ["Stockholm, İsveç", "Oslo, Norveç", "Kopenhag, Danimarka", "Helsinki, Finlandiya"],
        'a': "B"
    },
    {
        'q': "Periyodik tabloda atom numarası 1 olan element hangisidir?",
        'o': ["Helyum", "Lityum", "Hidrojen", "Karbon"],
        'a': "C"
    },
    {
        'q': "Shakespeare'in ünlü trajedisi 'Hamlet' hangi ülkede geçer?",
        'o': ["İngiltere", "Danimarka", "İtalya", "İskoçya"],
        'a': "B"
    },
    {
        'q': "Işık hızı saniyede yaklaşık kaç kilometredir?",
        'o': ["150,000 km/s", "300,000 km/s", "450,000 km/s", "600,000 km/s"],
        'a': "B"
    },
    {
        'q': "Hangi Antik Dünya Harikası günümüze kadar ulaşmıştır?",
        'o': ["Rodos Heykeli", "Babil'in Asma Bahçeleri", "İskenderiye Feneri", "Keops Piramidi"],
        'a': "D"
    },
    {
        'q': "İnsan vücudunda kaç adet kemik bulunur (yetişkin bir bireyde)?", # 15. Soru - Büyük Ödül
        'o': ["206", "212", "198", "220"],
        'a': "A"
    }
]

#Jokerler
lifelines = {
    "yari_yariya": True,  # 50/50
    "telefon": True,      # Telefon
    "seyirci": True       # Seyirciye sorma
}

def display_question(question_data, question_number, current_prize, visible_options=None):
    """Displays the current question, options, and prize money."""
    print("\n" + "="*50)
    print(f"Soru {question_number + 1} / {len(QUESTIONS)}")
    print(f"Bu soru için ödül: {current_prize:,} TL")
    print("="*50)
    print(f"\nSoru: {question_data['q']}")
    
    options_to_display = question_data['o']
    option_labels = ["A", "B", "C", "D"]

    for i, option_text in enumerate(options_to_display):
        if visible_options is None or option_labels[i] in visible_options:
            print(f"  {option_labels[i]}) {option_text}")
        elif visible_options is not None: 
             print(f"  {option_labels[i]}) ---")


def use_fifty_fifty(question_data):
    """İki yanlış seçenek 50/50 de kaldırılır."""
    if not lifelines["yari_yariya"]:
        print("Yarı Yarıya joker hakkınızı zaten kullandınız!")
        return None

    print("\nYarı Yarıya joker hakkı kullanılıyor...")
    time.sleep(1)
    lifelines["yari_yariya"] = False
    
    correct_option_char = question_data['a']
    options_chars = ["A", "B", "C", "D"]
    
    incorrect_options = [opt_char for opt_char in options_chars if opt_char != correct_option_char]
    
    # Rastgele yanlış seçeneği seçer
    option_to_keep_besides_correct = random.choice(incorrect_options)
    
    visible_options = sorted([correct_option_char, option_to_keep_besides_correct])
    
    print("İki yanlış seçenek elendi. Kalan seçenekler:")
    return visible_options

def use_phone_a_friend(question_data, visible_options=None):
    """Arkadaşına Telefon Et Simüle Eder."""
    if not lifelines["telefon"]:
        print("Telefon joker hakkınızı zaten kullandınız!")
        return
    
    print("\nTelefon joker hakkı kullanılıyor... Arkadaşınız aranıyor...")
    time.sleep(2)
    lifelines["telefon"] = False

    options_chars = ["A", "B", "C", "D"]
    if visible_options: 
        available_choices = [opt for opt_char, opt in zip(options_chars, question_data['o']) if opt_char in visible_options]
        available_option_chars = visible_options
    else:
        available_choices = question_data['o']
        available_option_chars = options_chars

    correct_answer_char = question_data['a']
    
    
    if random.random() < 0.80: 
        if correct_answer_char in available_option_chars:
            friend_says = correct_answer_char
        else: 
            friend_says = random.choice(available_option_chars)
    else:
        incorrect_choices = [opt_char for opt_char in available_option_chars if opt_char != correct_answer_char]
        if incorrect_choices:
            friend_says = random.choice(incorrect_choices)
        else: 
            friend_says = correct_answer_char
            
    print(f"Arkadaşınız: 'Bence doğru cevap {friend_says}.'")
    time.sleep(1)

def use_ask_audience(question_data, visible_options=None):
    """İzleyiciye Sor Jokerini Simüle Eder."""
    if not lifelines["seyirci"]:
        print("Seyirci joker hakkınızı zaten kullandınız!")
        return

    print("\nSeyirci joker hakkı kullanılıyor... Seyircilerin oyları:")
    time.sleep(2)
    lifelines["seyirci"] = False

    options_chars = ["A", "B", "C", "D"]
    correct_answer_char = question_data['a']
    
    
    if visible_options:
        active_options_chars = visible_options
    else:
        active_options_chars = options_chars

    votes = {opt: 0 for opt in active_options_chars}
    total_percentage = 100

    
    if correct_answer_char in active_options_chars:
        correct_vote = random.randint(40, 70) 
        votes[correct_answer_char] = correct_vote
        total_percentage -= correct_vote
    
    
    other_active_options = [opt for opt in active_options_chars if opt != correct_answer_char]
    
    if other_active_options:
        if len(other_active_options) == 1: 
            votes[other_active_options[0]] = total_percentage
        else:
            
            for i, opt_char in enumerate(other_active_options):
                if i == len(other_active_options) - 1: 
                    vote_share = total_percentage
                else:
                    
                    max_share = total_percentage - (len(other_active_options) - 1 - i) 
                    vote_share = random.randint(1, max_share if max_share > 0 else 1)
                
                votes[opt_char] = vote_share
                total_percentage -= vote_share
                if total_percentage <= 0 and i < len(other_active_options) - 1: 
                    
                    for remaining_opt_idx in range(i + 1, len(other_active_options)):
                        if votes[other_active_options[remaining_opt_idx]] == 0:
                           votes[other_active_options[remaining_opt_idx]] = 0 
                    break 

    
    
    current_sum = sum(votes.values())
    if current_sum != 100 and current_sum > 0 :
        factor = 100 / current_sum
        temp_votes = {opt: round(v * factor) for opt, v in votes.items()}
        
        diff = 100 - sum(temp_votes.values())
        if active_options_chars: 
             temp_votes[active_options_chars[-1]] += diff
        votes = temp_votes


    print("Seyirci Oyları:")
    for option_char, vote_percent in sorted(votes.items()):
        if option_char in active_options_chars: 
             print(f"  {option_char}: {vote_percent}%")
    time.sleep(1)


def get_guaranteed_winnings(questions_answered_correctly):
    """Cevaplanan sorulara göre garantili parayı hesaplar."""
    if questions_answered_correctly == 0:
        return 0
    
    money = 0
    # En yüksek garanti seviyesinden geriye doğru kontrol eder
    for level_idx in sorted(GUARANTEE_LEVELS, reverse=True):
        if questions_answered_correctly > level_idx: # Garanti sorusunu geçmiş olmak gerekir
            money = PRIZE_LADDER[level_idx]
            break
    return money

def play_game():
    """Oyunu çalıştırmak için kullanılan ana fonksiyon."""
    print("Kim 500 Milyon İster'e Hoş Geldiniz!")
    print("="*50)
    player_name = input("Yarışmacımızın adı nedir? ")
    print(f"\nHoş geldin, {player_name}! Bol şans!\n")
    time.sleep(1)

    current_money = 0
    questions_answered_correctly = 0
    active_lifelines = {"Yarı Yarıya (J1)": "J1", "Telefon (J2)": "J2", "Seyirci (J3)": "J3"}
    
    
    current_visible_options = None 

    for i in range(len(QUESTIONS)):
        question_data = QUESTIONS[i]
        current_prize_for_question = PRIZE_LADDER[i]
        
        
        current_visible_options = None 

        while True: 
            display_question(question_data, i, current_prize_for_question, current_visible_options)
            
            print("\nKullanılabilir Jokerler:")
            available_jokers_display = []
            if lifelines["yari_yariya"]: available_jokers_display.append("Yarı Yarıya (J1)")
            if lifelines["telefon"]: available_jokers_display.append("Telefon (J2)")
            if lifelines["seyirci"]: available_jokers_display.append("Seyirci (J3)")
            
            if not available_jokers_display:
                print("  Joker hakkınız kalmadı.")
            else:
                print(f"  {', '.join(available_jokers_display)}")

            print("\nSeçenekler:")
            print("  Cevaplamak için (A, B, C, D)")
            if available_jokers_display:
                print("  Joker kullanmak için (J1, J2, J3)")
            print("  Çekilmek için (W)")

            user_input = input("Kararınız nedir? ").strip().upper()

            if user_input in ["A", "B", "C", "D"]:
                
                if current_visible_options and user_input not in current_visible_options:
                    print("Geçersiz seçenek. Lütfen gösterilen seçeneklerden birini girin.")
                    continue

                if user_input == question_data['a']:
                    current_money = current_prize_for_question
                    questions_answered_correctly = i + 1
                    print(f"\nDoğru cevap! {current_money:,} TL kazandınız.")
                    time.sleep(1.5)
                    if questions_answered_correctly == len(QUESTIONS):
                        print("*"*50)
                        print(f"TEBRİKLER {player_name.upper()}! BÜYÜK ÖDÜLÜ KAZANDINIZ: {current_money:,} TL!")
                        print("*"*50)
                        return # Oyun sonu
                    break # Sonraki soruya geç
                else:
                    print(f"\nYanlış cevap! Doğru cevap {question_data['a']} idi.")
                    guaranteed_money = get_guaranteed_winnings(questions_answered_correctly)
                    print(f"{player_name}, maalesef kaybettiniz. Kazandığınız miktar: {guaranteed_money:,} TL.")
                    return # Oyun sonu
            
            elif user_input == "W":
                walk_away_money = 0
                if questions_answered_correctly > 0 : 
                    walk_away_money = PRIZE_LADDER[questions_answered_correctly -1]
                
                print(f"\n{player_name}, yarışmadan çekilmeye karar verdiniz.")
                print(f"Kazandığınız toplam miktar: {walk_away_money:,} TL. Tebrikler!")
                return # Oyun sonu

            elif user_input in ["J1", "J2", "J3"]:
                if user_input == "J1" and lifelines["yari_yariya"]:
                    
                    current_visible_options = use_fifty_fifty(question_data)
                elif user_input == "J2" and lifelines["telefon"]:
                    use_phone_a_friend(question_data, current_visible_options)
                elif user_input == "J3" and lifelines["seyirci"]:
                    use_ask_audience(question_data, current_visible_options)
                else:
                    print("Bu jokeri zaten kullandınız veya geçersiz joker kodu.")
                
            else:
                print("Geçersiz giriş. Lütfen A, B, C, D, J1, J2, J3 veya W girin.")
            
            time.sleep(1) 

    print(f"\nOyun bitti! {player_name}, katıldığınız için teşekkürler!")

if __name__ == "__main__":
    play_game()