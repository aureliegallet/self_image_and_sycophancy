## Local

### First run
1. Download Ollama
2. `ollama serve`
3. `ollama --version`
4. `ollama pull qwen3:4b` 
5. Open new Terminal
6. `ollama run qwen3:4b`
7. Type /bye to exit ollama chat interface
8. `ollama stop qwen3:4b`
9. Run code

### All subsequent runs
1. `ollama serve`
2. Open new Terminal
3. `ollama run qwen3:4b`
4. Type /bye to exit ollama chat interface
5. `ollama stop qwen3:4b`
6. Run code

## Cloud
1. Set API key using [.env Guide](configure_env.md)
2. `ollama serve`
3. Run code