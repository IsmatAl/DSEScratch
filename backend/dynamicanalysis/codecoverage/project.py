
from math import *
from decimal import *
import random
import math

def lcm( x ,  y ):
	prod = ( x  *  y )
	if (prod == 0):
		return 0
	if ( x  >  y ):
		greater =  x 
	else:
		greater =  y 
	while True:
		if (((greater %  x ) == 0) and ((greater %  y ) == 0)):
			lcm = greater
			return lcm
			break
		greater = (greater + 1)