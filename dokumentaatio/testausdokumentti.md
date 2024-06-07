# Testausdokumentti

## Yksikkötestit

Yksikkötesteissä on hyödynnetty unittest-kirjastoa ja ne kattavat src/services -hakemiston tiedostot. Testattavat luokat ovat siis DamerauLevenshtein, SpellChecker ja Trie. Juuri nämä luokat on päätetty sisällyttää testeihin, sillä ne sisältävät varsinaisen ohjelmalogiikan. Näin ollen ohjelman käyttöliittymä on päätetty jättää yksikkötestien ulkopuolelle.

### Testikattavuusraportti
![image](https://github.com/sonjaolkkonen/spell-checker/assets/117500758/72a707e4-abb9-4731-808a-f1aee11ebb09)

## Manuaalinen testaus
Sovellusta testataan manuaalisesti antamalla käyttöliittymälle erilaisia testisyötteitä. 

## Suorituskykytestaus

Algoritmia ja tietorakennetta on testattu ajamalla manuaalisesti testejä, joissa annetaan eripituisia testejä.

### Damerau-Levenshtein

Etäisyyden laskentaa suorittavaa Dameray-Levenshtein -algoritmia on testattu antamalla sille eri pituisia ja erilaisia syötteitä kerran tai useamman kerran peräkkäin. Näin varmistetaan, että algoritmi laskee etäisyyden oikein pitkillä syötteillä sekä useasti kutsuttuna

1. Pienet syötteet ("kissa" vs "koira")
   - Aika pienillä syötteillä: 2.6464462280273438e-05 sekuntia
   - Damerau-Levenshtein -etäisyys: 3

2. Pienet syötteet ("koti" vs "talo") 1000 kertaa peräkkäin
   - Aika pienillä syötteillä: 0.06526327133178711 sekuntia
   - Damerau-Levenshtein -etäisyys: 3998
     
4. Isot syötteet (1000 merkkiä pitkä "a" vs 1000 merkkiä pitkä "b")
   - Aika isoilla syötteillä: 0.4387481212615967 sekuntia
   - Damerau-Levenshtein -etäisyys: 1000
  
5. Isot satunnaiset syötteet kymmenen kertaa peräkkäin
   - Aika satunnaisilla syötteillä: 0.03721785545349121 sekuntia
   - Damerau-Levenshtein -etäisyys: 94

4. Epäsymmetriset syötteet (toinen 5 merkkiä & toinen 50 merkkiä) kymmenen kertaa peräkkäin
   - Aika epäsymmetrisillä syötteillä (lyhyt ensin): 0.0013117790222167969 sekuntia
   - Damerau-Levenshtein -etäisyys: 49
  
### Trie-tietorakenne

Tulossa..
  
   
