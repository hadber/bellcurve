import matplotlib.pyplot as plt
import random

TOTAL_TRIES = 50000
CONSECUTIVE_START = 1
MAX_CONS = 20


def sd(tota, cons_start, max_cons) -> list:

	# head is >= 0.5
	consHead = 0
	consTail = 0
	total = 0
	cons_outcome = []

	for cons_same in range(cons_start, max_cons):
		for _ in range(0, tota):
			outcome = random.uniform(0, 1)
			if(outcome >= 0.5):
				consHead += 1
				consTail = 0
				if(consHead == cons_same):
					total += 1	
			else:
				consTail += 1
				consHead = 0
				if(consTail == cons_same):
					total += 1
		cons_outcome.append((total/tota) * 100)
		total = 0
	
	return cons_outcome

def plot_sd(cons_start, max_cons, cons_outcome):		
	plt.bar([str(i) for i in range(cons_start, max_cons)], cons_outcome)
	plt.show()
	
probs = sd(TOTAL_TRIES, CONSECUTIVE_START, MAX_CONS)
plot_sd(CONSECUTIVE_START, MAX_CONS, probs)
