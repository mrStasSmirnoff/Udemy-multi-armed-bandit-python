count = 0
old_estimate = 0.0
while True:
    count += 1
    val = float(input("enter a number : "))
    cur_estimate = old_estimate + (1/count) * (val - old_estimate)
    #cur_estimate = old_estimate + (0.99) * (val - old_estimate) #with the sample size grown the contribution of each new sample decreases, lets mitigate by const step.
    old_estimate = cur_estimate
    print(f"running average : {cur_estimate}")