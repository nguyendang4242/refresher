''' 
Problem description:
    Given daily stock prices (open, daily low, and daily high), design an algorithm that determines the 
    maximum profit that could have been made by buying then selling a single share over a given day range,
    subject to the constraint that the buy and the sell have to take place at the start of the day.

Solution attempt:
    1. Intialize minimum buy price to be on first day.
    2. Intialize the total profit. Keep track of the days (indices) of the highest total. 
    3. Go through the list, update the minimum buy price if the current day's price is lower.
    4. Update the total if less than (current day price - minimum buy price). 
    5. Return the days (indices) associated with the final total profit. 

    Here's an example implementation of the algorithm. 
    Time complexity: O(N-1) - we loop through N-1 items of the input array once. 
    Space complexity: O(1) - constant variables stored.   

Brute force method:
    We have two nested loops -- the outer one starts are index i and the inner one starts at index j = i+1. 
    We loop through the input array n and keep track of the maximum profit, n[j] - n[i]. 
    Time complexity: O(N * N-1) = O(N^2) because we have a loop nested in another one. 
    Space complexity: O(1) because we have a fixed number of variables independent of input size. 
'''

def find_max_profit(openPrices):
    if (not openPrices or len(openPrices) <= 1):
        return (0)

    maxProfit = openPrices[1] - openPrices[0]
    minPrice = openPrices[0]

    for i in openPrices[1:]:
        diff = i - minPrice
        if (i < minPrice):
            minPrice = i

        maxProfit = diff if (diff > maxProfit) else maxProfit
    
    return (maxProfit)

# Should return 3
print(find_max_profit([1, 2, 3, 4]))

# Should return 19
print(find_max_profit([2, 10, -1, 11, 5, 7, 9, 18]))

# Should return -1
print(find_max_profit([4, 3, 2, 1, 0]))

# Should return 0, not enough data
print(find_max_profit([1]))