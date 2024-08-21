def media_mobile(numeri,n):
    media=[]
    
    for i in range(len(numeri)):
        if i<n:
            media.append((sum(numeri[:i+1]))/min(i+1,n))

    for i in range(len(numeri)-n):
            media.append(sum(numeri[i+1:i+(n+1)])/n)
    
    return media


numeri=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19]
n=3
print(media_mobile(numeri,n))





    
         
        