# SI 506: Problem Set 03

## This week's Problem Set

This Problem Set focuses on tuples, immutability, and string slicing.

## Background
"The Three Little Pigs" is a fable about three pigs who build three houses of different materials. A Big Bad Wolf blows down the first two pigs' houses, made of straw and sticks respectively, but is unable to destroy the third pig's house, made of bricks.

## 1.0 Problem 01 (20 Points)
1. Create a tuple with the building materials `straw`, `sticks` and `bricks` and assign it to a variable named `build_materials`. Use indexing to access the third item in the tuple and assign it to a variable named `brick_house`.
<br />

2. Create a tuple named `destroyed` with `straw house` and `stick house` as the items. Create another tuple named `withstanding` with `brick house` as the only item. Join the tuples `destroyed` and `withstanding` to form a tuple named `pig_houses`.

:warning: Make sure you add the tuples in the order mentioned above to avoid triggering autograder test failures.
<br />

3. Between `destroyed_houses1` and `destroyed_houses2`, choose the correct collection of objects that can be modified and add `stick house` to it.

:bulb: Remember the difference between mutable and immutable objects, one of these sequences can be modified while the other cannot.

## 2.0 Problem 02 (30 points)
1. Use string slicing to extract the string `'Little pigs! Little pigs!'` from `wolf_dialog_1` and assign the return value to a variable named `substr_dialog_1`.

:bulb: It would be helpful to use print statements to check if your indexes and substrings are correct throughout this problem set.
<br />

2. Use string slicing on `wolf_dialog_1` to produce the output `'pigs! Little'` and store the return value to `substr_dialog_2`.
<br />

3. Use string slicing to extract the first **10** characters from `wolf_dialog_1` by using only the index of the end of the substring and store the return value to `substr_dialog_3`.

:bulb: This can be done by excluding the index number of the start character which is usually placed before the colon.
<br />

4. Use string slicing to extract all characters starting from index **7** from `wolf_dialog_1` and store the return value to `substr_dialog_4`.

:bulb: This can be accomplised by either including the index of the end of the substring or also by excluding it.
<br />

5. Use string slicing with a starting index of **1**, ending index of **46** a stride of **2** from `wolf_dialog_1` and store the return value to `substr_dialog_5`.

:bulb: The expected substring is `'itepg!Ltl is e ei!Ltm n'`
<br />

6. Use string slicing on `wolf_dialog_1` to produce the output `'Ltl'` and store the return value to `substr_dialog_6`.

## 3.0 Problem 03 (30 points)
1. Use string slicing with a negative starting index of **-21** and a negative ending index of **-1** from `pigs_dialog_1` and store the return value to `substr_dialog_7`.
<br />

2. Use string slicing on `pigs_dialog_1` to produce the output `'No! No! No! Not by the hairs on our chin'` and store the return value to `substr_dialog_8`.
<br />

3. Use string slicing on `pigs_dialog_1`to produce the output `'chinny chin chin!'` and store the return value to `substr_dialog_9`.
<br />

4. Use string slicing on `pigs_dialog_1` to produce the output `'No! No! Not by the hairs on our chin'` and store the return value to `substr_dialog_10`.

:bulb: You can use both negative and positive indexing at the same time.
<br />

5. Use string slicing with a negative stride of **-1** to produce the reverse of `pigs_dialog_1` and store the return value to `substr_dialog_11`.
<br />

6. Use string slicing with a negative stride on `pigs_dialog_1` to produce the output `'!icnh nicron ra h btN!N!N!N'` and store the return value to `substr_dialog_12`.

## 4.0 Problem 04 (20 points)
1. Use tuple indexing on `wolf_dialog_2` to create a new tuple named `sliced_dialog_1` with elements `("I'll", "huff", "and", "I'll", "puff")`.
<br/>

2. Use negative tuple indexing on `wolf_dialog_2` to create a new tuple named `sliced_dialog_2` with elements `("your", "house", "down.")`.