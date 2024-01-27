def distribute_pizza_slices(n):
    slice_large = 8
    slice_medium = 6
    slice_regular = 4
    slice_small = 1
    large = 0
    medium = 0
    regular = 0
    small = 0

    
    while n > 0:
        if n >= slice_large:
            large+=1
            n-=slice_large
        elif n>=slice_medium:
            medium+=1
            n-=slice_medium
        elif n>=slice_regular:
            regular+=1
            n-=slice_regular
        elif n>=slice_small:
            small+=1
            n -= slice_small
        else:
            break

    
    print(f"We need {large} Large pizzas")
    print(f"We need {medium} Medium pizzas")
    print(f"We need {regular} Regular pizzas")
    print(f"We need {small} Small pizzas.")


num = int(input("Enter the number of individuals: "))
distribute_pizza_slices(num)
