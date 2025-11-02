# 🧩 Mech Attack – Personal Project Roadmap

A simple turn-based card game playable in the command line.
Designed for steady, low-stress progress (~4–5 hrs/week).

---

## ✅ Core Files
- [x] `card_type.py` – Card and CardType classes (complete)
- [ ] `mech.py` – Mech base class + subclasses
- [ ] `game.py` – Main game loop and CLI interface
- [ ] `utils.py` – Helper functions (shuffle, dice rolls, etc.)

---

## 📅 Week 1: Build the Foundations

- [x] Review `Card` and `CardType` classes (comment + clean)
- [x] Finish `Mech` base class + `Tank`, `Gunner`, `Bomber` subclasses
- [x] Add `__str__()` or `display_stats()` for Mechs
- [x] Implement `draw_card()` and `add_to_hand()` methods
- [ ] Write utility functions:
  - [ ] `roll_d4()`
  - [ ] `roll_d6()`
  - [ ] `shuffle_deck(deck)`
- [ ] Create simple unit tests for utilities

> 🎯 *Goal:* You can create a mech, shuffle a deck, and draw cards.

---

## 📅 Week 2: Game Mechanics
- [ ] Implement `boss_ai()`:
  - If HP ≤ 4 → 60% Repair  
  - If player shielded last turn → 60% Repair / 40% Attack  
  - Else → 70% Attack / 30% Shield  
  - Never Repair at max HP
- [ ] Write `resolve_turn()` logic:
  - Compare speed rolls
  - Apply card effects (attack, shield, repair)
- [ ] Test turn resolution updates HP correctly
- [ ] Implement discard pile + deck reshuffle or “take 1 dmg” option when empty

> 🎯 *Goal:* Two mechs can face off for a few turns successfully.

---

## 📅 Week 3: Game Loop + Interface
- [ ] Write startup sequence:
  - [ ] Display welcome message + mech selection
- [ ] Implement full game loop:
  - [ ] 5 enemies, increasing HP
  - [ ] Turns with draw → choose → roll → resolve
- [ ] Display game info each turn:
  - [ ] Player/enemy stats
  - [ ] Hand + deck count
  - [ ] Last card played
- [ ] Implement level-up logic after wins:
  - [ ] +1 random stat
  - [ ] +1 card
  - [ ] Restore HP to max

> 🎯 *Goal:* The complete game loop runs end-to-end (rough but functional).

---

## 📅 Week 4: Polish + Testing
- [ ] Improve text formatting for readability
- [ ] Playtest multiple full runs
- [ ] Fix edge cases:
  - [ ] Repair at max HP
  - [ ] Empty deck handling
  - [ ] Simultaneous KO?
- [ ] Add win/loss summary screen
- [ ] Refactor functions into clean modules
- [ ] Final test run + comment cleanup

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
