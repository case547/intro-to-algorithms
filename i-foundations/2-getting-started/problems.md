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
* Largest sublist length at which insertion sort would be faster than merge sort

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