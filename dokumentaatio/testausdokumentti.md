# Testausdokumentti

## Yksikkötestit

Yksikkötesteissä on hyödynnetty unittest-kirjastoa ja ne kattavat src/services -hakemiston tiedostot. Testattavat luokat ovat siis DamerauLevenshtein, SpellChecker ja Trie. Juuri nämä luokat on päätetty sisällyttää testeihin, sillä ne sisältävät varsinaisen ohjelmalogiikan. Näin ollen ohjelman käyttöliittymä on päätetty jättää yksikkötestien ulkopuolelle.

### Testikattavuusraportti


![image](https://github.com/sonjaolkkonen/spell-checker/assets/117500758/b036ef9a-ed8e-411c-a8bf-88b4ac8f7529)


## Manuaalinen testaus
Sovellusta on testattu manuaalisesti antamalla käyttöliittymälle erilaisia testisyötteitä, jolloin on varmistettu, että sana joko tunnistetaan tai sille annetaan korjausehdotus. Tämän lisäksi on myös testattu sanan lisäämistä sanastoon.

## Testitapaukset

### Yhden sanan korjaaminen

**Oikein kirjoitettu sana**
- Syötetään sovellukselle sanastossa oleva sana, esim. "kissa"
- Sovelluksen pitäisi antaa ilmoitus "Ei kirjoitusvirheitä!"

**Sana, jossa on kirjoitusvirhe**
- Syötetään sovellukselle sana, jossa on pieni kirjoitusvirhe, esim. "kisda"
- Sovelluksen pitäisi tulostaa: "Antamasi sana: kisda, Tarkoititko: [lista ehdotuksista]
- Ehdotuksissa pitäisi olla ainakin kissa, sekä mahdollisesti muitakin sanoja, joiden etäisyys sanasta "kissa" on 1

**Sana, joka sisältää erikoismerkkejä tai numeroita**
- Syötetään sovellukselle sana, joka sisältää numeroita, esim. "kissa1"
- Sovelluksen pitäisi antaa ilmoitus "Et voi antaa numeroita tai erikoismerkkejä, käytä pelkkiä kirjaimia!"
- Syötetään sovellukselle sana, joka sisältää erikoismerkkejä, esim. "kissa!"
- Sovelluksen pitäisi antaa ilmoitus "Et voi antaa numeroita tai erikoismerkkejä, käytä pelkkiä kirjaimia!"

**Sana, jolle ei löydy korjausehdotuksia**
- Syötetään sovellukselle sana, joka ei muistuta mitään sanaa, esim. "abcdefgh"
- Sovelluksen pitäisi tulostaa: "Antamasi sana: abcdefgh, Sanaa ei löytynyt sanastosta". 

**Tyhjä tekstikenttä**
- Jätetään tekstikenttä tyhjäksi ja painetaan tarkista-nappia
- Sovelluksen pitäisi antaa herja "Please fill in this field."

### Pidemmän tekstin korjaaminen

**Oikein kirjoitettu teksti**
- Syötetään sovellukselle teksti, jossa ei ole kirjoitusvirheitä, esim. "kissa ja koira!". Sanat tulee kirjoittaa perusmuodossa, sillä sovelluksen sanasto ei sisällä sanojen kaikkia taivutusmuotoja.
- Sovelluksen pitäisi palauttaa teksti samassa muodossa kuin se kirjoitettiin sekä ilmoitus "Ei kirjoitusvirheitä!"

**Teksti, joka sisältää kirjoitusvirheitä**
- Syötetään sovellukselle teksti, joka sisältää pieniä kirjoitusvirheitä, esim. "koida ja kissa!"
- Sovelluksen pitäisi palauttaa korjattu teksti "koira ja kissa" sekä ilmoitus "Korjaus onnistui!"

**Teksti, joka sisältää sanoja, joille ei löydy korjausehdotusta**
- Syötetään sovellukselle teksti, joka sisältää sanoja, jotka eivät muistuta mitään oikeita sanoja, esim. "abcdefgh"
- Sovelluksen pitäisi palauttaa muokkaamaton teksti sekä ilmoitus "Huom! Kaikkia sanoja ei voitu korjata."

**Tyhjä tekstikenttä**
- Jätetään tekstikenttä tyhjäksi ja painetaan tarkista-nappia
- Sovelluksen pitäisi antaa herja "Please fill in this field."

### Sanan lisääminen
Sanan voi lisätä sanastoon sen jälkeen, kun sanan korjausta on pyydetty ja sanaa ei löytynyt sanastosta.

**Sana, jota ei löytynyt sanastosta**
- Lisätään sana, jota ei löytynyt sanastosta
- Sovelluksen pitäisi tulostaa "Sanan lisääminen onnistui"

## Suorituskykytestaus

Algoritmia ja tietorakennetta on testattu ajamalla manuaalisesti testejä, joissa annetaan eripituisia testejä.

### Damerau-Levenshtein

Etäisyyden laskentaa suorittavaa Dameray-Levenshtein -algoritmia on testattu antamalla sille eri pituisia ja erilaisia syötteitä kerran tai useamman kerran peräkkäin. Näin varmistetaan, että algoritmi laskee etäisyyden oikein pitkillä syötteillä sekä useasti kutsuttuna.

**1. Pienet syötteet ("kissa" vs "koira")**
   - Aika pienillä syötteillä: 2.6464462280273438e-05 sekuntia
   - Damerau-Levenshtein -etäisyys: 3

**2. Pienet syötteet ("koti" vs "talo") 1000 kertaa peräkkäin**
   - Aika pienillä syötteillä: 0.06526327133178711 sekuntia
   - Damerau-Levenshtein -etäisyys: 3998
     
**4. Isot syötteet (1000 merkkiä pitkä "a" vs 1000 merkkiä pitkä "b")**
   - Aika isoilla syötteillä: 0.4387481212615967 sekuntia
   - Damerau-Levenshtein -etäisyys: 1000
  
**5. Isot satunnaiset syötteet kymmenen kertaa peräkkäin**
   - Aika satunnaisilla syötteillä: 0.03721785545349121 sekuntia
   - Damerau-Levenshtein -etäisyys: 94

**4. Epäsymmetriset syötteet (toinen 5 merkkiä & toinen 50 merkkiä) kymmenen kertaa peräkkäin**
   - Aika epäsymmetrisillä syötteillä (lyhyt ensin): 0.0013117790222167969 sekuntia
   - Damerau-Levenshtein -etäisyys: 49
  
### Trie-tietorakenne

Trie-luokan insert-, search- ja get_trie.content_metodeja on testattu erittäin suurilla syötteillä. Testauksessa on tutkittu toimivatko metodit ylipäätään suurilla syötteillä sekä niiden aikavaativuutta. Testaus on suoritettu useammalla pitkällä syötteellä kasvattaen syötteen kokoa. 

**insert-metodi**
- 1000 sanan lisäämiseen meni 0.003842 sekuntia
- 10 000 sanan lisäämiseen meni 0.089107 sekuntia
- 100 000 sanan lisäämiseen meni 1.100642 sekuntia

**search-metodi**
- 1000 merkin läpikäymiseen meni 0.000965 sekuntia
- 10 000 merkin läpikäymiseen meni 0.008733 sekuntia
- 100 000 merkin läpikäymiseen meni 0.086006  sekuntia

**get_trie_content-metodi**
- 1000 sanan trien sisällön saamiseen meni 0.001282 sekuntia
- 10 000 sanan trien sisällön saamiseen meni 0.019851 sekuntia
- 100 000 sanan trien sisällön saamiseen meni 0.132293 sekuntia
  
   
