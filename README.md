# PyTodoApp
PyTodoApp is a python CLI (Command Line Interface) app that lets users manage their daily tasks in different ways.

## Installation


## Usage

Once you’ve downloaded the repository on to your local machine, head over to your preferred IDE and open the project.
If you run into any issues, feel free to open an issue [here](https://github.com/teddygizachew/PyTodoApp/issues)

All of the Commands are here:
```
--query
--update
--remove
--record
--complete
```
### 1. Input

Command: 

  `python -m todoapp --record tonight "06:30 PM" "07:00 PM" "Cook Dinner" :Food`
  
Ouput:

`Successfully inserted 'Cook Dinner'!`

### 2. Read

Command: 

  `python -m todoapp --query all`
  
Ouput:

<img width="468" alt="image" src="https://user-images.githubusercontent.com/60460297/208086153-c2962368-1612-48d7-9ed8-d092293f7eb6.png">


Command: 

  `python -m todoapp --query tags`
  
Ouput:

<img width="162" alt="image" src="https://user-images.githubusercontent.com/60460297/208086138-224205e3-892e-4476-8fd2-14a3a24759cc.png">


### 3. Update

Command: 

  `python -m todoapp --update 1 Play`
  
Ouput:

<img width="468" alt="image" src="https://user-images.githubusercontent.com/60460297/208086402-e54526a4-7217-47dd-ac47-a230b57a4931.png">

### 4. Delete

Command:  `python -m todoapp --remove STUDY`

<img width="468" alt="image" src="https://user-images.githubusercontent.com/60460297/208086236-2f034dd2-0080-4456-93db-7bb59080d470.png">

Output:

<img width="468" alt="image" src="https://user-images.githubusercontent.com/60460297/208086943-554278b3-f6e7-4734-ba96-01a5dc3dd4f8.png">

### 5. Complete

Command: `python -m todoapp --complete 1`

Output:

<img width="468" alt="image" src="https://user-images.githubusercontent.com/60460297/208086705-25d13608-0258-41b0-92e7-ba73259dd399.png">


## Communication
