# Warehouse Location Planning under Demand Uncertainty
# Using stochastic optimization with PuLP

import pandas as pd
import matplotlib.pyplot as plt
from pulp import LpProblem, LpMinimize, LpVariable, lpSum, LpStatus, value


# ---------------------------------------------------
# Creating sample demand scenarios
# (No dataset was provided, so scenarios are assumed)
# ---------------------------------------------------
data = {
    "customer": ["C1","C1","C1",
                 "C2","C2","C2",
                 "C3","C3","C3",
                 "C4","C4","C4"],
    "scenario": ["Low","Medium","High"] * 4,
    "demand": [80,120,155,
               60,100,140,
               75,110,150,
               50,90,130]
}

df = pd.DataFrame(data)


# ---------------------------------------------------
# Sets and basic parameters
# ---------------------------------------------------
warehouses = ["W1", "W2", "W3"]
customers = df["customer"].unique()
scenarios = df["scenario"].unique()

scenario_prob = {
    "Low": 0.3,
    "Medium": 0.5,
    "High": 0.2
}

fixed_cost = {
    "W1": 5200,
    "W2": 6100,
    "W3": 5600
}

transport_cost = {
    ("W1","C1"):4, ("W1","C2"):6, ("W1","C3"):8, ("W1","C4"):5,
    ("W2","C1"):5, ("W2","C2"):4, ("W2","C3"):7, ("W2","C4"):6,
    ("W3","C1"):6, ("W3","C2"):5, ("W3","C3"):4, ("W3","C4"):6
}

demand = {(r.customer, r.scenario): r.demand for _, r in df.iterrows()}


# ---------------------------------------------------
# Building the optimization model
# ---------------------------------------------------
print("Running warehouse location model...")

model = LpProblem("Warehouse_Location_Stochastic", LpMinimize)

open_warehouse = LpVariable.dicts("OpenWH", warehouses, cat="Binary")
shipment = LpVariable.dicts(
    "Shipment",
    (warehouses, customers, scenarios),
    lowBound=0
)

model += (
    lpSum(fixed_cost[w] * open_warehouse[w] for w in warehouses) +
    lpSum(
        scenario_prob[s] * transport_cost[(w, c)] * shipment[w][c][s]
        for w in warehouses
        for c in customers
        for s in scenarios
    )
)

for c in customers:
    for s in scenarios:
        model += lpSum(shipment[w][c][s] for w in warehouses) == demand[(c, s)]

M = 10000
for w in warehouses:
    for c in customers:
        for s in scenarios:
            model += shipment[w][c][s] <= M * open_warehouse[w]


# ---------------------------------------------------
# Solving the model
# ---------------------------------------------------
model.solve()

print("\nSolver Status:", LpStatus[model.status])

print("\nWarehouses Selected:")
for w in warehouses:
    if open_warehouse[w].value() == 1:
        print(" ", w)

print("\nExpected Total Cost:", round(value(model.objective), 2))


# ---------------------------------------------------
# Sensitivity check by scaling demand
# ---------------------------------------------------
demand_scale = [0.8, 1.0, 1.2]
total_costs = []

for scale in demand_scale:
    test_model = LpProblem("Demand_Sensitivity", LpMinimize)

    y = LpVariable.dicts("Y", warehouses, cat="Binary")
    x = LpVariable.dicts(
        "X",
        (warehouses, customers, scenarios),
        lowBound=0
    )

    test_model += (
        lpSum(fixed_cost[w] * y[w] for w in warehouses) +
        lpSum(
            scenario_prob[s] * transport_cost[(w, c)] * x[w][c][s]
            for w in warehouses
            for c in customers
            for s in scenarios
        )
    )

    for c in customers:
        for s in scenarios:
            test_model += (
                lpSum(x[w][c][s] for w in warehouses)
                == demand[(c, s)] * scale
            )

    for w in warehouses:
        for c in customers:
            for s in scenarios:
                test_model += x[w][c][s] <= M * y[w]

    test_model.solve()
    total_costs.append(value(test_model.objective))


# ---------------------------------------------------
# Plotting sensitivity results
# ---------------------------------------------------
plt.figure()
plt.plot(demand_scale, total_costs, marker="o")
plt.xlabel("Demand Scaling Factor")
plt.ylabel("Expected Cost")
plt.title("Impact of Demand Change on Total Cost")
plt.grid(True)
plt.show()
