class Solution:
    
    def nearestPalindromic(self, n):
        """
        :type n: str
        :rtype: str
        """
        
        number = int(n)
        modulos = "1" + "0"*(len(n)-2)
        isOdd = True;
       
        if(number <= 10):
            return str(number-1)
        if(number == 11):
            return str(9)
        elif(n[0]=="1" and number % int(modulos)==0):
            return str(number-1)
        # elif(n[0]=="1" and ((number-1)%int(modulos))==0):
        #     return str(number-2)
        else:
            
            if(len(n) %2 == 0):
                halfLength = int(len(n)/2)
                
                isOdd = False;
            else:
                halfLength = int(len(n)/2) + 1
                
            resLess = str(int(n[:halfLength])-1)
            resMore = n[:halfLength]
            resM = str(int(n[:halfLength])+1)
            resMoreFinal = makePalin(resMore, halfLength, isOdd, n)
            resLessFinal = makePalin(resLess, halfLength, isOdd, n)
            resMFinal = makePalin(resM, halfLength, isOdd, n)
            
            minAbs = min(abs(resLessFinal - number),abs(resMoreFinal - number),abs(resMFinal - number))
            
            if(abs(resLessFinal - number) == minAbs):
                if(abs(resMoreFinal - number) == minAbs):
                    return str(min(resLessFinal,resMoreFinal))
                elif(abs(resMFinal - number) == minAbs):
                    return str(min(resLessFinal,resMFinal))
                else:
                    return str(resLessFinal)
                
            if(abs(resMoreFinal - number) == minAbs):
                if(abs(resMFinal - number) == minAbs):
                    return str(min(resMFinal,resMoreFinal))
                elif(abs(resLessFinal - number) == minAbs):
                    return str(min(resLessFinal,resMoreFinal))
                else:
                    return str(resMoreFinal)
                
            if(abs(resMFinal - number) == minAbs):
                if(abs(resMoreFinal - number) == minAbs):
                    return str(min(resMFinal,resMoreFinal))
                elif(abs(resLessFinal - number) == minAbs):
                    return str(min(resLessFinal,resMFinal))
                else:
                    return str(resMFinal)
            


def makePalin(res,halfLength,isOdd,n):
        number = int(n)
        if(isOdd):
                resFinal = res + res[halfLength-2::-1]         
                if(int(resFinal)==number):
                    if(res[halfLength-1:halfLength] == "0"):
                        resFinal = str(int(resFinal) + int("1"+"0"*(halfLength-1))) 
                    else:
                        resFinal = str(int(res)-1) + n[halfLength-2::-1]
        else:
                resFinal = res + res[halfLength-1::-1]
                if(int(resFinal)==number):
                    if(res[halfLength-1:halfLength+1] == "00"):
                        resFinal = str(int(resFinal) - int("11"+"0"*(halfLength-2))) 
                    else:
                        resFinal = str(int(res)-1) + str(int(n[halfLength:halfLength+1])-1) + res[halfLength+1:]
        return int(resFinal)  
    