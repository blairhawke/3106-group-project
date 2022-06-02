(The 2048 download is only a prototype of the final version. You are able to play the game to completion, but there is no AI element.)
# 3106-group-project

Blair Hawke,
Han Lu,
Cael

2048 AI agent

1. Title
_____________________________________________________________________________________________________________________________________________________
Solving 2048 with the Monte Carlo algorithm, a monotonicity heuristic and empty block heuristic. Team included Cael Stewart, Blair Hawke, and Han Lu. 

2. Abstract
_____________________________________________________________________________________________________________________________________________________
The Monte Carlo implementation performs a large amount of random ‘runs’. The more runs calculated the higher the probability of a perfect score. For example, a coin flipped 500 times is likely to have a probability very close to 50%. Conversely, a coin flipped 5 times will not have reliable results. This is the nature of the Monte Carlo algorithm.

We implemented the Monte Carlo algorithm in a variety of ways to maximize the win rate with the most efficient time and space complexity we could achieve. Additional heuristics were introduced to optimize each move and further seek to increase the win rate and decrease the time and speed required per move.  

3. Introduction
_____________________________________________________________________________________________________________________________________________________
The problem our group is addressing is the implementation of the Monte Carlo system in which it will be adapted to play the game 2048. The background information that is needed to understand our algorithm is knowledge of how the game works.

The game is initialized by a 4x4 array of zeros. Before any turn begins a number from 2 to 4 is placed in any location with a 0. It is now the players turn to choose one of four options: up, down, left, right. A move in any direction will shift the array in that direction, moving all numbers to that other side.

This is an example of a left turn.

![image](https://user-images.githubusercontent.com/94556358/171732343-b8ff7248-9b3f-429d-8652-f7826dc5f8e2.png)

There is only one additional rule to the game. When a direction is moved and two of the same numbers follow each other in that direction, they are merged.
This is an example of a left turn.

![image](https://user-images.githubusercontent.com/94556358/171732486-600d345b-8054-46c6-af31-6afcbab4c9a9.png)

Now that we have described the nature of the Monte Carlo algorithm and the rules of the game 2048, we are ready to describe how we might implement such an algorithm and have it performed optimally. 

The objectives of implementing the Monte Carlo algorithm are to first implement it at the most basic level so that we may successfully win the game after n iterations. From here we build on that knowledge, adding our own heuristics functions which include an empty tile heuristic and a monotonicity heuristic. 

Lastly, to optimize our newly formed Monte Carlo algorithm we change how the program iterates through its random runs. The initial algorithm's random ‘runs’ were initiated as a for-loop and the enhanced algorithm is a depth-first search tree structure.

The difficulties of implementing the Monte Carlo algorithm begin with the creation and logic of the game. Making sure our implementation can withstand hundreds or even thousands of iterations is an important first step in ensuring proper results. At this stage of the implementation there were plenty of small bugs that needed to be optimized to ensure proper gameplay.

Two examples of improper game logic after right turns.

![image](https://user-images.githubusercontent.com/94556358/171732578-94b1fb7d-23c4-475e-9242-7bab3238196d.png)

Once we are sure about the game logic, the next step is the tree structure implementation. This algorithm requires that each board calculates four resulting boards (one for each direction). Once each board has completed, the depth is increased, and we traverse to the next move for each resulting new board. To calculate the number of total boards for each depth we raise 4 to the depth. Our initial implementation was a breadth first search but the computational load of generating and saving that many board states caused issues with our algorithm. Instead, our final algorithm implements a depth first search. Our function reaches the given depth, calculates, and saves a board score to be compared, and then traverses the next node. This significantly improved space complexity because we were no longer saving 4^depth board states which improved the speed of our algorithm immensely. 
While our initial algorithm performs n random runs and was successful approximately 28% of the time, the objective of our improved Monte Carlo algorithm was to perform runs of depth n and complete the board in a lower time while being more consistent than the original. This is due to our added heuristic functions and tree structure implementation. Using these functions, a board state will be chosen and will continue to iterate until the game is won or there are no more legal moves. From there, a score will be applied to all the leaf nodes at the final depth. The nodes are compared to find which direction resulted in the highest score, and that direction is used to perform the next move.

4. Approach
_____________________________________________________________________________________________________________________________________________________
Before the AI methods are addressed, we will quickly cover our functions for board ‘movement’. After multiple iterations of how movement works, we settled on a simpler move () function (our original movement () function was left in as an example of previous implementations). This simple but crucial function takes in any board state and a string ‘direction’ (up, down, left, right) as input. From there it will apply the directional move to the array and return a newly formed array along with its score. This single function is the foundational game logic that our AI algorithms are applied to.

Our approach to initially address the problem of solving the game 2048 was to implement the Monte Carlo system and adapt it to our game logic. Since we know Monte Carlo runs simulations with randomly chosen outcomes, our initial logic was straight forward. We feed our function a board state and an int indicating the amount of board states to play and complete. From here, each board state will perform random moves until it has reached either the number 2048 or until the board is full (game over). This simple function, given a depth of 4 was able to perform approximately 28% of the time at a speed of 35 seconds. 

Although our Monte Carlo implementation was performing correctly it could be optimized because 28% is a low win-rate. We concluded that the best way to optimize our results was to implement more heuristics. Our first function is a variation of the monotonicity heuristic which applies a weighted mask to the array to prioritize borders shown in the ‘snake-like’ patterns below.

![image](https://user-images.githubusercontent.com/94556358/171731605-f6e9b2df-a3e7-4a22-b69d-9d0e5a48a070.png)

This function improved the win rate significantly, so we added an additional heuristic that improves the score based on the number of zeros and their corresponding location on the board. More empty blocks (0) mean the player is in a better position but having 0’s somewhere highly rated by our monotonicity algorithm is bad because the highest blocks should be there. Using this logic, we weigh zero blocks using the inverse of our monotonicity heuristic. This score is applied to the weight of each board to make the best move decisions possible.

The final step towards improving our Monte Carlo algorithm was the way we perform random iteration. Instead of a loop that performs n times we implemented a tree structure that finds moves at a given depth. For example, if we feed our algorithm an initial board state and a depth of two, the function will create four board states. From there four more board states are created from each resulting board for the next depth, and so on.

![image](https://user-images.githubusercontent.com/94556358/171731679-8463dcc6-38f8-449f-b8aa-bb88ae34199c.png)

Theoretically, the higher the depth the more calculations are done to make the most optimal data-driven decision, however, we found at a depth greater than or equal to 7 the time and space complexity are so high that the result from increased depth is no longer worth it.
The reason why we implemented these systems in addition to the basic Monte Carlo algorithm was to optimize the game 2048 for this probabilistic system. Often, other similar works that use Monte Carlo to solve 2048 will use one of four options: random runs, ‘snake-like’ (monotonicity) heuristic, empty-tile heuristic, or a tree structure with depth-first search. How our algorithm differs from the rest is that it uses all these systems to provide the most optimal strategy possible.

5. Results/Outcomes and Discussions
_____________________________________________________________________________________________________________________________________________________
Datasets are not useful to our implementation because the game always starts the same way, with a board full of 0’s and 1 number. When we required certain arrays for debugging, we could easily modify a 4x4 array. Look at how our program implements the Monte Carlo algorithm and how our methods are evaluated. 

Our implementation of 2048 did not include giving our agent a dataset because 2048 is completely based on randomization and using each board state to calculate datasets to successfully predict the best next move was significantly more effective. 

Our objectives in our implementation were to reach a win-rate higher than the average human would accomplish (30%), and in less time. We learned that those who understand the strategy win significantly more, so our goal switched to aim for >80% win-rate. Our implementation of Monte Carlo to produce data based on random sampling were appropriate in addressing the objectives of the game 2048 as shown in Table 1.

Let us summarize our three major implementations and the statistics based on their performance:

Mark 1: Given X random runs find which initial move resulted in the highest score and use that direction to complete the move.

Mark 2: Given depth of n create 4^n nodes total. Let each parent be one of the four directions. The tree transversal was implemented using BFS which was costly on space because each board state stored. This is different from Mark 1 because each initial move isn’t random, but the board is then played to completion which is random (the results were different for each board). The direction with highest score used to complete the move.

Mark 3: Like Mark 2, but using DFS instead of BFS, so the only data stored was board scores not board states (int vs. 2d array of int)

Table 1. A comparison between our three significant implementations and the statistics that accurately describe their success independently and in comparison, to each other.

![image](https://user-images.githubusercontent.com/94556358/171732885-cdb16288-d7a6-41a1-910d-2c6aa408f3c7.png)

For our experimental setting we had a grid exactly like the one you would find in the original 2048 app, but it was written in text and played from the terminal as shown in Figure 2. Implementing our algorithm behind the UI/UX of the 2048 would look and function identical to the app.

<img width="459" alt="image" src="https://user-images.githubusercontent.com/94556358/171731148-c68c3ddc-689b-4463-a62b-f021c1ffdaf5.png">

Figure 2. A screenshot of how our 2048 implementation is played currently. In more detail, it is the output from calling our 2048 file (Stopped at incomplete board because time-constraints).


6. Conclusion
_____________________________________________________________________________________________________________________________________________________
We were surprised to see how significantly we could improve our original algorithm, and in addition to see how close we were to achieving the 100% win-rate in a game that is completely random. 

We are interested to learn how different the win-rate would look if instead implemented with some deep-learning or machine-learning implementation. The heuristics in our implementation sort if implement the proven strategies to win 2048, so would/could the machine learn this by teaching itself? If this was successfully accomplished, would pairing this agent with our current one improves or instead do worse?

Regarding improvements to our own algorithm, we think there are small bugs and improvements that can be made to achieve that 100% win-rate. We think we have all the heuristics necessary for this milestone, but the implementation can likely be optimized to reach the perfect win-rate. Finally, we believe implementing a UI/UX to the game would make it easier to debug ourselves, but also invite new people to be inspired by the world and potentially add to it. 

7. User Manual
_____________________________________________________________________________________________________________________________________________________

![image](https://user-images.githubusercontent.com/94556358/171731820-2473527c-00aa-4b77-a6fe-ab97635b580d.png)

Figure 1. A diagram showing how are methods were implemented and evaluated for Mark 3 (Our final implementation).

Figure 1 is used to illustrate how our implementation works using our functions and a quick summary of each. To see a more detailed breakdown of each function please see Table 2.

![image](https://user-images.githubusercontent.com/94556358/171731971-0cb5be10-b5b8-4911-b71b-a0860bbd5c8d.png)
![image](https://user-images.githubusercontent.com/94556358/171732061-453662a2-905d-4ade-8c43-650340408b4e.png)

To run our implementation just run our game file using python3 using command: python3 file.py and the board state at each move will be printed with a summary on conclusion of the game.
