import sweetviz as sv
import pandas as pd

train = pd.read_csv('../dataset/star_classification_train.csv')
test = pd.read_csv('../dataset/star_classification_test.csv')

compare_report = sv.compare([train, 'Train'], [test, 'Test'])
compare_report.show_html('../notebooks/01_auto_EDA/compare_train_test.html', open_browser=False)
