# Project 11 – Jack Compiler: Code Generation

**Course:** Build a Modern Computer from First Principles (Nand2Tetris Part II)  
**Institution:** Hebrew University of Jerusalem  
**Author:** Aravind Kumar GS  
**Email:** aravindkumar06062006@gmail.com  
**License:** MIT (Educational purposes only)

---

## Overview

Project 11 completes the **Jack compiler** by implementing **code generation**. The compiler translates Jack programs into **VM code** for the Hack platform.  

Key features include:

- Handling **variables**: local, argument, static, field  
- Handling **expressions**: arithmetic, logical, unary  
- Handling **control flow**: `if`, `while`  
- Handling **objects**: construction (`new`), method calls, manipulation  
- Handling **arrays**: element access and assignment  
- Producing **VM code** that can be executed using the supplied Hack VM Emulator

This project builds on Project 10, which performed **syntax analysis** and generated XML from Jack programs.

---

## Source Files

- **JackCompiler.java** or **JackCompiler.py** (main file)  
  - Contains the **main method/function** that runs the compiler
- Other source files for:
  - Tokenization  
  - Parsing  
  - VM code generation

---

## Execution Helper File

You must include **one** of the following:

1. **Makefile**  
   - Automates compilation and execution of your compiler  
2. **lang.txt**  
   - A plain text file with **one or two terms**:  
     - First term: programming language (`java`, `python2.7`, `python3`, etc.)  
     - Optional second term: `debug` (to show error messages)  
   - Example:
     ```
     python3 debug
     ```

---

## Submission Instructions

1. Place **all source files** in a single folder.  
2. Include **lang.txt** or **makefile**.  
3. Zip all files at the **top level** (no folders) as:
