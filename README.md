# Pac-Man Clone 🎮

A simple **Pac-Man clone** built using **C++ and OpenGL (GLUT)** as part of a **Computer Graphics Mini Project**.
This project demonstrates **2D graphics, transformations, animation, clipping, and collision detection** concepts.

---

## 🚀 Features

* Pac-Man character with mouth animation.
* Arrow key controls (↑ ↓ ← →) for movement.
* Maze boundaries (walls).
* Collectible dots.
* Smooth animation with double buffering.
* Expandable to include **ghost AI, scoring, and levels**.

---

## 🛠️ Technologies Used

* **Language:** C++
* **Graphics Library:** OpenGL + GLUT / FreeGLUT
* **IDE/Editor:** VS Code (or Code::Blocks, Dev-C++)

---

## 📂 Project Structure

```
PacMan-Clone/
│── pacman.cpp      # Main source code
│── README.md       # Documentation
│── assets/         # (Optional) textures, images for extension
```

---

## ⚡ How to Run

### Windows

1. Install **MinGW** or any C++ compiler.
2. Install **FreeGLUT** and link OpenGL libraries.
3. Compile with:

   ```bash
   g++ pacman.cpp -o pacman -lopengl32 -lfreeglut -lglu32
   ```
4. Run:

   ```bash
   ./pacman
   ```

### Linux (Ubuntu/Debian)

1. Install OpenGL libraries:

   ```bash
   sudo apt-get install freeglut3-dev
   ```
2. Compile:

   ```bash
   g++ pacman.cpp -o pacman -lGL -lGLU -lglut
   ```
3. Run:

   ```bash
   ./pacman
   ```

---

## 🎮 Controls

* **Arrow Keys** → Move Pac-Man
* **Esc / Close Window** → Exit

---

## 📖 Computer Graphics Concepts Covered

* **2D Primitives:** Circles, arcs, lines (Pac-Man, dots, maze).
* **Transformations:** Translation (movement), rotation (mouth animation).
* **Clipping:** Pac-Man restricted to maze boundaries.
* **Animation:** Smooth frame updates with `glutTimerFunc`.
* **Collision Detection:** Dot eating, wall boundaries.

---

## 🌟 Future Improvements

* Add multiple dots & score counter.
* Add ghosts with AI (random/BFS/A*).
* Power-ups (Pac-Man eats ghosts).
* Levels with increasing difficulty.
* Background music / sound effects.

---

## 👨‍💻 Author

Developed as a **Computer Graphics Mini Project** for academic purposes.
You are free to use, modify, and expand this project.

---
