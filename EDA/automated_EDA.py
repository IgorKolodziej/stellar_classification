import pandas as pd
import sweetviz as sv
from ydata_profiling import ProfileReport

df = pd.read_csv('../dataset/star_classification.csv')

# Sweetviz
analyze_report = sv.analyze(df)
analyze_report.show_html('sweetviz_report.html', open_browser=False)

# YData Profiling
profile = ProfileReport(df, title="Pandas Profiling Report")
profile.to_file("ydata_profiling_report.html")
