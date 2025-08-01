import pandas as pd
from sklearn.ensemble import RandomForestRegressor

# ✅ Load CSV (tab-separated)
df = pd.read_csv("air_quality.csv", sep="\t")

# ✅ Select useful columns (drop missing)
df = df[['PM2.5', 'PM10', 'NO2', 'SO2', 'CO', 'O3', 'AQI']].dropna()

# ✅ Features & Target
features = ['PM2.5', 'PM10', 'NO2', 'SO2', 'CO', 'O3']
target = 'AQI'

X = df[features]
y = df[target]

# ✅ Train Model
model = RandomForestRegressor()
model.fit(X, y)

# ✅ Prediction Function
def predict_aqi(pm25, pm10, no2, so2, co, o3):
    pred = model.predict([[pm25, pm10, no2, so2, co, o3]])[0]
    return round(pred, 2)
