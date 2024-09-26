# Definisikan neuron dengan bobot dan threshold (fungsi McCulloch-Pitts)
def neuron(inputs, weights, threshold):
    # Hitung weighted sum
    weighted_sum = sum(i * w for i, w in zip(inputs, weights))
    # Jika weighted sum >= threshold, neuron aktif (output 1)
    return 1 if weighted_sum >= threshold else 0

# Definisikan fungsi logika dasar
def AND_gate(x1, x2):
    # Bobot untuk AND gate adalah 1, threshold adalah 2
    return neuron([x1, x2], [1, 1], 2)

def OR_gate(x1, x2):
    # Bobot untuk OR gate adalah 1, threshold adalah 1
    return neuron([x1, x2], [1, 1], 1)

def NOT_gate(x):
    # Bobot untuk NOT gate adalah -1, threshold adalah 0
    return neuron([x], [-1], 0)

# Gabungkan gerbang AND, OR, dan NOT untuk membentuk XOR
def XOR_gate(x1, x2):
    or_result = OR_gate(x1, x2)  # Output dari OR gate
    and_result = AND_gate(x1, x2)  # Output dari AND gate
    not_and_result = NOT_gate(and_result)  # Output dari NOT gate (membalik AND)
    # XOR adalah hasil dari OR dan NOT AND
    return AND_gate(or_result, not_and_result)

# Tabel kebenaran untuk XOR
print("X1 X2 | XOR")
for x1 in [0, 1]:
    for x2 in [0, 1]:
        print(f"{x1}  {x2}  |  {XOR_gate(x1, x2)}")