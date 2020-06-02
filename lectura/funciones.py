import re
import statistics
from .separarsilabas import silabizer

def count_letters(text):
    '''
    Text letter count
    '''
    count = 0
    for char in text:
        if char.isalpha():
            count += 1
    if count == 0:
        return 1
    else:
        return count

def count_words(text):
    '''
    Text word count
    '''
    text = ''.join(filter(lambda x: not x.isdigit(), text))
    clean = re.compile('\W+')
    text = clean.sub(' ', text).strip()
    # Prevents zero division
    if len(text.split()) == 0:
        return 1
    else:
        return len(text.split())

def count_sentences(text):
    '''
    Sentence count
    '''
    text = text.replace("\n","")
    sentence_end = re.compile('[.:;!?\)\()]')
    sencences=sentence_end.split(text)
    sencences = list(filter(None, sencences))
    if len(sencences) == 0:
        return 1
    else:
        return len(sencences)

def contar_vocales(cad):
    voc = 0
    for c in cad:
        if c == 'a' or c == 'e' or c == 'i' or c =='o' or c == 'u' or c == 'A' or c == 'E' or c == 'I' or c =='O' or c == 'U':
            voc=voc+1
    return voc

def count_syllables(word):
    '''
    Word syllable count
    '''
    word = re.sub(r'\W+', '', word)
    syllables = silabizer()
    return len(syllables(word))

def count_all_syllables(text):
    '''
    The whole text syllable count
    '''
    
    text = ''.join(filter(lambda x: not x.isdigit(), text))
    clean = re.compile('\W+')
    text = clean.sub(' ', text).strip()
    text = text.split()
    text = filter(None, text)
    total = 0
    for word in text:
        total += count_syllables(word)
    if total == 0:
        return 1
    else:
        return total

def calcular_perspicuidad(num_silabas,num_palabras,num_frases):
    """
    P es la perspicuidad, S el total de sílabas, W la cantidad de palabras y F el número de frases.
    """
    p = 206.835 - (62.3*num_silabas)/num_palabras - (num_palabras/num_frases)
    return p


def interpretaP(P):
    '''
    Szigriszt-Pazos score interpretation
    '''
    if P <= 15:
        return "muy difícil"
    elif P > 15 and P <= 35:
        return "árido"
    elif P > 35 and P <= 50:
        return "bastante difícil"
    elif P > 50 and P <= 65:
        return "normal"
    elif P > 65 and P <= 75:
        return "bastante fácil"
    elif P > 75 and P <= 85:
        return "fácil"
    else:
        return "muy fácil"

def inflesz(P):
    if P <= 40:
        return "muy difícil"
    elif P > 40 and P <= 55:
        return "algo difícil"
    elif P > 55 and P <= 65:
        return "normal"
    elif P > 65 and P <= 80:
        return "bastante fácil"
    else:
        return "muy fácil"