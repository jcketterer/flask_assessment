## Conceptual Exercise

Answer the following questions below:

### - What are important differences between Python and JavaScript?
  Some important differences between Python and JavaScript are:
  1. Variable name and varible style. Python does not use "let" or "const" also varibles are named using snake_case vs. camelCase. 
  2. Code blocks, javascript uses code blocks defined by curly brackets whereas python uses the colon and has to be indented properly. 
  3. Default error handling, JavaScript uses NaN or Undefined where python will throw an error. 
  4. A few syntax changes with boolean operators such as and, or and not. Python uses the english words where Javascript uses && || and !. 

### - Given a dictionary like ``{"a": 1, "b": 2}``: , list two ways you
  ### can try to get a missing key (like "c") *without* your programming
  ### crashing.
  You could use the `.get()` method to set if a key is missing to return with a certain statement. Or you can use the `defaultdict()` method. 

### - What is a unit test?
  A unittest tests code in isolated small pieces. One function at a time. 

### - What is an integration test?
  Integration testing tests within a flask application. 

### - What is the role of web application framework, like Flask?
  It is to give a fundamental structure to support development and application for a specific environment. Basically the skeleton of an application to build upon.
  
### - You can pass information to Flask either as a parameter in a route URL
  ### (like '/foods/pretzel') or using a URL query param (like
  ### 'foods?type=pretzel'). How might you choose which one is a better fit
  ### for an application?

  You would want to use a parameter if it was a subject or topic to a page to navigate too. With a query string when it is information you want to get or post from a form. 

### - How do you collect data from a URL placeholder parameter using Flask?
  You would have to set marking sections with `<some_variable>` then add that as a parameter in your decorator function. You can then return it to a webpage by passing it `{some_variable}`. Or in jinja `{{some_variable}}` within your HTML

### - How do you collect data from the query string using Flask?
  You would use the request.args() method.

### - How do you collect data from the body of the request using Flask?
  You would use request.form() method. 


### - What is a cookie and what kinds of things are they commonly used for?
  A cookie is a name/string-value pair stored by the client within the browser which is told by the server to store. They can be used to track number of visits, how long a customer has been a registered user. Or any other type of information like favorite soda or meal. 

### - What is the session object in Flask?
  The session object takes the form of a dictionary in the session data. Contains key-value pairs. 

### - What does Flask's `jsonify()` do?
  `jsonify()` method is a helper method which is provided by flask to return JSON data by returning a response object which is a string of JSON data. 
