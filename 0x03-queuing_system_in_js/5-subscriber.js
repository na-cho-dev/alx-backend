import { createClient } from 'redis';

const client = createClient();

client.on('error', (err) => {
  console.log(`Redis client not connected to the server: ${err}`);
});

client.on('connect', () => {
  console.log('Redis client connected to the server');
});

// Subscribe to the "holberton school channel"
client.subscribe('holberton school channel');

// Handle incoming messages
client.on('message', (channel, message) => {
  console.log(message);

  // Unsubscribe and quit if the message is "KILL_SERVER"
  if (message === 'KILL_SERVER') {
    client.unsubscribe();
    client.quit();
  }
});
