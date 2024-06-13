# Viikko 5

Tällä viikolla lisäsin sovellukseen uuden toiminnon, jonka avulla käyttäjä voi lisätä sanan sanastoon, mikäli sitä ei vielä trie-tietorakenteesta löydy. Lisäksi lisäsin ohjelmaan erilaisia ilmoituksia käyttäjälle helpottamaan ohjelman käyttöä. Esim. mikäli annetulle yksittäiselle sanalle ei löydetä läheisiä korjausehdotuksia, ilmoittaa ohjelma ettei sanaa löytynyt sanastosta. Ohjelma myös ilmoittaa mikäli jotain sanaa annetusta pidemmästä tekstistä ei pystytty korjaamaan. Itse ohjelmakoodin muutosten lisäksi muokkasin SpellChecker-luokan yksikkötestejä niin, että otin mock-kirjaston käyttöön sekä tein testit uudelle add_words-metodille. Nämä vaativat myös hieman muokkauksia ohjelman koodiin. Jatkoin myös suorituskykytestausta trie-tietorakenteelle. 

Tällä viikolla haasteita tuotti mock-kirjaston käyttö, sillä jouduin sen käyttöönoton yhteydessä myös hieman muokkaamaan olemassa olevaa koodia. Mock-kirjaston käyttö ei ole itselleni ihan hirveän tuttua, joten sen käyttö tuotti myös tämän takia aluksi haasteita. Eniten opinkin tällä viikolla juurikin yksikkötestaamisesta mock-olioiden avulla. 

Ensi viikolla suunnitelmissa olisi toteuttaa ohjelman manuaalinen testaus sekä luoda ohjelman käyttöohjeet. Luulen, että itse ohjelma on tässä vaiheessa suurimmilta osin valmis, joten suuria muutoksia tai uusia toiminnallisuuksia ei enää ole tulossa ellei sitten vertaisarvioijat löydä koodista jotain puutteita/bugeja. Ajattelin myös vielä käydä läpi Trie- ja Damerau-Levenshtein-luokkien yksikkötestit ja laajentaa näitä tarvittaessa. Mikäli aikaa jää ja hyviä ideoita tulee, suunnitelmissa olisi myös mahdollisesti vielä muokata ohjelman käyttöliittymää visuaalisemmaksi. 

## Tuntikirjanpito 
| **Päivä** | **Käytetty aika** | **Kuvaus** |
| ----------| ----------------- | ---------- |
| 11.6. | 6 h | Uusi metodi add_word |
| 12.6. | 7 h | Testausta ja ui:n muokkaus |
| 13.6. | 4 h | Dokumentointia ja vertaisarviointia |
| **yhteensä** | **17 h** |
