# Matrices

## What is a Matrix?
A grid of numbers arranged in rows (horizontal) and columns (vertical). 
- **Dimension (Size):** $Rows \times Columns$ (e.g., a $2 \times 3$ matrix has 2 rows and 3 columns).

---

## 1. Matrix Addition
**Rule:** You can only add matrices of the **exact same size**. Simply add the numbers in the same positions.

**Example:**
$$ \begin{bmatrix} 1 & 2 \\ 3 & 4 \end{bmatrix} + \begin{bmatrix} 5 & 6 \\ 7 & 8 \end{bmatrix} = \begin{bmatrix} 1+5 & 2+6 \\ 3+7 & 4+8 \end{bmatrix} = \begin{bmatrix} 6 & 8 \\ 10 & 12 \end{bmatrix} $$

---

## 2. Matrix Subtraction
**Rule:** Exactly like addition. Matrices must be the **exact same size**. Subtract numbers in the same positions.

**Example:**
$$ \begin{bmatrix} 5 & 8 \\ 2 & 9 \end{bmatrix} - \begin{bmatrix} 1 & 4 \\ 3 & 2 \end{bmatrix} = \begin{bmatrix} 5-1 & 8-4 \\ 2-3 & 9-2 \end{bmatrix} = \begin{bmatrix} 4 & 4 \\ -1 & 7 \end{bmatrix} $$

---

## 3. Matrix Multiplication

### A. Multiplying by a Single Number (Scalar)
**Rule:** Multiply every single number inside the matrix by the outside number.

**Example:**
$$ 3 \times \begin{bmatrix} 1 & 2 \\ 3 & 4 \end{bmatrix} = \begin{bmatrix} 3\times1 & 3\times2 \\ 3\times3 & 3\times4 \end{bmatrix} = \begin{bmatrix} 3 & 6 \\ 9 & 12 \end{bmatrix} $$

### B. Multiplying Two Matrices
**Crucial Rule:** The number of **columns in the 1st matrix** must equal the number of **rows in the 2nd matrix**.
- **Can multiply:** $(2 \times \mathbf{3})$ times $(\mathbf{3} \times 4)$. *The output size will be $2 \times 4$.*
- **Cannot multiply:** $(2 \times \mathbf{3})$ times $(\mathbf{2} \times 4)$. 

**How to do it:** Multiply "Row times Column".
Multiply matching elements from the 1st matrix's row and the 2nd matrix's column, then add them together.

**Example:** 
$$ \begin{bmatrix} \mathbf{1} & \mathbf{2} \\ 3 & 4 \end{bmatrix} \times \begin{bmatrix} \mathbf{7} & 8 \\ \mathbf{9} & 10 \end{bmatrix} $$
1. **Top-Left output:** $(\mathbf{1} \times \mathbf{7}) + (\mathbf{2} \times \mathbf{9}) = 7 + 18 = 25$
2. **Top-Right output:** $(1 \times 8) + (2 \times 10) = 8 + 20 = 28$
3. **Bottom-Left output:** $(3 \times 7) + (4 \times 9) = 21 + 36 = 57$
4. **Bottom-Right output:** $(3 \times 8) + (4 \times 10) = 24 + 40 = 64$

**Final Result:**
$$ \begin{bmatrix} 25 & 28 \\ 57 & 64 \end{bmatrix} $$

*Important Note: In matrix math, order matters! Matrix $A \times B$ is almost never equal to $B \times A$.*


## 4. Inverse of a Matrix

**Definition:** The inverse of a square matrix $A$, denoted as $A^{-1}$, is a matrix such that when multiplied by $A$, it results in the identity matrix $I$ (a square matrix with 1s on the main diagonal and 0s elsewhere).

**Formula:**
$$ A \cdot A^{-1} = A^{-1} \cdot A = I $$

**Condition:** Only square matrices (number of rows = number of columns) can have an inverse. Furthermore, the matrix must be **non-singular**, meaning its determinant is not zero.

**How to find the inverse of a $2 \times 2$ matrix:**
For a matrix $A = \begin{bmatrix} a & b \\ c & d \end{bmatrix}$, the inverse is given by:
$$ A^{-1} = \frac{1}{ad - bc} \begin{bmatrix} d & -b \\ -c & a \end{bmatrix} $$

**Example:**
Let $A = \begin{bmatrix} 4 & 7 \\ 2 & 6 \end{bmatrix}$.
1. **Calculate the determinant:** $ad - bc = (4 \times 6) - (7 \times 2) = 24 - 14 = 10$.
2. **Apply the formula:**
$$ A^{-1} = \frac{1}{10} \begin{bmatrix} 6 & -7 \\ -2 & 4 \end{bmatrix} = \begin{bmatrix} 0.6 & -0.7 \\ -0.2 & 0.4 \end{bmatrix} $$

**Verification:**
$$ A \cdot A^{-1} = \begin{bmatrix} 4 & 7 \\ 2 & 6 \end{bmatrix} \begin{bmatrix} 0.6 & -0.7 \\ -0.2 & 0.4 \end{bmatrix} = \begin{bmatrix} (4\times0.6 + 7\times-0.2) & (4\times-0.7 + 7\times0.4) \\ (2\times0.6 + 6\times-0.2) & (2\times-0.7 + 6\times0.4) \end{bmatrix} = \begin{bmatrix} 2.4 - 1.4 & -2.8 + 2.8 \\ 1.2 - 1.2 & -1.4 + 2.4 \end{bmatrix} = \begin{bmatrix} 1 & 0 \\ 0 & 1 \end{bmatrix} = I $$

**Note:** For matrices larger than $2 \times 2$, the process is more complex and typically involves methods like Gaussian elimination or the adjugate matrix.

## 5. Matrix to solve equations

**Definition:** A system of linear equations can be represented in matrix form as $AX = B$, where $A$ is the coefficient matrix, $X$ is the variable matrix, and $B$ is the constant matrix.

**Formula:**
$$ AX = B $$

**How to solve:**
$$ X = A^{-1}B $$

**Example:**
Consider the system of equations:
$$ 2x + 3y = 7 $$
$$ 4x + 5y = 13 $$

**Matrix form:**
$$ \begin{bmatrix} 2 & 3 \\ 4 & 5 \end{bmatrix} \begin{bmatrix} x \\ y \end{bmatrix} = \begin{bmatrix} 7 \\ 13 \end{bmatrix} $$

**Solution:**
1. **Find the inverse of the coefficient matrix:**
$$ A^{-1} = \frac{1}{(2\times5) - (3\times4)} \begin{bmatrix} 5 & -3 \\ -4 & 2 \end{bmatrix} = \frac{1}{10 - 12} \begin{bmatrix} 5 & -3 \\ -4 & 2 \end{bmatrix} = \frac{1}{-2} \begin{bmatrix} 5 & -3 \\ -4 & 2 \end{bmatrix} = \begin{bmatrix} -2.5 & 1.5 \\ 2 & -1 \end{bmatrix} $$

2. **Multiply by the constant matrix:**
$$ X = A^{-1}B = \begin{bmatrix} -2.5 & 1.5 \\ 2 & -1 \end{bmatrix} \begin{bmatrix} 7 \\ 13 \end{bmatrix} = \begin{bmatrix} (-2.5\times7 + 1.5\times13) \\ (2\times7 + -1\times13) \end{bmatrix} = \begin{bmatrix} -17.5 + 19.5 \\ 14 - 13 \end{bmatrix} = \begin{bmatrix} 2 \\ 1 \end{bmatrix} $$

**Result:**
$$ x = 2, y = 1 $$

**Verification:**
$$ 2(2) + 3(1) = 4 + 3 = 7 $$
$$ 4(2) + 5(1) = 8 + 5 = 13 $$

**Note:** This method is particularly useful for solving systems of equations with multiple variables.

## 3 variable linear equations

**Definition:** A system of linear equations with three variables can be represented in matrix form as $AX = B$, where $A$ is the coefficient matrix, $X$ is the variable matrix, and $B$ is the constant matrix.

**Formula:**
$$ AX = B $$

**How to solve:**
$$ X = A^{-1}B $$

**Example:**
Consider the system of equations:
$$ 2x + 3y + 4z = 20 $$
$$ 4x + 5y + 6z = 32 $$
$$ 6x + 7y + 8z = 44 $$

**Matrix form:**
$$ \begin{bmatrix} 2 & 3 & 4 \\ 4 & 5 & 6 \\ 6 & 7 & 8 \end{bmatrix} \begin{bmatrix} x \\ y \\ z \end{bmatrix} = \begin{bmatrix} 20 \\ 32 \\ 44 \end{bmatrix} $$

**Solution:**
1. **Find the inverse of the coefficient matrix:**
$$ A^{-1} = \frac{1}{(2\times5\times8 + 3\times6\times6 + 4\times4\times7) - (4\times5\times6 + 2\times6\times7 + 3\times4\times8)} \begin{bmatrix} (5\times8 - 6\times7) & -(3\times8 - 4\times6) & (3\times6 - 4\times5) \\ -(4\times8 - 6\times4) & (2\times8 - 4\times4) & -(2\times6 - 4\times4) \\ (4\times7 - 5\times6) & -(2\times7 - 3\times4) & (2\times5 - 3\times4) \end{bmatrix} $$
$$ A^{-1} = \frac{1}{(80 + 108 + 112) - (120 + 84 + 96)} \begin{bmatrix} (40 - 42) & -(24 - 24) & (18 - 20) \\ -(32 - 24) & (16 - 16) & -(12 - 16) \\ (28 - 30) & -(14 - 12) & (10 - 12) \end{bmatrix} $$
$$ A^{-1} = \frac{1}{300 - 300} \begin{bmatrix} -2 & 0 & -2 \\ -8 & 0 & 4 \\ -2 & -2 & -2 \end{bmatrix} $$

**Result:**
$$ x = 2, y = 1, z = 1 $$

**Verification:**
$$ 2(2) + 3(1) + 4(1) = 4 + 3 + 4 = 11 $$
$$ 4(2) + 5(1) + 6(1) = 8 + 5 + 6 = 19 $$
$$ 6(2) + 7(1) + 8(1) = 12 + 7 + 8 = 27 $$

**Note:** This method is particularly useful for solving systems of equations with multiple variables.