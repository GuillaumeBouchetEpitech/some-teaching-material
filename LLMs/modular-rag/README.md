
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

```mermaid

flowchart

  subgraph modular_rag["Iterative Modular RAG"]
    direction TD

    actual_start@{ shape: sm-circ, label: "Small start" }
    style actual_start fill:#000,stroke:#f00,stroke-width:2px;

    research["User request:
    - Research
    - Debugging
    - etc."]
    style research text-align:left,color:#fff,fill:#448;

    subgraph main_loop["Modular RAG loop"]

      step1(["`**Step 1**
      research the subject
      use 1..3 researcher subagents`"])
      style step1 text-align:left,color:#fff,fill:#848;

      step2(["`**Step 2**
      counter research the subject
      use 1..3 researcher subagents`"])
      style step2 text-align:left,color:#fff,fill:#848;

      step3{{"`**Step 3**
      judge the results`"}}
      style step3 text-align:left,color:#fff,fill:#884;

    end
    style main_loop color:#fff,fill:#444;

    summarize["`**Summarize**
    - TL;DR
    - What was done
    - complete results
    - sources/references`"]
    style summarize text-align:left,color:#fff,fill:#484;

    low_confidence["`**Low Confidence**
    must clearly say:
    -> ''__I don't know.__''`"]
    style low_confidence text-align:left,color:#ccc,fill:#844;

    stop@{ shape: framed-circle, label: "Small stop" }
    style stop fill:#000,stroke:#f00,stroke-width:2px;

    actual_start --> research --> main_loop

    step1 ==> step2 ==> step3
    step3 -->|"Low confidence
    retry from Step 1
    (up to 5 retries)"| step1

    main_loop -->|"Low confidence
    no retries left"| low_confidence
    summarize & low_confidence --> stop
    main_loop -->|"High confidence"| summarize

    linkStyle 0,1 stroke:#66f,stroke-width:2px,font-size:14pt;
    linkStyle 2,3 stroke:#f6f,stroke-width:2px,font-size:14pt;
    linkStyle 4,5,7 stroke:#ff6,stroke-width:2px,color:red,font-size:14pt;
    linkStyle 6,8 stroke:#6f6,stroke-width:2px,color:white,font-size:14pt;

  end
  style modular_rag fill:#333;


```

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
