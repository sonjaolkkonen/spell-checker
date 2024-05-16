# Vaatimusmäärittely

Opinto-ohjelma: Tietojenkäsittelytieteen kandidaatti (TKT)

## Aihe ja toteutus
  Harjoitustyöni aihe on kirjoitusvirheiden korjaaja, joka ehdottaa käyttäjän antamalle väärinkirjoitetulle sanalle oikein kirjoitettua muotoa sanasta. Ohjelma toteutetaan tallettamalla mahdollisia sanoja itse toteutettuun trie-tietorakenteeseen ja vertaamalla käyttäjän väärinkirjoitetun merkkijonon etäisyyttä oikein kirjoitettuihin sanoihin. Etäisyyden laskemisessa hyödynnetään Damerau–Levenshteinin -etäisyyttä, jonka avulla etsitään ne sanat, joiden etäisyysmitta korjattavasta sanasta on pienin. Valitsin juuri nämä algoritmit ja tietorakenteet kurssimateriaalin ehdotusten perusteella.

Käyttäjä antaa sovellukselle tekstisyötteenä sanoja, jotka analysoidaan vertaamalla niiden etäisyyttä sanastossa oleviin sanoihin. Mikäli sana löytyy sanastosta, eli etäisyys on 0, ei sovellus anna ehdotuksia. Mikäli taas sana ei löydy sanastosta, antaa sovellus korjausehdotuksina sanat, jotka ovat lähimpänä annettua tekstisyötettä. Vaihtoehtoisesti käyttäjä voi lisätä sanan sanastoon mikäli sana on kirjoitettu oikein, mutta sitä ei vielä löydy sanastosta. Sanastona käytetään suomen kielen sanastoa ja alustavasti tekstisyötteenä voi antaa kerrallaan vain yhden sanan.

Riippuvuuksien hallintaan käytetään Poetryä. Algoritmin oikea toiminta varmistetaan kattavalla yksikkötestauksella Unittest-kehystä hyödyntäen.

Lähteiden mukaan trie-tietorakenteen hakuoperaatiot voivat enimmillään viedä O(n) aikaa, kun taas Damerau-Levenshteinin etäisyyttä käyttävä algoritmi voi viedä enimmillään O(M*N) aikaa, missä M ja N ovat verrattavien merkkijonojen pituudet. Nämä ovat sovelluksen alustavat aikavaativuustavoitteet.

## Kielet
Harjoitustyö toteutetaan web-sovelluksena Pythonilla hyödyntäen ```Flask```-kirjastoa (pystyn vertaisarvioimaan Pythonilla toteutettuja projekteja). Projektin dokumentaatio kirjoitetaan suomeksi, mutta itse koodi toteutetaan englanniksi.

## Lähteet

- [Damerau–Levenshtein distance (Wikipedia)](https://en.wikipedia.org/wiki/Damerau%E2%80%93Levenshtein_distance)
- [Trie (Wikipedia)](https://en.wikipedia.org/wiki/Trie)
