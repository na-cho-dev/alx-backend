import kue from 'kue';

// Array of jobs to be queued
const jobs = [
  {
    phoneNumber: '4153518780',
    message: 'This is the code 1234 to verify your account',
  },
  {
    phoneNumber: '4153518781',
    message: 'This is the code 4562 to verify your account',
  },
  {
    phoneNumber: '4153518743',
    message: 'This is the code 4321 to verify your account',
  },
  {
    phoneNumber: '4153538781',
    message: 'This is the code 4562 to verify your account',
  },
  {
    phoneNumber: '4153118782',
    message: 'This is the code 4321 to verify your account',
  },
  {
    phoneNumber: '4153718781',
    message: 'This is the code 4562 to verify your account',
  },
  {
    phoneNumber: '4159518782',
    message: 'This is the code 4321 to verify your account',
  },
  {
    phoneNumber: '4158718781',
    message: 'This is the code 4562 to verify your account',
  },
  {
    phoneNumber: '4153818782',
    message: 'This is the code 4321 to verify your account',
  },
  {
    phoneNumber: '4154318781',
    message: 'This is the code 4562 to verify your account',
  },
  {
    phoneNumber: '4151218782',
    message: 'This is the code 4321 to verify your account',
  },
];

// Create a Kue queue instance
const queue = kue.createQueue();

// Loop through the array of jobs and queue each job
jobs.forEach((jobData) => {
  const job = queue.create('push_notification_code_2', jobData).save((err) => {
    if (err) {
      console.error(`Notification job failed to create: ${err}`);
    } else {
      console.log(`Notification job created: ${job.id}`);
    }
  });

  // Listen for job completion
  job.on('complete', () => {
    console.log(`Notification job ${job.id} completed`);
  });

  // Listen for job failure
  job.on('failed', (err) => {
    console.log(`Notification job ${job.id} failed: ${err}`);
  });

  // Listen for job progress
  job.on('progress', (progress) => {
    console.log(`Notification job ${job.id} ${progress}% complete`);
  });
});
