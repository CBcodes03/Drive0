<div align="center">

# 🚗 Drive0

**A fast-paced car dodging game built entirely in Python**
*Dodge incoming cars, rack up points, and see how far you can go before it's game over.*

</div>

---

## 📖 About

**Drive0** is a 2D arcade-style car dodging game developed entirely in Python using the **Pygame** library. Navigate your car through a busy road, dodge oncoming traffic, and survive as long as possible. The game progressively gets harder — every 20 points, the level increases and enemy cars move faster, keeping you on your toes.

---

## 🎬 Demo

> **Watch the gameplay demo below:**

[![Drive0 Demo](https://img.youtube.com/vi/Y_8jZqBHh7g/maxresdefault.jpg)](https://www.youtube.com/watch?v=Y_8jZqBHh7g)

> 📌 *Replace `YOUR_VIDEO_ID` with your actual YouTube video ID (e.g. `dQw4w9WgXcQ`). The thumbnail will auto-load from YouTube.*

---

## ✨ Features

- 🚘 **Smooth car movement** using `W`, `A`, `S`, `D` controls
- 📈 **Progressive difficulty** — speed and level increase every 20 points
- 💥 **Crash detection** — the game ends when you collide with an enemy car
- 🔊 **Sound effects** for an immersive experience
- 🏆 **Score tracking** — your score is saved to `score.txt`
- 🖼️ **Custom image assets** for cars and road elements

---

## 🗂️ Project Structure

```
Drive0/
├── game.py              # Main game entry point
├── requirnments.txt     # Python dependencies
├── score.txt            # Persistent high score storage
├── howtopay.txt         # How-to-play instructions
├── img_assets/          # All game images (cars, road, UI)
├── sounds/              # Sound effects
└── crashed/             # Crash screen assets
```

---

## 🛠️ Prerequisites

- Python 3.x
- pip

---

## ⚙️ Installation

**1. Clone the repository**

```bash
git clone https://github.com/CBcodes03/Drive0.git
cd Drive0
```

**2. Install dependencies**

```bash
pip install -r requirnments.txt
```

> This installs `pygame`, the only external dependency.

---

## ▶️ Running the Game

```bash
python game.py
```

Or on systems where Python 3 is explicit:

```bash
python3 game.py
```

---

## 🎮 Controls

| Key | Action |
|-----|--------|
| `W` | Move Up |
| `S` | Move Down |
| `A` | Move Left |
| `D` | Move Right |

---

## 📊 Scoring & Leveling

| Milestone | Event |
|-----------|-------|
| +1 point | Successfully dodge an enemy car |
| Every 20 points | Level up — enemy car speed increases by 1 |

The game gets progressively harder as your score climbs — how far can you go?

---

## 🧰 Built With

| Technology | Purpose |
|------------|---------|
| [Python 3](https://www.python.org/) | Core language |
| [Pygame](https://www.pygame.org/) | Game rendering, input, and audio |

---

## 🤝 Contributing

Contributions, bug reports, and feature suggestions are welcome!

1. Fork the repository
2. Create your feature branch: `git checkout -b feature/my-feature`
3. Commit your changes: `git commit -m 'Add my feature'`
4. Push to the branch: `git push origin feature/my-feature`
5. Open a Pull Request

---

## ⭐ Show Your Support

If you enjoyed this project, please consider giving it a ⭐ on GitHub — it means a lot!

---

<div align="center">

Made with ❤️ and Python

</div>
