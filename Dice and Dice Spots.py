# Define die a and die b
die_a = [1, 2, 3, 4, 5, 6]
die_b = [1, 2, 3, 4, 5, 6]

print()

# Total combinations possible
total_combinations = len(die_a) * len(die_b)
print("Total combinations possible:", total_combinations)
print()

# Distribution of possible combinations
combinations = [[0] * 6 for _ in range(6)]

for i in range(6):
    for j in range(6):
        combinations[i][j] = die_a[i] + die_b[j]

print("Distribution of possible combinations:")
for row in combinations:
    print(row)
print()

# Probability of each sum
probability = {}
for i in range(2, 13):
    count = sum(row.count(i) for row in combinations)
    probability[i] = count / total_combinations

print("\nProbability of each sum:")
for key, value in probability.items():
    print(f"P(sum={key}) = {value:.2f}")
print()


def calculate_probabilities(die_a, die_b):
    probabilities = {}
    for i in range(2, 13):
        count = sum(row.count(i) for row in combinations)
        probabilities[i] = count / total_combinations
    return probabilities

def calculate_expected_occurrences(probabilities, total_combinations):
    expected_occurrences = {}
    for sum_value, prob in probabilities.items():
        expected_occurrences[sum_value] = prob * total_combinations
    return expected_occurrences

def undoom_dice(die_a, die_b):
    original_probabilities = calculate_probabilities(die_a, die_b)
    total_combinations = len(die_a) * len(die_b)
    expected_occurrences = calculate_expected_occurrences(original_probabilities, total_combinations)
    
    new_die_a = [0] * len(die_a)
    new_die_b = die_b[:]
    
    # Calculate the total number of spots needed for Die_A
    total_spots_a = sum(expected_occurrences.values())
    
    for i, face_a in enumerate(die_a):
        for face_b in die_b:
            sum_value = face_a + face_b
            new_die_a[i] += expected_occurrences[sum_value] / total_spots_a * 6
    
    # Adjust Die_A to ensure no face has more than 4 spots
    new_die_a = [min(4, round(spots)) for spots in new_die_a]
    
    return new_die_a, new_die_b

# Test the function with the given input
Die_A = [1, 2, 3, 4, 5, 6]
Die_B = [1, 2, 3, 4, 5, 6]

New_Die_A, New_Die_B = undoom_dice(Die_A, Die_B)
print("New Die A:", New_Die_A)
print("New Die B:", New_Die_B)
