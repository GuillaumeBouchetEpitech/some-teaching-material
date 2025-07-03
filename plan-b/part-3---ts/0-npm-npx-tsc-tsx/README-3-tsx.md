


# TypeScript without "compilation"

## Install with npm

```bash
# this is how a the "package.json" file
# is created in the current folder
# => the "-y" is to force it to say "yes to all prompt"
npm init -y

# install the package "typescript" in the "node_module" folder
# => this will update the the "package.json" file
npm install --save-dev typescript tsx
```

## run with node

```bash
# this will create the "tsconfig.json" file
npx tsc --init

# this will run the "index.ts" file directly
npx tsx index.ts
```

## Graph

---
### Graph step 0: starting point

```mermaid
flowchart LR

  classDef executable fill:#632
  classDef command fill:#400
  classDef file fill:#326

  subgraph nodejs
    node:::executable
    npm:::executable
    npx:::executable
  end

  subgraph folder
    index.ts["index.ts
    (file)"]:::file
  end

```

```bash
.
└── index.ts
```

---

### Graph step 1: setup the package.json

```mermaid
flowchart LR

  classDef executable fill:#632
  classDef command fill:#400
  classDef file fill:#326

  subgraph nodejs
    node:::executable
    npm:::executable
    npx:::executable
  end

  npm_init["npm --init -y"]:::command

  subgraph folder
    index.ts["index.ts
    (file)"]:::file
    package.json["package.json
    (file)"]:::file
  end

  npm --> npm_init -. "this create
  the package.json" .-> package.json

```

```bash
.
├── index.ts
└── package.json
```

---
### Graph step 2: install packages

```mermaid
flowchart

  classDef executable fill:#632
  classDef command fill:#400
  classDef file fill:#326
  classDef folder fill:#440

  subgraph nodejs
    node:::executable
    npm:::executable
    npx:::executable
  end

  npm_install["npm install --save typescript tsx"]:::command

  npm --> npm_install

  npm_install -- "this installed
  the 'tsc' and 'tsx' packages" --> node_modules

  npm_install -. "the package.json file
  list the newly
  installed packages" .-> package.json

  subgraph folder
    index.ts["index.ts
    (file)"]:::file
    package.json["package.json
    (file)"]:::file
    node_modules["node_modules/
    (folder)"]:::folder
    node_modules --> tsc:::file
    node_modules --> tsx:::file
  end

```

```bash
.
├── index.ts
├── package.json
└── node_modules
    ├── typescript
    └── tsx
```

---

### Graph step 3: setup the typescript config

```mermaid
flowchart

  classDef executable fill:#632
  classDef command fill:#400
  classDef file fill:#326
  classDef folder fill:#440

  subgraph nodejs
    node:::executable
    npm:::executable
    npx:::executable
  end

  npx_tsc["npx tsc --init"]:::command

  npx --> npx_tsc

  npx_tsc -- "this setup the
  tsconfig.json file" ---> tsconfig.json

  subgraph folder
    index.ts["index.ts
    (file)"]:::file
    package.json["package.json
    (file)"]:::file
    tsconfig.json["tsconfig.json
    (file)"]:::file
    node_modules["node_modules/
    (folder)"]:::folder
    node_modules --> tsc:::file
    node_modules --> tsx:::file
  end

```

```bash
.
├── index.ts
├── package.json
├── node_modules
│   ├── typescript
│   └── tsx
└── tsconfig.json
```


---

### Graph step 4: run the typescript program

```mermaid
flowchart

  classDef executable fill:#632
  classDef command fill:#400
  classDef file fill:#326
  classDef folder fill:#440

  subgraph nodejs
    node:::executable
    npm:::executable
    npx:::executable
  end

  npx_tsx["npx tsx index.ts"]:::command

  npx --> npx_tsx

  npx_tsx -- "this runs the
  typescript file" ---> index.ts

  subgraph folder
    index.ts["index.ts
    (file)"]:::file
    package.json["package.json
    (file)"]:::file
    tsconfig.json["tsconfig.json
    (file)"]:::file
    node_modules["node_modules/
    (folder)"]:::folder
    node_modules --> tsc:::file
    node_modules --> tsx:::file
  end

```

```bash
.
├── index.ts
├── package.json
├── node_modules
│   ├── typescript
│   └── tsx
└── tsconfig.json
```



