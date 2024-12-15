import { createClient } from 'redis';

// Instantiate a redis client object
const client = createClient();

// Handle connection error event and log an error message to console
client.on('error', (err) => {
  console.log(`Redis client not connected to the server: ${err}`);
});

// Log connection success to the console
client.on('ready', () => {
  console.log('Redis client connected to the server');
});
