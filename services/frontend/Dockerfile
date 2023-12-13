FROM node:20.10-alpine

WORKDIR /app

ENV PATH /app/node_modules/.bin:$PATH

RUN npm config set registry https://registry.npmmirror.com && npm install @vue/cli -g

COPY package.json .
COPY package-lock.json .

RUN npm install

CMD ["npm", "run", "serve"]
