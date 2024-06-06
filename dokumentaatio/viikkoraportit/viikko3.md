# Viikko 3

Tällä viikolla tein ensimmäisen version trie-tietorakenteesta ja otin käyttöön Kotimaisten kielten keskuksen [Nykysuomen sanalistan](https://www.kotus.fi/aineistot/sana-aineistot/nykysuomen_sanalista). Lisäksi muokkasin SpellChecker-luokkaa niin, että mikäli annettu sana on kirjoitettu oikein, ei ohjelma anna käyttäjälle korjausehdotuksia. Luokan suggest-metodia on muokattu myös niin, että se palauttaa ehdotuksena listan kaikista niistä sanoista, joiden etäisyys annettuun sanaan on pienempi tai yhtä suuri kuin 1. Näiden muutosten lisäksi olen tehnyt myös yksikkötestejä Trie- ja SpellChecker-luokille, ottanut projektissa pylintin käyttöön sekä aloittanut testausdokumentin teon. 

Tällä viikolla opin enemmän trie-tietorakenteesta ja sen toiminnasta. Ensimmäinen tekemäni versio tietorakenteen search-metodista oli melko hidas ja sen nopeuttaminen vaati hieman pohdiskelua. Lopulta muokkasin metodia niin, että se hyödyntää etsinnässä käyttäjän antaman sanan ensimmäistä kirjainta. Tämä muutos nopeutti huomattavasti sovelluksen toimintaa. 

Haasteita tuotti yksikkötestaus ja erityisesti edustavien syötteiden keksiminen. Tein nyt mielestäni melko kattavat testit olemassa oleville metodeille, ja testeissä otin huomioon myös tyhjät syötteet. 

Ensi viikolla suunnitelmana olisi muuttaa sovelluksen toimintaa niin, että käyttäjä voi antaa sovellukselle kerralla pidemmän tekstin ja sovellus korjaa mahdolliset virheet suoraan tekstiin. Voi olla, että tämä osoittautuu haastavaksi toteuttaa suomen kielellä sanojen eri taivutusmuotojen vuoksi, joten voiko sanaston kielen muuttaa mahdollisesti englanniksi vielä tässä vaiheessa kurssia? Lisäksi suunnitelmissa on aloittaa yksikkötestejä täydentävien testien kehitys sekä ohjelman testien, testikattavuusraportin ja pylintin ajamisen konfigurointi automaattiseksi invoken avulla. 

## Tuntikirjanpito 
| **Päivä** | **Käytetty aika** | **Kuvaus** |
| ----------| ----------------- | ---------- |
| 29.5.| 5 h | Trie-tietorakenteen ensimmäinen versio ja sen yksikkötestit, SpellChecker-luokan muokkaus |
| 30.5. | 6 h | Trie- ja SpellChecker -luokan muokkaus ja yksikkötestit, pylintin käyttöönotto, testausdokumentin aloitus, viikkoraportointi |
| **yhteensä** | **11 h** |
