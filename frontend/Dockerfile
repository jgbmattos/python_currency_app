# Imagem de Origem
FROM node:13-alpine

WORKDIR /app

ENV PATH /app/node_modules/.bin:$PATH

COPY package.json ./
COPY package-lock.json ./
RUN npm install --silent
RUN npm install react-scripts@3.4.3 -g --silent

# add app
COPY . ./

CMD ["npm", "start"]