temp_f = int(input('Diga a temperatura em Fahrenheit:'))
f_para_c = (temp_f - 32)/1.8
print('A temperatura em graus Celcius é', f_para_c, 'C°')

def test():

temp_c = int(input('Diga a temperatura em Celcius'))
c_para_f = (1.8* temp_c) + 32
print('A temperatura em Farenheit é', c_para_f, 'F°'