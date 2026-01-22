# Stochastic Optimization for Warehouse Location Planning

This project addresses a warehouse location planning problem under uncertain customer demand using stochastic optimization.

As no real dataset was provided, demand scenarios (Low, Medium, High) were created with assigned probabilities to represent uncertainty. The objective of the model is to minimize the expected total cost, which includes fixed warehouse opening costs and transportation costs.

The optimization model was implemented using Python and PuLP. Sensitivity analysis was performed by varying demand levels to understand how changes in demand impact the overall cost.

## Technologies Used
- Python
- PuLP
- pandas
- matplotlib

## How to Run
1. Install the required libraries:
pip install pandas pulp matplotlib

2. Run the Python script:
python warehouse_stochastic_optimization.py

## Results
The model identifies optimal warehouse locations and shows that expected cost increases logically with demand, indicating a stable and robust solution.
