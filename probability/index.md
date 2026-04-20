# Probability: Quick Notes

## 1. What is Probability?
The mathematical chance of an event happening, expressed as a fraction or decimal between 0 (impossible) and 1 (certain).
**Formula:** $P(A) = \frac{\text{Number of favorable outcomes}}{\text{Total number of possible outcomes}}$

---

## 2. Essential Terminology
- **Sample Space ($S$):** All possible outcomes.
- **Event ($A$):** A specific outcome or set of outcomes you are measuring.
- **Complement ($A'$ or $A^c$):** The event NOT happening. **Rule:** $P(A') = 1 - P(A)$.

---

## 3. The OR Rule (Addition)
Used to find the probability of Event A **OR** Event B occurring.

### A. Mutually Exclusive (Cannot happen at the same time)
**Rule:** Simply add the probabilities.
**Formula:** $P(A \text{ or } B) = P(A) + P(B)$
**Example:** Rolling a 2 OR a 5 on a standard die. Cannot be both at once. 
$\frac{1}{6} + \frac{1}{6} = \frac{2}{6}$

### B. Non-Mutually Exclusive (Can happen at the same time)
**Rule:** Add the probabilities, but subtract the overlap to avoid double counting.
**Formula:** $P(A \text{ or } B) = P(A) + P(B) - P(A \text{ and } B)$
**Example:** Drawing a Heart OR a King from a deck.
$P(\text{Heart}) + P(\text{King}) - P(\text{King of Hearts})$
$\frac{13}{52} + \frac{4}{52} - \frac{1}{52} = \frac{16}{52}$

---

## 4. The AND Rule (Multiplication)
Used to find the probability of Event A **AND** Event B both occurring.

### A. Independent Events (One does not affect the other)
**Rule:** Multiply the probabilities.
**Formula:** $P(A \text{ and } B) = P(A) \times P(B)$
**Example:** Flipping Heads on a coin AND rolling a 4 on a die. 
$\frac{1}{2} \times \frac{1}{6} = \frac{1}{12}$

### B. Dependent Events (One outcome changes the odds of the other)
**Rule:** Multiply the first probability by the adjusted probability of the second.
**Formula:** $P(A \text{ and } B) = P(A) \times P(B | A)$ *(See Section 5)*
**Example:** Drawing two Aces from a deck **without** putting the first one back. 
$\frac{4}{52} \times \frac{3}{51} = \frac{12}{2652}$

---

## 5. Conditional Probability
Used when Event B relies on Event A having **already occurred**. The notation is $B | A$, read as "B given A".

**Rule:** Divide the probability of both happening by the probability of the given condition.
**Formula:** 
$$ P(B | A) = \frac{P(A \text{ and } B)}{P(A)} $$

**Example:** You roll a die. What is the probability it is a 6, given that you already know the result is an even number?
- Condition ($A$): The result is Even (2, 4, or 6). $P(A) = \frac{3}{6}$ 
- Both ($A \text{ and } B$): Being Even AND being a 6. $P({A \text{ and } B}) = \frac{1}{6}$
- Computation: $\frac{1/6}{3/6} = \frac{1}{3}$

---

## 6. Bayes' Theorem
Used to reverse conditional probability. It lets you find $P(A | B)$ when you only have the data for $P(B | A)$.

**Formula:**
$$ P(A | B) = \frac{P(B | A) \times P(A)}{P(B)} $$
