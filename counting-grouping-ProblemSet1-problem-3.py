def item_order(order):
    while True:
        count1 = order.count("salad")
        count2 = order.count('hamburger')
        count3 = order.count("water")
        break
    return "salad:"+str(count1)+" hamburger:"+str(count2)+" water:"+str(count3)
