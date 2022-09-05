[Striver A2Z DSA Sheet](https://takeuforward.org/strivers-a2z-dsa-course/strivers-a2z-dsa-course-sheet-2/)

<details>
  <summary>Learn the basics</summary>

#### Learn the basics

1. Things to Know in C++/Java/Python or any language
    1. [Python Output Formatting](https://www.geeksforgeeks.org/python-output-formatting/)
    2. [Iterate over multiple lists simultaneously `zip` _(smallest by default)_, `zip_longest`](https://www.geeksforgeeks.org/python-iterate-multiple-lists-simultaneously/)
    3. [Accept multiple arguments to a method &nbsp;&nbsp; **or** <br>Variable-length arguments (`*args`, `**kwargs`) in Python](https://note.nkmk.me/en/python-args-kwargs-usage/)
2. Build-up Logical Thinking
    1. [Must do Pattern Problems before starting DSA](https://takeuforward.org/strivers-a2z-dsa-course/must-do-pattern-problems-before-starting-dsa/)
    2. [Patterns Code](1_Basics/2_PatternProblems/patterns.py)
3. Collections in Python
4. Basic Math
    1. [Count digits in a number](1_Basics/4_Math/count_digits.py)
    2. [Reverse a number](1_Basics/4_Math/reverse_a_number.py)
    3. [check_palindrome_number](1_Basics/4_Math/check_palindrome_number.py)
        1. Variations : With Space, Without space, When number is very huge that it can't fit long
    4. [GCD or HCF of two numbers](1_Basics/4_Math/gcd_and_lcm/gcd_of_two_numbers.py)
        1. [GCD or HCF of Multiple numbers](1_Basics/4_Math/gcd_and_lcm/gcd_of_multiple_numbers.py)
    5. [LCM of two numbers](1_Basics/4_Math/gcd_and_lcm/lcm_of_two_numbers.py)
        1. [LCM of multiple numbers](1_Basics/4_Math/gcd_and_lcm/lcm_of_multiple_numbers.py) : What's the catch here?
    6. [Armstrong Number](1_Basics/4_Math/armstrong_number.py)
    7. [All Divisors of a Number](1_Basics/4_Math/all_divisors.py)
5. Recursion
    * For Recursion the absolute OG is Aditya Verma
    * [Recursion Playlist](https://www.youtube.com/playlist?list=PL_z_8CaSLPWeT1ffjiImo0sYTcnLzo-wY) This should be more than enough to understand recursion
    * **TODO** -> Will do these recursion problem when I revise recursion from my notes of these videos, till then I can move on
6. Hashing
    * [Count frequency of each element in the array](1_Basics/6_Hashing/count_frequenc_of_array_elements.py)
    * [Find the highest/lowest frequency element](1_Basics/6_Hashing/find_highest_and_lowest_frequency_element.py)

7. Sorting
    * What is stability in sorting algorithms?
    * Which algorithms are stable and which of them are unstable?
    * [Selection Sort](2_Sorting/selection_sort.py)
      <details>
            <summary>details</summary>

        * In the normal Selection sort (asc order)
        * We traverse from let to right and
        * The sorted array is also build form left to right direction
        * Basically : Here we push the smallest element to the first

      ##### Questions?       * [GFG Article For Answers](https://www.geeksforgeeks.org/selection-sort/)
        * What are the Boundary Cases of Selection Sort algorithm?
            * When does it take maximum time and
            * When does it take minimum time?
            * What's the time in each case
        * Is Selection Sort an in-place sorting algorithm?
        * Is Selection Sort a stable algorithm?
        * When is the Selection Sort algorithm used?

      </details>

    * [Bubble Sort](2_Sorting/bubble_sort.py)
      <details>
            <summary>details</summary>

        * In the normal Bubble sort (asc order)
        * We traverse from let to right and
        * But The sorted array is build form right to left direction
        * Basically : Here we push the largest element to the end

      ##### Questions?       * [GFG Article For Answers](https://www.geeksforgeeks.org/bubble-sort/)
        * What are the Boundary Cases of Bubble Sort algorithm?
            * When does it take maximum time and
            * When does it take minimum time?
            * What's the time in each case
        * Is Bubble Sort an in-place sorting algorithm?
        * Is Bubble Sort a stable algorithm?
        * When is the Bubble Sort algorithm used?

      </details>

    * [Insertion Sort](2_Sorting/insertion_sort.py)
      <details>
        <summary>details</summary>

        * Insertion sort is a bit trickier than selection and bubble sort,
        * and its is also used in many other places, with some modification
        * e.g. Quick sort's partition step

        - [ ]  To be verified

        <hr>

      ##### Questions?       * [GFG Article For Answers](https://www.geeksforgeeks.org/insertion-sort/)
        * What are the Boundary Cases of Insertion Sort algorithm?
            * When does it take maximum time and
            * When does it take minimum time?
            * What's the time in each case
        * What are the Algorithmic Paradigm of Insertion Sort algorithm?
        * Is Insertion Sort an in-place sorting algorithm?
        * Is Insertion Sort a stable algorithm?
        * When is the Insertion Sort algorithm used?

      </details>

        - What is [Binary Insertion Sort](https://www.geeksforgeeks.org/binary-insertion-sort/)?
            * We can use binary search to reduce the number of comparisons in normal insertion sort.
            * Binary Insertion Sort uses binary search to find the proper location to insert the selected item at each iteration.
            * In normal insertion, sorting takes O(i) (at ith iteration) in worst case.
            * We can reduce it to O(log i) by using binary search.
            * The algorithm, as a whole, still has a running worst case running time of O(n^2) because of the series of swaps required for each insertion.

        - How to implement [Insertion Sort in Linked List](https://www.geeksforgeeks.org/insertion-sort-for-singly-linked-list/)?

    * [Difference Bw Selection Sort and Insertion Sort]()
    * [merge_sort](2_Sorting/merge_sort.py)
    * [quick_sort](2_Sorting/quick_sort.py)

#

### Uncategorized

* [Frequency of the Most Frequent Element](https://leetcode.com/problems/frequency-of-the-most-frequent-element/)
    * suggested under [Find the highest/lowest frequency element](1_Basics/6_Hashing/find_highest_and_lowest_frequency_element.py)
    * But it does not fit there

</details>

<details>
  <summary>Click me</summary>

### Heading

1. Foo
2. Bar
    * Baz
    * Qux

### Some Code

  ```js
  function logSomething(something) {
    console.log('Something', something);
  }
  ```

</details>