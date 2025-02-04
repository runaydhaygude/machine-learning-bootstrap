# Import required libraries
import matplotlib.pyplot as plt
import numpy as np

# 1. create an virtual environment: python3 -m venv venv
# 2. activate the virtual environment: source venv/bin/activate
# 3. install the required packages: 
# 4. pip install matplotlib numpy 
# 5. run the script: python movie.py



# Function to predict the label of a movie
def predict_label(movie_x, movie_y, w0, w1, w2):
    val = movie_y * w2 + movie_x * w1 + w0
    return 1 if val > 0 else 0

# Function to calculate the decision boundary line
def calc_line_y(x, w1, w2, w0):
    return -(w1 * x + w0) / w2

# Function to update weights based on the error
def update_weights(w0, w1, w2, actual_label, predicted_label, movie_x, movie_y):
    error = actual_label - predicted_label
    return (
        w0 + error * 1,  # Bias term
        w1 + error * movie_x,
        w2 + error * movie_y
    )

# Function to plot the decision boundary and movie points
def plot_decision_boundary(line_x, line_y, points_good, points_bad, current_point, plot_counter):
    plt.figure(figsize=(6, 6))
    plt.xlim([0, 10])
    plt.ylim([0, 10])
    plt.plot(line_x, line_y, color='gray')
    
    # Scatter the good and bad movie points, separating x and y values
    if points_good:  # Ensure there's at least one good movie to plot
        good_x, good_y = zip(*points_good)
        plt.scatter(good_x, good_y, label='Good movies', marker='x')
    
    if points_bad:  # Ensure there's at least one bad movie to plot
        bad_x, bad_y = zip(*points_bad)
        plt.scatter(bad_x, bad_y, label='Bad movies', marker='o')
    
    # Highlight the current movie point being evaluated
    plt.gca().add_artist(plt.Circle(current_point, 0.3, color='gray', fill=False))
    
    plt.tight_layout()
    plt.savefig(f'plot{plot_counter}.png')
    plt.close()

# Main training loop
def train_perceptron(movies_data, w0, w1, w2, epochs=10):
    points_good, points_bad = [], []  # To store points for good and bad movies
    plot_counter = 0
    
    for epoch in range(epochs):
        for movie in movies_data:
            movie_x, movie_y, actual_label = movie
            current_point = [movie_x, movie_y]
            
            # Store good or bad movie coordinates
            (points_good if actual_label == 1 else points_bad).append(current_point)
            
            # Predict label and update weights
            predicted_label = predict_label(movie_x, movie_y, w0, w1, w2)
            w0, w1, w2 = update_weights(w0, w1, w2, actual_label, predicted_label, movie_x, movie_y)
            
            # Calculate decision boundary line
            line_x = np.arange(0, 10, 0.1)
            line_y = calc_line_y(line_x, w1, w2, w0)
            
            # Plot and save the current decision boundary
            plot_decision_boundary(line_x, line_y, points_good, points_bad, current_point, plot_counter)
            plot_counter += 1

    return plot_counter


# Read data from csv file
movies_data = np.loadtxt('movie-data.csv', delimiter=',')[:12]  # Extracting first 12 data points

# Weights
w0, w1, w2 = -10, 2, 1

# Run the training process and generate GIF
plot_counter = train_perceptron(movies_data, w0, w1, w2)