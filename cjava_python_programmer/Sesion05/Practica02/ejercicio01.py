class Math:
    
    def pow(self,x, n):
        """ 
        Funcion que calcula un numero elevado a la potencia
        """

        resultado = 1
        for i in range(1,n+1): 
            resultado=x*resultado 

        return resultado

math_operator = Math()
print(math_operator.pow(2,2)) 
print(math_operator.pow(5,4))
print(math_operator.pow(2,7))