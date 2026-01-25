# Automated Text-to-Video System - Module 1: LLM Setup

## 📌 Project Information
**Module:** 1 - Story to Scene Breakdown  
**Member:** M.Zaheer (1A)  
**Task:** LLM Setup with Qwen 2.5 1.5B  
**Model Used:** Qwen 2.5 1.5B (via Ollama)  
**Status:** ✅ COMPLETED AND WORKING  

## 🎯 Task Requirements & Status

| Requirement | Status | Implementation |
|------------|--------|----------------|
| **1. Choose LLM Model** | ✅ | Selected **Qwen 2.5 1.5B** from given options |
| **2. Install via Ollama** | ✅ | Ollama v0.14.3 + Qwen model installed |
| **3. Write code that sends text to model** | ✅ | `llm_scene_creator.py` sends stories to Qwen |
| **4. Test with different stories** | ✅ | 3+ story types successfully tested |
| **5. Deliverable: Working model** | ✅ | System breaks stories into 5 scenes |

## 🚀 Quick Start

### Prerequisites
1. **Ollama** installed from [ollama.com](https://ollama.com)
2. **Qwen 2.5 1.5B** model downloaded
3. **Python 3.8+**

### Installation
```bash
# 1. Install Ollama (download from website)
# 2. Download Qwen model
ollama pull qwen2.5:1.5b

# 3. No Python packages needed! Uses subprocess