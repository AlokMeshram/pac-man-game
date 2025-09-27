# Pac-Man Game

A classic Pac-Man game implementation in Python using Pygame.

## Features

- **Simplified maze**: Clean, easier-to-navigate maze layout with blue walls
- **Pac-Man character**: Yellow circle with animated mouth that opens and closes
- **Accurate movement**: Precise grid-based movement with improved boundary detection
- **Keyboard movement**: Use arrow keys (↑ ↓ ← →) to move Pac-Man
- **Dot collection**: Collect white dots to increase your score (10 points each)
- **Power pellets**: Large yellow pellets that make ghosts vulnerable (50 points each)
- **Smart Ghost AI**: Four colorful ghosts with intelligent movement patterns
- **Ghost vulnerability**: When powered up, chase and eat vulnerable ghosts (200 points each)
- **Game over system**: Collision detection with restart functionality
- **Score system**: Multiple scoring opportunities with power-up bonuses
- **Smooth animation**: 60 FPS gameplay with fluid movement

## Installation

1. Make sure you have Python installed on your system
2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## How to Run

1. Navigate to the game directory:
   ```
   cd pacman_game
   ```
2. Run the game:
   ```
   python pacman.py
   ```

## Controls

- **Arrow Keys**: Move Pac-Man in the desired direction
- **R Key**: Restart the game (when game over)
- **ESC Key**: Quit the game (when game over)
- **Close Window**: Exit the game

## Game Mechanics

- **Movement**: Pac-Man starts at position (1,1) - use arrow keys to navigate
- **Walls**: Blue blocks that Pac-Man cannot move through
- **Dots**: White dots worth 10 points each
- **Power Pellets**: Large yellow pellets in corners worth 50 points each
- **Power Mode**: Eating a power pellet makes all ghosts vulnerable for 5 seconds
- **Ghost AI**: 
  - **Normal**: Ghosts chase Pac-Man with 70% accuracy, 30% random movement
  - **Vulnerable**: Ghosts turn dark blue and flee from Pac-Man
  - **Collision**: Touching a normal ghost = game over, eating a vulnerable ghost = 200 points
- **Game Over**: Press R to restart or ESC to quit
- **Scoring**: Regular dots (10), Power pellets (50), Vulnerable ghosts (200)

## Code Structure

- `PacMan` class: Handles Pac-Man's movement, animation, and rendering
- `Ghost` class: Placeholder ghost objects with different colors
- `Game` class: Main game loop, input handling, and rendering
- Maze layout defined as a 2D array with walls (1), empty spaces (0), and dots (2)

## Future Enhancements

This implementation now includes core Pac-Man gameplay! You can extend it further with:
- Multiple levels with increasing difficulty
- Sound effects and background music
- Fruit bonuses and special items
- High score system with persistent storage
- Improved ghost AI personalities (each ghost behaves differently)
- Tunnel warping between maze sides
- Lives system (multiple chances before game over)