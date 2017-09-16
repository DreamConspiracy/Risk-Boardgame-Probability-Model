# Risk-Boardgame-Probability-Model

This is a barebones implementation of Nestor1's algorithm for calculating probabilities in Risk. While his implementation is intended to be used as a standalone application, this implementation is intended to be used as a module to support another application.

### Risk

Risk is very unique in it's usage of randomness to simulate battle. In any given battle, some number of attacking units fights against some number of defending units. The attacking player receives as many dice as he has attacking units, but at most three and the defending player receives as many dice as he has defending units, but at most two. All dice are then rolled. The dice are then organized into 'couplings': The highest dice on each side are combined into a coupling, and then the next highest dice on each side are also combined into a coupling, if both sides have at least two dice. Then for each coupling an attacking unit is 'killed' or removed from the playing field if the defending die is at least as high as the attacking die, and a defending unit is killed if the attacking die is higher than the defending die. If either side is now out of units, that side loses. Otherwise, the attacker can choose to go through another round of combat, or stop.

If the attacker wins, he can then attack a new set of defending units with the remaining attacking units; However, he must leave one attacking unit behind. Chaining attacks like this will be referred to as a campaign per Nestor15's terminology.

### Implementation Notes

This implementation assumes the attacking player does not stop attacking. It can then calculate the probability of success in any single attack or in any campaign, and the probabilites of winning any of the above with at least a certain number of surviving attacking troops, similar to Nestor15's implementation. See the risk.py file for more details.
