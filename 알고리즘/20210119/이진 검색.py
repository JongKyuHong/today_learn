def binary(gene,key_codon):
    low , high = 0,len(gene)-1
    while low <= high:
        mid = (low+high)//2
        if gene[mid] < key_codon:
            low = mid + 1
        elif gene[mid] > key_codon:
            high = mid - 1
        else:
            return True
    return False
gene = [i for i in range(int(input()))]
key_codon = int(input())
print(binary(gene,key_codon))