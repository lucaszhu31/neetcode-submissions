class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #The simple way is to simply use a set, as its a data structure that naturally removes duplicates, so thus its most likely O(1) or like even no time. So if the length of the set and the list is the same then output false and else output false. this runs in O(1) since its using the len function. in terms of memory, its maybe o(1) as well? 
        # For learning purposes, lets do it withotu the set though
        # We could simply do the brute force method, where you use an O(n^2) double for loop to check to see if the number appears twice in the list. Or you can define a hash map, loop thourhg the list so its O(N) and see if the key exists in the hash map, and if it does that means there is a duplicate, so you can reutrn true. Lets implement this: 
        check_dups = {}
        for i in nums: 
            if i in check_dups:
                return True
            check_dups[i] = 0
        return False       
        #Wait matter of fact I could just use a python list, actually no since that would be O(N^2), same for a dynamic array, however, using a hash map and a static array like using numpy would still both acheive O(N)
        #So that should be the solution but lets test, so lets use the array in the example, im tracing...  so yeah we could put an integer as a key since its immutable or hashable