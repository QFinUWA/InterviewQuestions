## Nash Equilibria

Many questions revolve around this notion of mixed strategies in 0-sum two player games. A mixed strategy can be defined as a strategy where the action taken is probabilistic, designed to make the opponent indifferent in their action. This may seem strange, but consider the example below.

### 1. Aces and Queens:

#### Question:  
Consider a two player poker-like game. There is $1 in the pot, and both players have $1 behind. There are no cards dealt (the higher pocket hand wins). You have aces half the time, and queens half the time. The other player has kings every time. You are in position, and the other player checks to you (if you check back the hand ends). How should you act? 

#### Answer: 
Clearly, you should bet when you have aces, as you either get called or don't but never lose. The question is should you bet with a queen. 

If you never bet with your queen, the other player should fold when you bet (they're never good). If you always bet with your queen, they should always call (they wi 50% of the time and are getting 2:1 odds to call).

Specifically, for these cases we can describe the EV of the other player for their actions.

Always Bet Queens:

Opponent Calls: $EV_{opponent} = 0.5(-1) + 0.5(2) = 0.5$ (when they call they get the dollar in the pot and your dollar)

Opponent Folds: $EV_{opponent} = 0$ (always folding)

Never Bet Queens:

Opponent Calls: $EV_{opponent} = 0.5(-1) + 0.5(1) = 0$ (when you bet you win, when you don't it just checks through)

Opponent Folds: $EV_{opponent} = 0.5(0) + 0.5(1) = 0.5$

So, with optimal strategy you both get &#36;0.50 of EV. Consider the case where you bet with half your queens. As such, 25\% of the time it checks though and your opponent wins (you have a queen), and $\frac{2}{3}$ of the time yoou beet you have a queen.

Opponent Calls: $EV = 0.25(1) + \frac{3}{4} (\frac{2}{3} (-1) + \frac{1}{3} (2)) = 0.25$

Opponent Folds: $EV = 0.25(1) = 0.25$

They less money - you get more. Great!

Indeed, it is actually correct to bet half your queens. There are two ways to show this that rely on this indifference notion

1) Intuitive Manner:

When your opponent calls they get paid 2:1. As such, to be indifferent about calling they must be winning a third of time. This occurs when you bet a queen half the time

2) More Math

Can also find the point at which the marginal EV to them of calling is 0 (clearly the marginal EV of folding is 0, so this is the point where the options have the same EV causing indifference). Consider $p$ the frequency of betting with a queen. (So if you bet, you have an ace $\frac{p}{1+p}$ of the time)

$EV_{marginal} = \frac{p}{1+p}(-1) + \frac{1}{1+p}(2) = 0$

Can solve this to give p = 0.5. Again we consider the ev from the POV of the opponent - we want them to be indifferent.

---

This outlines the basic idea of Nash questions - do the thing that makes your opponent indifferent. All the following questions do the same thing.

### 2. A Grid Payoff Scenario

#### Question: 
 Consider the following payoff grid. The entries are (player 1 payoff, player 2 payoff). For the respective actions. Player 1 chooses between up/down and Player 2 between left/right. 

| **P1 \\ P2** | **Left** | **Right** |
|-------------|----------|-----------|
| **Up**      | (3, -3)  | (-2, 2)   |
| **Down**    | (-1, 1)  | (0, 0)    |

What is the strategy employed?

#### Answer:
 Again, need to consider the EV of the opposition player to determine frequencies. Denote $p_L$ the probability Player 2 plays left, and $p_U$ the probability Player 1 plays up.

$EV_{P1, Up} = 3p_L - 2(1-p_L)$

$EV_{P1, Down} = -p_L$

Equate these to enforce indifference:

$3p_L - 2(1-p_L) = -p_L$

Can solve to give $p_L = \frac{1}{3}$

Similarly, consider the EV of Player 2:

$EV_{P2, Left} = -3p_U + (1 - p_U)$

$EV_{P2, Right} = 2p_U$

Can equate these, finding that $p_U = \frac{1}{6}$. As such, in equilibria, Player 1 goes up $\frac{1}{6}$ of the time, and Player 2 goes left $\frac{1}{3}$ of the time.