# 7-2 Count
# Count all letters, digits, and special symbols from a given string


word = input()

Tarer = 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 97,  98,  99,  100,  101,  102,  103,  104,  105,  106,  107,  108,  109,  110, 111,  112,  113,  114,  115,  116,  117,  118,  119,  120,  121,  122 
Tvanshanner = 48,49,50,51,52,53,54,55,56,57
nshanner = 33,34,35,36,37,38,39,40,41,42,43,44,45,46,47


chars = 0
digits = 0
symbol = 0


for i in word :
    if  ord(i) in Tarer :
        chars = chars + 1
    elif ord(i) in Tvanshanner :
        digits = digits + 1 
    elif ord(i) in nshanner :
        symbol = symbol + 1    

print(f"chars {chars}")
print(f"digits {digits}")
print(f"symbol {symbol}")
