# code from April 29 lecture
# The basic searching and sorting routines

def iterative_bubble_sort(numbers):
    # go through the entire list of numbers
    for i in range(len(numbers) - 1, 0, -1):
        for j in range(i):
            if (numbers[j] > numbers[j + 1]):
                # swap the numbers - we'll use a temp
                temp = numbers[j]
                numbers[j] = numbers[j + 1]
                numbers[j + 1] = temp
    return (numbers)

def recursive_bubble_sort (numbers):
   if len(numbers) == 1:
       return(numbers)
   else:
       #bubble the largest number to the end
       for j in range(len(numbers)-1):
           if numbers[j] > numbers[j+1]:
               temp = numbers[j]
               numbers[j] = numbers[j+1]
               numbers[j+1] = temp
#then recursively call the function with
#all but the last element of the list
       new_nums = recursive_bubble_sort(numbers[:-1])
       #add the last element back on
       sorted_list = new_nums + numbers[-1:]
       return(sorted_list)

def iterative_selection_sort(numbers):
    for i in range(len(numbers)):

    #find the smallest element remaining in the
    #unsorted list. Start by presuming it's the
    #first element
        smallest = i
        for j in range(i + 1, len(numbers)):
            if numbers[smallest] > numbers[j]:
                smallest = j

        # When the loop is done, we know that smallest is
        # the index of the smallest value. Swap it
        # with the first element
        temp = numbers[smallest]
        numbers[smallest] = numbers[i]
        numbers[i] = temp


def recursive_selection_sort(nums):
    # The base case is: a list of length 0 or 1 is sorted
    if len(nums) <= 1:
        return nums
    else:
        # the core of the algorithm is the same
        # as the iterative routine
        index_of_smallest = 0
        for j in range(1, len(nums)):
            if nums[j] < nums[index_of_smallest]:
                index_of_smallest = j
# now swap the smallest element found with the first
        temp = nums[0]
        nums[0] = nums[index_of_smallest]
        nums[index_of_smallest] = temp
       #now make the recursive call with the first
       #element stripped out
        r = recursive_selection_sort(nums[1:])
        results = nums[:1] + r
        return results

def quicksort(list_of_nums):
    # base case - a list of length one is sorted
    if len(list_of_nums) <= 1:
        return (list_of_nums)
    # recursive case
    else:
        # pick a pivot - the first element
        pivot = list_of_nums[0]
        # define three empty lists, for elements greater than the pivot, less than the pivot, and equal to the pivot
        less = []
        equal = []
        greater = []
# go through the list and put each element in the proper list
        for i in range(len(list_of_nums)):
            if list_of_nums[i] > pivot:
               greater.append(list_of_nums[i])
            elif list_of_nums[i] == pivot:
               equal.append(list_of_nums[i])
            else:
               less.append(list_of_nums[i])
            results = quicksort(less) + equal + quicksort(greater)
        return(results)


def binary_search (numbers, target):
   if len(numbers)//2 == 0:
       return -1
   if numbers[len(numbers)//2] == target:
       return len(numbers)//2
   elif numbers[len(numbers)//2] > target:
       return binary_search(numbers[:len(numbers)//2], target)
   else:
       return binary_search(numbers[len(numbers)//2:], target)

if __name__ == "__main__":
    #generate a random 10 integer list

    from random import randint
    random_nums = []
    for i in range(10):
        random_nums.append(randint(0,9))
    print(random_nums)

    answer = iterative_bubble_sort(random_nums)
    print(answer)



