# Mech_Attack
# Mech Attack — README

This README will guide players through installing requirements, setting up a terminal environment (including Ubuntu for Windows users), installing Python 3, running the game, and basic gameplay info.

## 📦 Project Structure


mech_attack/
├── card_type.py
├── dice_roll.py
├── main.py
├── mech_tests.py
├── mech_type.py
├── README.md
├── stat_blocks.py
├── tests.py
├── utility_functions.py


## 🛠️ Requirements

* Python 3.10 or newer
* A terminal (Ubuntu recommended for Windows users)

---

## 🖥️ Installing a Terminal (Windows Users)

### Option A — **Windows Terminal + Ubuntu (WSL)**

1. Install **Windows Terminal** from the Microsoft Store.
2. Install **Ubuntu** from the Microsoft Store.
3. Open Ubuntu and let it finish its first‑time setup.
4. Create a username + password when prompted.

### Option B — **Just Windows CMD or PowerShell**

Python will work fine directly, but Linux instructions become simpler through WSL.

---

## 🐍 Installing Python 3

### Ubuntu/WSL

```bash
sudo apt update
sudo apt install python3 python3-pip -y
```

Check version:

```bash
python3 --version
```

### Windows / macOS

Download Python from:
[https://www.python.org/downloads/](https://www.python.org/downloads/)

Make sure **Add Python to PATH** is checked during install.

---

## 📥 Downloading the Game

### Clone via Git:

```bash
git clone <https://github.com/Wayne-Francis/mech_attack>
```

---

## ▶️ Running the Game

1. Open your terminal
2. Navigate to the project folder:

```bash
cd mech_attack
```

3. Run the game:

```bash
python3 main.py
```

(Windows may require `python main.py` instead)

---

## 🎮 How to Play

* The game launches in the terminal.
* Pick your mech: **Tank, Gunner, Bomber**.
* Your mech draws cards and fights enemy waves.
* Survive as long as possible.

---

# - Notes From Project Design -

I did not keep track of 100% of my time, but I believe I spent between 30–40 hours (roughly 5–8 hours a week, over about 5 weeks).

I put a huge amount of effort into this, and it was extremely satisfying to see the project grow from idea to finished V1.

Huge amount of learnings, including realizing that small features may break the code and that adding new features is a huge time investment.

I used AI a lot, but when asking ChatGPT for help, I 95% insisted on no code—just help with debugging, syntax, or whether an idea I had would work, and also for bouncing ideas off.

The biggest advantage I personally got from AI was asking it to draw up a roadmap for the project. When I started, I was full of enthusiasm until I sat down for the first night and realized I didn’t have a clue how to start and went into a little bit of a shame cycle. Here’s how I fixed that:

Wrote down in English on paper what my game was and what I wanted it to be.

Wrote down a skeleton of what I needed, i.e., dice functions, classes for both cards and mechs, shuffles, rounds, etc.

Took pictures of my notes and asked the AI to generate a roadmap using 1-hour chunks and what’s realistically possible (see Personal Project Road Map). This helped hugely… checking off boxes is fun.

Code the AI did end up helping me with:

The first summary function—I didn’t have time to perfectly line up lots of ====, so I took the first one and ran with it.

I used it to help me re-write the resolve card function. My first one, while it worked, was extremely hard to debug and expand, so I got a lot of guidance from that.

In some cases, I had it refactor a few chunks of my code to help with readability, but I insisted that logic not change (it may be janky, but it’s my jank!).

Oh yeah—I got it to write most of this README; I ain’t got time for that.

It may not be a fun game, but I am terribly proud of it. Good luck, Pilots!