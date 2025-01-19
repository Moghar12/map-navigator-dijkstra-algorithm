# Hybrid Shortest Path Generation using Dijkstra's Algorithm and Linear Regression

This project combines **Dijkstra’s Algorithm** for shortest path calculations with a **Linear Regression** model (from Machine Learning) to predict or adjust path-related costs. The goal is to discover an optimal or near-optimal route between two cities by accounting for dynamic factors such as traffic, road conditions, or time-of-day effects.

---

## Table of Contents

1. [Overview](#overview)  
2. [Features](#features)  
3. [Project Structure](#project-structure)  
4. [Prerequisites](#prerequisites)  
5. [Installation](#installation)  
6. [Usage](#usage)  
7. [Contributing](#contributing)  
8. [License](#license)  

---

## Overview

- **Dijkstra’s Algorithm**: A graph search algorithm used to find the shortest path from a start node to other nodes in a weighted graph.  
- **Linear Regression**: A supervised machine learning algorithm that predicts a continuous value (e.g., cost) based on one or more input features.

### Why Hybridize Dijkstra with Linear Regression?

1. **Adaptive Weights**: Real-world travel costs (e.g., time, congestion) vary based on external factors such as time of day, traffic, or weather.  
2. **Predictive Adjustment**: A regression model can learn from historical data to update edge weights before running Dijkstra, yielding more accurate routing decisions.

---

## Features

1. **Shortest Path Calculation**: Implements Dijkstra’s algorithm to find the minimum-cost or minimum-distance route between two nodes.  
2. **Machine Learning Integration**: Uses a Linear Regression model to predict or adjust the edge weights (costs).  
3. **Configurable Graph**: Easily modify or add nodes (cities) and edges (roads).  
4. **Scalable**: Suitable for small or large datasets with minimal configuration changes.

---

## Prerequisites

- **Python 3.7+**  
- **pandas** (for data loading and manipulation)  
- **NumPy** (for numerical operations)  
- **scikit-learn** (for the Linear Regression model)  
- **joblib** (for model serialization)  
- **matplotlib** and **networkx** (optional, for visualization)

---

## Installation

1. **Clone the Repository**  
   ```bash
   git clone https://github.com/Moghar12/map-navigator-dijkstra-algorithm.git
   cd map-navigator-dijkstra-algorithm
   
1. **Contact**
If you have any questions, feel free to reach out:

Email: mogharali10@gmail.com
