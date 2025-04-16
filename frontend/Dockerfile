
# React Dockerfile
FROM node:18
WORKDIR /app
COPY package.json ./
RUN npm install
COPY . .
RUN npm start
CMD ["npm", "start"]
