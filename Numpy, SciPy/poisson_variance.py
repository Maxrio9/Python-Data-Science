'''
1. You work at ambulance dispatch where the number of calls that come in daily follows the Poisson distribution with lambda equal to 9. There’s a rule that a team can go on no more than 12 calls a day. But how often could this happen?

Create a variable calls that is the probability of observing more than 12 calls on a given day. Then print calls.

2. Let’s say that you have to call in a backup team if you have 10 or more calls in a given day. But you don’t want to have to call in a backup team unless they really will be needed. But what is the probability that they will be called and not needed?

Create and print a variable false_backup that is the probability of observing a minimum of 10 calls, but no more than 12. Then print false_backup.

3. A certain tennis star has a first-serve rate of 62%. Let’s say they serve 80 times in a given match. What is the expected value of the number of serves they make?

Create and print a variable expected_serves that is the number of first-serves they are expected to make.

4. At the same first-serve rate, what is the variance of this player’s first-serves?

Create and print a variable variance_serves that is the variance of the player making their first serve.
'''


import scipy.stats as stats

## Practice Question 1
calls = 1 - stats.poisson.cdf(12, 9)
print(calls)

## Practice Question 2
false_backup = stats.poisson.cdf(12, 9) - stats.poisson.cdf(9, 9)
print(false_backup)

## Practice Question 3
expected_serves = 0.62 * 80
print(expected_serves)

## Practice Question 4
variance_serves = 0.62 * 80 * 0.38
print(variance_serves)