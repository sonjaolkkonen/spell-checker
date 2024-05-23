# Viikko 2

Tällä viikolla koodasin sovellukselle hyvin alustavan käyttöliittymän sekä toteutin ensimmäisen version Damerau-Levensteinin etäisyyttä hyödyntävästä algoritmista, jolle kirjoitin myös ensimmäiset yksikkötestit. Lisäksi tein ensimmäisen version SpellChecker-luokasta ja triestä/sanakirjasta sekä konfiguroin GitHub Actionsin, joka ajaa yksikkötestit ja luo Codecoviin testikattavuusraportin. Pyrin myös lisäämään koodiin koodauksen yhteydessä tarvittavat kommentit ja docstringit. 

Tällä hetkellä sovellus käyttää trie-tietorakenteen sijaan yksinkertaista sanakirjaa. Aluksi otin projektiin käyttöön python-kirjaston PygTrie, mutta ohjaajan suosituksesta vaihdoin tämän tavalliseksi sanakirjaksi. Ohjelman käyttämä sanalista on myös tällä hetkellä hyvin lyhyt, ja se onkin tarkoitus korvata kattavalla suomen kielen sanastolla, kunhan trie-tietorakenne valmistuu. Trie.py-tiedostolle ei ole vielä tehty testejä, sillä tiedosto tulee luultavasti muuttumaan melko paljon. 

Ohjelmalla on nyt hyvin alustava käyttöliittymä, jolle käyttäjä voi antaa eri sanoja. Ohjelma vertaa sanakirjan sanojen etäisyyttä käyttäjän antamaan merkkijonoon ja palauttaa käyttöliittymälle korjausehdotuksena sanan, jolla on lyhin etäisyys. Tämän takia sovellus saattaa nyt antaa hieman hassujakin korjausehdotuksia, esimerkiksi "tietokone"-sanalle sovellus antaa ehdotuksen "retki". Sovellus antaa korjausehdotuksia myös oikeinkirjoitetuille sanoille. Alunperin koodasin ohjelmalle toisen result.html-sivun, jolla tulokset näytettiin, mutta päädyin muokkaamaan ohjelmaa niin, että ehdotukset tulevat näkyviin samalle aloitussivulle. 

Tällä viikolla opin enemmän Damerau-Levensteinin etäisyyttä hyödyntävän algoritmin toiminnasta. Toteutin oman versioni algoritmista wikipedian pseudokoodin pohjalta. Pseudokoodin lukeminen ja algoritmin hahmottaminen tuottivat aluksi haasteita, mutta algoritmi näyttäisi ainakin toistaiseksi toimivan kuten sen pitäisikin. Hieman yllättäen eniten haasteita tuotti kuitenkin testikattavuusraportin saaminen Codecoviin. Käytin ensin Ohjelmistotuotanto-kurssin ohjeita tämän tekemiseen, kunnes huomasin, että nykyään pitää ilmeisesti myös julkisiin repositorioihin lisätä Codecov token. Tokenin lisäyksenkään jälkeen en saanut testikattavuusraporttia toimimaan kunnolla, kunnes se vihdoin alkoi toimia. Tämän kanssa jumppaamiseen kului kuitenkin melko paljon turhaa aikaa. 

Ensi viikolla tarkoituksena on korvata sanakirja trie-tietorakenteella. SpellChecker-luokkaa voisi myös muuttaa niin, että mikäli sana on kirjoitettu oikein, ei ohjelma anna korjausehdotuksia. Luokan suggest-metodia voisi muuttaa myös siten, että se palauttaa ehdotuksina vain ne sanat, joiden etäisyys käyttäjän antamaan sanaan on 1 tai 0. Lisäksi tarkoituksena on ottaa pylint käyttöön sekä tehdä yksikkötestejä Trie- ja Spellchecker-luokille. 


## Tuntikirjanpito 
| **Päivä** | **Käytetty aika** | **Kuvaus** |
| ----------| ----------------- | ---------- |
| 19.5.| 1 h | Käyttöliittymän ensimmäinen alustava versio |
| 20.-21.5. | 6 h | Damerau-Lehvenshtein algoritmin ensimmäinen versio, Trie-tiedoston alustava versio (sanakirja) |
| 22.5. | 4 h | Docstringien kirjoittelua, algoritmin bugien korjaus, käyttöliittymän muokkaus, ensimmäinen versio SpellChecker-luokasta |
| 23.5. | 4 h | Damerau-Lehvenstein algoritmin yksikkötestit, GitHub Actions, Codecov, viikkoraportti |
| **yhteensä** | ** 15 h** |
