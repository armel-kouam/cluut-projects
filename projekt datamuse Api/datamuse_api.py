# Aufgabe 1: Datamuse API kennenlernen
# 1-Mann kann Datamuse API in Apps verwenden, um Wörter zu finden, die einem bestimmten Satz 
# von Einschränkungen entsprechen und die in einem bestimmten Kontext wahrscheinlich sind  .
# 2-Die Base URL ist https://api.datamuse.com
# 3-Die zwei Funktionen (Endpoints), die die API bietet: words Endpunkt und sug Endpunkt

import requests

print("Aufgabe 2: Wörter mit einer ähnlichen Bedeutung")

wor_on = "on top of"
url_bd = f"https://api.datamuse.com/words?ml={wor_on}"
reques = requests.get(url_bd)
w = reques.json()
# print(w)
print(w[:5])
print()
# wort=[]
# for wort in w[:5]:
#     # w=(wort["word"]["score"])
#     # print((wort["word"], wort["score"]))


from word_module import synonym_words, rhyme_words, antonym_words  
print(rhyme_words("", 4))




# print()
# print("Aufgabe 3: Wortgewandt sein - Funktion synonym_words")

# def synonym_words(word, num_results):
#     url_base = "https://api.datamuse.com/words"
#     param_r ={}
#     param_r["rel_syn"] = word
#     param_r["max"] = num_results
#     req = requests.get(url_base, params=param_r) 
#     wor = req.json()
#     wort_funf = wor[:5]
#     # ergebnis=[]
#     # for wort in wort_funf:
#     #     synonym = (wort["word"], wort["score"])
#     #     ergebnis.append(synonym)
#     synonym = [(wort["word"], wort["score"]) for wort in wort_funf]
#     return synonym
# print(synonym_words("hot", 5))
   
# print()
# print("Aufgabe 4: Reimen wie ein Profi - Funktion rhyme_words")

# def rhyme_words(word, num_results):
#     url = "https://api.datamuse.com/words"
#     param_r = {}
#     param_r["rel_rhy"] = word
#     param_r["max"] = num_results
#     req = requests.get(url, params=param_r) 
#     word = req.json()
#     wort_r = word[:5]
#     reimbar = [(wort["word"], wort["score"]) for wort in wort_r]
#     return reimbar
# print(rhyme_words("grape", 5))
    
# print()
# print("Aufgabe 5: Finde Antonyme")

# def antonym_words(word, num_results):
#     url = "https://api.datamuse.com/words"
#     param_r = {}
#     param_r["rel_ant"] = word
#     param_r["max"] = num_results
#     req = requests.get(url, params=param_r) 
#     word = req.json()
#     ant = [wort["word"] for wort in word]
#     return ant
# print(antonym_words("bright", 3))

# print()
# print("Aufgabe 6: Clean-Up: Erstelle ein Modul")
from word_module import*
print(synonym_words("good", 5))
print(rhyme_words("grape", 5))
print(synonym_words("bright", 5))


