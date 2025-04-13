


# Step 3: TypeScript with "transpilation"


## npm

```bash
# this is how a the "package.json" file
# is created in the current folder
# => the "-y" is to force it to say "yes to all prompt"
npm init -y

# install the package "typescript" in the "node_module" folder
# => this will update the the "package.json" file
npm install --save-dev tsx
```

## node

```bash
# this will create the "tsconfig.json" file
npx tsc --init

# this will run the "index.ts" file directly
npx tsx index.ts
```



