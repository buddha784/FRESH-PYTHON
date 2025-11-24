🐍 Problem Solving Using Python — Program Explanations

This repository contains 34 mathematical and computational Python programs designed to build logical thinking, problem-solving ability, and familiarity with number theory concepts in programming. Each function demonstrates a unique concept involving mathematical operations, recursion, primality, modular arithmetic, and algorithmic computation. Below is the detailed explanation of each program, describing what it achieves, why the concept matters, and where it can be applied.

1️⃣ factorial(n)

The factorial program computes the multiplication of all natural numbers from 1 up to a given number n. This concept is essential in mathematics, especially in combinatorics for calculating permutations, combinations, and probability outcomes. The program helps demonstrate recursive thinking or iterative loops and is often a beginner’s first exposure to mathematical algorithms in programming. Factorials also appear in formulas such as Taylor series expansions, binomial coefficients, and solving counting problems, making them foundational in computational mathematics.

2️⃣ is_palindrome(n)

This program checks whether a number reads the same forward and backward, classifying it as a palindrome. Palindromic numbers are interesting in number theory and appear in encryption patterns, pattern recognition, and digital error checking. The logic reinforces string conversion, digit manipulation, and conditional evaluation. Understanding palindrome detection strengthens the ability to work with loops, reverse logic, indexing, and string operations.

3️⃣ mean_of_digits(n)

The function calculates the arithmetic mean (average) of all digits in a number. This type of digit manipulation is commonly used in numerical analysis, checksum validation, and feature extraction in machine learning models involving numeric patterns. The program reinforces the idea of looping through digits and performing aggregation-based calculations, helping students practice modulus and integer division.

4️⃣ digital_root(n)

The digital root is found by repeatedly summing the digits of a number until a single digit remains. This concept appears in Vedic mathematics, checksum validation (ISBN/IMEI), modular arithmetic, and divisibility rules (especially for 9-based checks). The program helps understand iterative processes and mathematical simplification, giving insight into patterns behind numeric systems.

5️⃣ is_abundant(n)

An abundant number is one where the sum of its proper divisors is greater than the number itself. These numbers are studied in number theory and relate to the classification of integers (abundant, perfect, deficient). The program teaches divisor-finding logic and looping efficiency. Abundant numbers also appear in cryptographic mathematics and research into integer classification problems.

6️⃣ is_deficient(n)

A deficient number is the opposite of an abundant one: its proper divisor sum is less than the number. This function strengthens understanding of divisor computation and reinforces integer comparison logic. Like abundant numbers, deficient numbers belong to integer theory and help classify number behavior patterns.

7️⃣ is_harshad(n)

A Harshad (or Niven) number is divisible by the sum of its digits. This function demonstrates modular arithmetic and number decomposition, often used in numerical validation systems. The concept helps build foundational skills in splitting numbers, computing digit sums, and applying divisibility logic.

8️⃣ is_automorphic(n)

An automorphic number is one where the square of the number ends with the number itself. For example, 76² = 5776. This feature appears in hashing algorithms, number pattern research, and recreational mathematics. The logic strengthens understanding of string comparisons, slicing, and modular computation.

9️⃣ is_pronic(n)

A pronic number is the product of two consecutive integers (like 6 = 2×3). These numbers appear in geometry (rectangular arrangements), integer sequence studies, and algebraic patterns. The program builds logic for generating mathematical sequences and verifying integer properties.

🔟 prime_factors(n)

This program extracts and returns the prime factors of a number. Prime factorization is essential in cryptography (RSA encryption), computational math, optimization, and number theory research. Understanding factorization builds a foundation for more advanced algorithms like Pollard Rho and the Miller–Rabin test later in this assignment list.


1️⃣1️⃣ count_distinct_prime_factors(n)

This program identifies and counts how many unique prime factors a number has. Unlike basic factorization, this function focuses only on distinct primes, ignoring repeated multiplication. This concept is important in advanced number theory, especially in studying divisor functions, prime distributions, and cryptographic key structure. It improves problem-solving skills in factor extraction, looping efficiency, and set-based uniqueness logic.

1️⃣2️⃣ is_prime_power(n)

Checks whether a number can be expressed as a prime raised to a power. Relevant in algebraic number theory and computational mathematics.

1️⃣3️⃣ is_mersenne_prime(p)

Tests whether 
2p-1 is prime. Mersenne primes are significant in prime research and cryptographic applications.

1️⃣4️⃣ twin_primes(limit)

This function generates pairs of "twin primes"—two prime numbers differing by exactly 2 (e.g., 11 and 13). Twin primes are part of an unsolved mathematical mystery known as the Twin Prime Conjecture. Writing this function strengthens understanding of loop iteration, primality testing, and pair-wise conditions. It introduces students to algorithmic efficiency when handling ranges of prime checks.

1️⃣5️⃣ count_divisors(n)

This program calculates how many positive divisors a given number has. Divisor functions underpin topics like perfect numbers, partition theory, and sigma functions. The program enhances computational thinking through divisor search optimization. Counting divisors also appears in combinatorics, factor analysis, and algorithmic number theory.

1️⃣6️⃣ aliquot_sum(n)

The aliquot sum is the total of all proper divisors of a number (excluding the number itself). This function leads to the classification of abundant, perfect, and amicable numbers. It strengthens looping, divisor logic, and aggregation skills. Aliquot sums also appear in perfect number theory, an area studied since Euclid and still of research interest today.

1️⃣7️⃣ are_amicable(a, b)

This function checks whether two numbers form an "amicable pair," meaning each number’s aliquot sum equals the other. Amicable numbers are rare and mathematically interesting because they demonstrate relationships between divisor structures. The logic here encourages deeper understanding of perfect divisor behavior, conditional testing, and reusable functions (using the earlier aliquot sum).

1️⃣8️⃣ multiplicative_persistence(n)

Multiplicative persistence counts how many times the digits of a number must be multiplied together until only one digit remains. This concept appears in digit behavior research, computational pattern classification, and recreational number theory. This problem develops recursion/loop processing on digit data while demonstrating convergence-like iterative logic.

1️⃣9️⃣ is_highly_composite(n)

A highly composite number has more divisors than any number smaller than it. These numbers are important in the study of divisor growth, logarithmic distribution, and computational applications like data block sizing and hashing. Implementing this helps build performance-minded logic because it involves comparing multiple divisor counts efficiently.

2️⃣0️⃣ mod_exp(base, exponent, modulus)

Efficiently computes modular exponentiation, essential in cryptography and secure key generation.

2️⃣1️⃣ mod_inverse(a, m)

This function computes the modular multiplicative inverse of a number—meaning it finds a value x such that (a * x) ≡ 1 (mod m). This concept is crucial in cryptography, especially in RSA, elliptic curve encryption, and hashing systems. Implementing a modular inverse helps students understand the relationship between modular arithmetic, number theory, and the Extended Euclidean Algorithm. It introduces mathematical structures where normal division does not work, but modular arithmetic can still solve such problems.

2️⃣2️⃣ crt(remainders, moduli)

This program solves systems of simultaneous congruences using the Chinese Remainder Theorem (CRT). CRT is widely used in computational mathematics, computer architecture, clock arithmetic, and cryptographic applications such as RSA optimization. The function demonstrates handling lists, modular arithmetic, and applying algorithmic logic. Solving such systems is important because CRT allows extremely large computations to be performed using smaller modular operations — improving efficiency and speed.

2️⃣3️⃣ is_quadratic_residue(a, p)

This function checks whether there exists an integer x such that x² ≡ a (mod p). Quadratic residue theory forms the basis of advanced cryptography, primality testing, and elliptic curve systems. This program builds awareness of how numbers behave under modular squares and introduces the student to the structure of finite fields and modular patterns in algebra.

2️⃣4️⃣ order_mod(a, n)

This function finds the smallest positive integer k such that aᵏ ≡ 1 (mod n). This value is known as the multiplicative order of a modulo n and is a key concept in group theory, RSA key design, and discrete logarithm systems. Implementing this helps strengthen knowledge of modular exponentiation, repetitive computations, and abstract algebra concepts applied through programming.

2️⃣5️⃣ is_fibonacci_prime(n)

This program checks whether a number is both a Fibonacci number and a prime. Fibonacci primes are a rare and fascinating intersection of two important mathematical sequences. Writing this function helps reinforce primality testing, recursive or iterative Fibonacci computation, and logical condition design.

2️⃣6️⃣ lucas_sequence(n)

The Lucas sequence is similar to the Fibonacci sequence but begins with values 2 and 1. Lucas numbers appear in number theory, combinatorics, computer algorithms, and certain forms of cryptography. Implementing this function strengthens logic in generating numerical sequences, working with recurrence relations, and recognizing patterns in integer growth.

2️⃣7️⃣ is_perfect_power(n)

A perfect power is a number that can be expressed as aᵇ where a > 0 and b > 1. This concept is essential in algebraic number theory, integer factorization, and computational mathematics. Detecting perfect powers trains students to work with nested loops, exponentiation, and optimization logic while understanding the structural properties of integers.

2️⃣8️⃣ collatz_length(n)

This program implements the famous Collatz Conjecture, which remains one of mathematics’ most intriguing unsolved problems. The function counts how many steps it takes for a number to reach 1 when repeatedly applying the following rule:

If even → divide by 2

If odd → multiply by 3 and add 1
This strengthens recursive/iterative logic and exposes students to mathematical patterns that are simple to define but unpredictable to analyze — a key concept in algorithmic behavior.

2️⃣9️⃣ polygonal_number(s, n)

This function generates the nth s-gonal number, part of a family of sequences that includes triangular, square, pentagonal, and hexagonal numbers. Polygonal numbers connect arithmetic with geometry and appear in combinatorics, tiling, and mathematical modeling. Implementing this improves formula-based thinking and helps students work backwards from definitions into executable algorithms.

3️⃣0️⃣ is_carmichael(n)

This function checks whether a number is a Carmichael number—composite numbers that satisfy aₙ⁻¹ ≡ 1 (mod n) for all integers a coprime to n. Carmichael numbers are extremely important in cryptography because they can trick basic primality tests, making them key to understanding the weaknesses of naive algorithms. Writing this improves mathematical reasoning, divisor logic, and modular arithmetic implementation.

3️⃣1️⃣ is_prime_miller_rabin(n, k)

Implements the Miller–Rabin primality test, a fast probabilistic algorithm used to determine whether a number is prime. This method is widely used in modern cryptography due to its efficiency with large integers.

3️⃣2️⃣ pollard_rho(n)

Uses the Pollard Rho algorithm to factor large integers efficiently. This method is significant in computational number theory and cryptanalysis because it can break encryption systems based on factorization hardness.

3️⃣3️⃣ zeta_approx(s, terms)

Approximates the Riemann Zeta function using a finite summation approach. The function is important in analytic number theory and is connected to prime number distribution and convergence analysis.

3️⃣4️⃣ partition_function(n)

Calculates the number of distinct ways a number can be expressed as a sum of positive integers. This function is fundamental in combinatorics, number theory, and mathematical modeling of partitions.
