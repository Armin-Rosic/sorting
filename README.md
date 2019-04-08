**Project Overview**

This project is an implementation of an integer sorting algorithm that leverages Python generators. 

The idea is to spawn a generator for every input integer, and to have the size of the generator be the value of the corresponding integer. 

Sorting is accomplished by looping through the collection of generators and yielding from each one once at each iteration. When a given generator has been exhausted, the integer that was used to populate it is returned. Given that the input integer determined how many times the generator could yield, the resulting stream of integers is sorted in ascending order. 

**Usage Details**

 If used on the Unix Command-Line, the sorting functionality can be accessed in two ways:

   1. As a part of a Unix pipe

   2. As a Command-Line program accepting integers as Command-Line arguments


 Case 1:

       -The program will process incoming data from stdin.

       -The delimiter of the incoming data is specified as Command-Line argument 1

       -The desired output delimiter is specified as Command-Line argument 2

       (example 1) ... (CSV input, space-delimited output)

       $ cat dataFile | python3 gensort.py ',' ' '

       int1 int2 int3 …

       (example 2) ... (space-delimited input, semi-colon-delimited output)

       $ cat dataFile | python3 gensort ' ' ';'

       int1;int2;int3 …

   Case 2:

       -The program will sort integers provided as arguments

       (example)

       $python3 gensort.py 4 2 3 1 3

       1 2 3 3 4

**Inspiration**

This project was inspired by the work of Timothy Hopper (github.com/tdhopper) who was himself inspired by the following tweet:

**_Here's a very strange Sorting Algorithm:_**

**_For every element X of the sequence the program does this:_**

**_1) Sleeps for X seconds_**

**_2) Prints X_**

**_The clock starts simultaneously for all elements._**

**_— Fermat's Library (@fermatslibrary) [December 4, 2017](https://twitter.com/fermatslibrary/status/937687947041701888?ref_src=twsrc%5Etfw)_**

What Timothy did was to implement this algorithm using Python's asyncio library, which allowed for a nearly verbatim implementation that he called 'sleepsort.py'. 

My rendition of the algorithm extracts the notion of mapping each integer to an operation of the corresponding size, and uses yielding from generators as the operation. By extension, this technique can be used to construct sorting algorithms that utilize any mutable data-type. 
