def calculate_average(data, column):
    average = data[column].mean()
    return average

def calculate_summary(data):
    summary = data[["mood", "sleep", "stress"]].describe()
    return summary

def calculate_correlations(data):
    correlations = data[["mood", "sleep", "stress"]].corr()
    return correlations 