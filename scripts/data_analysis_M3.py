import matplotlib.pyplot as plt

def m3(collated_answers_path):
    sequences = []
    
    # open, read and close file. named file as "f". 
    with open(collated_answers_path, 'r') as f:
        # read text, clean text(\n) in opening/ closing and sperate answer from 4 answerers(by using *).
        blocks = f.read().strip().split("*\n")  
        for block in blocks:
            # turn text to string
            lines = block.strip().splitlines()
            # turn string to integers
            sequence = [int(x) for x in lines]
            sequences.append(sequence)
    return sequences
    
def generate_means_sequence(sequences):
# if seq[i]!= 0, add seq[i] in values.
    means=[]
    for i in range(100):
        values = [seq[i] for seq in sequences if seq[i] != 0]
        mean = sum(values) / len(values) if values else 0
        means.append(mean)
    return means

def visualize_data(sequences, n):
    # draw the average value of all the answer (exclude 0)
    if n == 1:
        means = generate_means_sequence(sequences)
        plt.scatter(range(1, 101), means)
        plt.title("Mean Answer Value per Question")
        plt.xlabel("Question Number")
        plt.ylabel("Mean Answer (1–4)")
    # draw every one(4 mumber) answer line.
    elif n == 2:
        for seq in sequences:
            plt.plot(range(1, 101), seq, alpha=0.3)
        plt.title("All Respondents’ Answer Sequences")
        plt.xlabel("Question Number")
        plt.ylabel("Answer (1–4 or 0)")
    else:
        print("Error: Invalid plot option. n must be 1 or 2.")
        return
    plt.grid(True)
    plt.show()
  