def main():
    print("Dobrodošli v programu za izračun povprečnih ocen po predmetih!")
    print("Za končanje programa vnesite 'konec' v ime predmeta.")

    predmeti = {}  # Slovar za shranjevanje ocen za vsak predmet

    while True:
        ime_predmeta = input("Vnesite ime predmeta: ")
        
        if ime_predmeta.lower() == 'konec':
            break  # Uporabnik je končal z vnašanjem predmetov

        ocene = []
        while True:
            ocena = input(f"Vnesite oceno za predmet '{ime_predmeta}' (za konec vnesite 'konec'): ")
            
            if ocena.lower() == 'konec':
                break  # Uporabnik je končal z vnašanjem ocen
            
            try:
                ocena = float(ocena)
                if 1.0 <= ocena <= 10.0:
                    ocene.append(ocena)
                else:
                    print("Ocena mora biti med 1.0 in 10.0.")
            except ValueError:
                print("Vnesite veljavno številčno oceno.")

        if ocene:
            povprecna_ocena = sum(ocene) / len(ocene)
            predmeti[ime_predmeta] = povprecna_ocena

    # Izpis povprečnih ocen za vsak predmet
    print("\nPovprečne ocene po predmetih:")
    for predmet, povprecna_ocena in predmeti.items():
        print(f"{predmet}: {povprecna_ocena:.2f}")

if __name__ == "__main__":
    main()
