from preloaded import LOVE_LANGUAGES

def love_language(partner, weeks):
    import random
    
    love_languages = {
        "words": 0, 
        "acts": 0, 
        "gifts": 0, 
        "time": 0, 
        "touch": 0
    }
        
    for i in range(1, (weeks*7)):
        r = random.randint(0, 4)
        value = 1 if partner.response(list(love_languages.keys())[r]) == "positive" else 0 
        love_languages[list(love_languages.keys())[r]] += value
    return max(love_languages, key=love_languages.get)