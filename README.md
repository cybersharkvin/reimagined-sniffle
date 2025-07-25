# reimagined-sniffle
GBNF programmatic extraction

## Usage

Run `generate_gbnf.py` to build the grammar from the annotated functions. The
tests rely on `todo.gbnf` being up to date.

```bash
python generate_gbnf.py
pytest
```

The grammar structure follows the same conventions as those found in
[llama.cpp's grammar examples](https://github.com/ggml-org/llama.cpp/tree/master/grammars).


# Context: GenAI Security

Since Grammar-Constrained Decoding is an external security control (it has to be) it's not so much a function of the LLM as it is a function of the loader.

To clarify, an LLM doesn't execute code or perform actions, it just generates text. Any real-world effect depends entirely on the external systems that process the generated text. Typically, agentic workflows, tool interactions, and data extraction involve structured outputs. You're already implicitly enforcing some data validation or typing at that stage.

With GCD, you explicitly provide a grammar as an additional parameter during inference time. At the token sampling stage, tokens not conforming to this grammar are removed entirely from the pool. The model isn't being trained or prompted; instead it's actively constrained, making invalid token selections impossible.

Rather than relying on prompts to encourage the model to use only predefined functions (and hoping it doesn't invent new ones), grammars ensure the model literally cannot output invalid tokens or hallucinate tools/functions.

In practical application, grammars are typically generated programmatically from type hints, docstrings, or schema definitions. Your application dynamically supplies the appropriate grammar with each inference call. And since grammar support already exists across most popular loaders like llama.cpp & vLLM, integration is pretty straightforward. 

Interestingly, since grammars significantly enhance the efficiency and safety of smaller models (1–3 billion parameters), you can get safe agentic behavior without heavyweight validation steps.

To sum up:

- Defensive prompting *asks* the model to behave.
- Grammar-Constrained Decoding *forces* it to.

Importantly, GCD doesn't reduce your LLM's capabilities. Since grammar constraints are applied at inference, you can dynamically filter outputs without wasting tokens, hitting tokens limits, or incurring extra latency.
