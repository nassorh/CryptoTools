#Cryptography#

class CryptoTools():

    def __init__(self,data):
        #data is inputted in as an array
        self.data = data
        self.ref = {'e': 13.62,'n': 7.83,'i': 7.49,'o': 7.33, 't': 7.32,'s': 7.22,'a': 7.01,'r': 6.46,'d': 5.17,'l': 4.32,'h': 3.16,'u': 3.08,'m': 2.94,'c': 2.81,'p': 2.67, 'y':2.39, 'g':2.12, 'f':1.72, 'w':1.51, 'b':1.33, 'v':1.15, 'k':0.54, 'x':0.41, 'j':0.23, 'q':0.15 , 'z':0.04}

    def alpha_to_num(self):
        num = ""
        for alpha in self.data:
            num += str(ord(alpha)-96)+" " #Changes the string into numbers and adds to string
        return num #Returns numeric equivalent 

    def num_to_alpha(self):
        alpha = ""
        for num in self.data:
            alpha += chr(num+96)+" " #Changes the number into strings and adds to string
        return alpha #Returns alpha equivalent 

    def ROT13(self):
        decrypt = " "
        for alpha in self.data:
            if ord(alpha) >= 78 and ord(alpha) <= 90: #Between N and Z
                decrypt += chr(ord(alpha)-13)+" " #Moves it back 13
            elif ord(alpha) >= 110 and ord(alpha) <= 122: #Between n and z
                decrypt += chr(ord(alpha)-13)+" " #Moves it back 13
            elif ord(alpha) >= 65 and ord(alpha) <= 77: #Between A and M
                decrypt += chr(ord(alpha)+13)+" " #Moves it foward 13
            elif ord(alpha) >= 97 and ord(alpha) <= 109: #Between a and m
                decrypt += chr(ord(alpha)+13)+" " #Moves it foward 13
        return decrypt

    def freqanalysis(self):
        freq = dict()
        for letter in self.data:
            if letter in freq:
                freq[letter] = freq[letter] + 1 #Incrments amount by the 1
            else:
                freq[letter] = 1 #Add the character to the dict 

        for letter,amount in freq.items():
            freq[letter] = round(amount/len(self.data)*100,2) #Converts all into percentages

        return freq

    def ceasarCipher(self,shift):
        shift = int(shift)
        string = ""
        for x in self.data:
            Num = ord(x)-97#Changes a to 0 because mod 26 cause a = 0
            newNum = (Num + shift)%26 #Ensures it loops back around
            string += chr(newNum + 97)
        return string

    def digraph(self):
        valueResult = dict()
        for x in range(len(self.data)-1):
            if(self.data[x],self.data[x+1]) in valueResult:
                valueResult[file[x],file[x+1]] = valueResult[file[x],file[x+1]] + 1
            else:
                valueResult[file[x],file[x+1]] = 1
        return valueResult

    def trigraph(self):
        valueResult = dict()
    
        for x in range(len(self.data)-2):
            if (self.data[x],self.data[x+1],self.data[x+2]) in valueResult:
                valueResult[file[x],file[x+1],file[x+2]] = valueResult[file[x],file[x+1],file[x+2]] + 1
            else:
                valueResult[file[x],file[x+1],file[x+2]] = 1
        return valueResult

    def printDic(dic):
        for key, value in sorted(dic.items(), key=lambda item: item[1], reverse=True):
            print(key, value)



