
"""
Binary search
test_case1 is test Cases
"""

test_case1={
    'input':[1,2,3,6,8,9,10,11,12,13],
    'search_key':[-10,-1,1,4,11,12,13,14,200],
    'result':[-1,-1,0,-1,7,8,9,-1,-1]
}



def my_search(input,key):
    len_input=len(input)
    #print(len_input)
    min_index=0
    max_index=len_input-1
    mid_index=(min_index+max_index)//2
    result=-1
    i=1
    if len_input<1:
        return result



    while min_index<=max_index:  
        #print(f'this {i} iteration, and index is {mid_index} and value is {input[mid_index]}, key is {key}, maxindex is {max_index}')  

        if input[mid_index]  == key:
            result=mid_index
            #print(f'Found the item {input[mid_index]} at index {mid_index}')
            return result

        elif input[mid_index]< key:
            min_index=mid_index+1
            mid_index=(min_index+max_index)//2
            #print(f'loop1: index {mid_index} and value {input[mid_index]}')

        elif input[mid_index]>key:
            max_index=mid_index-1
            mid_index=(min_index+max_index)//2
           # print(f'loop2: index {mid_index} and value {input[mid_index]}')
            
        i+=1
        if i==20:
            result=i
            return i

    return result




# call function with test cases
i=0  
while i<len(test_case1["input"])-1:
    print(my_search(test_case1["input"], test_case1["search_key"][i])==test_case1["result"][i])
    i+=1

    