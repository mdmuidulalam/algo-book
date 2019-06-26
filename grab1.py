def Solution(a, b, arr):
    str1 = ""
    str2 = ""
    
    for item in arr:
        if item == 1:
            if a==0 and b== 0:
                return "Not Possilbe"
            if a > b:
                str1 += "1"
                str2 += "0"
                a -= 1
            else:
                str1 += "0"
                str2 += "1"
                b -= 1
        if item == 2:
            if a==0 or b== 0:
                return "Not Possilbe"
            str1 += "1"
            str2 += "1"
            a -= 1
            b -= 1

    if a != 0 or b!= 0 :
        return "Not Possilbe"

    return str1 + "," + str2

print(Solution(2,4,[0,2,2,2,0]))