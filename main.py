def encontrarResistencia(a, b, c, d):
      
    digito_cor = {'preto': '0',
                   'marrom': '1', 
                   'vermelho': '2',
                   'laranja': '3', 
                   'amarelo': '4',
                   'verde' : '5', 
                   'azul' : '6',
                   'violeta' : '7', 
                   'cinza' : '8',
                   'branco': '9'}
      
    multiplicador = {'preto': '1',
                  'marrom': '10', 
                  'vermelho': '100', 
                  'laranja': '1k', 
                  'amarelo': '10k', 
                  'verde' : '100k', 
                  'azul' : '1M', 
                  'violeta' : '10M', 
                  'cinza' : '100M', 
                  'branco': '1G'}
      
    tolerancia = {'marrom': '+/- 1 %', 
                  'vermelho' : '+/- 2 %', 
                 'verde': "+/- 0.5 %", 
                  'azul': '+/- 0.25 %', 
                 'violeta' : '+/- 0.1 %', 
                  'dourado': '+/- 5 %', 
                 'prateado' : '+/- 10 %', 
                  'nenhum': '+/-20 %'}
      
    if a in digito_cor\
       and b in digito_cor\
       and c in multiplicador\
       and d in tolerancia:
           xx = digito_cor.get(a)
           yy = digito_cor.get(b)
           zz = multiplicador.get(c)
           aa = tolerancia.get(d)
           print("Resistencia: = "+xx + yy+" x "+zz+" ohms. Tolerância = "+aa)
    else:
        print("Cor inválida!")
  

if __name__ == "__main__":
    a = input("Digite a cor 1:")
    b = input("Digite a cor 2:")
    c = input("Digite a cor 3:")
    d = input("Digite a cor 4:")
      
    encontrarResistencia(a, b, c, d)
