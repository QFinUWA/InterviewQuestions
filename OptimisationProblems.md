## Optimal Stopping / Threshold Games

### 1. D20 Threshold Game

#### Question:  
You have a dice with 20 (a D20). You have 100 turns in total. You roll the dice until you get a roll Y that is greater or equal than X, and then receive &#36;Y per turn for the remaining turns. Find X that that maximises the expected value of this game (no calculator).

An example:

If you pick 13, and it takes 8 rolls to get a 13 you make 13*92 dollars.

---

#### Answer:

Money per turn in expectation: $$\frac{X + 20}{2}$$

Turns to roll >= X: There are 20 numbers in total, and (20 - X + 1) that are >= X. Therefore on each there is a probability of (20 - X + 1)/20 of ending, so in expectation it takes $$\frac{20}{20 - X + 1}$$ to get to a number that we are happy with.

Remaining rolls after getting it in expectation: $$100 - \frac{20}{20 - X + 1}$$

So, the expectancy of the game can be given by:

$$(X + 20)/2 * (100 - 20/(20 - X + 1))$$

There is a trick in optimising these things. Option 1 is to differentiate, which is messy and perhaps doesn't demonstrate exceptional reasoning skills.

Option 2 is to consider the rate of change of the different parts. The first part has a derivative of 0.5, so it increases by roughly 0.5/15 every time (very rough). Here note that 15 is my rough prior on what the answer will be.

Need to consider when the latter part is decreasing by roughly that much. So the latter part will be idk roughly 90. 0.5/15 is 3/90. So, when is 20/(20 - X + 1) roughly changing by 3.

So, we can set that for what X changing X by 1 changes 20/(20 - X + 1) by 3. From X = 20 to X = 19, it changes the quotient by 10, X = 19 to X = 18 changes it from 10 to 6.67 (change of 3.33), and X = 18 to X = 17 changes it from 6.67 to 5 (change of 1.67).

If two of the points had a difference that was close to the target (3) in different directions, we would rerun the question with different assumptions (prior of 18 on what the answer is, and consider the second part to be changing as a/93 ish)

The change from 18 to 19 is the closest to these two parts being balanced, so we know that the turning point exists somewhere between these points. This is likely enough for interviews, although comparing these two quantites without calculator/computation by hand is a fun exercise (I believe, not having have done it)

This answer is a bit convoluted so ask me if you have questions. In this case it may not actually be the easiest way to do it, but building up some skills for these games is important.
 
A similar question is Place or Take, another question in this set

---

### 2. Place or Take

#### Question:  
You are playing a one-player game with two opaque boxes. At each turn, you can choose to either "place" or "take". "Place" places &#36;1 from a third party into one box randomly. "Take" empties out one box randomly and that money is yours. This game consists of 100 turns where you must either place or take. Assuming optimal play, what is the expected payoff of this game? Note that you do not know how much money you have taken until the end of the game.

This is ripped straight from quantguide, but is a very good question that feels extremely Jane Street -y

Do this without a calculator, or differentiation

---

#### Answer:

You collect all the money unless you are super unlucky, and grab one box every time, in which you leave behind half your money in expectation.

It should be clear to place money for first (100-n) turns (giving 100-n dollars) and then take for last n turns

As such, can express the expectation as:

$$(100 - n) * (1 - (1/2)^n)$$

The numerator changes by roughly 1% when n changes, so need to consider when the 2nd part changes by 1%.

The 2nd part looks like:

n = 1: 1/2  
n = 2: 3/4  
n = 3: 7/8  
n = 4: 15/16  
n = 5: 31/32  
n = 6: 63/64  
n = 7: 127/128  

From 6 to 7 it changes by 1/128 which is close to 1/100.

Therefore, the optimum EV is at n = 6 or 7; taking 93 or 94 turns to start taking.

This is sufficient as an answer.