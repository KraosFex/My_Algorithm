import re
from unicodedata import normalize


s = 'niÑo feo, es un niño feo, feo niÑo. Cara de popo?'
# s = s.upper()


s = s.replace('ñ', 'n')
s = re.sub(r'[.,"\'-?:!;]', '', s)  # Elimina signos de puntuacion
s = re.sub(r"([^n\u0300-\u036f]|n(?!\u0303(?![\u0300-\u036f])))[\u0300-\u036f]+",
           r"\1", normalize("NFD", s), 0, re.I)  # Elimina signos diacriticos

print(s)
