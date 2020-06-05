from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .tablas_resultados.tabla_flesch import tabla_flesch
from .tablas_resultados.tabla_inflesz import tabla_inflesz
from .funciones import contar_vocales,count_letters,count_sentences,count_words,count_all_syllables,calcular_perspicuidad
from users.models import Resultado

@login_required
def home_view(request):
  if request.method == 'POST':
    text = request.POST['text']
    numero_str = 'Número de'

    num_vocales = contar_vocales(text)
    num_letters = count_letters(text)
    num_sentences = count_sentences(text)
    num_words = count_words(text)
    num_syllables = count_all_syllables(text)
    perspicuidad = calcular_perspicuidad(
      num_silabas = num_syllables,
      num_palabras = num_words,
      num_frases = num_sentences
    )
    resultado = Resultado()
    resultado.user = request.user
    resultado.perspicuidad = perspicuidad
    resultado.save()

    num_vocales_str = '{} vocales = {}'.format(numero_str,num_vocales)
    num_letters_str = '{} letras = {}'.format(numero_str,num_letters)
    num_sentences_str = '{} frases = {}'.format(numero_str,num_sentences)
    num_words_str = '{} palabras = {}'.format(numero_str,num_words)
    num_syllables_str = '{} silabas = {}'.format(numero_str,num_syllables)
    perspicuidad_str = '{:f}'.format(perspicuidad)

    fila_1 = [num_letters_str,num_vocales_str]
    fila_2 = [num_words_str,num_sentences_str]
    fila_3 = [num_syllables_str,'']

    tabla_1_hightlight = interpretaP(perspicuidad)
    tabla_2_hightlight = inflesz(perspicuidad)


    return render(request,'home/tabla-resultado.html',
    {
    'tabla_flesch': tabla_flesch,
    'tabla_inflesz': tabla_inflesz,
    'info':[fila_1, fila_2,fila_3],
    'text':text,
    'resultado':perspicuidad_str,
    'tabla_1_hightlight':tabla_1_hightlight,
    'tabla_2_hightlight':tabla_2_hightlight
    }
    )

  return render(request,'home/index.html')



def inflesz(P):
    if P <= 40:
        return 1
    elif P > 40 and P <= 55:
        return 2
    elif P > 55 and P <= 65:
        return 3
    elif P > 65 and P <= 80:
        return 4
    else:
        return 5

def interpretaP(P):
  '''
  Szigriszt-Pazos score interpretation
  '''
  if P <= 15:
    return 1
  if P > 15 and P <= 35:
    return 2
  if P > 35 and P <= 50:
    return 3
  if P > 50 and P <= 65:
    return 4
  if P > 65 and P <= 75:
    return 5
  if P > 75 and P <= 85:
    return 6
  if P >= 85:
    return 7
 

@login_required
def about_view(request):
  return render(request,'home/about.html')
