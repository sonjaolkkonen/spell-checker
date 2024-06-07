# Toteutusdokumentti

## Ohjelman yleisrakenne

Spell Checker -sovellus tarkistaa käyttäjän antaman sanan tai tekstin oikeinkirjoituksen vertailemalla niitä Trie-tietorakenteeseen talletettuun sanastoon. Vertailu tehdään Damerau-Levenshtein -algoritmilla, joka tutkii kahden sanan välistä etäisyyttä. Etäisyys määritellään sen mukaan kuinka monta kirjaimen poistoa, lisäystä tai korvaamista tarvitaan merkkijonon muuntamiseen toiseksi.

## Aika- ja tilavaativuudet

Lähteiden mukaan trie-tietorakenteen hakuoperaatiot voivat enimmillään viedä O(n) aikaa, kun taas Damerau-Levenshteinin etäisyyttä käyttävä algoritmi voi viedä enimmillään O(M*N) aikaa, missä M ja N ovat verrattavien merkkijonojen pituudet.

## Puutteet ja parannusehdotukset

## Laajojen kielimallien käyttö

## Viitteet
- [Damerau–Levenshtein distance (Wikipedia)](https://en.wikipedia.org/wiki/Damerau%E2%80%93Levenshtein_distance)
- [Trie (Wikipedia)](https://en.wikipedia.org/wiki/Trie)
