# Prepare for Behaviour

## Intro

- Graduated from Dal with computer engineering degree
- Currently working in IBM as a pod lead where i will be leading teams iOS, android, QA, Backend
- I am mostly responsible  is **enabling** our team member to finish their work 
- Work on more**global scope features,** investigation for future stories so that we can continue making reasonable**technical decisions**
- **Mentoring** more junior developers, by help breaking down the story for them, pair programing and code review
- Other than the day to day kind of work, I have co-hosted**lunch and learn**sessions to share some of my personal experience, both technical and mentallys.
(Situation, Task, Action, Result)

## Copy and paste field

- This is when I was the iOS platform lead, login sheets are very common in a lot of apps hence 
- I was asked to create the login sheet that can open up everywhere in the app.
- As I was developing the app, I noticed that there is a lot of things that I can do to improve the user experience. Such as handle situation when user try to  paste more characters that it is allow. In iOS app, these are the things that are not natively supported out of the box, the app at the time were just disallow the content to be pasted if it is more than the limit. So I went in and implemented this new so called feature after chatting with the PO. Essentially, it will crop all the characters that is exceeding the limit.
- PO was very pleased with the result, and I eventually make this feature globally available through the app for all input boxes

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

## ask back

https://github.com/viraptor/reverse-interview/blob/master/README.md

## Resume Walk-Through

I am a xxx at xxx. In College, I studied xxx at xxx. Then I worked for xxx where I , Then I worked for xxx where I xxx. In my current job, I've accomplished xxx

- things that we want interview to be interested
- reArchitecture
- technical hobby

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

## Design problem

- Scope
- Key components
- identify issues
- Repair

## SOLID Principle + python funcitonal

Solid
https://medium.com/ios-expert-series-or-interview-series/solid-design-principle-using-swift-34bb1731cfb3
s: singer responsibility
o: open-closed : open for extension but not modification
l: liks something, interface can be replace with their subclass
i: interface serfration,  finer grain of abstraction
d: dependency inversion, High level modules should not depend on low level modules both should depend on Abstractions.


copy and paste
core data
open critisim


Question To Ask:
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
