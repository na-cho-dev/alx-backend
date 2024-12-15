import { expect } from 'chai';
import { after, afterEach, before, describe, it } from 'mocha';
import kue from 'kue';

import createPushNotificationsJobs from './8-job.js';

// Create a kue instance
const queue = kue.createQueue();

before(() => {
  queue.testMode.enter();
});

afterEach(() => {
  queue.testMode.clear();
});

after(() => {
  queue.testMode.exit();
});

const jobs = [
  {
    name: 'Leykun',
    origin: 'Ethiopia',
  },
  {
    name: 'Fred',
    origin: 'Ghana',
  },
];

describe('createPushNotificationsJobs', () => {
  it('display an error message if jobs is not an array', () => {
    expect(() => createPushNotificationsJobs(jobs[0], queue)).to.throw();
  });
  it('create two new jobs to the queue', () => {
    createPushNotificationsJobs(jobs, queue);
    expect(queue.testMode.jobs.length).to.equal(2);
    expect(queue.testMode.jobs[0].type).to.equal('notification');
    expect(queue.testMode.jobs[0].data).to.eql({
      name: 'Leykun',
      origin: 'Ethiopia',
    });
    expect(queue.testMode.jobs[1].data).to.eql({
      name: 'Fred',
      origin: 'Ghana',
    });
  });
});
