import kue from 'kue';

// Create a Kue queue instance
const queue = kue.createQueue();

/**
 * Function to simulate sending a notification
 * @param {string} phoneNumber - The recipient's phone number
 * @param {string} message - The notification message
 */
function sendNotification(phoneNumber, message) {
  console.log(
    `Sending notification to ${phoneNumber}, with message: ${message}`
  );
}

// Process jobs from the `push_notification_code` queue
queue.process('push_notification_code', (job, done) => {
  const { phoneNumber, message } = job.data;
  sendNotification(phoneNumber, message);
  done();
});
