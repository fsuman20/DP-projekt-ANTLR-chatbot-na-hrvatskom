import random
import logging
from datetime import datetime
from antlr4 import *
from hrvatski_turistickiLexer import hrvatski_turistickiLexer
from hrvatski_turistickiParser import hrvatski_turistickiParser
from hrvatski_turistickiListener import hrvatski_turistickiListener

logging.basicConfig(
    filename=f'chatbot_{datetime.now().strftime("%Y%m%d")}.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

class TuristickiChatbot(hrvatski_turistickiListener):
    def __init__(self):
        self.odgovori = {
            'smjestaj': {
                'lokacija': [
                    'Na toj lokaciji možete pronaći više vrsta smještaja.',
                    'Dostupni su hoteli, apartmani i sobe na željenoj lokaciji.'
                ],
                'cijena': [
                    'Smještaj u prosjeku košta od 40 do 150 eura po noćenju.',
                    'U predsezoni i posezoni cijene su uglavnom niže.'
                ],
                'opis': [
                    'Smještaj je prilagođen raznim potrebama i kategorijama.',
                    'Većina smještaja ima dobru opremljenost i pristup internetu.'
                ]
            },
            'hrana': {
                'lokacija': [
                    'Najviše restorana nalazi se uz rivu i u samom centru.',
                    'Konobe i kafići raspoređeni su po čitavom gradu.'
                ],
                'cijena': [
                    'Obroci u restoranima kreću se od 10 do 50 eura, ovisno o ponudi.',
                    'Konobe često nude jeftinije menije, a luksuzni restorani su nešto skuplji.'
                ],
                'opis': [
                    'Restorani nude raznoliku gastronomsku ponudu s naglaskom na lokalne specijalitete.',
                    'Konobe su poznate po domaćoj atmosferi i autentičnim jelima.'
                ]
            },
            'atrakcije': {
                'lokacija': [
                    'Većina znamenitosti nalazi se u starom gradu ili uz obalu.',
                    'Parkovi i galerije raspoređeni su po različitim dijelovima grada.'
                ],
                'cijena': [
                    'Ulaznice za znamenitosti uglavnom su između 5 i 15 eura.',
                    'Neke crkve i parkovi imaju besplatan ulaz.'
                ],
                'opis': [
                    'Atrakcije su dobro očuvane, s bogatom kulturnom i povijesnom baštinom.',
                    'Znamenitosti privlače posjetitelje iz cijelog svijeta.'
                ]
            }
        }

        self.odgovori_muzej = {
            'lokacija': [
                'Mnogi muzeji smješteni su u povijesnoj jezgri.',
                'Neki su muzeji u blizini centra i lako dostupni javnim prijevozom.'
            ],
            'cijena': [
                'Ulaznice u muzej kreću se od 5 do 15 eura.',
                'Za studente i umirovljenike često postoje popusti.'
            ],
            'opis': [
                'Muzej nudi razne zbirke, često tematske izložbe i stručna vodstva.',
                'U muzeju možete pronaći eksponate iz lokalne i svjetske povijesti.'
            ]
              
        }
        
        self.ime_odgovori = [
            "Ja sam Tina, virtualni turistički vodič Hrvatske turističke zajednice.",
            "Zovem se Tina i tu sam da vam pomognem u planiranju vašeg boravka u Hrvatskoj.",
            "Moje ime je Tina, vaš AI asistent Hrvatske turističke zajednice."
        ]
        

        self.trenutni_odgovor = None

    # Listener methods
    def exitPozdravniIzraz(self, ctx):
        self.trenutni_odgovor = "Pozdrav! Kako vam mogu pomoći?"

    def exitImeUpit(self, ctx):
        self.trenutni_odgovor = random.choice(self.ime_odgovori)
        
    def exitGdjeUpit(self, ctx):
        obj = self._izvuci_objekt(ctx.lokacijski_upit())
        lok = self._izvuci_lokaciju(ctx.lokacijski_upit())

        if obj:
            if obj == 'muzej':
                odgovor = random.choice(self.odgovori_muzej['lokacija'])
            else:
                if obj in self.odgovori:
                    odgovor = random.choice(self.odgovori[obj]['lokacija'])
                else:
                    odgovor = "Trenutno nemam podataka o toj lokaciji."
            if lok:
                odgovor = f"Za {lok}: {odgovor}"
            self.trenutni_odgovor = odgovor
        else:
            self.trenutni_odgovor = "Nisam siguran koji objekt tražite."

    def exitKolikoUpit(self, ctx):
        obj = self._izvuci_objekt(ctx.cjenovni_upit())
        if obj:
            if obj == 'muzej':
                self.trenutni_odgovor = random.choice(self.odgovori_muzej['cijena'])
            else:
                if obj in self.odgovori:
                    self.trenutni_odgovor = random.choice(self.odgovori[obj]['cijena'])
                else:
                    self.trenutni_odgovor = "Nemam podatke o cijenama za taj objekt."
        else:
            self.trenutni_odgovor = "Nisam siguran na što se odnosi cijena."

    def exitKakovUpit(self, ctx):
        obj = self._izvuci_objekt(ctx.opisni_upit())
        if obj:
            if obj == 'muzej':
                self.trenutni_odgovor = random.choice(self.odgovori_muzej['opis'])
            else:
                if obj in self.odgovori:
                    self.trenutni_odgovor = random.choice(self.odgovori[obj]['opis'])
                else:
                    self.trenutni_odgovor = "Nemam detaljan opis za taj objekt."
        else:
            self.trenutni_odgovor = "Nisam siguran na što mislite."

    def exitZahvalaIzjava(self, ctx):
        self.trenutni_odgovor = "Nema na čemu! Drago mi je pomoći."

    # Helper functions
    def _izvuci_objekt(self, ctx):
        if not ctx:
            return None
        txt = ctx.getText().lower()

        if 'muzej' in txt:
            return 'muzej'
        if 'hotel' in txt or 'smjestaj' in txt or 'apartman' in txt or 'soba' in txt:
            return 'smjestaj'
        if 'restoran' in txt or 'konoba' in txt or 'kafic' in txt or 'kafić' in txt:
            return 'hrana'
        if 'plaža' in txt or 'plaza' in txt or 'znamenitost' in txt or 'atrakcija' in txt:
            return 'atrakcije'
        return None

    def _izvuci_lokaciju(self, ctx):
        if not ctx:
            return None
        for child in ctx.getChildren():
            text = child.getText().lower()
            if 'split' in text or 'zadar' in text or 'zagreb' in text or 'rijeka' in text or 'dubrovnik' in text or 'pula' in text:
                return text
            if 'dalmacija' in text or 'istra' in text or 'slavonija' in text:
                return text
        return None

def main():
    print("Hrvatski turistički chatbot je pokrenut!")
    logging.info("Chatbot started")
    chatbot = TuristickiChatbot()

    while True:
        try:
            unos = input("Vi: ").strip()
            if not unos:
                continue

            if unos.lower() in ("dovidjenja", "doviđenja", "bye", "exit"):
                print("Bot: Doviđenja! Hvala na razgovoru!")
                break

            input_stream = InputStream(unos.lower())
            lexer = hrvatski_turistickiLexer(input_stream)
            token_stream = CommonTokenStream(lexer)
            parser = hrvatski_turistickiParser(token_stream)
            tree = parser.razgovor()

            chatbot.trenutni_odgovor = None
            walker = ParseTreeWalker()
            walker.walk(chatbot, tree)

            if chatbot.trenutni_odgovor:
                print("Bot:", chatbot.trenutni_odgovor)
            else:
                print("Bot: Oprostite, nisam razumio pitanje. Možete li preformulirati?")

        except EOFError:
            print("\nBot: Doviđenja!")
            break
        except Exception as e:
            logging.error(f"Greška u main loopu: {e}")
            print("Bot: Došlo je do pogreške u obradi vašeg upita.")

if __name__ == "__main__":
    main()