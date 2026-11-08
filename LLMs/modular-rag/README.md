
# Modular RAG

## TL;DR

The research happen "inside a loop"

ex of request: `I need a research about X.`

Here assuming a "Modular RAG based researcher skill/subagent".

### The loop
- <u>**STEP 1**</u>:
  - do research about X
- <u>**STEP 2**</u>:
  - now challenge the results from `STEP 1` with a counter-research
    - think of it as an "adversarial approach"
- <u>**STEP 3**</u>:
  - compare the results from `STEP 1` and `STEP 2`
  - consider a `confidence level/score` from those results
  - `IF`
    - the `confidence level/score` is "high enough"
    - `THEN`
      - `STOP` and return the results to the caller
      - the final `confidence level/score` can also be shared
  - `ELSE`
    - `REPEAT` from `STEP 1`
    - a maximum number of `REPEAT` must be setup (ex: 5)
    - `IF`
      - there is no more `REPEAT` left
      - and <u>**the confidence level/score is still too low**</u>
      - `THEN`
        - it <u>**MUST**</u> clearly reply to the caller `"I don't know"`.
          - this is will drastically the reduce/cancel the risk of hallucinations.

### Diagram

![modular-rag.svg](./diagrams/modular-rag.svg)

## Official Research Paper

- https://arxiv.org/html/2407.21059v1

## Legends

![img/1.1-modular-rag---legend-1.png)](img/1.1-modular-rag---legend-1.png)
![img/1.2-modular-rag---legend-2.png)](img/1.2-modular-rag---legend-2.png)

## Naive RAG

![img/2-modular-rag---naive-rag.png.png)](img/2-modular-rag---naive-rag.png.png)

## Advanced RAG

![img/3-modular-rag---advanced-rag.png.png)](img/3-modular-rag---advanced-rag.png.png)

## Loop
### "Iterative" Modular RAG

![img/4-modular-rag---iterative.png.png)](img/4-modular-rag---iterative.png.png)

### "Recursive" Modular RAG

![img/5-modular-rag---recursive.png)](img/5-modular-rag---recursive.png)

### "Adaptive" Modular RAG

![img/6-modular-rag---adaptive.png)](img/6-modular-rag---adaptive.png)

## "Full" Modular RAG

![img/8-modular-rag---full-modular.png](img/8-modular-rag---full-modular.png)
