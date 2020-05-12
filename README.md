<h1> Book discount service for labirint.ru and book24.ru </h1>

Thank you for your interest in my project, i will be glad if you find it useful.

<h2> Instalation </h2>

Please make sure the files is unpacked under a Web-accessible directory. You shall see the following files and directories:

<pre>
<code>
  webapp/              main folder of project
  .gitignore           gitignore file
  Pipfile              file with programs you will need for work and their version
  create_admin.py      file for project admin creation      
  requirements.txt     requirement checker
  README               this file
  run.sh               executable file for this project
</code>
</pre>

Let's see what includes webapp folder, the main folder of project

<pre>
<code>
  books/               book's model, parser, form for db
  static/              all project images
  templates/           html templates for the project
  user/                eser's model, form for db, view      
  __init__.py          main view file of the project
  config.py            configuration file
</code>
</pre>


<h2> Requirements </h2>

For working with this project you must have base skills in Python 3.X and Flask 1.1

book discount has been tested with local server on Ubuntu 19.04 and 20.04 in Firefox 75.0 and Chrome 81.0.4044

<h2> Quick start </h2>

On command line, type in the following commands:

<pre>
<code>
  $ cd book_discount/                (Linux)
  $ ./run.sh                         (Linux)
  
</code>
</pre>
