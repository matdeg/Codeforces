"""
buy x tickets on the day i costs:
    x * ai + remaining * x


if i buy 
    x tickets on day i
    y tickets on day j
    z tickets on day k

    it costs 

    x * ai + (y + z) * x
    y * aj +      z  * y
    z * ak

if costs are 
1 2 3 4 5 
and m = 3

then for x ticket 
1 -> 1 0 0 0 0
2 -> 2 0 0 0 0
3 -> 3 0 0 0 0
4 ->  


"""