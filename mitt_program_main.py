import mitt_program_funktioner as mp

#     # # Steg 1: Välj kommun och församling

def main():
    mp.welcome()
    skattetabell = mp.reader_csv()
    
    # steg 1: välj kommun och visa församlingar
    while True:
        kommun_val = input("\tAnge din kommun ('q' för att avsluta): ").upper().strip()
        
        if kommun_val == "Q":
            mp.avsluta_program()
        
        matchande_rader_kommun = [rad for rad in skattetabell if rad[2].upper() == kommun_val]
        
        if matchande_rader_kommun:
            print(f"\nMatchande kommuner för: {kommun_val}")
            re_choice = input("Bekräfta val? (Tryck:'Y') / Välj om val? (Tryck:'N'): ").upper().strip()
            
            if re_choice == 'N':
                continue
            elif re_choice == 'Y':
                print(f"\n\tVald kommun: {kommun_val}\n")
                print("Tillgängliga församlingar:")
                for rad in matchande_rader_kommun:
                    print(rad[3])
                break
        else:
            print("Gör om gör rätt, finns ej med")
    
    matchande_rader_forsamling = mp.val_forsamling(skattetabell)
    
    if matchande_rader_kommun and matchande_rader_forsamling:
        valda_rader = matchande_rader_kommun + matchande_rader_forsamling
        mp.berakna_nettolon(valda_rader)

    # Huvudmeny
    mp.visa_menu()
    while True:
        user_input = input("\nAnge ett val (1-7) eller tryck 'y' för att visa menyn: ").strip().upper()
        if user_input == "Y":
            mp.visa_menu()
        elif user_input == "1":
            timPris = float(input("Mata in företagets timpris (exkl. moms): "))
            antalTimmar = float(input("Ange antal arbetade timmar: "))
            bruttoInkomst, inkomstMedMoms = mp.berakna_brutto(timPris, antalTimmar)
            mp.skriva_ut_faktura(antalTimmar, timPris, bruttoInkomst, inkomstMedMoms)
        elif user_input == "2":
            bruttoLon = float(input("Ange önskad bruttolön: "))
            ag, tp, se, total = mp.berakna_lone_kostnad(bruttoLon)
            mp.skriv_ut_lonekostnad(bruttoLon, ag, tp, se, total)
        elif user_input == "3":
            pass
        elif user_input == "4":
            pass
        elif user_input == "5":
            mp.stapel_diagram()
        elif user_input == "6":
            mp.berakna_netto()
        elif user_input == "7":
            mp.avsluta_program()
        else:
            print("Ogiltigt val! Försök igen.")

if __name__ == "__main__":
    main()