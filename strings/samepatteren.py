def search(pat,text):
    n= len(text)
    m = len(pat)
    
    for i in range(n-m+1):
        j = 0
        while j<m :
            if text[i+j] != pat[j]:
                break
            j += 1
            
        if j == m:
            print("index: ",i)
            
            
txt = "AABAACAADAABAAABAA"
pat = "AABA"
search(pat, txt)