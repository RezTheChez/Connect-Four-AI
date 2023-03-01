### Understanding components to the AI
- How minimax works
  - Game trees
    - Terminal vs non-terminal nodes
    - Minimizing vs maximizing turn 
- Evaluation function: win, lose, draw
  - What to do when there are too many moves to evaluate?
    - Search depth
    - Heuristic evaluation function: how do we know how close we are to winning?

### Implementation plan
1. Game logic
2. Design a heuristic
3. Write a heuristic evaluation function 
4. Implement minimax
5. Implement alpha beta pruning
6. Optimize winning ability
- Experiment with different heuristics
- Prolong and shorten game with score +/- depth, in case of loses or wins
- Anticipate and prevent direct losing moves
- Other edge cases
7. Optimize compute speed 
- Experiment with search depths
- Ordered exploration (center first, sides later)
- Transposition table - save positions in fixed size hash table - recent + upper bound results
8. Add-ons
- Leaderboard
- Progress/evaluation bar
- Difficulty settings
- Website to display GitHub work or this game

### Resources 
- https://roadtolarissa.com/connect-4-ai-how-it-works/
- http://blog.gamesolver.org/solving-connect-four/01-introduction/
- Helpful pseudocode: https://www.geeksforgeeks.org/finding-optimal-move-in-tic-tac-toe-using-minimax-algorithm-in-game-theory/, https://www.geeksforgeeks.org/minimax-algorithm-in-game-theory-set-4-alpha-beta-pruning/?ref=rp 
