# Customer Segmentation using K-Means

## Internship
This project is completed as part of the **Intern Alpha Data Analytics Internship**.

---

## Objective
The goal of this project is to segment customers into different groups based on their purchasing behavior using clustering techniques.

---

## Tools & Technologies Used
- Python 🐍
- Pandas (Data Processing)
- Matplotlib (Visualization)
- Scikit-learn (K-Means Clustering)

---

## Dataset
- File: `Mall_Customers.csv`
- The dataset includes:
  - CustomerID
  - Gender
  - Age
  - Annual Income (k$)
  - Spending Score (1-100)

---

## Steps Performed

### 1. Data Loading
- Loaded dataset using Pandas

### 2. Data Cleaning
- Checked for missing values
- Ensured data consistency

### 3. Feature Selection
- Selected:
  - Annual Income
  - Spending Score

### 4. Clustering
- Applied K-Means algorithm with 5 clusters
- Assigned cluster labels to each customer

### 5. Visualization
- Created scatter plot to visualize customer segments

---

## Key Insights
- Customers are divided into 5 distinct segments.
- High-income, high-spending customers form a premium group.
- Some customers have high income but low spending.
- Some customers have low income but high spending.
- These segments help businesses target customers effectively.

---

## Output Visualization

### Customer Segmentation
![Customer Segments](customer_segments.png)


---

## Conclusion
Customer segmentation helps businesses understand different types of customers and create targeted marketing strategies.
