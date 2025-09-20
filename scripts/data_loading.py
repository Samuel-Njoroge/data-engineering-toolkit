import pandas as pd

# Load data
def load_data(file_path):
    file_path = "/downloads/files/"
    data = pd.read_csv(file_path)