# coding : utf-8

# Bonjour Jean-Hugues! Voici mon quatrième devoir sur les fameuses chroniques de Richard Martineau. 
# Vous trouverez ma démarche justifiée en #commentaires. Bonne lecture! Amélie :-) 

import csv, spacy
from collections import Counter
# Importation des fichiers nécessaires à la création du .csv

tal = spacy.load("fr_core_news_md")
# Importation du réseau neuronal

tal.Defaults.stop_words.add("y")
tal.Defaults.stop_words.add("t")
tal.Defaults.stop_words.add("il")
tal.Defaults.stop_words.remove("gens")
# Add termes vides voulus et remove terme vide non voulu. 

martino = "martino.csv"
# Importation du fichier.csv

f = open(martino)
chroniques = csv.reader(f)
# Ouverture du fichier.csv

next(chroniques)
# Modification afin que le fichier ne prenne pas en compte la première ligne.

tousMots = []
    # Création d'une liste vide à l'intérieur de la boucle préalablement créée.
bigrams = []
    # Création d'une deuxième liste vide pour grouper des mots ensemble.

for mots in chroniques:
# Création de la boucle qui permet d'imprimer toutes les données voulues, ici le caractère "3" qui correspond au texte des chroniques.
    doc = tal(mots[3])
    #for token in doc:
        #print(token.text)
    #tokens = [token.text for token in doc]
    #print(tokens)

    tokens = [token.text for token in doc if token.is_stop == False and token.is_punct == False]
    #print(tokens)
    # Conserver les tokens "faux", exclusion des mots vides de mes lemmes ET supression de la ponctuation.

    lemmes = [token.lemma_ for token in doc if token.is_stop == False and token.is_punct == False]
    #print(lemmes)
    # Lemmatisation du fichier. 

    for motsfreq in lemmes:
        for x,y in enumerate(lemmes[:-1]):
            if "islam" in motsfreq:
                bigrams.append("{} {}".format(lemmes[x],lemmes[x+1]))
            elif "musulm" in motsfreq:
                # Création des boucles me permettant de sélectionner le vocabulaire voulu dans les chroniques de Martineau.
                bigrams.append("{} {}".format(lemmes[x],lemmes[x+1]))
                # Append des lemmes à la liste vide "bigrams" préalablement créée.

freq = Counter(bigrams)
print(freq.most_common(50))
# Impression des 50 termes les plus fréquents dans les chroniques de Martineau.    

# Voici le résultat de mes précieux essais-erreurs. Comme j'exécute mon code avec un ordinateur Windows, j'éprouve quelques problèmes avec l'impression de mon script (tel qu'expérimenté lors du dernier cours en classe).
# Il m'est donc assez ardu de vérifier si mon code s'exécute bien. 
# J'espère donc que j'arrive au résultat voulu. :-) 