def quickSort(array,l,h):
    if(l<h):
        p=partition(array,l,h)
        quickSort(array,l,p-1)
        quickSort(array,p+1,h)

def partition(array,l,h):
    pivot=array[l]
    i=l
    j=h
    while(i<j):
        while((i<j) &(array[j]>=pivot)):
            j-=1

        while((i<j) & (array[i]<=pivot)):
            i+=1

        swap(array,i,j)

    swap(array,l,j)
    return j


def findKth(array,k,l,h):
    while(l<h):
        p = partition(array, l, h)
        if p<k:
            l=p+1
        elif p>k:
            h=p-1
        else:
            break
    return array[k]

def swap(array,i,j):
    tmp=array[i]
    array[i]=array[j]
    array[j]=tmp

if __name__=='__main__':
    array=[2,5,1,4,7,9,3]
    #print(partition(array, 3, len(array) - 1))
    quickSort(array,0,len(array)-1)
    print(array)
    print(findKth(array, 6, 0, len(array) - 1))