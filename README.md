# Stochastic Optimization for Warehouse Location Planning

This project focuses on solving a warehouse location planning problem where customer demand is uncertain. The goal is to decide which warehouses should be opened so that the overall expected cost is minimized while still meeting customer demand.

In real-world supply chain systems, demand often fluctuates and cannot be predicted with complete accuracy. To capture this uncertainty, multiple demand scenarios (Low, Medium, High) were considered, each with an assigned probability.

---

## Problem Overview
The objective of this project is to:
- Select optimal warehouse locations
- Satisfy customer demand under different demand scenarios
- Minimize expected total cost, including:
  - Fixed warehouse opening costs
  - Transportation costs

The same warehouse opening decisions are maintained across all scenarios to ensure a robust and practical solution.

---

## Approach
- Demand uncertainty was modeled using scenario-based stochastic optimization.
- An expected cost minimization model was formulated using Python and PuLP.
- Binary decision variables were used to represent warehouse opening decisions.
- Continuous variables were used for shipment quantities.
- Sensitivity analysis was performed by scaling demand levels to evaluate solution stability.

---

## Technologies Used
- Python
- PuLP (Optimization Solver)
- pandas (Data Handling)
- matplotlib (Visualization)

---

## How to Run
1. Install the required libraries:
pip install pandas pulp matplotlib

2. Run the Python script:
python warehouse_stochastic_optimization.py


---

## Results and Insights
- The optimization model successfully identified the most cost-effective warehouse locations.
- The solution remained stable under moderate demand variations.
- Sensitivity analysis showed that expected cost increases logically as demand increases, indicating a robust decision-making framework.

---

## Key Takeaway
This project demonstrates how stochastic optimization can be applied to real-world logistics and supply chain problems to support better decision-making under uncertainty.
