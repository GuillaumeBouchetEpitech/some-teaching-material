

# Step 2: TypeScript with tsx

## npm

```bash
# this is how a the "package.json" file
# is created in the current folder
# => the "-y" is to force it to say "yes to all prompt"
npm init -y

# install the package "typescript" in the "node_module" folder
# => this will update the the "package.json" file
npm install --save-dev typescript
```

## node

```bash
# this will create the "tsconfig.json" file
npx tsc --init

# this will generate the javascript file "index.js" from
# the typescript file "index.ts"
npx tsc

# this is how to run the javascript file "index.js"
node index.js
```



