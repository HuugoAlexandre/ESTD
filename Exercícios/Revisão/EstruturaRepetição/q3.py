cidade_a = 80000
cidade_b = 200000
taxa_anual_crescimento_cidade_a = 3/100
taxa_anual_crescimento_cidade_b = 1.5/100

anos = 0
while cidade_a < cidade_b:
    cidade_a += cidade_a * taxa_anual_crescimento_cidade_a 
    cidade_b += cidade_b * taxa_anual_crescimento_cidade_b 
    anos+=1

print(f"Serão necessários {anos} anos para que a cidade A se iguale ou supere a cidade B.")