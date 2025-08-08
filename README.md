# SongAgent

**🎵 Compose Music with Natural Language | 🤖 LLM-powered Music Generation Interface | 🚀 Lower the Barrier to AI Music Creation**

[![Project License](https://img.shields.io/badge/license-[License]-blue.svg)](LICENSE)
[![Python Version](https://img.shields.io/badge/python-3.10%2B-blue)]()

## ✨ Introduction

`SongAgent` is an innovative demo project designed to...  **TODO**

1. **🎯 Intelligent User Profiling:** The LLM engages in natural dialogue with the user to understand their musical preferences (such as genre, mood, tempo, instrument preferences), creative intentions (e.g., "write a song for my cute cat" or "compose a sad folk song"), and skill level (beginner or professional musician), dynamically building a user profile.
2. **🗣️ Natural Language Command Parsing:** Users can describe the music they want using everyday language (e.g., "some relaxing jazz with a sax solo, slower tempo" or "speed up the melody just generated, add drums, make it more intense"). The LLM accurately parses these vague or complex requests.
3. **🔧 Atomic Operation Instruction Generation:** The parsed user intent is transformed by the LLM into a series of precise, executable **atomic operation instructions**. These instructions are low-level commands or parameter combinations that underlying music generation models (such as MusicLM, Riffusion, MAGNeT, or custom models) can directly understand and process.
4. **🎼 Seamless Driving of Music Generation Models:** The generated atomic instructions are sent to one or more backend music generation models for execution, and the resulting music fragments are returned to the user.
5. **⏱️ Iterative Creation:** Users can give feedback on the generated results ("make the drums stronger", "change the chord progression"), the LLM understands the feedback and generates new operation instructions, forming a creative loop.

**Core Idea:** Abstract complex and professional music generation parameters and operations, allowing users to **focus on creative expression** without needing to understand the technical details of underlying models or tedious parameter adjustments. The LLM acts as a music-savvy, tech-savvy "intelligent assistant" and "translator".

## 🖥 Showcase (Screenshots / GIFs / Video)

**TODO**

*  Screenshot
*  Video
*  Audio sample links


## 🚀 Getting Started

### Installation

1. **Clone the repository:**
    ```bash
    git clone https://github.com/tuteng0915/SongAgent.git
    cd SongAgent
    ```

2. **(Recommended) Create and activate virtual environment:**
    ```bash
    conda env -n songagent python=3.10
    conda activate songagent
    ```

3. **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    pip install transformers==4.51.0
    ```

### Run Demo

```bash
python main.py
```

