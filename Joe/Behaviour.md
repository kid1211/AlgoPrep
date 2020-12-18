# Prepare for Behaviour

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

Accessibility vs QA
regex 
what did i actually talk
QA?:


Snack bar



### Problem solving

- Give me a specific example of a time when you used good judgment and logic in solving a problem (no debugging tool)
- give me an example of a time when you used your fact-finding skills to solve a problem. (thing not neccssary true)

user randomly sign out, big problem for airline

Crashes - stuff


### Get it done x2

- Tell me about a time when you had to go above and beyond the call of duty in order to get a job done (dbaas?)
- Give me an example of when you showed initiative and took the lead
- Describe a time when you anticipated potential problems and developed preventive measures
DevOps?

arrange meeting, talk to the admin and get it done

late night, 
code refactor??

### Time management

- Tell me about a time when you had too many things to do and you were required to prioritize your tasks (pending first)

urgent, release bug, triage
in sprint story based on road map
refactor list, i will be looking for things that will yield the highest benefit

### Motivated others

- Give me an example of a time when you motivated others

### something i regret



## Over engineering core data, fix it after

- It was very early phase of the project and we were just starting to use core data which is a custom database wrapper in iOS
- There isn't a set rules or clear documentation on what is the right architectture of the database schemas. At the time most people were just have one entity, and save the value that get back from the server as it is, even if the response from server was a object, they will stringify it and save it. However, my collegue and mhyself think there could be a better way to do this. As you may know I was responseible for doing the login and profile services. 
- So i decided to seperate the passenger data and payment data to a different table entity, and the main profile will have a parent child relationship. At the time, it sounds like a good idea, but there isn't anyone else doign this even on the internet, so the resources was very limited. The bigger problem is that this implmentation is very different from the rest of the app, and others won't be able to understand what is goign on easily. and that causes a big problme.
- Refactor to the previous one, and not over engineering it, if there isnt'a clear benefit, cuz even though it helps on sorting and get count and so, but there isnt' too much data to make such an impact

## Snack bar

- I was asked to create a snack bar, which is an idea borrow from andoid, where it shows up from the bottom, attaching to views, you can swipe it to dismiss
- When we first have this story, there is no clear idea where it will be used, and we were only asked to implent this on a page for QA to test, and just develop it so that it is easy to use globally
- Because it is lack of the clear idea where it would be used, we significantly understimated the effort, when it was used, there are tons of problem, it was orgianlly attached to a speicific view, but the snack bar is a hint for the user. So it happens a lot when user are navigating through pages, and that causes a problem when the bar is attaching to the view controller. So we later rework the snack bar and make it attach to the tab bar. When there is no tab bar, it will have to attach to the rootview controller, but there is safe area in iOS that you shouldn't put any interactive item. And also when transisstioning in pages, there is existing footer that is block, and we will have to raise it and so on.
-
## Jenkins and automation, git blame

- It is kind of rare to have automation on mobile apps, as far as i know. We don't actually have a deveop guy so to speak, we only have one person who volunteer to take care of this on going development, where it detect PR merge, and make a build and send the link to slack for QA to test
- I help to maintain the build machine and jenkins on AWS, set up security groups and stuff. Problem is that it ran out of memory very fast, so i created scripts to restart, also created scripts to clean up wrong naming of branchs

## 2 - Hard/Cool Projects

- Hard/cool
- Central
- Technical depth

- Challenges? Architecture? Tradeoffs? mistaks? successes? Motivations?
- Teamwork, leadership? Conflicts?

- Be passionate
- Be knowledgeable
- Be a good teammate

## other

- weakness
- 3 year plan
- why jump?

## Question To Ask:
1. What are the core atrributes that you are looking for in an ideal canadiate?
2. What is the hightlight of your day to day works?
3. What do you see as the most challenging aspect of this job?
4. Are there opportunities for professional development?  If so, what do those look like?
5. What is the next step?




Python Functional
- use functions
* avoid side-effects
* first-class functions
* laziness
* immutability
 
library
- functools
	* partial
		* def add1(x): return add(1,x) -> add1 = partial(add, 1)
	* reduce
- iterators
	* it = iter(xs) -> generate on demand, laziness
	* next(it) and yield

// comment MaxSum




#### initiative

was just a front end dve, go above an beyond to figure out how it work
wrote a script for them
and also a full documentation on what ouwl happen if a or B

front end