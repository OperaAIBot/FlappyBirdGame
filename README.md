# FlappyBirdGame

*A single-file Flappy Bird clone generated in five iterations  
by **Ollama Granite-Code 20 B** (2025-06-05) and archived read-only (2025-06-27).*

---

<details>
<summary>Table of Contents</summary>

1. [Introduction](#introduction)  
2. [Key Features](#key-features)  
3. [Quick Start](#quick-start)  
4. [Gameplay](#gameplay)  
5. [Project Structure](#project-structure)  
6. [AI Generation Process](#ai-generation-process)  
7. [Customisation Guide](#customisation-guide)  
8. [License](#license)  
9. [Contribution](#contribution)  
10. [References](#references)  
11. [Appendix A – AI Prompt Templates](#appendix-a--ai-prompt-templates)
</details>

---

## 1. Introduction <a id="introduction"></a>

**FlappyBirdGame** is a lightweight 2-D casual game built with  
[**Pygame**](https://www.pygame.org/). Press **Space** to make the bird jump through
pipe gaps and collect points. Because all logic, physics, and rendering live in
one script, it is perfect for educational or demo purposes.

---

## 2. Key Features <a id="key-features"></a>

- **Minimal dependencies**  
  - Python ≥ 3.8  
  - Pygame 2.x → `pip install pygame`
- **Compact architecture**  
  - ≈ 4 KB, single file, one `main()` defines the whole loop
- **Instant tuning**  
  - Change constants such as `GRAVITY`, `PIPE_GAP`, `WIDTH`, `HEIGHT`

---

## 3. Quick Start <a id="quick-start"></a>

```bash
# 1 – Install dependency
python -m pip install -U pygame

# 2 – Clone repository
git clone https://github.com/OperaAIBot/FlappyBirdGame.git
cd FlappyBirdGame

# 3 – Run
python flappy_bird.py
```

> **Tip** Use a virtual environment:  
> `python -m venv venv && source venv/bin/activate`

---

## 4. Gameplay <a id="gameplay"></a>

| Key           | Action                               |
| ------------- | ------------------------------------ |
| Space         | Bird jumps upward (`Bird.jump()`)    |
| Window close  | Exit game (`pygame.QUIT`)            |

*Score* = frame count ÷ 100 (≈ elapsed seconds).  
Game-over triggers when the bird hits a pipe or screen border;
the final score prints to the console.

---

## 5. Project Structure <a id="project-structure"></a>

```text
FlappyBirdGame/
 ├─ flappy_bird.py   # full game logic
 └─ LICENSE          # GNU GPL v3.0
```

No external images or sounds – only shapes drawn with Pygame primitives.

---

## 6. AI Generation Process <a id="ai-generation-process"></a>

Code produced locally with **Ollama** running *IBM Granite-Code 20 B*  
in five commits (`AI_GEN_25.06.05 – Iteration 1‒5`).  
A final commit added GPL headers.  
The repo was **archived read-only on 2025-06-27**.

---

## 7. Customisation Guide <a id="customisation-guide"></a>

- **Difficulty** → tweak `GRAVITY`, `JUMP_STRENGTH`, `PIPE_GAP`, `PIPE_SPACING`
- **Resolution** → change `WIDTH`, `HEIGHT`; sizes auto-scale
- **Visuals** → swap `pygame.draw.*` calls for sprite images (`pygame.image.load`)
- **AI experiments** → plug in Q-Learning, NEAT, etc.

---

## 8. License <a id="license"></a>

Released under the **GNU General Public License v3.0**.  
Any derivative must remain GPL-v3. See `LICENSE` for details.

---

## Appendix A – AI Prompt Templates <a id="appendix-a--ai-prompt-templates"></a>

### A.1 Partial-Fix **System** Prompt
```text
You are an expert Python and Pygame developer.
Fix the specific error in the provided code with minimal changes.

CRITICAL RULES:
- Provide ONLY the complete corrected Python code
- Use a single ```python code block
- No explanations or text outside the code block
- Fix only what's necessary to resolve the reported error
- Maintain the project goal: {self.project_goal}
```

### A.2 Partial-Fix **User** Prompt Template
```text
PROJECT GOAL: {self.project_goal}

Fix ONLY the specific error in the Python code for '{filename}'.
Do NOT rewrite the entire code. Only modify the minimal parts necessary.

ERROR TO FIX:
{error_message}

{error_line_info}

CURRENT CODE:
```python
{code}
```

INSTRUCTIONS:
You must respond with ONLY the corrected code in a single code block.
Fix only what is necessary to resolve the error.
Do not include explanations, markdown formatting outside the code block, or any other text.

Provide the complete corrected code:
```

### A.3 Full-Rewrite **System** Prompt
```text
You are an expert Python and Pygame developer.
Fix the provided code to achieve: {self.project_goal}

REQUIREMENTS:
- Provide complete, working Python code
- Use a single ```python code block
- No explanations or text outside the code block
- Fix all errors and ensure the code runs properly
```

### A.4 Full-Rewrite **User** Prompt Template
```text
PROJECT GOAL: {self.project_goal}

Fix the Python code for '{filename}' to resolve the error and achieve the project goal.
{error_context_for_ai}

Current code:
```python
{code}
```

Provide ONLY the complete corrected Python code in a single code block. No explanations.
```

### A.5 New-Code **System** Prompt
```text
You are an expert Python developer.
Create code to achieve: {self.project_goal}

REQUIREMENTS:
- Start with: # filename: chosen_filename.py
- Provide complete Python code in ```python code blocks
- No explanations outside the code block
- Ensure the code achieves the project goal
```

### A.6 New-Code **User** Prompt Template
```text
PROJECT GOAL: {self.project_goal}

Current project state:
Files: {files}
Directory structure: {structure}

Create complete Python code from scratch to achieve the project goal.

At the VERY BEGINNING of your response, include: # filename: chosen_filename.py
Then provide ONLY Python code in a code block, no explanations.
```

### A.7 Initial Project Goal
```text
Create a functional Flappy Bird game using pygame with a bird that can jump and basic physics.
The game must use only basic geometric shapes (e.g., rectangles, circles) drawn with pygame.draw functions
for all visual elements including the bird, pipes, and background.
No external image files or other asset files should be loaded or used.
```
