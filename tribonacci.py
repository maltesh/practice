def tribonacci(signature, n):
    a, b, c = signature
    if not n :
        return []
    if n < len(signature):
        return signature[:n]
    i = 3
    temp = signature[:]
    while i < n :
        k = sum(temp[::-1][:3])
        temp.append(k)
        i = i +1
    return temp



# def tribonacci(signature,n):
#     while len(signature) < n:
#         signature.append(sum(signature[-3:]))
    
#     return signature[:n]