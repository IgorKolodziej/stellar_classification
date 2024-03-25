import sweetviz as sv
import pandas as pd

# Load the data
train = pd.read_csv('../dataset/star_classification_train.csv')
test = pd.read_csv('../dataset/star_classification_test.csv')

# Compare the two datasets
compare_report = sv.compare([train, 'Train'], [test, 'Test'])
compare_report.show_html('compare_train_test.html', open_browser=False)
