# Pull Node.js image
FROM node:20

# Set working directory
WORKDIR /usr/src/app

# Copy code
COPY ./front-end-nextjs .

# Install packages
RUN npm install

# Make build
RUN npm run build

# Start app server
CMD [ "npm", "start"]