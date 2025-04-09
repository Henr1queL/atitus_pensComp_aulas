temp_f = float(input('Diga a temperatura em Fahrenheit:'))
f_para_c = (temp_f - 32)/1.8
print('A temperatura em graus Celcius é', f_para_c, 'C°')
 
t_celsius = float(input('Diga a temperatura em Celcius'))
c_para_f = (1.8* t_celsius) + 32
print('A temperatura em Farenheit é', c_para_f, 'F°')

def test():
    assert (32 - 32) / 1.8 == 0.0
    assert (212 - 32) / 1.8 == 100.0
    assert (98.6 - 32) / 1.8 == 37.0
    
    assert (1.8 * 0) + 32 == 32.0
    assert (1.8 * 100) + 32 == 212.0
    assert (1.8 * 37) + 32 == 98.6