import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pylab import figure, axes, pie, title
import math

class MySeries:
    '''
    Time series prediction.  User need only input time series csv
    (note: this should consist of a single row/column without header)
    '''

    def __init__(self):
        # variables for training / predictions
        self.w = 0
        self.y = 0
        self.y_predictions = []

    # load data
    def load_data(self, csvname):
        self.y = np.asarray(pd.read_csv(csvname, header=None))

    # trains linear time series model - outputing weights
    def train_model(self):
        # determine training period - preset
        P = min(24, int(math.floor(len(self.y) / float(4))))

        # initialize A and b
        A = 0
        b = 0

        # loop over vectors to build A and b
        for n in range(0, len(self.y) - P):
            x_n = np.fliplr(self.y[n:n + P])
            y_n = self.y[n + P]
            A += np.outer(x_n, x_n)
            b += x_n * y_n

        # solve linear system Ax = b for properly tuned weights w using pinv (for stability)
        self.w = np.dot(np.linalg.pinv(A), b)

    # make predictions - after training - returns predictions
    def make_predictions(self):
        P = len(self.w)  # prediction period

        # loop over most recent part of series to make prediction
        y_input = list(self.y[-P:])
        for p in range(P):
            # compute and store prediction
            pred = list(sum([s * t for s, t in zip(y_input, self.w)]))
            self.y_predictions.append(pred[0])

            # kick out last entry in y_input and insert most recent prediction at front
            del y_input[-1]
            y_input = pred + y_input

    # plot input series as well as prediction
    def plot_all(self):
        # plt.savefig('foo.png')

        f = figure(figsize=(6, 6))
        # grab the last chunk of the series for plotting (for visualization purposes)
        mult = 4
        while mult * len(self.y_predictions) > len(self.y):
            mult -= 1
        pts_to_plot = mult * len(self.y_predictions)
        y_plot = self.y[-pts_to_plot:]

        # plot the last chunk of the series
        plt.plot(np.arange(len(y_plot)), y_plot, color='b', linewidth=3)

        # plot fit
        plt.plot(len(y_plot) + np.arange(len(self.y_predictions)), self.y_predictions, color='r', linewidth=3)
        plt.plot([len(y_plot) - 1, len(y_plot)], [y_plot[-1], self.y_predictions[0]], color='r', linewidth=3)
        plt.xlabel('time period', fontsize=13)
        plt.ylabel('value', fontsize=13)
        plt.title('simple time series prediction (in red)', fontsize=15)

        plt.close(f)
        return f


