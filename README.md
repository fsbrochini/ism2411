# ISM2411 — Python for Business

**Name:** Francisco Sanchez Brochini

**Semester:** Fall 2026

**Instructor:** Markum Reed

## About This Repo

This repository contains my weekly lab submissions for ISM2411.
Each folder corresponds to one module.

## Modules

- `week05/` — Conditionals: tiered discount calculator
- `week06/` — Loops: sales report with sum, average, max
- `week07/` — Functions: calculate_tax, apply_discount
- `week08/` — Git: first GitHub submission

## How to Run

Each script is standalone. Open a terminal and run:
```
python week07/functions.py
```


## Reflection

**1. Commit history**

```
7d6767a (HEAD -> main, origin/main, origin/HEAD) add README with course info and module list
ac0954f add module 7 functions: calculate_tax, apply_discount, final_price
4e483b0 add .gitignore for Python and OS files
43388c9 Initial commit
```

If I were to hire them, this would tell me that they work in clear chunks with each commit doing a single task and the commit message being very specific about what has changed. You can easily see what has happened in the project without having to open any files.

**2. How Git changes editing a script**

Prior to this module I would edit the script without committing, just hoping I wouldn't break anything. I didn't have an easy way to return to the working version. Now I would commit the working version and then make the changes. This means I can always return to a safe version. I will also be committing more frequently and with clear descriptions.

**3. Something I would add to .gitignore**

I will add `.venv/`, since I make use of Python virtual environments for some of my projects. This is a local virtual environment which could be hundreds of megabytes in size depending on how many packages are installed. It should not be added to the repo since anyone can recreate this on their own machine using a requirements file.