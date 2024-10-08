
-------------- ASSIGNMENT I --------------

* Part One - for mark 3
	
	A) "Mom bought me a new computer"

	Implement the following pattern matching algorithms: Brute-force, Sunday, KMP, FSM, Rabin-Karp, Gusfield Z.
	Compare their running times using chapters of a book, with a small (few words or a sentence) and a large pattern (a paragraph).
	Your report should contain some description of the algorithms and, most importantly, your findings.
	Include a graph showing the relation of RT against the text length.
	(This implies that you have to use several different lengths, which are placed on the x-axis of a graph.)
	The results should be reproducible.

	B) "Wacky Races"

	Prove empirically that there can be situations in which
		- Binary Sunday (the first algorithms covered in class) is at least twice as fast as Gusfield Z.
		- KMP is at least twice as fast as Rabin-Karp.
		- Rabin-Karp is at least twice as fast as Sunday
	It means that you should present a specific P and a specific T for which this happens.
	T should be at least 100kB long. The results should be reproducible and you are expected
	to explain the outcome of the comparison in each case.

** Part Two - for mark 4

	"What was that char again?"

	Implement the Brute-force and Sunday algorithms so that they accept wildcards ? and *.
	Your implementation should produce a Boolean value of a match found or not.
	The wildcards and \ itself can be escaped with a backslash.
	Explain your extensions to the algorithms in your report.


*** Part three - for mark 5

	"Jewish-style carp"

	Devise a version of Rabin-Karp algorithm which will check if for a given
	picture* M by N large its top-right K by K corner is duplicated somewhere in the picture.
	Your algorithm should replace slow modulo prime operations with faster bitwise mask &'s.
	!!!! Do make sure that the RT is at most linear in the number of pixels in the text !!!

	* Here, picture is a two-dimensional array of arbitrary items.



NOTE:
The main part of your work is the report, rather then the code itself (except for the "carp", where both are important).
Completing the first task is neccessary to get a positive mark.


-------------- ASSIGNMENT II --------------

Please include a report file with a discription of your solution along with the actual source code.


* Part One - for mark 3

	A) "Me spell rite"

	The Evil Lord Wladimir has cast the Spellus Incorrectus magical spell on your fellow students. Your task is to
	implement a simple spell checker that decides whether each individual word in a text file is spelled correctly.
	You might use the english word list available in this directory.
	Try: a naive (linear list) approach, string BBST, trie and a hash map. You may use library solutions for BBST, e.g. std::ordered_set or alike.
	Compare running times for dictionary building and spell checking on a large piece of text.
	Your report should contain description of algorithms, comparison findings including graphs showing the relation of RT against the text length.

	B) "Triwizard Tournament"
	One competition in the TT is to get out of a labyrinth as quickly as possible. Your task as the tournament supervisor is:
	given the labyrinth map, initial positions of the three competing wizzards and their speeds (in corridors per minute)
	predict which of them will reach the exit first. Assume that the magical wands used in the play
	are capable of guiding the wizards to the exit along a shortest possible path. The BFS should be used exactly once.


** Part Two - for mark 4

	"Aunt's Namesday"

	Your beloved aunt Petunia is throwing her namesday party, to which as usual, she invites all her friends and family.
	There are however some animosities among the invited guests. Aunt's idea is to have two separate tables, so that no two disliking one another people would have to sit at the same table.
	Given the list of the invited guests and the corresponding list of your aunt's suggestions on "who doesn't like whom",
	your task, as your aunt's dear little pumpkin sausage computer genius, is to use a non-recursive DFS algorithm to set up a "sitting scheme".

*** Part three - for mark 5

	"Full house"

	Implement a Hash Table with separate chaining and two HTs with open addressing, say linear probing and double hashing.
	Compare the relations between the search/insert times (y-axis) and the load factor (x-axis) for each implementation.
	


NOTE:
Completing the first task is neccessary to get a positive mark.



