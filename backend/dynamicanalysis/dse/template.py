combinedProgram = '''
import importlib

method1 = importlib.import_module('static.{{ referenceId }}.{{ solution }}').{{ entry }}
method2 = importlib.import_module('static.{{ id }}.{{ submission }}').{{ entry }}

def pairedProgram({{ variables }}):
    return method1({{ variables }}) == method2({{ variables }})
'''
