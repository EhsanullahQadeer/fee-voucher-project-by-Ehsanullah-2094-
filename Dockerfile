# Use an official Node.js runtime as the parent image
FROM node:20

# Set the working directory in the container
WORKDIR /usr/src/app


# Copy package.json and package-lock.json to the container
COPY package*.json ./

# Install application dependencies in the container
RUN npm install

# Copy the rest of the application source code from your local machine into the container
COPY . .

# Specify the command to run when the container starts
CMD [ "npm", "run", "start" ]

# Expose the port the app will run on
EXPOSE 5000
