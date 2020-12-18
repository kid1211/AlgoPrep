# Prepare for Behaviour

<!-- TOC -->autoauto- [Prepare for Behaviour](#prepare-for-behaviour)auto    - [Intro](#intro)auto    - [SOLID Principal](#solid-principal)auto    - [STAR Interviewing Technique](#star-interviewing-technique)auto    - [Questions](#questions)auto        - [Soft skill in Persuasion](#soft-skill-in-persuasion)auto            - [Accessibility vs QA](#accessibility-vs-qa)auto        - [Problem solving](#problem-solving)auto            - [Git Bisect](#git-bisect)auto        - [Get it done x2](#get-it-done-x2)auto            - [BMO](#bmo)auto            - [Branching strategy](#branching-strategy)auto        - [Time management](#time-management)auto        - [Regret](#regret)auto        - [Motivated others](#motivated-others)auto        - [Hard/Cool Projects](#hardcool-projects)auto        - [Trade-off](#trade-off)auto    - [Question To Ask:](#question-to-ask)autoauto<!-- /TOC -->

## Intro

- Graduated from Dal with Computer engineering degree, and recently become a Professional Engineer
- Currently working at IBM as a pod lead for an Airline project, leading an team of iOS, android QA and backend team.
- Main responsibility is to enable our team member to deliver their work
- secondary, building reusable component and mentoring junior developers
- breaking down the story into steps, pair programing and code review to ensure the code follow good practices 
- co-host on lunch and learn session sharing my personal experience and technical knowledge, some times presuade others to hop on the same boat

## SOLID Principal

s: singer responsibility
o: open-closed : open for extension but not modification
l: liks something, interface can be replace with their subclass
i: interface serfration,  finer grain of abstraction
d: dependency inversion, High level modules should not depend on low level modules both should depend on Abstractions.

## STAR Interviewing Technique

- Situation or Task: Describe the situation that you were in or the task that you needed to accomplish. You must describe a specific event or situation, not a generalized description of what you have done in the past. Be sure to give enough detail for the interviewer to understand.
- Action you took: Describe the action you took and be sure to keep the focus on you. Even if you are discussing a group project or effort, describe what you did -- not the efforts of the team. Don't tell what you might do, tell what you did
- Results you achieved. What happened? How did the event end? What did you accomplish? What did you learn? 

## Questions

### Soft skill in Persuasion

- Describe a situation in which you were able to use persuasion to successfully convince someone to see things your way.
- Tell me about a time when you had to use your presentation skills to influence someone's opinion

#### Accessibility vs QA

- Task: composite key, flight search block. QA tool rely on Appium
- Action: Convince QA all the works we do is meaningless without user satisfaction, and 100% is impossible, and provided regex
- Result: Win win, test accessibility and the component

### Problem solving

- Give me a specific example of a time when you used good judgment and logic in solving a problem (no debugging tool)
- give me an example of a time when you used your fact-finding skills to solve a problem. (thing not necessary true)

#### Git Bisect

- Task: After upgrade to the latest version of the app, keep on crashing. Debugging is not possible because dependency and xcode version
- Action: Read the Crashlytics and pin point potential issue, and use git bisect
- Result: Fix the issue, later integrated a data migration manager based on the resources and experience

### Get it done x2

- Tell me about a time when you had to go above and beyond the call of duty in order to get a job done (dbaas?)
- Give me an example of when you showed initiative and took the lead
- Describe a time when you anticipated potential problems and developed preventive measures

#### BMO

- Task: We were asked to implement a maintenance page for a bank. And as most banking system, the backend is pretty legacy. 
- Action: As a front end developer, I read through their limited documentation and combine with my knowledge in web hosting, I was able to take over this task from our architect and finish this. It was using terminal plus FTP to manage the system, and there is revers proxy and load manger that needs to conffigured. I had a full documentation listed detailer what steps needs to be taken and plan b for different situations. And updated their old shell script in order for this to work. 
- Results: As far as i know, there is no issue has found and I also receive a recognition from the architect (IBM Manager's choice award, Unit and get it done)

#### Branching strategy

- Task: I was supporting DevOps on a part time basis, I wouldn't claim to be an expert in this.(Happen to have a wide range of knowledge in web that helps.) I found an issue that is created by the wrong naming convention. And unfortunately we were using a relatively lower tier BitBucket cloud.
- Action: Created a script that identify the wrongly named branch and its owner. Inform the owner, and added archive tags and delete the branch after they confirm. Also added rules in their pre-hook script
- Results: The build machine hasn't been getting the same problem since, and the branch names are much more manageable.

### Time management

- urgent, release bug, triage
- in sprint story based on road map
- refactor list, i will be looking for things that will yield the highest benefit

### Regret

- Situation: We just start using core data, no documentation on what is the best practice,
- Action: implemented a parent-child relationship, but it is not needed. TOO FOCUS ON the Tech
- Result: Always the go to person for anything core data, luckily refactored that part.

### Motivated others

- Give me an example of a time when you motivated others

- Task: COVID
- Action: Game and freedom for explore code, not just day to day
- Results; devliver everythign on time and lunch and learn

### Hard/Cool Projects

- Task: During Job Hunting after I just graduated, I need to apply to a lot of job, and each company have their own platform, unlike now. And I found copy and paste such a tedious job
- Action: Builded a website that has a resume template format and text fields are lockable to prevent accidental edit, and also a copy button right next to it.
- Results: seems working fine, should have make it into a chrome plugin, and add functionality to auto fill. But now there is more and more password manager, seems obsolete.

### Trade-off

- Building the user profile login/logout feature, it is very tempting to use signelton and we were initially.
- Refactored it to a dependency injection design pattern
- much more testable, and also it can be swap to something else which it does now.
- it is a lot of work 

## Question To Ask:

1. What are the core atrributes that you are looking for in an ideal canadiate?
2. What is the hightlight of your day to day works?
3. What do you see as the most challenging aspect of this job?
4. Are there opportunities for professional development?  If so, what do those look like?
5. What is the next step?
