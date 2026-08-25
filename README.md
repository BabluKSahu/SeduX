# SeduX

Realtime AI assistant foundation for voice, avatar, emotion, task, home, and device workflows.

## First Build Slice

The repository currently contains an executable, dependency-free control plane. It exposes the gateway health contract and reports the eight planned backend services without requiring model weights, API keys, a GPU, or external infrastructure.

Run the tests:

```bash
python -m unittest discover -s tests -v
```

Run the gateway:

```bash
python -m services.gateway.main
```

Then inspect `http://127.0.0.1:8080/health` or `http://127.0.0.1:8080/services`.

The complete dependency-aware backlog is in [IMPLEMENTATION_TODO.md](IMPLEMENTATION_TODO.md). The build guide remains the product and architecture reference; unchecked items are intentionally not represented as completed functionality.
