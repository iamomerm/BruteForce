import os
import itertools
from selenium import webdriver

# Driver
chrome_driver = webdriver.Chrome(executable_path='chromedriver\chromedriver.exe')
chrome_driver.get('file:\\' + str(os.path.abspath('webpage\Index.html')))

#Alphabet = 'aAbBcCdDeEfFgGhHiIjJkKlLmMnNoOpPqQrRsStTuUvVwWxXyYzZ123456789!@#$%^&*()'

Alphabet = 'admin'

print('Passwords: \n')

# Calculate Possibilties (Pass Length = 5)
Possibilities = (itertools.product(Alphabet, repeat=5))

Counter = 0
LPWD = '';

for Tuple in Possibilities:
	Counter = Counter + 1
	
	PW = ''.join(Tuple)
	
	try:
		chrome_driver.find_element_by_id("Password").send_keys(PW)
		chrome_driver.find_element_by_id("Login").click()
		print(str(Counter) + ' - ' + PW)
		LPWD = PW # Last Password
		
	except: 
		print('Decrypted Password: ' + LPWD + ', Iterations: ' + str(Counter - 1))
		break
