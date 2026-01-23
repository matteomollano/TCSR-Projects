import pandas as pd
import matplotlib.pyplot as plt

# dataset: https://www.kaggle.com/datasets/adityadesai13/used-car-dataset-ford-and-mercedes?select=audi.csv
df = pd.read_csv("audi.csv")
# print(df.head())
# print(df.info())

# df['price'] = df['price'].astype('int64')

# print(df['fuelType'].value_counts())
# print(df['fuelType'].unique())

# print(df.describe())

# barplot for model type
model_counts = df['model'].value_counts().reset_index()
model_counts.columns = ['model', 'count']
# print(model_counts)

# x = model_counts['model']
# y = model_counts['count']

# plt.bar(x, y)
# plt.xlabel("Model")
# plt.ylabel("Count")
# plt.title("Number of cars per Model")
# plt.show()

top_10_models = model_counts.head(10)
# x = top_10_models['model']
# y = top_10_models['count']
# plt.bar(x, y)
# plt.xlabel("Model")
# plt.ylabel("Count")
# plt.title("Top 10 Models")
# plt.show()

import plotly.express as px
fig = px.bar(model_counts, x='model', y='count', title="Model Type Distribution")
# fig.show()

fuel_type_counts = df['fuelType'].value_counts().reset_index()
fuel_type_counts.columns = ["fuelType", "count"]
fig = px.bar(fuel_type_counts, x="fuelType", y="count", title="Fuel Type Distribution")
# fig.show()

tranmission_counts = df['transmission'].value_counts().reset_index()
tranmission_counts.columns = ["transmission", "count"]
fig = px.bar(tranmission_counts, x="transmission", y="count", title="Transmission Type Distribution")
# fig.show()

# corrrelation matrix using plotly including only numerical columns
numerical_df = df.select_dtypes(include=['int64', 'float64'])
corr_matrix = numerical_df.corr()
fig = px.imshow(corr_matrix, text_auto=True, color_continuous_scale='RdBu', title="Correlation Matrix")
# fig.show()