# 🧩 Mech Attack – Personal Project Roadmap

A simple turn-based card game playable in the command line.
Designed for steady, low-stress progress (~4–5 hrs/week).

---

## ✅ Core Files
- [x] `card_type.py` – Card and CardType classes (complete)
- [x] `mech.py` – Mech base class + subclasses
- [x] `game.py` – Main game loop and CLI interface (this is just main)
- [x] `utils.py` – Helper functions (shuffle, dice rolls, etc.)

---

## 📅 Week 1: Build the Foundations

- [x] Review `Card` and `CardType` classes (comment + clean)
- [x] Finish `Mech` base class + `Tank`, `Gunner`, `Bomber` subclasses
- [x] Add `__str__()` or `display_stats()` for Mechs
- [x] Implement `draw_card()` and `add_to_hand()` methods
- [x] Write utility functions:
  - [x] `roll_d4()`
  - [x] `roll_d6()`
  - [x] `shuffle_deck(deck)`
- [x] Create simple unit tests for utilities

> 🎯 *Goal:* You can create a mech, shuffle a deck, and draw cards.

---


## 📅 Week 2: Game Mechanics
- [x] Implement `boss_ai()`:
  - If HP ≤ 4 → 60% Repair  
  - If player shielded last turn → 60% Repair / 40% Attack  
  - Else → 70% Attack / 30% Shield  
  - Never Repair at max HP
- [x] Write `resolve_turn()` logic:
  - Compare speed rolls
  - Apply card effects (attack, shield, repair)
- [x] Test turn resolution updates HP correctly
- [x] Implement discard pile + deck reshuffle or “take 1 dmg” option when empty

> 🎯 *Goal:* Two mechs can face off for a few turns successfully.

---

## 📅 Week 3: Game Loop + Interface
- [x] Write startup sequence:
  - [x] Display welcome message + mech selection
- [x] Implement full game loop:
  - [x] 5 enemies, increasing HP
  - [x] Turns with draw → choose → roll → resolve
- [x] Display game info each turn:
  - [x] Player/enemy stats
  - [ ] Hand + deck count
  - [ ] Last card played
- [x] Implement level-up logic after wins:
  - [x] +1 chosen stat
  - [x] +1 chosen card
  - [x] Restore HP to max
  - [x] Clear Shields

> 🎯 *Goal:* The complete game loop runs end-to-end (rough but functional).

---

## 📅 Week 4: Polish + Testing
- [x] Improve text formatting for readability
- [x] Playtest multiple full runs
- [x] Fix edge cases:
  - [x] Repair at max HP
  - [x] Empty deck handling
  - [x] Simultaneous KO?
- [x] Add win/loss summary screen
- [x] Refactor functions into clean modules
- [x] Final test run + comment cleanup

> 🎯 *Goal:* Fully playable, stable, and nicely formatted CLI game.

---

## 💡 Optional Extras (Future)
- [ ] Difficulty settings (enemy AI or HP curve)
- [ ] Save/load progress (JSON)
- [ ] Achievements or scoring system
- [ ] Colored CLI output (via `colorama` or `rich`)
- [ ] Sound or simple ASCII effects

---

### 🧘 Tips
- Each checkbox ≈ 1 focused hour.
- End each session on a working milestone (never stop mid-bug).
- Commit after every small success — progress over perfection.
- Don’t worry about “beautiful” code until Week 4 polish!

---

### 🌟 Final Goal
A functional, replayable **text-based mech card battler** that demonstrates:
- Object-oriented design (classes, inheritance)
- Functional decomposition (utility functions)
- Basic AI decision-making
- Game loop and state management
