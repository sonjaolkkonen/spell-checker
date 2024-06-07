![GHA workflow badge](https://github.com/sonjaolkkonen/spell-checker/workflows/CI/badge.svg) [![codecov](https://codecov.io/github/sonjaolkkonen/spell-checker/graph/badge.svg?token=L0PHFZ9ZRR)](https://codecov.io/github/sonjaolkkonen/spell-checker)

# Spell Checker - Kirjoitusvirheiden korjaaja

Spell Checker on ohjelma, joka tarjoaa korjausehdotuksia käyttäjän väärin kirjoittamille sanoille.

Ohjelma on toteutettu tallettamalla mahdollisia suomen kielen sanoja trie-tietorakenteeseen ja vertaamalla käyttäjän väärinkirjoitetun merkkijonon etäisyyttä oikein kirjoitettuihin sanoihin Damerau–Levenshtein -etäisyysmittaa käyttämällä.

## 📄 Dokumentaatio
- [Vaatimusmäärittely](https://github.com/sonjaolkkonen/spell-checker/blob/main/dokumentaatio/vaatimusmaarittely.md)
- [Testausdokumentti](https://github.com/sonjaolkkonen/spell-checker/blob/main/dokumentaatio/testausdokumentti.md)
- [Toteutusdokumentti](https://github.com/sonjaolkkonen/spell-checker/blob/main/dokumentaatio/toteutusdokumentti.md)

## 📆 Viikkoraportit
- [Viikko 1](https://github.com/sonjaolkkonen/spell-checker/blob/main/dokumentaatio/viikkoraportit/viikko1.md)
- [Viikko 2](https://github.com/sonjaolkkonen/spell-checker/blob/main/dokumentaatio/viikkoraportit/viikko2.md)
- [Viikko 3](https://github.com/sonjaolkkonen/spell-checker/blob/main/dokumentaatio/viikkoraportit/viikko3.md)
- [Viikko 4](https://github.com/sonjaolkkonen/spell-checker/blob/main/dokumentaatio/viikkoraportit/viikko4.md)

## ⚙️ Asennus- ja käynnistysohjeet

Kloonaa repositio omalle koneellesi:
```
 git clone git@github.com:sonjaolkkonen/spell-checker.git
```

Käynnistä poetry projektin juurihakemistissa:
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

Aja yksikkötestit:
```
poetry run invoke test
```

Muodosta testikattavuusraportti:
```
poetry run invoke coverage
```
