### Conceptual Exercise

Answer the following questions below:

- What are important differences between Python and JavaScript?

  JS is used primarily as a tool for front end development as it is intended for use by the broswer to make the webpage work. In contrast, Python is a for use on the backend and cannot be used by the browser. Python has multiple types of data structures that JavaScript does not have such as tuples and dictionaries and is also intended to be used as an object oriented programming language whereas JS was not originally built for this purpose.

- Given a dictionary like ``{"a": 1, "b": 2}``: , list two ways you
  can try to get a missing key (like "c") *without* your programming
  crashing.

  

- What is a unit test?

  A test that will only test one function.

- What is an integration test?

  A test that tests multiple functions and how they work together.

- What is the role of web application framework, like Flask?

  To help the developer easily create webb apps by handling things like HTTP requests for them and also make it easier to send data to the browser.

- You can pass information to Flask either as a parameter in a route URL
  (like '/foods/pretzel') or using a URL query param (like
  'foods?type=pretzel'). How might you choose which one is a better fit
  for an application?

  URL Params are for when it feels like the "subject" of the page (like looking at a page about pretzels) whereas query params are more often used when you have information coming from a form and tends to involve extra information about the page.

- How do you collect data from a URL placeholder parameter using Flask?

  Create a variable within the @APP.ROUTE statement such as "/news/<num>" and then insert num as an argument on the route function for use on the server side.

- How do you collect data from the query string using Flask?

  You use request.args[ITEM YOU'RE LOOKING FOR]

- How do you collect data from the body of the request using Flask?

  Here, you would still use the request object but would likely use a statement like request.form instead of request.args.

- What is a cookie and what kinds of things are they commonly used for?
 
 cookies are information stored by the browser often based on user input or other data gathered from the user such as login credentials, other user data, and authentification tokens.

- What is the session object in Flask?

  It is an item that stores all of the information from a given user's usage of the site in a given sesison and stores it in the browser as a cookie. It also allows for larger chunks of information to be stored than a regular cookie because magic.

- What does Flask's `jsonify()` do?

 It turns whatever data is passed into the function into json.
