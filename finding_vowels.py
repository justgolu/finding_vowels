st= input("Enter String: ")
vowels =0
for i in st:
    if(i=="a" or i=="e" or i=="i" or i=="o" or i=="u" or i=="A" or i=="E" or i=="I" or i=="O" or i=="U"):
        vowels=vowels + 1

print("No of vowels present: ",vowels)