import random
def method1(iters):
    PAIR_MAPPING = {
        (1, 1): "WIN", (1, 2): "WIN", (1, 3): "WIN", (1, 4): "WIN", (1, 5): "WIN", (1, 6): "WIN",
    
        (2, 1): "LOSE", (2, 2): "LOSE", (2, 3): "LOSE", (2, 4): "LOSE", (2, 5): "LOSE", (2, 6): "LOSE",
        (3, 1): "LOSE", (3, 2): "LOSE", (3, 3): "LOSE", (3, 4): "LOSE", (3, 5): "LOSE", (3, 6): "LOSE",
        (4, 1): "LOSE", (4, 2): "LOSE", (4, 3): "LOSE", (4, 4): "LOSE", (4, 5): "LOSE", (4, 6): "LOSE",
        (5, 1): "LOSE", (5, 2): "LOSE",
    
        (5, 3): "REROLL", (5, 4): "REROLL", (5, 5): "REROLL", (5, 6): "REROLL",
        (6, 1): "REROLL", (6, 2): "REROLL", (6, 3): "REROLL", (6, 4): "REROLL", (6, 5): "REROLL", (6, 6): "REROLL"
    }
    def signal_draw():
        n = random.randint(1, 6)
        p = random.randint(1, 6)

        pair = (n, p)

        result = PAIR_MAPPING[pair]
        new_draws = 2

        return result, new_draws

    num_wins = 0
    num_losses = 0
    num_draws = 0

    for _ in range(int(iters)):
        r = "REROLL"

        while r == "REROLL":
            r, new_draws = signal_draw()
            num_draws += new_draws
        if r == "WIN":
            num_wins+=1
        else:
            num_losses += 1

    return num_wins/iters, num_draws/iters

def method2(iters):
    def signal_draw():
        n = random.randint(1, 6)
     

        if n == 1:
            return "WIN", 1

        elif n in [2, 3, 4]:
            return "LOSE", 1

        elif n == 6:
            return "REROLL", 1

        elif n == 5:
            p = random.randint(1, 6)
            if p < 3:
                return "LOSE", 2
            elif p >= 3:
                return "REROLL", 2


    num_wins = 0
    num_losses = 0
    num_draws = 0

    for _ in range(int(iters)):
        r = "REROLL"

        while r == "REROLL":
            r, new_draws = signal_draw()
            num_draws += new_draws
        if r == "WIN":
            num_wins+=1
        else:
            num_losses += 1

    return num_wins/iters, num_draws/iters

def method3(iters):
    num_draws = 0
    num_wins = 0

    def single_iter():
        result = "REROLL"
        current_prob = 3/13
        draws = 0
        while result == "REROLL":
            draws += 1
            n = random.randint(1, 6)

            prob_transformation = 6 * current_prob 

            lower = int(prob_transformation)
            upper = lower + 1

            if n <= lower:
                result = "WIN"


            elif n > upper: 
                result = "LOSE"

            else:
                result = "REROLL"
                current_prob = (prob_transformation/6 - lower/6)/(1/6)
                

        
        return result, draws
    for _ in range(int(iters)):
        result, draws = single_iter()
        if result == "WIN":
            num_wins += 1
        num_draws += draws

    return num_wins/iters, num_draws/iters
if __name__ == "__main__":
    print("Intended Probability:", 3/13)

    win_percentage, ev_draws = method1(1e6)

    print("Method 1 Win Percentage:", win_percentage)
    print("Method 1 EV (Simulated):", ev_draws)
    print("Method 1 EV (Analytic):", 2 * 36/26)


    win_percentage, ev_draws = method2(1e6)

    print("Method 2 Win Percentage:", win_percentage)
    print("Method 2 EV (Simulated):", ev_draws)
    print("Method 2 EV (Analytic):", 36/26 * 7/6)

    win_percentage, ev_draws = method3(1e7)

    print("Method 3 Win Percentage:", win_percentage)
    print("Method 3 EV (Simulated):", ev_draws)
    print("Method 3 EV (Analytic):", 1.2)


    

    
        
        

    