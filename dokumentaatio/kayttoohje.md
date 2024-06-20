# Käyttöohje

## Asennus- ja käynnistysohjeet

Kloonaa repositio omalle koneellesi:
```
 git clone git@github.com:sonjaolkkonen/spell-checker.git
```

Käynnistä poetry projektin juurihakemistossa:
```
poetry shell
```

Lataa projektin riippuvuudet:
```
poetry install
```

Käynnistä sovellus:
```
poetry run invoke start
```

Sovelluksen web-käyttöliittymä aukeaa terminaalin antamaan osoitteeseen, jota klikkaamalla voi avata lokaalisti pyörivän sovelluksen. Sovellus sulkeutuu antamalla terminaaliin ctr+c.

## Testaus

Yksikkötestit voi ajaa komennolla:
```
poetry run invoke test
```

Testikattavuusraportin voi muodostaa komennolla:
```
poetry run invoke coverage
```

## Sovelluksen käyttö

Spell Checker on ohjelma, joka tarjoaa korjausehdotuksia käyttäjän väärin kirjoittamille sanoille. Käyttäjä voi syöttää sovellukselle joko yhden yksittäisen sanan (max 20 merkkiä) tai pidemmän tekstin (max 200 merkkiä). Sanojen syöttäminen tapahtuu etusivulta löytyvien tekstikenttien avulla. 

![image](https://github.com/sonjaolkkonen/spell-checker/assets/117500758/b66b9b1a-cc8e-4e80-b0c3-d270d93166c8)

### Yksittäisen sanan korjaaminen

Yhden sanan tekstikenttään voi syöttää enintään 20 merkkiä pitkän sanan, joka ei sisällä erikoismerkkejä tai numeroita. Sanan oikeinkirjoituksen tarkastaminen tapahtuu painamalla tarkista-nappia. 

![image](https://github.com/sonjaolkkonen/spell-checker/assets/117500758/183604d6-057a-429a-8643-7311849977ea)

Mikäli annettu sana on kirjoitettu oikein, ilmoittaa sovellus siitä:

![image](https://github.com/sonjaolkkonen/spell-checker/assets/117500758/cfd8d187-3874-48ff-92c4-2980724fbc66)

Sovellus myös ilmoittaa mikäli syötetty sana sisältää numeroita tai erikoismerkkejä:

![image](https://github.com/sonjaolkkonen/spell-checker/assets/117500758/3c1eaad2-78dd-4b93-97d1-342c71eb3970)

Mikäli sanaa ei löydy sellaisenaan trie-rakenteesta, palauttaa sovellus listana kaikki triestä löydetyt syötettä muistuttavat sanat:

![image](https://github.com/sonjaolkkonen/spell-checker/assets/117500758/0db78db9-5758-4a73-a29c-f85c97a16654)


Mikäli sanaa ei löydy sellaisenaan trie-rakenteesta, mutta sanalle ei myöskään löydy ehdotuksia, antaa sovellus ilmoituksen "Sanaa ei löytynyt sanastosta":

![image](https://github.com/sonjaolkkonen/spell-checker/assets/117500758/14802b38-5db4-4d6c-b106-98c1e06db927)

### Pidemmän tekstin korjaaminen

Pidemmän tekstin kenttään voi syöttää enintään 200 merkkiä pitkän tekstin. Teksti voi sisältää erikoismerkkejä, mutta se ei voi sisältää numeroita. Tekstin oikeinkirjoituksen tarkastaminen tapahtuu painamalla tarkista-nappia.

![image](https://github.com/sonjaolkkonen/spell-checker/assets/117500758/ceb68d6f-006c-4fa6-8c66-3a931f915d37)

Korjattu teksti palautetaan tekstikenttään, jota voi muokata: 

![image](https://github.com/sonjaolkkonen/spell-checker/assets/117500758/b951e592-fc0a-48e5-ab22-2dcd4bc0d1f1)

Mikäli kaikkia sanoja ei voitu korjata, ilmoittaa sovellus tästä:

![image](https://github.com/sonjaolkkonen/spell-checker/assets/117500758/e9ae5186-f8b3-43b9-b349-3949b96bf50d)

Mikäli syötetyssä tekstissä ei ollut kirjoitusvirheitä, palauttaa sovellus annetun tekstin sellaisenaan sekä ilmoituksen ettei tekstistä löytynyt kirjoitusvirheitä:

![image](https://github.com/sonjaolkkonen/spell-checker/assets/117500758/f37147c9-cb69-4830-8780-ad77aafb79d5)


### Sanan lisääminen sanastoon

Mikäli sanaa ei löydy trie-rakenteesta, mutta se on oikeinkirjoitettu, voi käyttäjä lisätä sanan sanastoon: 

![image](https://github.com/sonjaolkkonen/spell-checker/assets/117500758/4dd7abda-c2ea-4fe4-932f-79be55c91cc5)

Käyttäjä saa ilmoituksen onnistuiko sanan lisääminen sanastoon vai ei. 









