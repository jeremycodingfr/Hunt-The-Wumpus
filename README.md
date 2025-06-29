# Hunt The Wumpus

A Python remake of the classic 1970s game **Hunt the Wumpus**, where you explore a dangerous cave system and try to survive long enough to slay the mysterious Wumpus.

## 🎮 Game Overview

You are a hunter exploring a cave made up of connected rooms. Somewhere in this cave lurks the Wumpus. Your goal is to find and shoot the Wumpus without falling into a bottomless pit or getting dragged away by bats.

As you explore, you'll get clues that help you sense nearby dangers:

* **You see a bloody circle beneath you – the Wumpus is near.**
* **"You feel a draft nearby."** – there's a pit nearby.
* **"You hear the squeaking of bats nearby."** – bats are in a nearby room.

Make your moves carefully, as one wrong step can end your adventure.

## 🐍 Technologies Used

* Python 

## 🛠️ How to Install and Run

1. Clone the Repository:

   ```
   git clone https://github.com/jeremycodingfr/Hunt-The-Wumpus.git
   cd Hunt-The-Wumpus
   ```

2. Run the Game:

   ```
   python main.py
   ```

Make sure you have Python 3 installed on your system.

## 🎯 How to Play

* Start in a random cave room.
* Choose a connected room to move to.
* Watch for clues and avoid dangers.
* You only get one arrow to shoot the Wumpus.
* Survive and win, or die trying.

## 📁 File Structure

```
Hunt-The-Wumpus/
├── main.py          # Main game loop
├── map.py           # Cave generation and room connections
├── player.py        # Player state and actions
├── wumpus.py        # Game mechanics and hazards
└── README.md        # This file
```

## 👤 Author

Created by **Jeremy Nguyen**
GitHub: [jeremycodingfr](https://github.com/jeremycodingfr)

## 📄 License

This project is licensed under the MIT License.
