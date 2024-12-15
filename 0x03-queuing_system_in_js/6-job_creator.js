import kue from 'kue';

// Create a Kue queue instance
const queue = kue.createQueue();

// Define job data
const jobData = {
  phoneNumber: '4153518780',
  message: 'This is the code to verify your account',
};

// Create a job in the `push_notification_code` queue
const job = queue.create('push_notification_code', jobData).save((err) => {
  if (err) {
    console.log('Error creating job:', err);
  } else {
    console.log(`Notification job created: ${job.id}`);
  }
});

// Handle job completion
job.on('complete', () => {
  console.log('Notification job completed');
});

// Handle job failure
job.on('failed', () => {
  console.log('Notification job failed');
});
