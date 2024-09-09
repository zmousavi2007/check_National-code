from os import system
def test_code(code):
    rest=False
    if 8<=len(code)<=10 and code.isdigit():
        if len(code)==9 or len(code)==8:
            code="0"*(10-len(code))+code
        s=0
        c=10
        for i in range(len(code)-1):
            s+=int(code[i])*c
            c-=1
        av=s%11
        if(av<2 and av==int(code[9]))or(11-av==(int(code[9]))):
            rest=True
        return rest 
def program():
    code=input("Enter your national code : ")
    print(f"{code} is valid" if test_code(code) else "National code is invalid ")
if __name__=="__main__":
        system('cls')
        program()
