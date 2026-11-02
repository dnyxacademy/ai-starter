# How to submit your work

Every submission is a **pull request link**, pasted into the Dnyx Learn lesson before its due date.
No zip files, no screenshots of code, no "it is on my laptop".

## Every day

1. Branch off `main`: `git switch -c week-2/train-a-network`
2. Build the thing. Commit as you go, in small steps.
3. Push: `git push -u origin week-2/train-a-network`
4. Open a pull request on GitHub. Fill in the template — it asks for the week, the assignment, the
   "Done when" checklist and how you used AI.
5. Copy the pull request URL into the Dnyx Learn lesson and submit.
6. **Keep it open** until your mentor has reviewed it. Reply to every comment, push the fixes, then
   merge it yourself.

## Each week

Alongside the last pull request of the week, your weekly note goes in the lesson:

- **What I built** — in your own words, not a list of commits.
- **What was hard** — the thing that took three hours.
- **What I would change** — if you started again.
- **How I used AI** — which tools, for what.

## Deadlines

Work is due by the date on the lesson. Up to 24 hours late loses 20 percent of that item. After
that it is marked as a partial, with feedback, and you move on to the next week's work — you do not
have to catch up on everything before continuing.

Medical or family reasons are excused. Tell your mentor **before** the deadline where you can.

## Checks before you submit

- [ ] The pull request has a description, not just a title
- [ ] The "Done when" checklist is honest — unticked boxes are better than false ones
- [ ] No `.env`, keys or tokens anywhere in the diff
- [ ] No full dataset, model weights or `.ipynb_checkpoints/`
- [ ] Your notebook runs top to bottom on a fresh kernel
- [ ] Notebook output is cleared, unless a chart is the point

## Common ways people lose marks

| Mistake | Fix |
|---|---|
| One commit, the last evening | Commit each day. Mentors read the history |
| Review comments ignored | Reply in writing to every one |
| Repository is private | Make it public, or your mentor sees a 404 |
| The notebook only runs out of order | Restart the kernel and run it top to bottom |
| A key committed "just to test" | Rotate it, tell a mentor, use `.env` |
