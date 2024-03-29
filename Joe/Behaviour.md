<!-- vscode-markdown-toc -->
* 1. [Intro](#Intro)
* 2. [SOLID Principal](#SOLIDPrincipal)
* 3. [STAR Interviewing Technique](#STARInterviewingTechnique)
* 4. [Questions](#Questions)
	* 4.1. [Soft skill in Persuasion](#SoftskillinPersuasion)
		* 4.1.1. [Accessibility vs QA](#AccessibilityvsQA)
	* 4.2. [Problem solving](#Problemsolving)
		* 4.2.1. [Git Bisect](#GitBisect)
	* 4.3. [Get it done x2](#Getitdonex2)
		* 4.3.1. [BMO](#BMO)
		* 4.3.2. [Branching strategy](#Branchingstrategy)
	* 4.4. [Time management](#Timemanagement)
	* 4.5. [Regret](#Regret)
	* 4.6. [Motivated others](#Motivatedothers)
	* 4.7. [Hard/Cool Projects](#HardCoolProjects)
	* 4.8. [Trade-off](#Trade-off)
* 5. [Question To Ask:](#QuestionToAsk:)

<!-- vscode-markdown-toc-config
	numbering=true
	autoSave=true
	/vscode-markdown-toc-config -->
<!-- /vscode-markdown-toc -->

##  1. <a name='Intro'></a>Intro

- Graduated from Dal with Computer engineering degree, and recently become a Professional Engineer
- Currently working at IBM as a pod lead for an Airline project, leading a team of iOS, android, QA and backend(nodejs, graphql).
- Main responsibility is to enable our team member to deliver their work
- as well as, building reusable component and mentoring junior developers
- breaking down the story into steps, pair programing and code review to ensure the code follow good practices 
- other than the day-to-day, co-host on lunch and learn session sharing my personal experience and technical knowledge.
- [Only when asked!] IBM provide the flexibility for you to switch roles and projects as long as you are able to bring value. I think after the experimenting, I wanna do more coding.

##  2. <a name='SOLIDPrincipal'></a>SOLID Principal

- s: single responsibility
- o: open-closed : open for extension but not modification
- l: liks something, interface can be replace with their subclass
- i: interface segregation, finer grain of abstraction
- d: dependency inversion, High level modules should not depend on low level modules both should depend on Abstractions.
- https://towardsdatascience.com/5-principles-to-write-solid-code-examples-in-python-9062272e6bdc

## 2.2 OOP

- Encapsulation – Encapsulation is capturing data and keeping it safely and securely from outside interfaces.
- Inheritance- This is the process by which a class can be derived from a base class with all features of base class and some of its own. This increases code reusability.
- Polymorphism- This is the ability to exist in various forms. For example an operator can be <b>overloaded</b> so as to add two integer numbers and two floats.
- Abstraction- The ability to represent data at a very conceptual level without any details.
##  3. <a name='STARInterviewingTechnique'></a>STAR Interviewing Technique

- Situation or Task: Describe the situation that you were in or the task that you needed to accomplish. You must describe a specific event or situation, not a generalized description of what you have done in the past. Be sure to give enough detail for the interviewer to understand.
- Action you took: Describe the action you took and be sure to keep the focus on you. Even if you are discussing a group project or effort, describe what you did -- not the efforts of the team. Don't tell what you might do, tell what you did
- Results you achieved. What happened? How did the event end? What did you accomplish? What did you learn? 

##  4. <a name='Questions'></a>Questions

###  4.1. <a name='SoftskillinPersuasion'></a>Soft skill in Persuasion

- Describe a situation in which you were able to use persuasion to successfully convince someone to see things your way.
- Tell me about a time when you had to use your presentation skills to influence someone's opinion

####  4.1.1. <a name='AccessibilityvsQA'></a>Accessibility vs QA

- Task: composite key, flight search block. QA tool rely on Appium
- Action: (Everyone has their own prespective) Convince QA all the works we do is meaningless without user satisfaction, and 100% is impossible, and provided regex
- Result: Win win, test accessibility and the component

###  4.2. <a name='Problemsolving'></a>Problem solving

- Give me a specific example of a time when you used good judgment and logic in solving a problem (no debugging tool)
- give me an example of a time when you used your fact-finding skills to solve a problem. (thing not necessary true)

####  4.2.1. <a name='GitBisect'></a>Git Bisect

- Task: After upgrade to the latest version of the app, keep on crashing. Debugging is not possible because dependency and xcode version
- Action: Read the Crashlytics and pin point potential issue, and use git bisect
- Result: Fix the issue, later integrated a data migration manager based on the resources and experience

###  4.3. <a name='Getitdonex2'></a>Get it done x2

- Tell me about a time when you had to go above and beyond the call of duty in order to get a job done (dbaas?)
- Give me an example of when you showed initiative and took the lead
- Describe a time when you anticipated potential problems and developed preventive measures

####  4.3.1. <a name='BMO'></a>BMO

- Task: We were asked to implement a maintenance page for a bank. Most banking system, the backend is pretty legacy. 
- Action: As a front end developer, I read through their limited documentation and combine with my knowledge in web hosting, I was able to take over this task from our architect and get it done. It was (essentially hosting a web folder) using FTP to manage the system, and there is revers proxy and load manger that needs to configured. I had a full documentation listed detailer what steps needs to be taken and plan b for different situations. And provided a shell script to automate some of the work. 
- Results: As far as i know, there is no issue has found and I also receive a recognition from the architect (IBM Manager's choice award, Unit and get it done)

####  4.3.2. <a name='Branchingstrategy'></a>Branching strategy

- Task: I was supporting DevOps on a part time basis, I wouldn't claim to be an expert in this.(Happen to have a wide range of knowledge in web that helps.) I found a frequent crash that is created by the wrong naming convention. And unfortunately we were using a relatively lower tier BitBucket cloud.
- Action: Created a script that identify the wrongly named branch and its owner. Inform the owner, and added archive tags and delete the branch after they confirm. Also added rules in their pre-hook script
- Results: The build machine hasn't been getting the same problem since, and the branch names are much more manageable.

###  4.4. <a name='Timemanagement'></a>Time management

- urgent, release bug, triage
- in sprint story based on road map
- refactor list, i will be looking for things that will yield the highest benefit

###  4.5. <a name='Regret'></a>Regret

- Situation: We just start using core data, no documentation on what is the best practice, profile + payment, passenger
- Action: implemented a parent-child relationship, but it is not needed. TOO FOCUS ON the Tech, once you invest too much it is hard to let go
- Result: Always the go to person for anything core data, luckily refactored that part.

###  4.6. <a name='Motivatedothers'></a>Motivated others

- Give me an example of a time when you motivated others

- Task: COVID
- Action: Game and freedom for explore code, not just day to day. Organized a among us session.
- Results; deliver everything on time and lunch and learn

###  4.7. <a name='HardCoolProjects'></a>Hard/Cool Projects

- Task: During Job Hunting after I just graduated, I need to apply to a lot of job, and each company have their own platform, unlike now. And I found copy and paste such a tedious job
- Action: Builded a website that has a resume template format and text fields are lockable to prevent accidental edit, and also a copy button right next to it.
- Results: seems working fine, should have make it into a chrome plugin, and add functionality to auto fill. But now there is more and more password manager, seems obsolete.

###  4.8. <a name='Trade-off'></a>Trade-off

- Building the user profile login/logout feature, it is very tempting to use singleton(feature is global, and transitional of screen) and we were using it initially.
- Refactored it to a dependency injection design pattern
- much more testable, and also it can be swap to something else which it does now.
- it is a lot of work 

##  5. <a name='QuestionToAsk:'></a>Question To Ask:

1. What are the core attributes that you are looking for in an ideal candidate?
2. What is the highlight of your day to day works?
3. What do you see as the most challenging aspect of this job?
4. Are there opportunities for professional development?  If so, what do those look like?
5. What is the next step?

##  6. <a name='CodingInterview:'></a>Coding Interview:

- Ask clarifying questions
	- *reprhase the question*
	- should this be done in place
	- can we make any *assumptions* about the inputs? 
		- RED FLAG if you didn't ask
		- intergers are positive?
		- array not empty
		- all input is safe
	- do we care more about *performance or saving memory*
- Analyze various solutions and tradeoffs
- plan solution with pseudocode
- implement solution
- test
	- check optional
	- check syntax name

## 7. <a name='SwiftAnswer:'></a>Swift Answer:

more data structure: https://dennis-xlc.gitbooks.io/swift-algorithms-data-structures/content/chapter7.html
Ans: https://github.com/raywenderlich/swift-algorithm-club

FB:
- https://www.facebookrecruiting.com/portal/interview_prep_hub?c=399863738457834
- https://www.facebook.com/notes/10158791573512200/
- https://engineering.fb.com/category/ios/
- https://www.facebook.com/notes/10158791572847200/



## 8. <a name='LinkedList:'></a>Linked List:
reversing:
[NONON]next should point to current (next.next = current) 
update current next, (current.next = previous) [also update prev]

In my loop, i shoudl only myself!!!!