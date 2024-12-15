#!/usr/bin/node
import { createClient, print } from 'redis';
import { promisify } from 'util';

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

/**
 * Function to set a new value in Redis
 * @param {string} schoolName - The key to set in Redis
 * @param {string} value - The value to associate with the key
 */
function setNewSchool(schoolName, value) {
  client.set(schoolName, value, print);
}

// Promisify the `get` method for async/await
const getAsync = promisify(client.get).bind(client);

/**
 * Async function to retrieve and log the value of a key from Redis
 * @param {string} schoolName - The key to retrieve from Redis
 */
async function displaySchoolValue(schoolName) {
  try {
    const result = await getAsync(schoolName);
    console.log(result);
  } catch (err) {
    console.error(err);
  }
}

(async () => {
  await displaySchoolValue('Holberton');
  setNewSchool('HolbertonSanFrancisco', '100');
  await displaySchoolValue('HolbertonSanFrancisco');
})();
