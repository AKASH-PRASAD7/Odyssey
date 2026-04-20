# Statistics: Quick Notes

## 1. Population vs. Sample
- **Population ($N$):** The *entire* group of items or individuals you want to study.
- **Sample ($n$):** A specific, smaller subset chosen from the population to estimate its properties.

---

## 2. Mean (Average)
The central value of a dataset. Add all numbers and divide by the count.

### A. Population Mean ($\mu$)
**Explanation:** The true, exact average of the entire population.
**Formula:** $\mu = \frac{\sum x}{N}$

### B. Sample/Estimated Mean ($\bar{x}$)
**Explanation:** The average of the sample. Used as a best-guess estimate for the population mean ($\mu$).
**Formula:** $\bar{x} = \frac{\sum x}{n}$

---

## 3. Variance
Measures how spread out the numbers are from the mean. (Higher number = more spread).

### A. Population Variance ($\sigma^2$)
**Explanation:** The exact spread of the complete population. Divide by $N$.
**Formula:** $\sigma^2 = \frac{\sum(x - \mu)^2}{N}$

### B. Sample/Estimated Variance ($s^2$)
**Explanation:** The estimated spread. Crucially, we divide by $(n - 1)$ instead of $n$. This is called Bessel's correction, which prevents us from underestimating the true spread.
**Formula:** $s^2 = \frac{\sum(x - \bar{x})^2}{n - 1}$

---

## 4. Standard Deviation
The exact square root of the Variance. It brings the spread measurement back to the same unit as the original data.

### A. Population Standard Deviation ($\sigma$)
**Formula:** $\sigma = \sqrt{\frac{\sum(x - \mu)^2}{N}}$

### B. Sample/Estimated Standard Deviation ($s$)
**Formula:** $s = \sqrt{\frac{\sum(x - \bar{x})^2}{n - 1}}$

---

## 5. Normal Distribution (Gaussian)
A symmetric, continuous, bell-shaped probability distribution.

**Core Rules:**
- The Mean, Median, and Mode are exactly the same and hit at the peak center.
- It is entirely defined by just two parameters: Mean ($\mu$) and Standard Deviation ($\sigma$).
- **The Empirical Rule (68-95-99.7%):**
  - $\approx 68\%$ of data falls within **1** standard deviation from the mean ($\pm 1\sigma$).
  - $\approx 95\%$ of data falls within **2** standard deviations from the mean ($\pm 2\sigma$).
  - $\approx 99.7\%$ of data falls within **3** standard deviations from the mean ($\pm 3\sigma$).

---

## 6. Covariance & Correlation
Both metrics measure how two connected variables (like height and weight) move together.

### A. Covariance ($Cov$)
**Explanation:** Measures the **direction** of the linear relationship between two variables.
- **Positive (+):** As $x$ goes up, $y$ goes up.
- **Negative (-):** As $x$ goes up, $y$ goes down.
- **Flaw:** It is heavily affected by units. A covariance of 5000 means perfectly nothing without knowing the context of the data size, making it hard to interpret.

**Formula (Sample):** $Cov(x, y) = \frac{\sum (x - \bar{x})(y - \bar{y})}{n - 1}$

### B. Correlation ($r$ or $\rho$)
**Explanation:** A standardized version of covariance. It fixes the flaw of covariance by measuring both the **direction** AND **strength** of the relationship on a strict scale from **-1 to 1**.
- **+1:** Perfect positive relationship.
- **-1:** Perfect negative relationship.
- **0:** No linear relationship.
- **Pro:** Completely unitless. An $r$ of $0.9$ is always a very strong positive correlation, no matter what you're measuring.

**Formula (Sample Correlation Coefficient $r$):** 
$r = \frac{Cov(x, y)}{s_x s_y}$
*(Where $s_x$ and $s_y$ are the standard deviations of datasets $X$ and $Y$)*
