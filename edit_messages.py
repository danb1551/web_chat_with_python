from datetime import datetime

# Globální seznam zpráv (musí být načten z Flask aplikace nebo jiného úložiště)
zpravy = [
    {'jmeno': 'Alice', 'text': 'Ahoj světe!', 'cas': datetime.now().strftime("%H:%M:%S")},
    {'jmeno': 'Bob', 'text': 'Jak se máš?', 'cas': datetime.now().strftime("%H:%M:%S")}
]

def zobraz_zpravy():
    print("\nAktuální zprávy:")
    for i, item in enumerate(zpravy):
        print(f"{i + 1}. {item['jmeno']} ({item['cas']}): {item['text']}")

def upravit_zpravu():
    zobraz_zpravy()
    try:
        inp = int(input("Zadejte číslo zprávy, kterou chcete upravit: ")) - 1
        if 0 <= inp < len(zpravy):
            choice = input("Chcete upravit (j)méno nebo (t)ext? ").lower()
            if choice == 'j':
                nove_jmeno = input("Zadejte nové jméno: ")
                zpravy[inp]['jmeno'] = nove_jmeno
                print(f"Jméno bylo změněno na '{nove_jmeno}'")
            elif choice == 't':
                novy_text = input("Zadejte nový text zprávy: ")
                zpravy[inp]['text'] = novy_text
                print(f"Text zprávy byl změněn na '{novy_text}'")
            else:
                print("Neplatná volba. Zkuste znovu.")
        else:
            print("Zadané číslo zprávy není platné.")
    except ValueError:
        print("Zadali jste neplatné číslo. Zkuste to znovu zadáním čísla zprávy.")

if __name__ == '__main__':
    while True:
        zobraz_zpravy()
        inpu = input("Zadejte '/stop' pro ukončení nebo Enter pro pokračování: ")
        if inpu == '/stop':
            with open('zpravy.txt', 'w') as f:
                for item in zpravy:
                    f.write(f"{item['jmeno']} ({item['cas']}): {item['text']}\n")
            print("Program ukončen.")
            break
        upravit_zpravu()
