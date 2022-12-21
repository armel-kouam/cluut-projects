import requests
def synonym_words(word, num_results):
    url_base = "https://api.datamuse.com/words"
    param_r ={}
    param_r["rel_syn"] = word
    param_r["max"] = num_results
    req = requests.get(url_base, params=param_r) 
    word = req.json()
    wort_funf = word[:5]
    # for wort in wort_funf:
    #     synonym = (wort["word"], wort["score"])
    synonym = [(wort["word"], wort["score"]) for wort in wort_funf]
    return synonym


def rhyme_words(word, num_results):
    url = "https://api.datamuse.com/words"
    param_r = {}
    param_r["rel_rhy"] = word
    param_r["max"] = num_results
    req = requests.get(url, params=param_r) 
    word = req.json()
    wort_r = word[:5]
    reimbar = [(wort["word"], wort["score"]) for wort in wort_r]
    return reimbar


def antonym_words(word, num_results):
    url = "https://api.datamuse.com/words"
    param_r = {}
    param_r["rel_ant"] = word
    param_r["max"] = num_results
    req = requests.get(url, params=param_r) 
    word = req.json()
    ant = [wort["word"] for wort in word]
    return ant
print(__name__)
if __name__ == "__main__":
    print(synonym_words("good", 5))
    print(rhyme_words("grape", 5))
    print(synonym_words("bright", 5))
    
    
