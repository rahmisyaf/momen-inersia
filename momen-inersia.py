import pandas as pd # type: ignore
from tabulate import tabulate # type: ignore
import math

import time

bola_pejal = {'t (s)': [11.89, 9.321, 9.143, 8.441, 9.263],
					'n (s)': [10, 10, 10, 10, 10],
					'T (s)': [0, 0, 0, 0, 0],
					'T0 (s)': [0.267, 0.267, 0.267, 0.267, 0.267,],
					'I0 (kg.m²)': [0.967, 0.967, 0.967, 0.967, 0.967],
					'I (kg.m²)': [0, 0, 0, 0, 0]
					}

silinder_pejal = {'t (s)': [7.857, 7.864, 6.727, 6.452, 6.417],
						'n (s)': [10, 10, 10, 10, 10],
						'T (s)': [0, 0, 0, 0, 0],
						'T0 (s)': [0.267, 0.267, 0.267, 0.267, 0.267,],
						'I0 (kg.m²)': [0.967, 0.967, 0.967, 0.967, 0.967],
						'I (kg.m²)': [0, 0, 0, 0, 0]
						}

silinder_pejal_174 = {'t (s)': [11.46, 11.82, 10.72, 11.57, 10.90],
							'n (s)': [10, 10, 10, 10, 10],
							'T (s)': [0, 0, 0, 0, 0],
							'T0 (s)': [0.267, 0.267, 0.267, 0.267, 0.267,],
							'I0 (kg.m²)': [0.967, 0.967, 0.967, 0.967, 0.967],
							'I (kg.m²)': [0, 0, 0, 0, 0]
							}

silinder_pejal_213 = {'t (s)': [13.09, 13.09, 12.78, 13.37, 12.81],
							'n (s)': [10, 10, 10, 10, 10],
							'T (s)': [0, 0, 0, 0, 0],
							'T0 (s)': [0.267, 0.267, 0.267, 0.267, 0.267,],
							'I0 (kg.m²)': [0.967, 0.967, 0.967, 0.967, 0.967],
							'I (kg.m²)': [0, 0, 0, 0, 0]
							}

silinder_berongga = {'t (s)': [8.248, 7.639, 7.937, 6.880, 6.995],
							'n (s)': [10, 10, 10, 10, 10],
							'T (s)': [0, 0, 0, 0, 0],
							'T0 (s)': [0.267, 0.267, 0.267, 0.267, 0.267,],
							'I0 (kg.m²)': [0.967, 0.967, 0.967, 0.967, 0.967],
							'I (kg.m²)': [0, 0, 0, 0, 0]
							}

kerucut_pejal = {'t (s)': [7.882, 7.593, 7.876, 9.089, 8.008],
						'n (s)': [10, 10, 10, 10, 10],
						'T (s)': [0, 0, 0, 0, 0],
						'T0 (s)': [0.267, 0.267, 0.267, 0.267, 0.267,],
						'I0 (kg.m²)': [0.967, 0.967, 0.967, 0.967, 0.967],
						'I (kg.m²)': [0, 0, 0, 0, 0]
						}

def inertia(data) :
	for i in range (5) :
		time = data['t (s)'][i]
		cycle_num = data['n (s)'][i]
		period = time/cycle_num
		data['T (s)'][i] = period

		first_period = data['T0 (s)'][i]
		first_inertia = data['I0 (kg.m²)'][i]

		inertia = ((period**2/first_period**2) - 1)*first_inertia
		data['I (kg.m²)'][i] = inertia
		
	print(f'inersia rata rata : {sum(data['I (kg.m²)'])/5}')
	
	df = pd.DataFrame(data) #creating dataframe from 'data'
	print(tabulate(df, 
						headers='keys', 
						tablefmt='grid')) #adding the border line and headers

def uncertainty(data) :
	data['(t - tbar)²'] = [0, 0, 0, 0, 0]
	
	mean = sum(data['t (s)'])/5

	for i in range (5) :
		data['(t - tbar)²'][i] = (data['t (s)'][i] - mean)**2

	uncer = math.sqrt(sum(data['(t - tbar)²'])/5)

	df = pd.DataFrame(data, columns=['t (s)', '(t - tbar)²']) #creating dataframe from 'data'
	print(tabulate(df, 
						headers='keys', 
						tablefmt='grid')) #adding the border line and headers

	uncertainty_value = {'tbar' : [mean], 'σ' : [uncer] }

	df = pd.DataFrame(uncertainty_value)
	print(tabulate(df, 
					headers='keys', 
					tablefmt='grid'))

def show_inertia() :
	print("~~~~~~~~~~~~~~~~~~~~~~ BOLA PEJAL ~~~~~~~~~~~~~~~~~~~~~~~~~")
	inertia(bola_pejal)

	print("~~~~~~~~~~~~~~~~~~~~~~ SILINDER PEJAL ~~~~~~~~~~~~~~~~~~~~~~~~~")
	inertia(silinder_pejal)

	print("~~~~~~~~~~~~~~~~~~~~~~ SILINDER PEJAL 174 ~~~~~~~~~~~~~~~~~~~~~~~~~")
	inertia(silinder_pejal_174)

	print("~~~~~~~~~~~~~~~~~~~~~~ SILINDER PEJAL 213 ~~~~~~~~~~~~~~~~~~~~~~~~~")
	inertia(silinder_pejal_213)

	print("~~~~~~~~~~~~~~~~~~~~~~ SILINDER BERONGGA ~~~~~~~~~~~~~~~~~~~~~~~~~")
	inertia(silinder_berongga)
	
	print("~~~~~~~~~~~~~~~~~~~~~~ KERUCUT PEJAL ~~~~~~~~~~~~~~~~~~~~~~~~~")
	inertia(kerucut_pejal)

def show_uncertainty() :
	print("~~~~~~~~~~~~~~~~~~~~~~ BOLA PEJAL ~~~~~~~~~~~~~~~~~~~~~~~~~")
	uncertainty(bola_pejal)

	print("~~~~~~~~~~~~~~~~~~~~~~ SILINDER PEJAL ~~~~~~~~~~~~~~~~~~~~~~~~~")
	uncertainty(silinder_pejal)

	print("~~~~~~~~~~~~~~~~~~~~~~ SILINDER PEJAL 174 ~~~~~~~~~~~~~~~~~~~~~~~~~")
	uncertainty(silinder_pejal_174)

	print("~~~~~~~~~~~~~~~~~~~~~~ SILINDER PEJAL 213 ~~~~~~~~~~~~~~~~~~~~~~~~~")
	uncertainty(silinder_pejal_213)

	print("~~~~~~~~~~~~~~~~~~~~~~ SILINDER BERONGGA ~~~~~~~~~~~~~~~~~~~~~~~~~")
	uncertainty(silinder_berongga)

	print("~~~~~~~~~~~~~~~~~~~~~~ KERUCUT PEJAL ~~~~~~~~~~~~~~~~~~~~~~~~~")
	uncertainty(kerucut_pejal)

def show() :
	show_inertia()
	show_uncertainty()

start = time.time()
show()
stop = time.time()

print(f'time : {stop - start}')
