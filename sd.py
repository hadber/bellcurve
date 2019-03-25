import matplotlib.pyplot as plt
import random

TOTAL_TRIES = 50000
CONSECUTIVE_START = 1
MAX_CONS = 20


def sd(TOTAL_TRIES, CONSECUTIVE_START, MAX_CONS) -> list:

	# head is >= 0.5
	consHead = 0
	consTail = 0
	total = 0
	cons_outcome = []

	for CONSECUTIVE_SAME in range(CONSECUTIVE_START, MAX_CONS):
		for _ in range(0, TOTAL_TRIES):
			outcome = random.uniform(0, 1)
			if(outcome >= 0.5):
				consHead += 1
				consTail = 0
				if(consHead == CONSECUTIVE_SAME):
					total += 1	
			else:
				consTail += 1
				consHead = 0
				if(consTail == CONSECUTIVE_SAME):
					total += 1
		cons_outcome.append((total/TOTAL_TRIES) * 100)
		total = 0
	
	return cons_outcome

def plot_sd(CONSECUTIVE_START, MAX_CONS, cons_outcome):		
	plt.bar([str(i) for i in range(CONSECUTIVE_START, MAX_CONS)], cons_outcome)
	plt.show()
	
probs = sd(TOTAL_TRIES, CONSECUTIVE_START, MAX_CONS)
plot_sd(CONSECUTIVE_START, MAX_CONS, probs)
