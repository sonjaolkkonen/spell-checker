# Toteutusdokumentti

## Ohjelman yleisrakenne

Spell Checker -sovellus tarkistaa käyttäjän antaman sanan tai tekstin oikeinkirjoituksen vertailemalla niitä Trie-tietorakenteeseen talletettuun sanastoon. Vertailu tehdään Damerau-Levenshtein -algoritmilla, joka tutkii kahden sanan välistä etäisyyttä. Etäisyys määritellään sen mukaan kuinka monta kirjaimen poistoa, lisäystä tai korvaamista tarvitaan merkkijonon muuntamiseen toiseksi.

Ohjelman käynnistyessä tallennetaan SpellChecker-luokalle annettu tekstitiedostossa oleva sanasto trie-tietorakenteeseen. Sanastona hyödynnetään Kotimaisten kielten keskuksen Nykysuomen sanalistaa, joka sisältää yli 100 000 sanaa. Ohjelman käynnistämisen jälkeen käyttäjälle avautuu etusivu, jossa on kaksi eri tekstikenttää. Lyhyempään tekstikenttään käyttäjä voi syöttää yhden sanan (max 20 merkkiä) ja pidempään useamman sanan (max 200 merkkiä).

Jos käyttäjä syöttää yhden sanan ja sana löytyy trie-tietorakenteesta, annetaan käyttäjälle ilmoitus ettei kirjoitusvirheitä löytynyt. Mikäli taas sanaa ei löytynyt trie-tietorakenteesta palautetaan käyttäjälle lista ehdotetuista sanoista, jotka ovat korkeintaan yhden etäisyyden päässä annetusta sanasta. Mikäli sanalle ei löydy ehdotuksia eikä sitä löydy trie-tietorakenteesta, ilmoitetaan käyttäjälle ettei sanaa löytynyt. 

Mikäli käyttäjä syöttää tekstikenttään useamman sanan, palauttaa sovellus korjatun tekstin suoraan teksikenttään. Sovellus pilkkoo tekstin listaksi sanoja ja vertaa näitä yksitellen trie-tietorakenteeseen. Virheelliset sanat korjataan aina trie-rakenteesta löytyvällä ensimmäisellä yhden etäisyyden päässä olevalla sanalla. Mikäli kaikkien sanojen korjaaminen ei onnistu (sana ei löydy trie-tietorakenteesta eikä sille löydy läheistä sanaa), tulee käyttäjälle ilmoitus ettei kaikkia sanoja pystytty korjaamaan ja sana palautetaan alkuperäisessä muodossaan. Myös oikeinkirjoitetun sanat (löytyy trie-tietorakenteesta) palautetaan tekstissä sellaisenaan. 

Käyttäjän on myös mahdollista lisätä sana sanastoon, mikäli se ei sieltä vielä löydy. 

## Aika- ja tilavaativuudet

Lähteiden mukaan trie-tietorakenteen hakuoperaatiot voivat enimmillään viedä O(n) aikaa, kun taas Damerau-Levenshteinin etäisyyttä käyttävä algoritmi voi viedä enimmillään O(M*N) aikaa, missä M ja N ovat verrattavien merkkijonojen pituudet.

## Puutteet ja parannusehdotukset

Tulossa..

## Laajojen kielimallien käyttö

Tulossa..

## Viitteet
- [Damerau–Levenshtein distance (Wikipedia)](https://en.wikipedia.org/wiki/Damerau%E2%80%93Levenshtein_distance)
- [Trie (Wikipedia)](https://en.wikipedia.org/wiki/Trie)
- [Nykysuomen sanalista](https://www.kotus.fi/aineistot/sana-aineistot/nykysuomen_sanalista)
