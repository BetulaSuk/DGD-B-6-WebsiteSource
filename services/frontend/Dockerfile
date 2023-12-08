FROM node:20.10-alpine

WORKDIR /app

ENV PATH /app/node_modules/.bin:$PATH

RUN npm install @vue/cli -g

COPY package.json .
COPY package-lock.json .
COPY node_modules .

CMD ["npm", "run", "serve"]