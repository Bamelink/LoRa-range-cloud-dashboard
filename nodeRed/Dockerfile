FROM nodered/node-red
# Install plugin for inserting data into mysql
RUN npm install node-red-node-mysql
RUN npm install node-red-node-geohash
# Copy your Node-RED project files into place
COPY flows.json /data