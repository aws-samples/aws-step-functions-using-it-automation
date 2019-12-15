# IT Operations Automation using AWS Step functions

## Overview

"Everything fails all the time" - Werner Wogels

Everything fails all the time and our systems should be ready to respond to such kind of events automatically. To automate the entire incident management you need a workflow that gets triggered when an incident happens. Let's take a simple usecase.

## A simple automation usecase

I want an auto-remediation (self-healing) solution for incidents like opening of SSH port, low disk space, or when a public access is given to a S3 bucket


The workflow will look like this.


![](./images/Incident-work-flow.png)

Note: Manual approval is a optinal step.


We need some kind of work flow engine that can keep track of various states, re-try things and also have a capability of manual intevention when required. AWS Step function is a service that perfectly fits this usecase.

AWS Step Functions provides auditable automation of routine deployments, upgrades, installations, and migrations. You can use Step Functions to easily automate recurring tasks such as patch management, infrastructure selection, and data synchronization, and Step Functions will automatically scale, respond to timeouts, and retry failed tasks.


We can change the above workflow to below architecture using AWS Step functions.

![](./images/StepfunctionsArchitecture.png)


## About the repo
This code repsoitory will help you do create a workflow engine template that you can re-use.

ITAutomationWorkFlow.yaml will create following object in your environment

1. State Machine: It will create a state machine depcting above flow. 

State machine details are there in stepfunction.json

2. EvaluateRequest lambda function: A Lambda function to evaluate the incident and take a decision on the next steps. It will decide whether an automation process is required or a manual approval is required or nothing has to be done.

3. OpenIncident lambda function: A Lambda function to open the incident ticket.

4. ResolveIncident lambda function:
A Lambda to resolve the incident. For example, closign the SSH port or removing the public access for S3 bucket.

5. PrepareMessage lambda function: A Lambda function to close ticket and prepare the message/email for Operations manager. 

## License

This library is licensed under the MIT-0 License. See the LICENSE file.
