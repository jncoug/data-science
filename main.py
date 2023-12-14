# Use 2023 college basketball data and learn cool information.


import pandas as pd
import matplotlib.pyplot as plt
import altair as alt

# Read the csv data
df = pd.read_csv("cbb23.csv")

# Group by conferences, check who has best shooting percentages
conference_stats = df.groupby("CONF")[["2P_O", "3P_O"]].mean().reset_index()

# Sort conferences by average 2P_O and select the top 15
top_15_2P_O = conference_stats.sort_values(by="2P_O", ascending=False).head(15)

# Sort conferences by average 3P_O and select the top 15
top_15_3P_O = conference_stats.sort_values(by="3P_O", ascending=False).head(15)

# Plotting with Matplotlib
fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(12, 6))

# Bar plot for top 15 2P_O
axes[0].bar(top_15_2P_O["CONF"], top_15_2P_O["2P_O"], color="blue")
axes[0].set_title("Top 15 Conferences - Average 2%")
axes[0].set_xlabel("Conference")
axes[0].set_ylabel("Average 2P%_O")

# Bar plot for top 15 3P_O
axes[1].bar(top_15_3P_O["CONF"], top_15_3P_O["3P_O"], color="green")
axes[1].set_title("Top 15 Conferences - 3P%")
axes[1].set_xlabel("Conference")
axes[1].set_ylabel("Average 3P%")

# Adjust layout for better readability
plt.tight_layout()
plt.show()

conference_barthag = df.groupby("CONF")["BARTHAG"].mean().reset_index()

# Sort conferences by average BARTHAG and select the top 10
top_10_conferences = conference_barthag.sort_values(by="BARTHAG", ascending=False).head(
    10
)

# Plotting with Matplotlib
plt.figure(figsize=(10, 6))

# Bar plot for top 10 conferences by BARTHAG
plt.bar(top_10_conferences["CONF"], top_10_conferences["BARTHAG"], color="purple")
plt.title("Top 10 Conferences - Average BARTHAG")
plt.xlabel("Conference")
plt.ylabel("Average BARTHAG")

# Rotate x-axis labels for better readability
plt.xticks(rotation=45, ha="right")

# Show the plot
plt.tight_layout()
plt.show()

pac_12_teams = df[df["CONF"] == "P12"]

# Order teams by most wins to least wins
pac_12_teams = pac_12_teams.sort_values(by="W", ascending=False)

# Plotting with Matplotlib
plt.figure(figsize=(12, 6))

# Scatter plot for ORB and DRB
plt.scatter(
    pac_12_teams["ORB"],
    pac_12_teams["DRB"],
    s=pac_12_teams["W"] * 10,
    c="orange",
    alpha=0.7,
)

# Annotate each point with the team name
for i, team in pac_12_teams.iterrows():
    plt.annotate(
        team["TEAM"],
        (team["ORB"], team["DRB"]),
        textcoords="offset points",
        xytext=(0, 5),
        ha="center",
    )

plt.title("Pac-12 Teams: ORB vs DRB (Size represents Wins)")
plt.xlabel("Offensive Rebound Percentage (ORB)")
plt.ylabel("Defensive Rebound Percentage (DRB)")

plt.grid(True)
plt.show()
