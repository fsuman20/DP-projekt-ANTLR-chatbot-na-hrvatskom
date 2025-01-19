grammar hrvatski_turisticki;

razgovor: (pozdravniIzraz | gdjeUpit | kolikoUpit | kakovUpit | zahvalaIzjava | imeUpit)+ EOF;

pozdravniIzraz: POZDRAV;
gdjeUpit: GDJE lokacijski_upit;
lokacijski_upit: (JE | SE NALAZI | SU | MOGU (LI)? (NACI)?)? turisticki_objekt (PRIJEDLOG lokacija)?;
kolikoUpit: KOLIKO cjenovni_upit;
cjenovni_upit: KOSTA turisticki_objekt | JE CIJENA turisticki_objekt | KOJA JE CIJENA turisticki_objekt;
kakovUpit: KAKAV opisni_upit;
opisni_upit: (JE | SU)? turisticki_objekt;
zahvalaIzjava: HVALA;
imeUpit: KAKO SE ZOVES | PREDSTAVI SE | TKO SI (TI)?;

turisticki_objekt: MUZEJ | HOTEL | RESTORAN | KONOBA | KAFIC | PLAZA | ATRAKCIJA;
lokacija: GRAD | REGIJA | MJESTO;

POZDRAV: 'bok' | 'zdravo' | 'hej' | 'pozdrav' | 'dobar dan' | 'dovidjenja' | 'doviđenja';
GDJE: 'gdje';
KOLIKO: 'koliko';
KAKAV: 'kakav' | 'kakva' | 'kakvo' | 'kakvi' | 'kakve';
KOJA: 'koja' | 'koje';
MOGU: 'mogu';
LI: 'li';
NACI: 'naci' | 'naći';
JE: 'je';
SU: 'su';
SE: 'se';
NALAZI: 'nalazi';
KOSTA: 'košta' | 'kostaju' | 'koštaju' | 'kosta';
CIJENA: 'cijena' | 'cijene';
HVALA: 'hvala';
KAKO: 'kako';
ZOVES: 'zoves' | 'zoveš';
PREDSTAVI: 'predstavi';
TKO: 'tko';
SI: 'si';
TI: 'ti';

MUZEJ: 'muzej';
HOTEL: 'hotel';
RESTORAN: 'restoran';
KONOBA: 'konoba';
KAFIC: 'kafic' | 'kafić';
PLAZA: 'plaža' | 'plaza';
ATRAKCIJA: 'znamenitost' | 'atrakcija';

PRIJEDLOG: 'u' | 'na' | 'za' | 'iz' | 'kod' | 'pokraj';
GRAD: 'split' | 'splitu' | 'zadar' | 'zadru' | 'zagreb' | 'zagrebu' | 'rijeka' | 'rijeci' | 'dubrovnik' | 'dubrovniku' | 'pula' | 'puli';
REGIJA: 'dalmacija' | 'dalmaciji' | 'istra' | 'istri' | 'slavonija' | 'slavoniji';
MJESTO: 'otok' | 'obala' | 'obali' | 'centar' | 'centru' | 'riva' | 'rivi' | 'okolina';

fragment INTERPUNKCIJA: [.!?]+;
WS: [ \t\r\n]+ -> skip;