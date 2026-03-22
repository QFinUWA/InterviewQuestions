## Counting Questions

### 1. John's Dinner Party

#### Question:

John has 8 friends. He will invite 5 to his party. However, two of his friends have beef and they refuse to attend together. How many possible combinations of guests are possible given this constraint?

#### Solution:

Just sum up the combos from the different cases. If neither of the beefy friends attend, then have $\binom{6}{5} = 6$ combinations. Then have $\binom{6}{4} = 15$ for each of the combinations involving a single one of the two friends. As such, the final answer is $6 + 2(15) = 36$

---

### 2. Moving in a Grid

#### Question:

You are playing a 2D game where your character is trapped in a 6×6 grid. Your character starts at (0,0) and can only move up and right. There are two power-ups located at (2,3) and (4,6). How many possible paths can your character take to get to (6,6) such that it can collect at least one power-up?

#### Solution:

Firstly, we know that given an n by m grid there are $\binom{n+m}{m} = \binom{n+m}{n}$ ways to traverse it only going up/right - need to just select where the ups/rights are.

Gives this, there are $\binom{5}{2} = 10$ ways to get to (2, 3), and another 10 ways to get from (2, 3) to (4, 6). From (4, 6) there is only 1 way to get to (6, 6). As such, there are 100 paths that go via both points.

Additionally, there are $\binom{7}{3} = 35$ paths that go through (2, 3) to end up at (6, 6), As such, there are $35(10) = 350$ paths that pass through (2, 3)

There are $\binom{10}{4} = 210$ paths that go through (4, 6)

Via inclusion-exclusion, there are therefore 210 + 350 - 100 = 460 paths that go through either of the target points.

---