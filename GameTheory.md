## Game Theory 

### 1. Don't say 50. 

#### Question:

You and your opponent go in turns saying numbers 1:10 inclusive, and keeping a running total of the sum. If you say 50, you win. You go first, what number do you say?

#### Solution:

You say 6. Given any number said by your opponent, you can make the number said by you and your opponent equal to 11 by saying 11-x for your opponent. As such, you can say 6 first then just say the number taking you to a number of the form 6 + 11n

---

### 2. Pirates:

#### Question:

Five pirates looted a chest full of 100 gold coins. Being a bunch of democratic pirates,
they agree on the following method to divide the loot:

The most senior pirate will propose a distribution of the coins. All pirates, including the
most senior pirate, will then vote. If at least 50% of the pirates (3 pirates in this case)
accept the proposal, the gold is divided as proposed. If not, the most senior pirate will be
fed to shark and the process starts over with the next most senior pirate ... The process is
repeated until a plan is approved. You can assume that all pirates are perfectly rational:
they want to stay alive first and to get as much gold as possible second. Finally, being
blood-thirsty pirates, they want to have fewer pirates on the boat if given a choice
between otherwise equal outcomes.

How will the gold coins be divided in the end?

#### Solution:

Here we use the concept of problem simplification.

Consider two pirates. The most senior pirate proposes 100, 0 and votes for it, and the vote splits

As such, in the three pirate case, the senior pirate only has to give the least senior pirate \$1 for them to agree giving him a 2/3 majority. As such, the proposal of 99, 0, 1 is accepted. 

In the four pirate case, the 2nd least senior pirate only needs 1 gold coin to upvote, so the distribution of 99, 0, 1, 0 passes. 

In the five pirate case, the 3rd least senior and the least senior pirate need only \$1 to accept, so the distribution 99, 0, 1, 0, 1 passes. 

---

### 3. Tigers and Sheep:

#### Question:

One hundred tigers and one sheep are put on a magic island that only has grass. Tigers
can eat grass, but they would rather eat sheep. Assume: A. Each time only one tiger can
eat one sheep, and that tiger itself will become a sheep after it eats the sheep. B. All
tigers are smart and perfectly rational and they want to survive. So will the sheep be
eaten?

#### Solution:

A similar argument to that used in the prior question can be used

If there are two tigers, the sheep doesn't get eaten as the tiger doing the eaten would get chomped by the remaining tiger. 
As such, with three tigers the sheep can be eaten because then we reduce to the 2 tiger case with the safe sheep.

It is clear that this argument follow parity and with 100 tigers the sheep cannot be eaten.