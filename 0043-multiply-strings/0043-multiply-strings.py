class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        def conversion(num):
            dic={'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}
            ans=0
            for i in num:
                ans=ans*10 + dic[i]
            return ans
        return str(conversion(num1)*conversion(num2))                
        