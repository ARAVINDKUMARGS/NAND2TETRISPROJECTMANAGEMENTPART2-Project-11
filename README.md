# NAND2TETRISPROJECTMANAGEMENTPART2-Project-11
# NAND2TETRISPROJECTMANAGEMENTPART2-Project-11

## Project 11 – CPU Emulator & Assembler

**Project Code:** PROJECT11
**Course:** Build a Modern Computer from First Principles (Nand2Tetris Part II)
**Institution:** Hebrew University of Jerusalem

---

## Overview

Project 11 focuses on **hardware-level emulation**, including the **Hack CPU emulator** and the **assembler**. The assembler converts `.asm` assembly files into binary `.hack` machine code, while the CPU emulator executes Hack instructions, allowing you to **run programs directly on the Hack platform**.

This project is essential for testing the output of compiled VM code and user programs from previous projects.

---

## Objectives

* Implement an **assembler** that translates Hack assembly (`.asm`) into binary machine code (`.hack`).
* Implement a **CPU emulator** capable of executing Hack machine instructions.
* Test arithmetic, logical, memory, and control flow operations using sample programs.
* Debug and validate programs produced by the Jack compiler (Projects 7 & 8) and OS routines (Projects 9 & 10).

---

## Folder Structure

```
Project11/
│── README.md
│── src/
│   ├── Assembler.java
│   └── CPUEmulator.java
│── examples/
│   ├── Add.asm
│   ├── Max.asm
│   └── Rect.asm
│── output/
│   ├── Add.hack
│   ├── Max.hack
│   └── Rect.hack
│── docs/
│   └── CPUEmulator_Guide.pdf
```

---

## Getting Started

### Step 1: Compile Assembler & Emulator

```bash
cd Project11/src
javac Assembler.java CPUEmulator.java
```

### Step 2: Assemble Hack Program

```bash
java Assembler ../examples/Add.asm
```

* Output: `Add.hack` in the `output/` folder.

### Step 3: Run CPU Emulator

```bash
java CPUEmulator ../output/Add.hack
```

* Observe program execution step-by-step.
* Use emulator debugging tools to inspect memory, registers, and stack.

---

## Supported Features

### Assembler

* Converts symbolic Hack assembly to binary machine code.
* Supports A-instructions (`@value`) and C-instructions (`dest=comp;jump`).
* Handles labels and variables.

### CPU Emulator

* Emulates the Hack CPU instruction set.
* Supports memory segments: `RAM`, `ROM`, `stack`.
* Executes arithmetic, logical, and control flow instructions.

### Example

**Add.asm:**

```asm
@2
D=A
@3
D=D+A
@0
M=D
```

**Output Add.hack (binary):**

```
0000000000000010
1110110000010000
0000000000000011
1110000010010000
0000000000000000
1110001100001000
```

**Behavior:** Stores the sum of 2 + 3 in RAM[0].

---

## Notes

* CPU Emulator is crucial for testing VM code output from Projects 8–10.
* Provides detailed debugging support for memory, stack, and instruction flow.
* Must verify all compiled programs for correctness before proceeding to Project 12 (Final Integration).

---

## Author

**Aravind Kumar GS**
Email: `aravindkumar06062006@gmail.com`

---

## License

Educational purposes only. Do not distribute or claim as your own work.
