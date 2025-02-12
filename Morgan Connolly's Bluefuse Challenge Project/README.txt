-=-=- Morgan's Bluefuse Challenge Entry -=-=- 
I implemented the two functions specified using a web-based GUI.

The project is comprised of:
- Frontend: HTML & CSS for structure and styling, and JS for animations.
- Backend: Fask micro-web framework for local hosting and function implementation through Python.
- Input gathered through HTML forms which is passed to backend using a POST request.
- Functions that calculate output which Flask returns to the page by reloading using Jinja2 templates.

-=- Running the Website Locally -=- 
- Run the Python-based API using Flask and go to: http://127.0.0.1:8080
- If this doesn't work, I've recorded a video to show the functionality.

-=- Development Process -=- 
Used iterative development to implement features:
1. Core functionality (HTML and backend)
2. Styling (CSS)
3. Animations (JS)

-=- Resources Used -=- 
I read over some of my previous projects to jog my memory. Then, I used internet forums and websites to determine the most effective methods to achieve my objectives
and support development by providing useful examples. Examples of this include:
- Looking up element attributes and CSS properties.
   e.g. HTML form input attributes to enable validation: https://www.w3schools.com/html/html_form_attributes.asp
        Aligning text and changing the colour: https://www.w3schools.com/css/css_text_align.asp
        Selecting the best units to use: https://www.w3schools.com/cssref/css_units.php
        Adding transitions: https://www.w3schools.com/css/css3_transitions.asp
- Researching different fonts and how to import them: https://www.w3schools.com/css/css_font.asp
- Recapping how flexboxes work to align the scrolling element and text contained in the fib output: https://www.w3schools.com/css/css3_transitions.asp
- Researching the feasibility of combining all pages into one, using JS to hide sections: https://stackoverflow.com/questions/40446658/javascript-add-transition-between-displaynone-and-displayblock6/show-or-hide-section-in-html-with-javascript

When I encountered bugs and unexpected behaviour, I utilised GPTs to point me in the right direction and then internet forums and websites to help diagnose and solve the problem.
For example:
- The output section of the fibonacci page misaligned itself when I added the overflow bar. I tried to fix this by changing the display to "inline-box" to no avail.
  Copilot reccommended using flexboxes so I researched how to use these (https://www.w3schools.com/css/css3_transitions.asp) and implemented them, solving the problem. 
- I originally intended to iterate to combine the three pages into one, but after a bit of work I realised that would require the backend to be rewritten in JS. Hence, I used
  Copilot to come up with alternatives to make transitioning between the pages seemless. It suggested implementing a few animations in JS to fade in and out when pages are loaded.
- Generating examples to compare against my implementation.