# Brainstorming

No-sense ideas...

What if we extract chords for modern music just getting from chord pages instead of midi files?

Use chord live detection project (fropm KSchool) to listen to a guitar, detect chords and suggest next. 

I should explain why I decided to change the strategy from midi processing to scraping. 

I should explain msuc conceps using music21, with sheets and music examples:
* Notes.
* Chords.
* Notas extrañas 
....

If I could represent the chords as vector, It would be easier and faster to train

https://medium.com/@gruizdevilla/introducci%C3%B3n-a-word2vec-skip-gram-model-4800f72c871f

Como represento el círuclo de quintas en términos de distancia. Idea parecida. 

https://towardsdatascience.com/feature-engineering-time-3934038e0dbe

Ver snnipters de https://github.com/huanlui/snippets.

Usar Gatsby. Ver https://github.com/huanlui/gatsby-cloud-spike u otras herramientas más flexibles:

https://es.reactjs.org/docs/create-a-new-react-app.html#gatsby

Cómo meter features ctes por batch, década, género.

Como codificar género. O 21 features independientemente o one shot encoding teniendo en cuenta las repetidas como nuevos géneros

Como estadística, la complejidad de un acorde se puede medir usando el círculo de quitas 

Lq nota fundamental del acorde tendrá que ser una variable circular 

La nota del bajo podría ser la distancia en saltos dentro del círculo de quintas 

Anonimizar datos antes de meterlos en sitios como public Tableau 

## Encoging

Choose A for examples:

Chord features-OPTION 1:
- 12 position vectors. 1 if the chord has this note. Otherwise: 0. 

TODO
```
[0,0,0,0,1
```

Chord features - OPTION 2:
- Root fundamental (xy). In A chord, an A
- First most "similar" note. In A chord, an E.
- Second most "similar" note. In a chord, a C#
- ... until 5th most "similar" note. Since we wont consider chords with more than 6 notes. 

But we can encode them this ways:
- 0-11. But...its a C Chord nearer to D that to G? And, if so, what about C and G (0-11). We definitively need a circular enconding. 
- 0-11 converted to X,Y. C is near B and D. Ok, but we have the same problem: C es more similar to D that to G? Anyway,now we are taking about notes.


Podríamos comaparar:
- One shot encoding.
- Word embedding. 
- Mis manual embedding:
    * 12 features (12 notas a 1 o 0 si las tienen). 
    * 12 features (6 notas con posiciones de esas notas). Creo que es info menos dispersa. 
    * 12 features (6 notas con posiciones en círculo de quintas de esas notas). Creo que es info menos dispersa. 
    * Usar directamente info de frequencias?

