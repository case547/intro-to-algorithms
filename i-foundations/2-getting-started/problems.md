***2-1 Insertion sort on small arrays in merge sort***<br>
Although merge sort runs in Θ(_n_ lg _n_) worst-case time and insertion sort runs in Θ(_n_<sup>2</sup>) worst-case time, the constant factors in insertion sort can make it fasterin practice for small problem sizes on many machines. Thus, it makes sense to ***coarsen*** the leaves of the recursion by using insertion sort within merge sort when subproblems become sufficiently small. Consider a modification to merge sort in which _n_/_k_ sublists of length _k_ are sorted using insertion sort and then merged using the standard merging mechanism, where k is a value to be determined.

***a.*** Show that insertion sort can sort the _n_/_k_ sublists, each of length _k_, in Θ(_nk_) worst-case time.
* For each sublist, the sorting will take Θ(_k_<sup>2</sup>) worst-case time
* As there are _n_/_k_ sublists, sorting all sublists will be sorted in Θ(_n_/_k_ * _k_<sup>2</sup>) = Θ(_nk_) worst-case time

***b.*** Show how to merge the sublists in Θ(_n_ lg(_n_/_k_)) worst-case time.
* The n/k piles are progressively combined to n/2k, n/4k, etc. piles until there remains 1 pile left
* This results in a tree with lg(n/k) + 1 levels
* Each level compares n elements, so the cost is Θ(n (lg n/k)) + Θ(n), which is Θ(n lg(n/k))

***c.*** Given that the modified algorithm runs in Θ(_nk_ + _n_ lg(_n_/_k_)) worst-case time, what is the largest value of k as a function of n for which the modified algorithm has the same running time as standard merge sort, in terms of Θ-notation?
* Evaluating Θ(nk + n lg n - n lg k) = Θ(n lg n)
* In order for LHS to be of the same order as RHS, k ≤ lg n
* Verifying that k = lg n works: nk + n lg n - n lg k = n lg n + n lg n - n lg(lg n)
* Θ(2n lg n - n lg(lg n)) = Θ(n lg n)

***d.*** How should we choose _k_ in practice?
* Largest sublist length with which insertion sort would be faster than merge sort

***2-2 Correctness of bubblesort***<br>
Bubblesort is a popular, but inefficient, sorting algorithm. It works by repeatedly swapping adjacent elements that are out of order.
```
Bubblesort(A)
    for i = 1 to A.length - 1
        for j = A.length downto i + 1
            if A[j] < A[j-1]
                exchange A[j] with A[j-1]
```
***a.*** Let _A_' denote the output of `Bubblesort(A)`. To prove that `Bubblesort` is correct, we need to prove that it terminates and that _A_'[1] ≤ _A_'[2] ≤ ... ≤ _A_'[_n_], where _n_ = _A.length_. In order to show that `Bubblesort` actually sorts, what else do we need to prove?

* That the elements in A' are the same as A.

***b.*** State precisely a loop invariant for the for loop in lines 2–4 (the **downto** loop), and prove that this loop invariant holds. Your proof should use the structure of the loop invariant proof presented in this chapter.

* The loop in question maintains the following loop invariant: at the start of each iteration of the loop, the subarray A[j..n] is a permutation of the values that were in A[j..n] when the loop started, and the element A[j] is the smallest among them.
* **Initialisation:** Initially, j = n, so the subarray A[j..n] contains only one one element A[n], trivially the smallest element of the subarray, and thus the loop invariant holds
* **Maintainence:** Every iteration of the loop, A[j] is compared to A[j-1], and is swapped if smaller. After each iteration, the length of subarray A[j..n] increases by one and A[j] is the smallest element within it. The elements in the subarray remain a permutation of the elements that were it at the start of the loop.
* **Termination:** The loop terminates when j = i. As A[i] is the smallest element in A[i..n], and A[i..n] would consist of the same elements as at the start of the loop, the loop invariant is held.

***c.*** Using the termination condition of the loop invariant proved in part (b), state a loop invariant for the **for** loop in lines 1–4 that will allow you to prove _A_'[1] ≤ _A_'[2] ≤ ... ≤ _A_'[_n_]. Your proof should use the strucutre of the loop invariant prof present in this chapter.

* At the start of each iteration of the loop, the subarray A[1..i-1] contains the i-1 smallest values in the array in sorted order. Subarray A[i..n] contains the remaining n-i+1 remaining values in the array.
* **Initialisation:** Initially, i = 1, therfore the subarray A[1..i-1] is empty, and trivially contains the smallest zero elements.
* **Maintenance:** At the end of the inner loop, A[i] becomes the smallest element of the array, so A[1..i] contains the i smallest values in the array, in sorted order. Meanwhile, A[i+1..n] contains the remaining n-i remaining elements.
* **Termination:** The loop terminates when i = n, such that by the loop invariant, A[1..n-1] would contain the n-1 smallest elements in the array, sorted; A[n] would contain the last element, which must be the largest element, thus resulting in a fully sorted array.

***d.*** What is the worst-case running time of bubblesort? How does it compare to the running time of insertion sort?

* For every value of i from 1 to n-1, the inner for loop makes n-i iterations:
```
n-1
 Σ(n - i) = (n-1)/2 * [n-1 + n-(n-1)]
i=1
          = (n-1)/2 * (n - 1 + n - n + 1)
          = (n-1)/2 * n
          = (n^2 - n)/2
```
* Thus, the worst case running time of bubblesort is Θ(n<sup>2</sup>), the same as insertion sort.

***2-3 Correctness of Horner's rule***
The following code fragment impelements Horner's rule for evaluating a polynomial

*P*(*x*) = Σ<sup>*n*</sup><sub>*k*=0</sub> = a<sub>k</sub> x<sup>k</sup> = *a*<sub>0</sub> + *x*(*a*<sub>1</sub> + *x*(*a*<sub>2</sub> + ... + *x(a*<sub>*n*-1</sub> + *xa<sub>n</sub>*) ... )),

given the coefficients *a*<sub>0</sub>, *a*<sub>1</sub>, ... ,*a*<sub>n</sub> and a value for *x*:
```
y = 0
for i = n downto 0
    y = a_i + x*y
```
***a.*** In terms of Θ-notation, what is the running time of this code fragment for Horner's rule?

* Θ(n)

***b.*** Write pseudocode to implement the naive polynomial evaluation that computes each term from scratch. What is the running time of this algorithm? How does it compare to Horner's rule?
```
# Treating power as non-primitive operation

y = 0
for j = 0 to n
    # first compute x term by multiplication
    hold = 1
    for i = 1 to j
        hold = hold * x

    y = y + a_j * hold
```
* Running time is Θ(n<sup>2</sup>), which is worse than using Horner's rule