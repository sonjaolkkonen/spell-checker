# Viikko 4

Tällä viikolla muokkasin ohjelmaa niin, että sille voi antaa myös pidemmän tekstin tarkistettavaksi. Nyt ohjelmassa on kaksi eri tekstikenttää, joihin käyttäjä voi syöttää sanoja. Ensimmäinen kenttä on tarkoitettu yksittäisten sanojen tarkistamiseen, kun taas toinen kenttä on tarkoitettu pidempien tekstien tarkistamiseen. Mikäli käyttäjä haluaa tarkistaa yksittäisen sanan oikeinkirjoituksen, palauttaa sovellus listana kaikki ne sanat, joiden etäisyys annetusta sanasta on 1. Jos taas käyttäjä haluaa tarkistaa pidemmän tekstin oikeinkirjoituksen, palauttaa ohjelma käyttäjälle korjatun tekstin. Näiden muutosten lisäksi olen refaktoroinut koodia Trie- ja SpellChecker-luokkien osin sekä muokannut ja lisännyt yksikkötestejä. Yksikkötestien lisäksi aloitin Damerau-Levenhstein -algoritmin suorituskykytestauksen. 

Haasteita tuotti tällä viikolla uusi ominaisuus, joka mahdollistaa myös pidemmät syötteet kuin vain yhden sanan pituiset syötteet. Koodi vaati jonkin verran muokkausta ja refaktorointia, jotta tämän sai toimimaan järkevästi. Tällä viikolla opinkin eniten oman koodin refaktoroinnista ja muokkaamisesta. Tein alunperin erillisen suggest_text-metodin, joka olisi tarkistanut pidemmän tekstin, mutta päädyin lopulta poistamaan tämän. Sen sijaan suggest-metodiin on lisätty ominaisuus, joka tunnistaa onko tarkistettava teksti yksi sana vai useampi. Sain myös viime viikolla palautetta, että ohjelma ei voi tutkia ainoastaan samalla kirjaimella alkavia sanoja, joten myös tämä ominaisuus on nyt muokattu pois tällä. Tuntuu, että ohjelma toimii tämän muutoksen jälkeen hieman hitaasti, mutta ainakaan itse en keksi miten sitä saisi nopeutettua. Ongelma tuntuu olevan trie-rakenteen läpikäynnissä.

Ensi viikolla suunnitelmana olisi lisätä sovellukseen uusi toiminta, jonka avulla käyttäjä voi lisätä sanan sanastoon, mikäli sitä ei sieltä vielä löydy. Ajattelin myös vaihtaa sanaston suomesta englanniksi, sillä suomen kielen sanojen taivutusmuodot muodostavat haasteita oikeinkirjoituksen tsekkaamisessa. Mielestäni englanti toimii nyt paremmin tämän kurssin puitteissa. Lisäksi tavoitteena olisi muokata käyttöliittymää ja yksikkötestejä (mock-objektit käyttöön) sekä jatkaa suorituskykytestausta (trie-tietorakenne)



## Tuntikirjanpito 
| **Päivä** | **Käytetty aika** | **Kuvaus** |
| ----------| ----------------- | ---------- |
| 3.6.| 4 h | Invoken konfigurointi, SpellChecker-luokan, routesin ja index.html-sivun muokkaus |
| 4.6. | 1 h | Testausta |
| 6.6. | 6 h | Refaktorointia, SpellChecker -luokan muokkaus, uusia metodeja routes.py -tiedostoon |
| 7.6. | 5 h | Testausta, dokumentointia |
| **yhteensä** | **16 h** |
