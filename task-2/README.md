# 🎮 CodSoft AI Internship – Task 2: Tic Tac Toe AI

This is my **Tic Tac Toe AI project** for the CodSoft AI Internship (AI Domain).  
You play as **X** and the AI plays as **O**. The AI uses the **Minimax algorithm** to always make the best moves, so it’s basically unbeatable.

---

## 🧩 Features
- Human vs AI gameplay in the terminal  
- AI uses **Minimax algorithm** for optimal moves  
- Detects wins, draws, and invalid moves  
- Simple text-based interface  
- Lightweight and beginner-friendly  

---

## ⚙️ Technologies Used
- **Python 3.x** (3.12+ recommended)  
- **Minimax algorithm** for decision-making  
- Can run in **VS Code, PowerShell, or any Python IDE**  

---


## Reference
This project was structured based on the following video:  
[YouTube Video Title](https://www.youtube.com/watch?v=trKjYdBASyQ)

---


## 🚀 How to Run
1. Clone or download this repository.  
2. Open a terminal and navigate to the project folder:
   ```bash 
3. Run this command in terminal:
   python chatbot.py


SAMPLE INTERACTION:
=== Tic Tac Toe AI Using Minimax ===
You = X, AI = O



  |   |
---------
  |   |
---------
  |   |
---------



Enter your move (row[0-2] and column[0-2]): 0 1


  | X |
---------
  |   |
---------
  |   |
---------



AI is making a move...



O | X |  
---------
  |   |
---------
  |   |
---------



Enter your move (row[0-2] and column[0-2]): 0 1

Invalid move! Try again.


Enter your move (row[0-2] and column[0-2]): 2 1


O | X |
---------
  |   |
---------
  | X |
---------



AI is making a move...



O | X |
---------
  | O |
---------
  | X |
---------



Enter your move (row[0-2] and column[0-2]): 1 0


O | X |
---------
X | O |
---------
  | X |
---------



AI is making a move...



O | X | O
---------
X | O |
---------
  | X |
---------



Enter your move (row[0-2] and column[0-2]): 2 2


O | X | O
---------
X | O |
---------
  | X | X
---------



AI is making a move...



O | X | O
---------
X | O |
---------
O | X | X
---------



AI wins!