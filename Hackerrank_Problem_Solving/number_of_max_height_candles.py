# You are in charge of the cake for a child's birthday. 
# You have decided the cake will have one candle for each year of their total age. 
# They will only be able to blow out the tallest of the candles. Count how many 
# candles are tallest.

def birthdayCakeCandles(candles):
    # Write your code here
    count=0
    max_height = 0
    for i in range(len(candles)-1):
        if(candles[i]>=max_height):
            if(candles[i]>=candles[i+1]):
                max_height=candles[i]
            else:
                max_height=candles[i+1]
    for candle in candles:
        if(candle == max_height):
            count += 1
            print(candle)
    return count

arr = [82,49,82,82,41,82,15,63,38,25]
print(birthdayCakeCandles(arr))