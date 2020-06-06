# About the Book
- Author: GAYLE LAAKMANN MCDOWELL
- Edition: 6TH
- [**Amazon様**](https://www.amazon.com/Cracking-Coding-Interview-Programming-Questions/dp/0984782850)



# 1. The Interview Process

the interviews are watching the points below

- Analytical skills: how optimal was your solution?
- Coding skills: were you able to successfully translate your sketch of an algorithm into readable/reasonable code?
- Technical Knowledge: do you have a strong foundation in CS or related domains?
- Experience: have you made good technical decisions in the past?
- Communication skills: do your personality and values fit with the company or a team?



## Why?

For those who blame the difficulties and tediousness of interviews
"Why do we need to prepare things that we aren't using so much at the REAL-WORLD??"

- False negatives are acceptable
- Problem-solving skills are valuable
- Basic data structure and algorithm knowledge is useful
- whiteboards let you focus on what matters
- but it's not for everyone or every company or every situation



## How Questions are Selected

At the vast majority of companies, there are no lists of what interviewers should ask. Rather, each interviewer selects its own questions. 



## It's All Relative

Interviewers assess you relative to other candidates on that same question by the same interviewer. It's a relative comparison.



## Frequently Asked Questions

skip



# 2. Behind the Scenes

- Screening: once you passed the resume phase, you'll come to this phase, in which you'll get Technical questions by engineers. About data structures/algorithms etc. Just a phone version of on-site interviews.
- On-site interviews: if you pass the process above, you usually have 3 to 6 in-person interviews at the site of the company. One of those is often over lunch.  Your other interviews will be mostly technical and will involve a combination of coding, algorithm, design/architecture, and behavioural/experience questions.



## The Microsoft Interview

read if needed



## The Amazon Interview

read if needed



## The Google Interview

read if needed



## The Apple Interview

read if needed



## The Facebook Interview

read if needed



## The Palantir Interview

read if needed



# 3. Special Situations



## Experienced Candidates

Even experienced candidates are probably getting technical questions such as data structures or algorithms.



## Testers and SDEts

SDEts(software design engineers in test) are the same as above.



## Product (and Program) Management

Same as above



## Dev Lead and Managers

Same as above



## Startups

> Many startups might post job listings, but for the hottest startups, often the best way in is through a personal
referral. This reference doesn't necessarily need to be a close friend or a coworker. Often just by reaching
out and expressing your interest, you can get someone to pick up your resume to see if you're a good fit. 



## Acquisitions and Acquihires

skip



## For Interviewers

- Ask Medium and Hard Problems: because they would like to see how a candidate approaches to solve such difficult tasks.
- Look for questions with multiple hurdles.
- Use hard questions, not hard knowledge: Again, it is the problem-solving skill they want to see, not the thing to ask if you memorise
- Offer positive reinforcement / Coach your candidates
- Know your mode: sanity check, quality, specialist, and proxy
    - Sanity check: easy questions to see the minimum degree of competency
    - Quality check: by giving them medium/hard tasks, interviewers can examine their potentialities
    - Specialist Questions: to test knowledge of specific topics
    - Proxy Knowledge: trivial though good to see if a candidate tends to pay attention to detailed parts of a project in the past



# 4. Before the Interview



## Getting the Right Experience

Without a great resume, there's no interview. And without great experience, there's no great resume. It's such a egg-hen situation.

- Take the big project classes
- Get an internship
- Start a project alone: good projects are bright on your resume!!



## Writing a Great Resume

skip, you can use some proofreading services out there!



## Preparation Map

- 1+ years(before the interview)
    - build projects outside of school/work
    - learn multiple programming languages
    - find internships
    - expand your network, eg, LinkedIn
- 3 - 12 months
    - continue working on projects
    - read intro sections of CtCI
    - make a target list of preferred companies
    - create a draft of resume and send it out for a resume reviewing service
    - Learn and master BigO
    - implement data structures and algorithms from scratch
    - try mock interview, eg., interviewing.io
    - do several mock interviews
- 1 - 3 months
    - continue practising interview questions
    - create a list to track mistakes you've made solving problems
- 4 weeks
    - begin applying companies
    - review/update resume
    - create interview prep grid(pg 32 on CtCI)
    - re-read intro to CtCI especially Tech & Behavioural sections
    - Do another mock interview
    - continue practising questions, writing code on paper
    - do a final mock interview
    - if you get a phone interview: mush have headset and/or video camera
- 1 week
    - rehearse stories from the interview prep grid(pg 32)
    - re-read algorithm approaches(pg 67)
    - re-read BigO section(pg 38)
    - rehearse each story from the interview prep grid once
- Day Before
    - continue practising interview questions
    - continue practising questions & review your list of mistakes
    - review powers of 2 table(pg 61). Print for a phone screen
- Day of
    - Remember to talk out loud. show how you think
    - Be confident(Not cocky!)
    - wake up in plenty of time to eat a good breakfast & be on time
    - don't forget: Stumbling and struggling are normal
- After
    - Write a thank-you note to the recruiter
    - get an offer? Celebrate!
    - If no offer, get ready for other companies!!
    - If you haven't heard from the recruiter, follow up him/her after one week.



# 5. Behavioural Questions



## Interview Preparation Grid

You should be able to talk about the things listed below for a few projects you've done and on your resume!

- Challenges
- Mistakes/Failures
- Enjoyed
- Leadership
- Conflicts
- What you'd do differently

Be able to tell your weakness as well as the strength as follows;

> Sometimes, I don't have very good attention to detail. While that's good because it lets me execute quickly, it also means that I sometimes make careless mistakes. Because of that, I make sure to always have someone else double-check my work



## Know your Technical Projects

You should focus on two or three technical projects that you should deeply
master.

- The project had challenging components (beyond just "learning a lot").
- You played a central role (ideally on the challenging components).
- You can talk at technical depth.



## Responding to Behavioural Questions

- Be Specific, Not Arrogant
- Limit details
- focus on yourself, not your team
- give structured answers



## So, tell me about yourself

Kind of template

1. Current Role: Headline Only
2. College: your academic background
3. Post College & Onwards: what you did after the graduation
4. Current Role(Details): what are you doing at the moment
5. Outside of Work: your free-time activities(related to the work lol)
6. Warp Up: why you'd like to work at the company



# 6. Big O



## An Analogy

Skip



## Time Complexity

The time complexity is the computational complexity that describes the amount of time it takes to run an algorithm.

- Big O, Big Theta, and Big Omega: all the same things
- Best case, Worst case, and Expected case: Minimum, Maximum, and average of Big O



## Space Complexity

The amount of memory/space required by an algorithm



## Drop the Constants

Remove the constant from the complexities

- 2N -> N
- N + 1 -> N



## Drop the Non-Dominant Terms

we only care the dominant term in Big O.

- $O(N^2 + 3N)$  -> $O(N^2)$ 



## Multi-Part Algorithms: Add vs. Multiply

```python
def A():
    # n + n -> O(n)
    for i in range(n):
        print()

    for i in range(n):
        print()

def B():
    # n * n -> O(n^2)
    for i in range(n):
        for i in range(n):
        	print()
```





## Amortised Time

If a heavy operation which happens rarely involves an algorithm, then we can amortise its heavy cost over time and get even it over time. In the it becomes a constant, eg., $O(1)$ operation in an insertion operation in the list manipulation.



## Log N Runtimes

When the number of elements in the problem space gets halved each iteration of an algorithm, it's likely to be $O(\log N)$. ** Bases of logs at this point isn't matter! lol



## Recursive Runtimes

When you have a recursive function that makes multiple calls inside, the runtime will be likely to look like $O(\text{num_call}^N)$

```python
def f(n):
    if n <= 1:
        return 1
    else:
        return f(n - 1) + f(n - 2)
```

the runtime above is $O(2^N)$



## Examples and Exercises

skip



# 7. Technical Questions
## How to prepare

- Try to solve a problem on your own: Don't just memorise the Q&A pair
- Write the code on paper
- Test your code on paper
- Test it on the computer



## What You Need to Know

- Core Data Structures, Algorithms, and Concepts

  | Data Structures        | Algorithms           | Concepts                |
  | ---------------------- | -------------------- | ----------------------- |
  | Linked Lists           | Breadth-First Search | Bit Manipulation        |
  | Trees, Tries, & Graphs | Depth-First Search   | Memory (Stack vs. Heap) |
  | Stacks & Queues        | Binary Search        | Recursion               |
  | Heaps                  | Merge Sort           | Dynamic Programming     |
  | Vectors/ArrayLists     | Quick Sort           | Big O Time & Space      |
  | Hash Tables            |                      |                         |

  ** Understand how to use/implement and, where applicable, the space/time complexity



## Walking Through a Problem: [PDF](http://www.crackingthecodinginterview.com/resources.html)

- Listen: Pay close attention to any detail of the problem description.
- Example: Ask an interview for showing some example input/output
- Brute Force: Get a brute-force solution at first, just state an **inefficient naive** algorithm and its runtime, then **optimise** from there. **Don't code yet!!**
- Optimise: BUD(**B**ottlenecks/**U**nnecessary Work/**D**uplicated Work)
  - Look for any unused info. You usually need all the information in a problem.
  - Solve it manually on an example, then reverse engineer your thought process. How did you solve it? 
  - Solve it *incorrectly* and then think about why the algorithm fails. Can you fix those issues?
  - Make a time vs. space trade-off. Hash tables are especially useful!
- Walk Through
  - Now that you have an optimal solution, walk through your approach in detail. Make sure you understand each detail before you **start coding**
- Implement
  - Your goal is to write the beautiful code/solution.
  - Modularise your code from the beginning and refactor to clean up anything that isn't beautiful
  - Keep talking!! Your interviewer wants to hear how you approach the problem
- Test
  - Conceptual test: walk through your code like a detailed code review
  - Unusual or non-standard code is fine
  - Hot spots, like arithmetic and null nodes in a tree structure
  - Small test cases, quickly!
  - Special/edge cases



## Optimise & Solve Technique: #1: Look for BUD

- Bottlenecks: which part of your code takes time the most? -> time complexity analysis
- Unnecessary Work: Break a loop when you find an answer!!
- Duplicated Work: Is this for-loop necessary??



## Optimise & Solve Technique: #2: DIY(Do It Yourself)

Don't jump into solving the problem, think about some of example in the problem. Then try solving it manually by hand. This though process comes in handy later!



## Optimise & Solve Technique: #3: Simplify and Generalise

When you manually work out examples you came up with, pay attention to two things;

- Simplify: simplify a procedure to solve it
- Generalise: generalise a procedure to be applicable for more general cases



## Optimise & Solve Technique: #4: Base Case and Build

With Base Case and Build, we solve the problem first for a base case (e.g., n = 1) and then try to build up from there.



## Optimise & Solve Technique: #5: Data Structure Brainstorm

We can simply run through a list of data structures and try to apply each one. This approach is useful because solving a problem may be trivial once it occurs to us to use, say, a tree.



## Best Conceivable Runtime(BCR)

The best conceivable runtime is, literally, the best runtime you could conceive of a solution to a problem having. You can easily prove that there is no way you could beat the BCR.



## Handing Incorrect Answers

Everyone else makes mistake at an interview so that it's not the place to count how many "right" answer you got, but rather **how your approached** the problem!!



## What You've Heard a Question Before

If you've heard a question before, admit this to your interviewer. Your interviewer is there to evaluate your problem-solving skills, not memory.



## The "Perfect" Language for Interviews

At many of the top companies, interviewers aren't picky about languages. They're more interested in how well you solve the problems than whether you know a specific language



## What Good Coding Looks Like

- Correct(having said that mistakes are allowed, still they want correct answers lol)
- Efficient: Time/Space complexities wise
- Simple: lengthy code isn't good...
- **Readable**: leave the comment and make your code highly readable/understandable
- Maintainable: modularise and simplify the interface



## Don't Give Up!

skip



# 8. The Offer and Beyond
## Handling offers and Rejection
## Evaluating the Offer
## Negotiation
## On the Job

# 9. Interview Questions
## Data Structures
### Chapter 1 | Arrays and Strings
#### Hash Tables
#### ArrayList & Resizable Arrays
#### StringBuilder

### Chapter 2 | Linked Lists
#### Creating a Linked List
#### Deleting a Node from a Singly Linked List
#### The "Runner" Technique
#### Recursive Problems

### Chapter 3 | Stacks and Queues
#### Implementing a Stack
#### Implementing a Queue

### Chapter 4 | Trees and Graphs
#### Types of Trees
#### Binary Tree Traversal
#### Binary Heaps(Min-Heaps and Max-Heaps)
#### Tries(Prefix Trees)
#### Graphs
#### Graph Search

## Concept and Algorithms
### Chapter 5 | Bit Manipulation
#### Bit Manipulation By Hand
#### Bit Facts and Tricks
#### Two's Complement and Negative Numbers
#### Arithmetic vs. Logical Right Shift
#### Common Bit Tasks: Getting and Setting

### Chapter 6 | Math and Logic Puzzles
#### Prime Numbers
#### Probability
#### Start Talking
#### Develop Rules and Patterns
#### Worst Case Shifting
#### Algorithm Approaches

### Chapter 7 | Object-Oriented Design
#### How to Approach
#### Design Patterns

### Chapter 8 | Recusion and Dynamic Programming
#### How to Approach
#### Recursive vs. Iterative Solutions
#### Dynamic Programming and Memoisation

### Chapter 9 | Systems Design and Scalability
#### Handling the Questions
#### Design: Step-By-Step
#### Algorithms that Scale: Step-By-Step
#### Key Concepts
#### Concentrations
#### There is no "perfect" system
#### Example Problem

### Chapter 10 | Sorting and Searching
#### Common Sorting Algorithms
#### Searching Algorithms

### Chapter 11 | Testing
#### What the Interviewer is Looking For
#### Testing a Real-World Object
#### Testing a Piece of Software
#### Testing a Function
#### Troubleshooting Questions

## Knowledge Based
### Chapter 12 | C and C++
#### Classes and Inheritance
#### Constructions and Destructors
#### Virtual Functions
#### Virtual Destructor
#### Default Values
#### Operator Overloading
#### Pointers and References
#### Templates

### Chapter 13 | Java
#### How to Approach
#### Overloading vs. Overriding
#### Collection Framework

### Chapter 14 | Databases
#### SQL Syntax and Variations
#### Denormalised vs. Normalised Databases
#### SQL Statements
#### Small Database Design
#### Large Database Design

### Chapter 15 | Threads and Locks
#### Threads in Java
#### Synchronisation and Locks
#### Deadlocks and Deadlock Prevention

## Additional Review Problems
### Chapter 16 | Moderate
### Chapter 17 | Hard

## 10. Solutions
### Data Structures
### Concepts and Algorithms
### Knowledge Based
### Additional Review Problems

## 11. Advanced Topics
### Useful Maths
### Topological Sort
### Dijkstra's Algorithm
### Hash Table Collision Resolution
### Rabin-Karp Substring Search
### AVL Trees
### Red-Black Trees
### MapReduce
### Additional Studying

## 12. Code Library
### HashMapList<T, E>
### TreeNode(Binary Search Trees)
### LinkedListNode(Linked List)
### Trie & TrieNode

## 13. Hints
### Hints for Data Structures
### Hints for Concepts and Algorithms
### Hints for Knowledge-Based Questions
### Hints for Additional Review Problems

## 14. About the Author
