import { createClient, print } from 'redis';

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

/**
 * Function to retrieve and log the value of a key from Redis
 * @param {string} schoolName - The key to retrieve from Redis
 */
function displaySchoolValue(schoolName) {
  client.get(schoolName, (err, result) => {
    if (err) console.log(err);
    else console.log(result);
  });
}

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
