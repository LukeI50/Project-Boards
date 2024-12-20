# Project Overview

Insert responsive image:

## Live Site:
link to live project

## Purpose Statement:
What is Boards?
Boards is a project tracker, very similar to the project boards found on GitHub. It is designed to allow individuals, and groups, keep track of projects they might have in a manner that makes progress easilly visual. 
Essentially, this is a web app designed with the Agile methodology in mind. As such it will aid in any work that is already suited, or could be adapted to suit the requirements of Agile.

<details>
<summary>Target Audience/Demographic</summary>
Who is this app/project for?

It will cater to many different groups, individuals, and teams, across fields. Though its benefits will primarily be seen by those who have to most need to keep track of their tasks within a team or general life. Demographics likely to benefit at face value are...

- Students:
    - individually they will be able to keep track of their work
    - groups can keep track of a group project meaning that everyone is up to date no matter what
- Coders/Software Engineers:
    - similarly to GitHub, this project tracker will provide a similar functionality to the project boards found on GitHub
    - Agile development teams, that could keep track of a project with multiple editors
- Businesses:
    - businesses that have a strong culture of planning and making tasks visible
    - large teams of people that need to be aware of how a project is coming along
</details>

<details>
<summary>Unique Selling Points</summary>
1. Simplified Agile Project Tracking:
    Boards will provide a user-friendly interface that enables users to effortlessly track projects, tasks, and progress.
Unlike complex tools like GitHub Projects, Boards will focus on simplicity and ease-of-use without sacrificing essential functionality.

2. Task Management for Individuals and Teams:
    Boards will cater to individuals such as students managing multiple projects or Agile development teams with numerous tasks.
Users will be able to create, edit, assign, and prioritize tasks seamlessly, ensuring everyone remains aligned and progress is visible.

3. Progress Visualization:
    With Boards' intuitive task board layout, users will be able to instantly see the status of each task.
Tasks can be updated between columns (e.g., To Do, In Progress, Done), providing an immediate understanding of project progress.

4. Cross-Platform Accessibility:
    Boards will be designed to be responsive and accessible on various devices and screen sizes.
Whether users are working from their laptop, tablet, or mobile phone, Boards ensures they can stay on top of tasks anytime, anywhere.
</details>

<hr>

## Table of Contents:
Insert table of contents for easy navigation of readme.
- [Project Overview](#project-overview)
- [Development Path](#development-path)
    - [Strategy](#strategy)
        - [Plan](#plan)
        - [Scope](#scope)
        - [Structure](#structure)
        - [Skeleton](#skeleton)
        - [Surface](#surface)
    - [Project Features](#project-features)
        - [Current Features](#current-features)
        - [Future Features](#future-features)
    - [Methodologies](#methodologies)
        - [Version Control](#version-control)
        - [Agile Methodology](#agile-methodology)
        - [Frameworks](#languages--frameworks-utilised)
    - [Testing & Validation](#testing--validation)
        - [Bugs](#bugs)
        - [Manual Tests](#manual-tests)
        - [Validation](#validation)
    - [Deployment](#deployment)
        - [Steps to Deploy](#steps-to-deploy)
    - [Reflection](#reflection)
        - [Achievements](#achievements)
        - [Critical Analysis](#critical-analysis)
    - [Final Thoughts](#final-thoughts)

# Development Path:

## Strategy

### Design
The strategy behind this app was to utilise the Agile Methodologies learnt, and work towards a User Centered Design.

#### User Stories: Must Haves

<details>
<summary>User Story: Register Account</summary>

**User Story:** As a **User** I would like to be able to **Create an Account** so that I can **Access My Work Spaces Securely.**

Acceptance Criteria:
1. User can register account
    - [ ] allauth is installed as dependancy
    - [ ] can access registration page
    - [ ] can use form
    - [ ] can submit form
2. User is able to login
    - [ ] using submitted account creation details
    - [ ] login form works
3. User is able to see created Project Boards
    - [ ] user is displayed a list of their created projects

</details>


<details>
<summary>User Story: Create Data</summary>

**User Story:** As a **User** I would like to be able to **Create a Project and Tasks** so that I can **Keep Track of Ongoing Tasks and their Progress**.

Acceptance Criteria:
1. User is able to create new tasks by pressing add task button.
    - [ ] Add task button populates relevant kanban section
2. User is able to create project board by clicking the new project button.
    - [ ] New Project... button allows user to fill out form to create new project

</details>

<details>
<summary>User Story: Read Data</summary>

**User Story:** As a **User** I would like to be able to **See the Tasks I have Completed in a Project** so that I can **Track my Progress.**

Acceptance Criteria:
1. User is able to see a list of all their projects.
    - [ ] list of owned projects
2. User is able to select a project that they want to see.
    - [ ] projects linked to each relevant instance of project model
3. User is able to see information containerd within the relevant project.
    - [ ] templates load object of project model into view
4. Project board has a list of tasks sorted by their status.
    - [ ] user is able to read the title of the tasks
    - [ ] user is able to open task and read additional info
</details>

<details>
<summary>User Story: Update Data</summary>

**User Story:** As a **User** I would like to be able to **Update the Information on my Project Board** so that I can **Add and Remove Tasks, and Notes Based on Relevance.**

Acceptance Criteria:
1. User is able to open a project and add tasks to it.
    - [ ] tasks can be added to project
    - [ ] tasks are saved to the project
2. User is able to remove tasks from an opened project.
    - [ ] tasks can be removed from project
3. User is able to alter contents of task.
    - [ ] state of tasks is saved
4. Upon returning to the project, the users changes are present.
    - [ ] user is able to retrieve their project from the state in which they left it
</details>


<details>
<summary>User Story: Delete Data</summary>

**User Story:** As a **User** I would like to be able to **Delete my Tasks and their Data** so that I can **Keep my Tasks List Short and Current.**

Acceptance Criteria:
1. User is able to delete a task from the board.
    - [ ] user is able to click delete button on relevant task and delete it from board and model
2. User is asked to confirm their choice and give a warning.
    - [ ] user is asked to confirm their choice via modal before data is deleted
3. Users data is deleted, and user is sent back to list of tasks which will no longer contain the deleted item.
    - [ ] task is deleted from the tasks on the projects Kanban board.
</details>


<details>
<summary>User Story: Responsive Design</summary>

**User Story:** As a **User** I would like to be able to **User the App on Multiple Devices of Differeing Sizes** so that I am able to **User it on the go and at Home/Work.**

Acceptance Criteria:
1. Web app uses Bootstrap or Media Queries to adapt to multiple screen sizes.
    - [ ] bootstrap, media queries, and JavaScript with cookies
2. App is usable on small screens.
    - [ ] functional on small displays
3. App is usable on medium displays.
    - [ ] function on medium displays
4. App is usable on laptop/desktop displays.
    - [ ] functional on large displays
</details>


### User Stories: Should Haves

<details>
<summary>User Story: Intuitive Layout</summary>

As a **User** I would like to be able to **Navigate the Site easily and Intuitively** so that I can get to **Where I Need to Be within Three Clicks of Any Page.**

Acceptance Criteria:
1. Layout of the site takes into account the three clicks rule.
    - [ ] create wire frames looking at UI/UX
2. Site is intuitively navigable for the average user.
    - [ ] everything is where one would expect to find it
    - [ ] links go to correct pages, or do not load if they are a future feature
3. All relevant information is displayed upon clicking any link
    - [ ] click link takes user to established pages that load relevant info

</details>

<details>
<summary>User Story: Todo Views</summary>

As a **User** I would like to be able to **~See my todo list items as a list and as a kanban Board** so that I am able to **Better see my progress and find items.**

Acceptance Criteria:
1. User is able to access todo list view
    - [ ] One longlist of all todo items, not separated by status
2. User is able to view list as Kanban board
    - [ ] user is able to toggle between views
3. User is able to see all todo items in List View.

</details>

<details>
<summary>User Story: Formatted Notes</summary>

As a **User** I would like to be able to **Format my Notes (i.e., make bold, italic, checkboxed, etc.,)** so that I am able to **Clearly Highlight important information within the notes.**

Acceptance Criteria:
1. User is able to make text in notes bold.
    - [ ] summernotes is imported and working
    - [ ] user is able to make text bold
2. User is able to add checkboxes to notes.
    - [ ] user is able to add checkboxes into tex fields
3. User is able to make text italic.
    - [ ] user can italicise text

</details>


### User Stories: Could Haves

<details>
<summary>User Story: Add Editors</summary>

As a **User** I would like to be able to **Add additional editors to a project** so that I am able to **Collaborate with Classmates/Peers/Colleagues easily.**

Acceptance Criteria:
1. User is able to see list of authorised editors for each project.
2. User is able to add editors, by username, to list.
3. User is able to remove editors, by button, from list.

</details>

<details>
<summary>User Story: Smooth Task Updates</summary>

As a **User** I would like to be able to **Update the status of a task by Dragging it to the relevant Kanban Section** so that I am able to **Perform the Operation Faster.**

Acceptance Criteria:
1. User is able to interact with todo items and drag them around the screen
2. Todo item status is updated by where the user drops the item.
3. User is able to drop item on bin to delete it.

</details>

## Scope

Features:
- User registration, login, and role-based access (user/admin)
- Dashboard with am index of projects
- Project board with kanban board of tasks
- Project creation and management (title, description, date created)
- Task creation, editing, and deletion within projects
    - Task types: To Do, In Progress, Completed
    - Task content: for additional information
    - Task author: to see creator of task
- Real-time notifications for task updates and changes
- Responsive design for accessibility on various devices

Technologies:
- Back-end: Django (Python)
- Front-end: HTML5, CSS3 (Bootstrap), JavaScript
- Database: PostgreSQL with Django ORM
- Version Control: Git and GitHub
- Deployment: Heroku

### Plan
To get a clear understanding of the agile methodology used, and the benefits of such a practice, it is worth while referring to this repo's project board here - [Project Board](https://github.com/users/LukeI50/projects/8/settings)

![Project Board Screenshot](assets/README/wireframes/project/project_board.png)


## Structure
<details>
<summary>Logic Overview</summary>

- Greeting page for user to register or login.
- A dashboard that allows the user to easily navigate all features of the site.
- Navbar always stuck to left side of screen to keep uniformity, and provide more height.
- Project index with project cards displaying the title, description, and date. All with an "open project" button.
- Project view of kanban board for task organisation. Clear columns for Todo, In Progress, and Done.
- Tasks can be updated and deleted by pressing visible buttons on task.
- Users can see the tasks associated to the selected project and plan accordingly.

</details>

<details>
<summary>Site Map</summary>

New Users
1. Greeting page
2. Registration / SignUp page
3. Navbar not present until user is authorised
4. Projects Dashboard
5. Projects Kanban view

Registered Users
1. Project Index Dashboard
2. Projects Kanban View
3. Navbar present at all times
4. Form Modals
5. Toast Notifications
</details>

## Skeleton

### Wireframes

<details>
<summary>Desktop Wireframes</summary>

Initial idea for the greeting page is to use bootstrap cards and jumbotrons to achive a nice aesthetic that guides the user to the sign up button.
![Greeting Page Desktop](assets/README/wireframes/desktop/greeting_page_desktop_wireframe.png)

The Projects Index page is set up in columns, though the actual ammount of columns is something that will be made responsive to device width.
Each Project will be openable. In case of too many projects on the page at once, an overflow on the y axis will be set to scroll.
![Project List Desktop](assets/README/wireframes/desktop/project_list_desktop_wireframe.png)

The Task view will be setup similarly to the kanban board on GitHub. This means that users are able to have tasks in their desired column, and provides a quick overview of the progress made towards the overall project.
![Task Board Desktop](assets/README/wireframes/desktop/detail_task_view_desktop_wireframe.jpg)

</details>

<details>
<summary>Tablet Wireframes</summary>

![Greeting Page Tablet](assets/README/wireframes/tablet/greetings_page_tablet_wireframe.png)

![Project List Tablet](assets/README/wireframes/tablet/project_list_tablet_wireframe.png)

![Task Board Tablet](assets/README/wireframes/tablet/task_list_tablet_wireframe.png)

</details>

<details>
<summary>Mobile Wireframes</summary>

![Greeting Page Mobile](assets/README/wireframes/mobile/greeting_page_mobile_wireframe.png)

![Project List Mobile](assets/README/wireframes/mobile/project_list_mobile_wireframe.png)

![Task Board Mobile](assets/README/wireframes/mobile/task_view_mobile_wireframe.png)

</details>

### Database Diagram

<details>
<summary>Database Relational Diagram</summary>

![erd](assets/README/wireframes/erd/erd.png)

</details>

## Surface

### On Design
I decided to stay simple during the course of this project and stick to tried and tested colour schemes. To do this, I utilised bootstraps generic colour pallete to ensure that the look of the overall site blended together well, and that contrast between elements was good.

The text/fonts on the site were not altered from the default. The most important task at the time was developing a working MVP, so this is what was focused on.

<details>
<summary>Ideas</summary>

Certain ideas were taken into account during the creation of the layout of the site, most of which were to facilitate an easy user experience.

1. the three click rule
2. good colour contrast to ensure people can read all text
3. button stying to ensure buttons stand out

## Project Features:

<details>
<summary>Greetings Page</summary>

The Greetings Page is designed to say hi to our new users. Once registered they likely wont see this page again. At least that's the hope anyway.
The page greets you with info about the company and the product, with a clear Agreement button placed in the bottom right.

![Greetings Page](assets/README/wireframes/project/greetings_page/greetings_page.png)

![Agreement Modal](assets/README/wireframes/project/greetings_page/agreement_modal.png)

</details>

<details>
<summary>User Credentials</summary>

The user is able to create an account, before they can access the sites features.
- Upon registration or sign in a notification will appear to tell the user that it was successful or not.
- Role based functionality is present as only owners of a project are able to access their projects.
- The login status of the user is displayed in the bottom right corner of the screen from then on until the user logsout.

Once the sign up button is clicked the user is taken to the registration page:
![Sign Up Page](assets/README/wireframes/project/authentication_pages/signup_page.png)

or, alternatively, they can login instead:
![Sign In Page](assets/README/wireframes/project/authentication_pages/signin_page.png)

</details>

<details>
<summary>Projects List Page</summary>

The user, once logged in, is presented with a list of all their projects. They can either open an existing one, or create a new project by clicking on their name in the bottom left corner and then selecting New Project...

![Projects List Page](assets/README/wireframes/project/projects_list_page/projects_list.png)

![New Project Modal](assets/README/wireframes/project/projects_list_page/new_project_modal.png)

User options in the bottom left:
![User options](assets/README/wireframes/project/projects_list_page/user_options.png)

</details>

<details>
<summary>Kanban View: defaul/small</summary>

The view for the Kanban renders differently dependant on display size. In the defaul/small view the tasks are placed within an accordion that houses each status of a task.
![Tasks Page](assets/README/wireframes/project/tasks_page/task_page.png)

Each task has a delete button, and an edit button. Both of which raise a relevant modal with a form in to submit changes or deletions.

The edit form allows for addition notes to be added:
![Edit form](assets/README/wireframes/project/tasks_page/edit_modal.png)

The delete is simple and so well skip it, it just confirms you want to take the action.

In this view, you will also notice that the option to add a task appears in the side navbar. Adding a task creates another modal similar to the edit:
![New Task Form](assets/README/wireframes/project/tasks_page/new_task.png)

</details>

<details>
<summary>Kanban View: large</summary>

Some of the information on the large view has already been give, so this will be brief.
In the large view, the kanban is rendered as three columns that are separate (for more similar to the way GitHub boards do it).

![Kanban Large](assets/README/wireframes/project/tasks_page/kanban_large.png)

This is more readable for the user, and allows them to see all tasks in their relevant section.

If a task is updated, added, or deleted, then a notification will appear to tell the user as much.
</details>


# Methodologies:

## Version Control
Git and GitHub were used for version controll in this project. The main branch was protected, and I tried only to work on branches and merge them in so as to avoid major issues.
For the most part this worked, although there were a couple of times were I had to push to the main branch to update something or attempt to fix a bug.

# Testing & Validation
<details>
<summary>LightHouse</summary>

Lighthouse scores for the Projects list page:
desktop:

![lighthouse desktop projects](assets/README/wireframes/lighthouse/projects_lighthouse.png)

mobile:
![lighthouse mobile projects](assets/README/wireframes/lighthouse/project_mobile_lighthouse.png)

Lighthouse scores for Task/Kanban page:
desktop:
![taks view kanban lighthouse](assets/README/wireframes/lighthouse/lighthouse_tasks.png)

mobile:
![tasks view mobile lighthouse](assets/README/wireframes/lighthouse/mobile_task_lighthouse.png)

</details>

## Bugs
No major bugs were found, only minor elements needed tweaking as project progressed. This was many around css styling, but nothing big that stood out.

## Manual Tests
User Can create an account
| **Test** | **Steps** | **Expected Result** | **Actual Result** |
|User can sign up | 1. go to site | greetings page | pass |
| | 2. click agreement | agreement modal appears | pass |
| | 3. click sign up | signup page loads | pass |
| | 4. input credentials | creates user account | pass |

User can create tasks
| **Test** | **Steps** | **Expected Result** | **Actual Result** |
| User can create new task| 1. go to task view | loads kanban board| pass |
| | 2. click add new task button | loads add task modal | pass |
| | 3. fill out modal and submit | creates new task with notification | pass |

User can delete tasks
| **Test** | **Steps** | **Expected Result** | **Actual Result** |
| User can delete tasks | 1. click on delete button on task | confirm delete modal appears | pass |
| | 2. click confirm | task is deleted and notification appears | pass |

User can update tasks
| **Test** | **Steps** | **Expected Result** | **Actual Result** |
| User can update a task| 1. click edit button on task | update task modal appears | pass |
| | 2. alter the task and click update | task is updated and notification appears | pass |

User can see tasks
| **Test** | **Steps** | **Expected Result** | **Actual Result** |
| user can see list of tasks for project | 1. go into project | loads kanban board | pass |
| | 2. tasks are present on the board | tasks should be visible if created | pass |

## Validation
HTML validation was done with [W3C](https://validator.w3.org/)


![Greeting page errors](assets/README/wireframes/Validation/greeting_page_validation_errors.png)
All necessary edits were made to fix html here.

![Signup page errors](assets/README/wireframes/Validation/Signup%20page%20html%20validation%20errors.png)


# Deployment

## Steps to Deploy
install django

setup database

setup environment

Add WhiteNoise

Configure Heroku


# Reflection

## Achievements

## Critical Analysis

# Final Thoughts


## Areas to Improve



# References/Attributions


