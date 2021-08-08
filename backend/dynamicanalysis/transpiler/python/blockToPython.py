event_whenflagclicked = '''
from math import *      # pragma: no cover
from decimal import *   # pragma: no cover
import random           # pragma: no cover
import math             # pragma: no cover
def FILE({{ variables }}):'''


control_forever = '\n{{ tbs }}while True:{{ sb1 }}'


# control_stop = '\n{{ tbs }}break'
control_stop = ''


control_wait = '\n{{ tbs }}control_wait({{ i1 }})'

control_wait_until = '\n{{ tbs }}control_wait_until({{ i1 }})'

control_create_clone_of = '\n{{ tbs }}control_create_clone_of({{ i1 }})'

control_create_clone_of_menu = '\ncontrol_create_clone_of_menu({{ f1 }})'

control_start_as_clone = '\n{{ tbs }}control_start_as_clone'

control_delete_this_clone = '\n{{ tbs }}control_delete_this_clone'

data_setvariableto = '\n{{ tbs }}{{ f1 }} = {{ i1 }}'

data_changevariableby = '\n{{ tbs }}{{ f1 }}+={{ i1 }}'

looks_sayforsecs = '\n{{ tbs }}return {{ i1 }}'

looks_say = '\n{{ tbs }}return {{ i1 }}'

motion_movesteps = '\n{{ tbs }}motion_movesteps({{ i1 }})'

operator_gt = '({{ i1 }} > {{ i2 }})'

operator_add = '({{ i1 }} + {{ i2 }})'

operator_subtract = '({{ i1 }} - {{ i2 }})'

operator_multiply = '({{ i1 }} * {{ i2 }})'

operator_divide = '({{ i1 }} / {{ i2 }})'

operator_random = 'random.uniform({{ i1 }}, {{ i2 }})'

operator_equals = '({{ i1 }} == {{ i2 }})'

operator_join = '({{ i1 }} + {{ i2 }})'

operator_letter_of = '{{ i2 }}[{{ i1 }} - 1]'


operator_length = 'len({{ i1 }})'

operator_contains = '({{ i2 }} in {{ i1 }})'

operator_mod = '({{ i1 }} % {{ i2 }})'

operator_round = 'Decimal({{ i1 }}).to_integral_value(rounding=ROUND_HALF_UP)'

operator_and = '({{ i1 }} and {{ i2 }})'

operator_or = '({{ i1 }} or {{ i2 }})'

operator_not = '(not {{ i1 }})'

operator_lt = '({{ i1 }} < {{ i2 }})'

control_repeat_until = '\n{{ tbs }}while not {{ i1}}:{{ sb1 }}'

control_repeat = '\n{{ tbs }}for __index__ in range({{ i1 }}):{{ sb1 }}'

control_if_else = '\n{{ tbs }}if {{ i1 }}:{{ sb1 }}\n{{ tbs }}else:{{ sb2 }}'

control_if = '\n{{ tbs }}if {{ i1 }}:{{ sb1 }}\n'

sensing_dayssince2000 = 'sensing_dayssince2000'


# math operations

operator_mathop = ''

abs = 'abs({{ i1 }})'


floor = 'floor({{ i1 }})'

ceiling = 'ceil({{ i1 }})'

sqrt = 'sqrt({{ i1 }})'

sin = 'sin({{ i1 }})'

cos = 'cos({{ i1 }})'

tan = 'tan({{ i1 }})'

asin = 'asin({ i1 }})'

acos = 'acos({{ i1 }})'

atan = 'atan({{ i1 }})'

log = 'log2({{ i1 }})'

ln = 'log10({{ i1 }})'

exp = 'exp({{ i1 }})'

pow10 = 'pow(10, {{ i1 }})'


procedures_definition = '''from math import *   # pragma: no cover
from decimal import *   # pragma: no cover
import random           # pragma: no cover
import math             # pragma: no cover
import sys             # pragma: no cover

def {{ i1 }}:'''

procedures_prototype = '{{ i1 }}({{ i2 }})'

argument_reporter_string_number = ' {{ f1 }} '

scratchToPython = {
    'event_whenflagclicked': event_whenflagclicked,
    'control_forever': control_forever,
    'control_stop': control_stop,
    'control_wait': control_wait,
    'control_wait_until': control_wait_until,
    'control_create_clone_of': control_create_clone_of,
    'control_create_clone_of_menu': control_create_clone_of_menu,
    'control_start_as_clone': control_start_as_clone,
    'control_delete_this_clone': control_delete_this_clone,
    'data_setvariableto': data_setvariableto,
    'data_changevariableby': data_changevariableby,
    'looks_sayforsecs': looks_sayforsecs,
    'looks_say': looks_say,
    'motion_movesteps': motion_movesteps,
    'operator_gt': operator_gt,
    'operator_add': operator_add,
    'operator_subtract': operator_subtract,
    'operator_multiply': operator_multiply,
    'operator_divide': operator_divide,
    'operator_random': operator_random,
    'operator_equals': operator_equals,
    'operator_join': operator_join,
    'operator_letter_of': operator_letter_of,
    'operator_length': operator_length,
    'operator_mod': operator_mod,
    'operator_round': operator_round,
    'operator_and': operator_and,
    'operator_or': operator_or,
    'operator_not': operator_not,
    'operator_lt': operator_lt,
    'operator_contains': operator_contains,
    'control_repeat_until': control_repeat_until,
    'control_repeat': control_repeat,
    'control_if_else': control_if_else,
    'control_if': control_if,
    'e ^': exp,
    'ln': ln,
    'log': log,
    'atan': atan,
    'acos': acos,
    'asin': asin,
    'tan': tan,
    'abs': abs,
    'operator_mathop': operator_mathop,
    'sensing_dayssince2000': sensing_dayssince2000,
    'floor': floor,
    'ceiling': ceiling,
    'sqrt': sqrt,
    'sin': sin,
    'cos': cos,
    'pow10': pow10,
    'procedures_definition': procedures_definition,
    'procedures_prototype': procedures_prototype,
    'argument_reporter_string_number': argument_reporter_string_number
}
