# Worklog Generator

To save a few minutes editing .docx and exporting it as .pdf, I spent hours
working on this script to automate that process through terminal. There are two
ways to enter data:
- at script runtime through prompts
- through .txt files defined in a certain syntax*

## Usage: 
To make it easier to: `set up python virtual environment > activate the
environment > install pip packages > run the script > close the environment`
I've also written a bash script `run.sh` that does everything for you. So to run
the program, just run this script.

<details>
  <summary>Entering data at runtime </summary>

  ![runtime](/screenshots/runtime.png)
</details>

<details>
  <summary>Passing in file </summary>

  ![runtime](/screenshots/file.png)
</details>

## Config:
Name and StudentID can be changed in the first lines of `main.py` 

<details>
  <summary>Setting up Name and ID</summary>

  ![runtime](/screenshots/config.png)
</details>


## Syntax for .txt files: 
```
{week number}

task:
> {description} 
> {status} 
> {time_taken} 
> {notes}

plan:
> {description}
> {expected_time}

summary: 
{text} 
```
`time_taken` for tasks should be in `hh:mm` format to allow
total time generation, however this requirement is not continued for
`expected_time` in plan, as there text like "about 2hrs" might also be entered.

### Example file (used in above screenshot)
```
1

task:
> Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor
incididunt ut labore et dolore magna aliqua. 
> Completed 
> 4:00 
> Pretium quam vulputate dignissim suspendisse in est ante. Sit amet risus
nullam eget.

task:
> Velit aliquet sagittis id consectetur. Orci sagittis eu volutpat odio
facilisis mauris sit amet. 
> On Hold 
> 3:45 
> Eget est lorem ipsum dolor. Vestibulum morbi blandit cursus risus.

plan:
> Diam quam nulla porttitor massa id neque. Nunc lobortis mattis aliquam
faucibus purus in massa tempor nec. 
> ~3:00

summary: 
Diam vel quam elementum pulvinar etiam non quam lacus suspendisse. Mauris cursus
mattis molestie a iaculis at erat pellentesque adipiscing. Lectus arcu bibendum
at varius vel pharetra vel turpis. Turpis egestas pretium aenean pharetra magna.
Velit scelerisque in dictum non consectetur a.
```

