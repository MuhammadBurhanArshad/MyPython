w1 = 0.9
w2 = 0.9

learning_rate = 0.5
threshold = 0.5

def activation_function(sum_unit) :
    if sum_unit > threshold:
        return 1
    else:
        return 0

def predict(x1, x2, current_w1, current_w2) :
    sum_unit = (x1 * current_w1) + (x2 * current_w2)
    return activation_function(sum_unit)

def train_preceptron(training_data, epochs) :
    global w1, w2

    for round_num in range(epochs) :
        print(f"\n--- Round {round_num + 1} --- ")
        for data in training_data:
            x1 = data[0]
            x2 = data[1]
            actual = data[2]

            prediction = predict(x1, x2, w1, w2)

            error = actual - prediction

            if error != 0:
                w1 = w1 + (learning_rate * error * x1)
                w2 = w2 + (learning_rate * error * x2)
                print(f"Inputs ({x1}, {x2}) -> Error! Updated Weights: w1={w1:.2f}, w2={w2:.2f} ")
            else:
                print(f"Inputs ({x1}, {x2}) -> Correct no updated needed.")
                
and_gate_data = [
    [0, 0, 0],
    [0, 1, 0],
    [1, 0, 0],
    [1, 1, 1],
]
        
train_preceptron(and_gate_data, epochs=6)