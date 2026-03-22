## Miscellaneous Questions

### 1. Dice Simulation Problem

#### Question:

You have a dice. Simulate the probability of picking a Picture card from a 52-card deck:
$$
P(\text{Picture}) = \frac{3}{13}
$$
while **minimising the expected number of dice rolls**.



#### Solution:

We construct increasingly efficient schemes.



#### Level 1

Roll two dice → 36 equally likely outcomes.

- Assign:
  - 6 outcomes → **True**
  - 20 outcomes → **False**
  - 10 outcomes → **reroll**

Example mapping:
- $(1, x)$ → True  
- $(2, x), (3, x), (4, x), (5,1), (5,2)$ → False  
- Remaining → reroll  

**Expected number of rolls**

Each iteration uses 2 rolls and succeeds with probability $$26/36$$:

$$
\mathbb{E}[\text{rolls}] = 2 \cdot \frac{36}{26}
$$



#### Level 2

Improve efficiency by avoiding unnecessary second rolls.

**Strategy**

1. Roll one die:
   - $1 \to$ True  
   - $2,3,4 \to$ False  
   - $5 \to$ need second roll  
   - $6 \to$ reroll  

2. If first roll = 5:
   - Second roll $\le 2 \to$ False  
   - Second roll $3\text{–}6 \to$ reroll  

**Expected number of rolls**

Per iteration:
$$
\frac{5}{6}(1) + \frac{1}{6}(2) = \frac{7}{6}
$$

Number of iterations:
$$
\frac{36}{26}
$$

Total:
$$
\mathbb{E}[\text{rolls}] = \frac{36}{26} \cdot \frac{7}{6} \approx 1.62
$$



#### Level 3 (Optimal)

Target probability:
$$
\frac{3}{13} \approx 0.231
$$

Each die roll partitions $$[0,1]$$ into 6 equal intervals of size $$1/6$$.

**Step 1**

- If roll $=1$ → True  
- If roll $>2$ → False  
- If roll $=2$ → refine  

**Step 2 (refinement)**

Position within bucket:
$$
\frac{0.23 - 1/6}{1/6} \approx 0.38
$$

So:
- If next roll $<3$ → True  
- If next roll $>3$ → False  
- If roll $=3$ → repeat refinement  

**Expected number of rolls**

Each step stops with probability $$5/6$$:

$$
\mathbb{E}[\text{rolls}] = \frac{6}{5} = 1.2
$$



#### Final Result
<p align="center">

| Method   | Expected Rolls |
|:--------:|:--------------:|
| Level 1  | $$2 \cdot \frac{36}{26} \approx 2.77$$ |
| Level 2  | $$1.62$$ |
| Level 3  | **$$1.2$$ (optimal)** |

</p>


The code for all the methods here can be found in ../Code/PictureCardProbability.py; this may make more sense


### 2. Missing Number Problem

#### Question:

You are given the numbers $1,2,\dots,n$ in random order, but one number is missing.

**(a)** What is the most efficient way to find the missing number?

**(b)** Now suppose **two** numbers are missing. What is the most efficient way to find the two missing numbers?



#### Solution:

We use identities for sums of integers and sums of squares.



#### (a) One missing number

If all numbers were present, their sum would be

$$
\sum_{i=1}^{n} i = \frac{n(n+1)}{2}.
$$

Let the observed list be $l$. Then the missing number is

$$
\frac{n(n+1)}{2} - \sum_{x \in l} x.
$$



#### Example

Take $n=6$, and suppose

$$
l = [5,3,6,4,1].
$$

Then

$$
\sum_{i=1}^{6} i = 21, \quad \sum l = 19.
$$

Hence the missing number is

$$
21 - 19 = 2.
$$



#### (b) Two missing numbers

Let the missing numbers be $a$ and $b$.

We use two equations:

**Sum:**
$$
a + b = \frac{n(n+1)}{2} - \sum_{x \in l} x
$$

**Sum of squares:**
$$
a^2 + b^2 = \frac{n(n+1)(2n+1)}{6} - \sum_{x \in l} x^2
$$

This gives a system of two equations in two unknowns.



#### Example

Take $n=6$, and suppose

$$
l = [2,5,1,3].
$$

Compute totals:

$$
\sum_{i=1}^{6} i = 21, \quad \sum l = 11
$$

$$
\sum_{i=1}^{6} i^2 = 91, \quad \sum_{x \in l} x^2 = 39
$$

So

$$
a + b = 10, \quad a^2 + b^2 = 52.
$$

Substitute $a = 10 - b$:

$$
(10 - b)^2 + b^2 = 52
$$

$$
2b^2 - 20b + 100 = 52
$$

$$
b^2 - 10b + 48 = 0
$$

Solving:

$$
b = 4, 6
$$

Hence the missing numbers are

$$
\boxed{4, 6}.
$$



#### Final Result

- **One missing number:**  
  $$\frac{n(n+1)}{2} - \sum l$$

- **Two missing numbers:**  
  Solve
  $$
  a+b,\quad a^2+b^2
  $$
  via simultaneous equations.


### 3. Chess Tournament:

#### Question:

A chess tournament has 128 players, each with a distinct rating. Assume that the player with the higher rating always wins against a lower rated opponent and that the winner proceeds to the subsequent round. What is the probability that the highest rated and second-highest rated players will meet in the final?

#### Solution:

Consider the initial brackets. At the lowest level there are 128 players. The two players meet in the final if they don't meet earlier; they are on opposite sides of the draw. Place the top player. There are 127 remaining spots, 64 of which are on the opposite side of the draw. So, the answer is 64/127.

