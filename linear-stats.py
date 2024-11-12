import sys
import numpy as np

def main(data_file):
    try:
        y_data = np.loadtxt(data_file)
        x_data = np.arange(len(y_data))
        
        a, b = np.polyfit(x_data, y_data, 1)
        
        r = np.corrcoef(x_data, y_data)[0,1]

        print(f"Linear Regression Line: y = {a:.6f}x + {b:.6f}")
        print(f"Pearson Correlation Coefficient: {r:.10f}")
        
    except FileNotFoundError:
        print(f"Error: {data_file} not found.")
    except ValueError:
        print("Error: data must be numeric.")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 program.py data.txt")
    else:
        main(sys.argv[1])