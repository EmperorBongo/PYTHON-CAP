### Python notes

log in

create account 

write some puesdocode for my project 

When arrives to pigeon polls a welcome page with a login will appaear with a button option to create an account. 


Questions for data base 

Gets sent to Suvery page. 

User table. questions table.

 Response table ID Response date and time | user ID | Response type | Response ID | list Reponse. 

 MAIN THREE TABLES.

 QUESTIONS

 USERS 

 RESPONSES
    YES/NO Responses forgien key to main responses table. 


    Headache from data base Database is just a fancy dictionary. Make a simple python database. holds a list of questions. 



- finish program flow. 

- how does this translate into python 
what is the start what is the we can ad the end later

- how does th flow translate into functions


- what is most important


FRONTEND 
login
home 
polls 
stats
css 

server

Crud 

need to add update and delete functions

user login
completed

Features


completed 
login 



add
Update user information and view it user information
button on home page to update user info

delete response to poll question.

user can answer multiple choice questions
one time a day the question will be posted 


in html i will create a poll structure that will populate with questions 

query the question and potential answers that is logged under todays date in the 

POLLS AND POLL DATA
Diplaying the question and answer options. HTML

CONNECT javascipt file to the HTML for dispaying questions and responses 

Add event listener to each response. Inside event listener capture 

response_ID (what answer did they click?)

AJAX 
POST EXAPLE FROM HAND OUT 
we want to post information to new route in the backend

python

Route will extract reponse it will log the response into data base 

python will pull quantity of responses for todays qeustion for a count

after determineing count package it into python dict. return dictionary into the route. 

from flask import jsonify
return jsonify(dictionary)





save the  in session



display up to date stats or reponses upon finishing polls



later 
old poll data





 body {
    font-family: Arial, sans-serif;
  }
  body {
    font-family: Arial, sans-serif;
    margin: 0;
    padding: 0;
  }
  
  h1, h2 {
    color: #333;
  }
  
  ul {
    list-style-type: none;
    padding: 0;
  }
  
  a {
    text-decoration: none;
    color: #007bff;
  }
  
  a:hover {
    text-decoration: underline;
  } 

  button {
    background-color: blue; /* Green */
    border: none;
    color: white;
    padding: 15px 32px;
    text-align: center;
    text-decoration: none;
    display: inline-block;
    font-size: 16px;
  }

  
  /* Home Page Styles */
  h1 {
    color: #333;
  }
  
  p {
    color: #666;
  }
  
  button[type="submit"] {
    background-color: #007bff;
    color: #fff;
    border: none;
    padding: 10px 20px;
    cursor: pointer;
    margin-right: 10px;
  }
  
  button[type="submit"]:hover {
    background-color: #0056b3;
  }
  [c]
  /*Home Page Styles */
   .home-content {
    text-align: center;
    background-color: #fff;
    padding: 20px;
    border-radius: 8px;
    box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.1);
  } 
   .home-content {
    text-align: center;
    margin-top: 50px;
  }
  
  .home-content h1 {
    color: #333;
  }
  
  .home-content p {
    color: #666;
  }
  
  .home-content button[type="submit"] {
    background-color: #007bff;
    color: #fff;
    border: none;
    padding: 10px 20px;
    cursor: pointer;
    margin-top: 20px;
  }
  
  .home-content button[type="submit"]:hover {
    background-color: #0056b3;
  } 

  .response-summary {
    margin-top: 20px;
    padding: 10px;
    border: 1px solid #ccc;
    border-radius: 5px;
    background-color: #f7f7f7;
}

.response-option {
    margin: 5px 0;
    font-size: 16px;
}

.total-response {
    margin-top: 10px;
    font-size: 18px;
    font-weight: bold;
}

.container {
    max-width: 800px;
    margin: 0 auto;
    padding: 20px;
}

.btn-primary {
    background-color: #007bff;
    color: #fff;
    border: none;
    padding: 10px 20px;
    cursor: pointer;
}

.btn-primary:hover {
    background-color: #0056b3;
}

.btn-danger {
    background-color: #dc3545;
    color: #fff;
    border: none;
    padding: 10px 20px;
    cursor: pointer;
}

.btn-danger:hover {
    background-color: #c82333;
}

/* login Styles */
.login-content {
    text-align: center;
    margin-top: 50px;
}

.login-content h1 {
    color: #333;
}

.login-content p {
    color: #666;
} 
Home Page Styles
.home-content {
    text-align: center;
    margin-top: 50px;
}

.home-content h1 {
    color: #333;
}

.home-content p {
    color: #666;
}

/* Polls Page Styles */
  .polls-content {
    text-align: center;
    margin-top: 50px;
}

.polls-content h1 {
    color: #333;
}

.polls-content p {
    color: #666;
}

.polls-content button {
    margin: 10px;
} 