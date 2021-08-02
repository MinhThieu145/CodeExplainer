def caesarCipher(s, k):
    temp = []
    
    # chuyển tất cả character qua ASCII 
    for character in s:
        temp.append(ord(character))
        
    for i in range(len(temp)):
        # uppercase trong ASCII là từ 65 đến 90
        if 65 <= temp[i] <= 90:
            # -65 + k % 26 là để trường hợp nếu số vượt qua 90 thì quay ngược lại 
            temp[i] = (65 + ((temp[i]) - 65 + k)% 26) 
        # lowercase trong ASCII là từ 97 đến 122
        elif 97 <= temp[i] <= 122:
            # để quay ngược tương tự như trên
            temp[i] = (97 + ((temp[i]) - 97 + k)% 26) 
    return ("".join(chr(x) for x in temp))