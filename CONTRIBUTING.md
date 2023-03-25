# Contributing
To contribute to [pro-football-reference-web-scraper](https://github.com/mjk2244/pro-football-reference-web-scraper/), please adhere to the following guidelines:

## Prerequisites
Make sure `python` is installed on your computer.  

## Cloning the Repo
First, `fork` the main branch of the repo. For more information on forking, please read this [tutorial](https://docs.github.com/en/get-started/quickstart/fork-a-repo).  

Then, in your local environment, run `git clone https://github.com/<your_username>/pro-football-reference-web-scraper.git`.  

## Installing Dependencies
Before you begin working on your contributions, you need to make sure you have all of the library's dependencies installed. To do that, simply run `make develop`.  

## Before Opening a Pull Request (PR)
Before submitting your contributions through a [PR](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/about-pull-requests), make sure to do the following:  
- Write tests for any new features you build
- `make lint` to run static analysis
- `make format` to run autoformatting
- `make test` to make sure all tests pass
