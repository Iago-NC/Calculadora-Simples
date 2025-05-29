#!/usr/bin/env python
# coding: utf-8

# Código para uma simples calculadora.

# In[3]:


print("bem vindo a calculadora!")

num1 = float(input("Digite o primeiro número!"))
num2 = float(input("Digite o segundo número!"))
operacao = input("Selecione a operação (+ , - , / , *):")

if operacao  == "+":
    resultado = num1 + num2
    print("O resultado é: ", resultado)
    
elif operacao == "-":
    resultado = num1 - num2
    print("O resultado é: " , resultado)
    
elif operacao == "/":
    resultado = num1 / num2
    print("O resultado é: " , resultado)
    
elif operacao == "*":
    resultado = num1 * num2
    print("O resultado é: " , resultado)
    
else:
    print("operação inválida!")


# In[ ]:





# In[ ]:




