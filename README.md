
# Club Tracker - A database management CLI

This is a command line interface (CLI) designed to manage a many-to-one relationship between students who are each enrolled in one of the school clubs.  With some modification of prompts and table names, the functions and menu system can work to manage any database with a similar many-to-one relationship between two classes.

## Setup

In order to use this app on your own machine, first make sure you have Python and pipenv installed on yor computer.  From there fork fork and clone this repository and run the following commands in the club-tracker directory to enter the virtual environment:

```bash
pipenv install

pipenv shell
```
Change into the /lib directory and run the CLI:

```bash
cd lib

python cli.py
```

## Usage

![](https://github.com/apatari/phase-2-Project-disc-bag/blob/main/BagGif.gif)

Add discs using the 'Add New Discs' tab.  The submit button and a preview of your discs will appear once all fields are filled.  From there, you can add discs to the bag from the 'Select Discs' tab and see the current state of the bag with the 'View Bag' tab.

A browser window should open up with the app running.  

## Acknowledgment

Thanks to the folks who created and maintain the Create React App and Bootstrap React

This project was bootstrapped with [Create React App](https://github.com/facebook/create-react-app), and uses [Bootstrap React](https://react-bootstrap.netlify.app/) for styling.

## Updating README.md

`README.md` is a Markdown file that should describe your project. You will
replace the contents of this `README.md` file with a description of **your**
actual project.

Markdown is not a language that we cover in Flatiron's Software Engineering
curriculum, but it's not a particularly difficult language to learn (if you've
ever left a comment on Reddit, you might already know the basics). Refer to the
cheat sheet in this assignments's resources for a basic guide to Markdown.

### What Goes into a README?

This README serves as a template. Replace the contents of this file to describe
the important files in your project and describe what they do. Each Python file
that you edit should get at least a paragraph, and each function should be
described with a sentence or two.

Describe your actual CLI script first, and with a good level of detail. The rest
should be ordered by importance to the user. (Probably functions next, then
models.)

Screenshots and links to resources that you used throughout are also useful to
users and collaborators, but a little more syntactically complicated. Only add
these in if you're feeling comfortable with Markdown.

---
