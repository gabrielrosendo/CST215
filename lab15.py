import random

# Initialize a dictionary to count the number of times each number of fixed points was obtained
counts = {i: 0 for i in range(11)}  # The maximum number of fixed points is 10

# Set the size of the deck
n = 45

# Run the simulation 1000 times
for i in range(1000):
    # Initialize the decks
    d1 = [i + 1 for i in range(n)]
    d1copy = [i + 1 for i in range(n)]
    B = []
    C = []

    # Draw cards from the decks
    for i in range(n):
        rand1 = random.choice(d1)
        B.append(rand1)
        d1.remove(rand1)
        rand2 = random.choice(d1copy)
        C.append(rand2)
        d1copy.remove(rand2)

    # Count the number of fixed points
    count = 0
    for k in range(n):
        if B[k] == C[k]:
            count += 1

    # Increment the count for the number of fixed points obtained in this iteration
    counts[count] += 1

# Divide the counts by 1000 to get the percentage of times each number of fixed points was obtained
print("Fixed Points\tPercentage")
for i in range(11):
    counts[i] /= 1000
    print(f"{i}\t        {counts[i]:.3f}")