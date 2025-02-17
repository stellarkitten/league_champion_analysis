import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px

df = pd.read_csv("data/data.csv")

# TODO: To what do the style integers correspond?
style = df["Style"]

labels, counts = np.unique(style, return_counts=True)

plt.pie(counts, labels=labels, autopct="%1.1f%%")

plt.title("Style Frequency")

plt.tight_layout()
plt.show()

labels = ["Difficulty", "Damage", "Durability", "Crowd Control", "Mobility", "Utility"]
mean_playstyle = [np.mean(df[i]) for i in labels]

playstyle = pd.DataFrame(dict(r=mean_playstyle, theta=labels))

fig = px.line_polar(playstyle, r="r", theta="theta", line_close=True, range_r=[0, 3], title="Mean Playstyle")

fig.show()

damage_type = df["Damage Type"]

labels, counts = np.unique(damage_type, return_counts=True)

plt.pie(counts, labels=labels, autopct="%1.1f%%")

plt.title("Damage Type Frequency")

plt.tight_layout()
plt.show()

primary_role = df["Primary Role"]
secondary_role = df["Secondary Role"]
secondary_role = [i for i in secondary_role if str(i) != "nan"]

roles = list(primary_role)+secondary_role

labels, counts = np.unique(roles, return_counts=True)

plt.pie(counts, labels=labels, autopct="%1.1f%%")

plt.title("Role Frequency")

plt.tight_layout()
plt.show()

skins = df["Skins"]

plt.hist(skins, bins=range(min(skins), max(skins)+1, 1), align="left")

plt.xlabel("Skins")
plt.ylabel("Counts")
plt.title("Skin Distribution")

plt.tight_layout()
plt.show()
