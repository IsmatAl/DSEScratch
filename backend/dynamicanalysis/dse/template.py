combinedProgram = '''
import importlib

a_{{ entry }} = importlib.import_module('static.{{ referenceId }}.{{ solution }}').{{ entry }}
b_{{ entry }} = importlib.import_module('static.{{ id }}.{{ submission }}').{{ entry }}

def pairedProgram({{ variables }}):
    return a_{{ entry }}({{ variables }}) == b_{{ entry }}({{ variables }})
'''
