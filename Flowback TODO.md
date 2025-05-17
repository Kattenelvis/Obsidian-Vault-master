
The great flowback rework/refactor of 2025

- API rework in conversation with Siamand
- Analyze the code for unnecessary stuff
- Modularity and expandability
- Fixing problems at their core
- Decrease code count by 10-20%
- Research svelte and svelte kit 5, push up to standard (runes maybe?)
- Research code standard and large scale maintainability (like +server.svelte, +layout.svelte etc), separation of concerns. 
- Optimizing by minimizing API calls, page loads etc
- Playwright tests for the frontend
- Ask about future features to prepare for those
- Calculations in C on bet calculations
- Backend renaming group tagss to group tags (or area etc we'll see)
- Merge back and frontend into one repository?
- Gamification
- Preparing for future features
- Alignment scores
- Better poppup and feedback system 
- For most API calls, receive the item, not just the id, so we don't need to double the amount of work in the frontend
- Backend refactoring of Poll process, notifications, removing delegate pools




Top 5 people to talk to and effective thesis can provide support.

- David Chalmers
- Nick Boström
- 




Features för Loke att rangordna i prioritet: 

Lägga till delegat relation
(DONE) Göra sig själv till delegat
(DONE) Bug: Duplicate names in Delegation
Bug: Drag-drop on proposals not working
Fix User profile and user list
Editable Permissions (Do in Figma first)
Fix Invitation
Fix Modal (with <modal> tag)
Fix Timeline (with <progress> tag)
Are you sure when deleting poll/group (after fixing modal)
Using svelte stores for webtoken and permission in group.
Derived Svelte stores and class
(DONE) Implement "unsaved" indications and warnings
Translation
Bug: Backspace from poll to groups lead to error
Grupp i Flowback för feedback på hemsidan
(DONE) Lägga till proposal läggs in
Gör till single-page app (gör hemsidan snabbare)
Create a poll fix design for mobile
Autoexpanable descriptions (när man skriver på polls, comments and proposals)
Comments
Date Picker in forms
Display "User not logged in" when non-user tries to enter things
(DONE) Mobile group menu (display sticky hamburger icon)
Commonly used colors/other designs in one file
Global Prediction Market (figma design first)
Prediction market in polls (figma design first)




A reminder to always report which tasks you're doing! It might already be finished or someone else might be working on it. Tasks without time estimates are counted as 30 minutes. If a task is unclear, ask about that task.


Events (at least those with the same start and end dates and times) change place when reloading and just after reloading you get the error “this field can not be null” on description when you try to create a new event 

Delegation does not work, button stops being filled after I select a delegate 
To recreate: 
test on IMMR: 
create a new user 
join a group 
delegate in a subject area 
click on another subject area 
click back to the previous subject area
Now radio button is not filled in 

Auto-vote is not saved when reloaded

Chat notifications should work properly in real time: purple dot next to direct chat when someone else has posted, blue dot next to group chat when someone else has posted, purple dot next to “direct” if at least one purple dot in the direct chat list, blue dot next to “groups” if at least one blue dot in the group chat list, if at least one purple dot in direct chat have a purple dot on the chat box outside the chat, if at least one blue dot in group chat have a blue dot on the chat box outside the chat (the small circle with the chat icon to the left) next to the group text there should be a dot indicating that there is chat. The small chat icon should remain, but the dots are removed if you are already in the chat (1 hour)

Sometimes a user can't delegate to delegates, delegation doesn't count in voting, delegated but it wasn't counted in the results.

When I go to a poll that is in a subject area I delegated in, I can't see what my delegate voted for.

Comments: non-image file types should work in comments without having to reload

Sometimes the blue-stripe with the event title on the day disappears when clicking on it - Clicks on an existing event, clicks out, clicks plus, then sometimes the existing event disappears.

Kanbantasks sometimes changes priority, tried moving and reloading after I updated it and it changed; does not update in real time (for example when changing workgroup)

Group Kanban just seems to have problems with the date not being filled in either. To recreate: create a task and assign someone, reload the page, then try to change workgroup

The original date is not set when editing Kanban tasks.

In schedule events: Choose frequency (never, daily, weekly, monthly, annually, custom), Add/delete members, reminders. 

View poll information (description, subject area, the historical IMAC) in delegate history 

View comments on proposals

Comments sometimes disappear when clicking on the comment symbol with the number on proposals at least during the proposal phase, weird things happen when reloading too, both a and #a were counted as comments on proposal a weird 

The number of comments on a proposal is not updated in real time

Filtering on workgroups on threads unsure

You should be able to edit files and images on comments (delete/replace)

Control shift r twice quickly on home leads to a strange page





Fast forward with permission and with non fast forwardable poll: I as a regular user managed to fast forward a poll it seemed like iaf, shouldn't even seem like that, and as admin I also seem to be able to click and the next phase appears but when I reload I'm back.

Fix the design on report boxes, you should not be able to submit without both description and title

Fix the design on public? In threads and polls now work groups jump in and out.

Fix show members in chat button 

Search does not work in feeds

Next should make you end up at the top of the feed and the buttons can be at the top as well, previous makes sense at the bottom though

The number of members should be updated in real time on working groups 

When someone becomes an admin, it should also be on the permissions page, not just on the members page 

Style delegate history

Sort members on roles say admin and other roles

The creator should auto like their threads 

Clicking back in the browser does not work properly in chat 

Fix better design for invitations.

Click on clear filter and IMAC values on tags disappear







T_P vs Baymax



Ingen fixade, baymax hade delegering helt breakat
´´´Delegering fungerar inte, knappen slutar vara ifylld efter jag valt ett delegat [FUNKTIONALITET/DESIGN] 

För att återskapa: 

- testa på IMMR: 
    
- skapa en ny användare 
    
- gå med i en grupp 
    
- delegera i en subject area 
    
- klicka på en annan subject area 
    
- klicka tillbaka till förra subject arean 
    
- Nu är radio button inte ifylld´´´


båda gjorde chatten värre
Chattnotifikationer ska fungera som de ska i realtid: lila prick bredvid direct chat när någon annan skrivit, blå prick bredvid group chat när någon annan skrivit, lila prick bredvid “direct” om minst en lila prick i direct chat-listan, blå prick bredvid “groups” om minst en blå prick i group chat-listan, om minst en lila prick i direct-chat ha en lila prick på chattrutan utanför chatten, om minst en blå prick i group-chat ha en blå prick på chattrutan utanför chatten (den lilla cirkeln med chat icon till vänster) brevid group texten ska det finnas en prick som indikerar att det finns chatter. Den lilla chatt symbolen ska vara kvar, men prickarna tas bort om man redan är inne i chatten. [FUNKTIONALITET] osäkert


Baymax hade gjort mycket finare Modal window för Calendar... kanske tar in det iaf.... men breakar att klicka utanför så stängs den inte

Calendar bug fixad dessutom. förutom vid dubbel klick

