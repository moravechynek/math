from django.test import TestCase
import evaluate

if 10 == eval(str(evaluate.evaluate('5+5'))):
    print('Scitani probehlo uspesne.')
else:
    print('Scitani probehlo neuspesne.')

if 0 == eval(str(evaluate.evaluate('5-5'))):
    print('Odcitani probehlo uspesne.')
else:
    print('Odcitani probehlo neuspesne.')