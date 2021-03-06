from random import randint

def quick_sort(sequence):
    length = len(sequence)
    if length <= 1:
        return sequence
    else: 
        pivot = sequence.pop()
        
        lower_bin = []
        upper_bin = []

        for element in sequence:
            if element > pivot:
                upper_bin.append(element)
            else:
                lower_bin.append(element)
  
        return quick_sort(lower_bin) + [pivot] + quick_sort(upper_bin)

#This rand array generator is from https://realpython.com/sorting-algorithms-python/
ARRAY_LENGTH = 100
array = [randint(0,100) for i in range(ARRAY_LENGTH)]

#[5,3,4,7,9,2,10,15,0,5]
print(array)
print(quick_sort(array))