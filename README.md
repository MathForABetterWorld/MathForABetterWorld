# Database Team!

## Links
- https://github.com/ChrisWilhelm/MathForABetterWorld/issues
- https://mathforabetterworld.slack.com/
- https://www.prisma.io/docs/concepts/components/prisma-schema/data-model

## Getting Started:
```
git clone https://github.com/ChrisWilhelm/MathForABetterWorld
cd MathForABetterWorld

echo "DATABASE_URL='postgresql://prisma:prisma@127.0.0.1:5432/math-for-better-world-local'">>./server/.env
```


## Development and Testing:
```
cd server
yarn install
# start docker daemon
yarn run dev
# test all the routes to make sure they work!!
```


## Best practices, for making a feature branch:
```
git checkout -b name_feature_description       
git push -u origin name_feature_description  
```