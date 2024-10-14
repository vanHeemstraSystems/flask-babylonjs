# 100 - Install using NPM

Make sure that you have [Node.js](https://nodejs.org/en/) and [Tailwind CSS](https://tailwindcss.com/) installed.

> Install Tailwind CSS as follows:
> $ cd flask_app
> $ npm install -D tailwindcss
> $ npx tailwindcss init

1. Install Flowbite as a dependency using NPM by running the following command:

```
$ cd flask_app
$ npm install flowbite --save-dev
```

2. Require Flowbite as a plugin inside the ```tailwind.config.js``` file:

```
module.exports = {
    ...
    plugins: [
        require('flowbite/plugin')
    ]
    ...
}
```
flask_app/tailwindcss.config.js

3. Make sure that you add the template path to the ```tailwind.config.js``` file:

```
module.exports = {
    ...
    content: [
        "./app/templates/**/*.html",
        "./app/static/src/**/*.{css,js}",
        "./node_modules/flowbite/**/*.js"
    ]
    ...
}
```

4. Include the main JavaScript file to make interactive elements work:

```
...
<body>
  ...
  <script src="../path/to/flowbite/dist/flowbite.js"></script>
  ...
</body>
```
flask_app/app/templates/base.html

Or from the CDN:

```
...
<body>
   ...
   <script src="https://cdn.jsdelivr.net/npm/flowbite@2.5.2/dist/flowbite.min.js"></script>
   ...
</body>
```
flask_app/app/templates/base.html

5. Add the Tailwind directives to your CSS

```
@tailwind base;
@tailwind components;
@tailwind utilities;
```
flask_app/app/static/src/css/input.css

6. Start the Tailwind CLI build process

Run the CLI tool to scan your template files for classes and build your CSS.

```
$ cd flask_app
$ npx tailwindcss -i ./app/static/src/input.css -o ./app/static/dist/css/output.css --watch
```

7. Start using Tailwind in your HTML

Add your compiled CSS file to the '<head>' and start using Tailwinds's utility classes to style your content.

```
<!DOCTYPE html>
<html lang="en">
<head>
   <meta charset="UTF-8">
   <meta name="viewport" content="width=device-width, initial-scale=1.0">
   <title>{% block title %} {% endblock %}</title>
   <link rel="stylesheet" href="{{ url_for('static', filename='css/style.css') }}">
   <link rel="stylesheet" href="{{ url_for('static', filename='dist/css/output.css') }}">
   <script src="https://cdn.babylonjs.com/babylon.js"></script>
</head>
```
flask_app/app/templates/base.html

8. Now if you style an HTML element and run the flask server, you will see the style applied to that element, e.g.:

```
...
    <h1 class="text-blue-600">Index Page</h1>
...
```
flask_app/app/templates/index.html

9. As an example, let us make the Navbar component with Flowbite:

```
<nav class="bg-white border-gray-200 px-2 sm:px-4 py-2.5 rounded dark:bg-gray-900">
    <div class="container flex flex-wrap items-center justify-between mx-auto">
        <a href="{{ url_for('main.index') }}" class="flex items-center">
            <img src="{{ url_for('static', filename='images/logo.svg') }}" class="h-6 mr-3 sm:h-9" alt="Flask App Logo">
            <span class="self-center text-xl font-semibold whitespace-nowrap dark:text-white">Flask App</span>
        </a>
        <div class="flex md:order-2">
            <button type="button"
                class="text-white bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:outline-none focus:ring-blue-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center mr-3 md:mr-0 dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800">Get
                started</button>
            <button data-collapse-toggle="navbar-cta" type="button"
                class="inline-flex items-center p-2 text-sm text-gray-500 rounded-lg md:hidden hover:bg-gray-100 focus:outline-none focus:ring-2 focus:ring-gray-200 dark:text-gray-400 dark:hover:bg-gray-700 dark:focus:ring-gray-600"
                aria-controls="navbar-cta" aria-expanded="false">
                <span class="sr-only">Open main menu</span>
                <svg class="w-6 h-6" aria-hidden="true" fill="currentColor" viewBox="0 0 20 20"
                    xmlns="http://www.w3.org/2000/svg">
                    <path fill-rule="evenodd"
                        d="M3 5a1 1 0 011-1h12a1 1 0 110 2H4a1 1 0 01-1-1zM3 10a1 1 0 011-1h12a1 1 0 110 2H4a1 1 0 01-1-1zM3 15a1 1 0 011-1h12a1 1 0 110 2H4a1 1 0 01-1-1z"
                        clip-rule="evenodd"></path>
                </svg>
            </button>
        </div>
        <div class="items-center justify-between hidden w-full md:flex md:w-auto md:order-1" id="navbar-cta">
            <ul
                class="flex flex-col p-4 mt-4 border border-gray-100 rounded-lg bg-gray-50 md:flex-row md:space-x-8 md:mt-0 md:text-sm md:font-medium md:border-0 md:bg-white dark:bg-gray-800 md:dark:bg-gray-900 dark:border-gray-700">
                <li>
                    <a href="{{ url_for('main.index') }}"
                        class="block py-2 pl-3 pr-4 text-white bg-blue-700 rounded md:bg-transparent md:text-blue-700 md:p-0 dark:text-white"
                        aria-current="page">Home</a>
                </li>
                {% if current_user.is_authenticated %}
                <li>
                    <a href="{{ url_for('game.menu') }}"
                        class="block py-2 pl-3 pr-4 text-gray-700 rounded hover:bg-gray-100 md:hover:bg-transparent md:hover:text-blue-700 md:p-0 md:dark:hover:text-white dark:text-gray-400 dark:hover:bg-gray-700 dark:hover:text-white md:dark:hover:bg-transparent dark:border-gray-700">New Game</a>
                </li>
                <li>
                    <a href="{{ url_for('game.join_game') }}"
                        class="block py-2 pl-3 pr-4 text-gray-700 rounded hover:bg-gray-100 md:hover:bg-transparent md:hover:text-blue-700 md:p-0 md:dark:hover:text-white dark:text-gray-400 dark:hover:bg-gray-700 dark:hover:text-white md:dark:hover:bg-transparent dark:border-gray-700">Join Game</a>
                </li>
                <li>
                    <a href="{{ url_for('logout.logout') }}"
                        class="block py-2 pl-3 pr-4 text-gray-700 rounded hover:bg-gray-100 md:hover:bg-transparent md:hover:text-blue-700 md:p-0 md:dark:hover:text-white dark:text-gray-400 dark:hover:bg-gray-700 dark:hover:text-white md:dark:hover:bg-transparent dark:border-gray-700">Logout</a>
                </li>
                {% else %}
                <li>
                    <a href="{{ url_for('registration.registration') }}"
                        class="block py-2 pl-3 pr-4 text-gray-700 rounded hover:bg-gray-100 md:hover:bg-transparent md:hover:text-blue-700 md:p-0 md:dark:hover:text-white dark:text-gray-400 dark:hover:bg-gray-700 dark:hover:text-white md:dark:hover:bg-transparent dark:border-gray-700">Registration</a>
                </li>
                <li>
                    <a href="{{ url_for('login.login') }}"
                        class="block py-2 pl-3 pr-4 text-gray-700 rounded hover:bg-gray-100 md:hover:bg-transparent md:hover:text-blue-700 md:p-0 md:dark:hover:text-white dark:text-gray-400 dark:hover:bg-gray-700 dark:hover:text-white md:dark:hover:bg-transparent dark:border-gray-700">Login</a>
                </li>
                {% endif %}
            </ul>
        </div>
    </div>
</nav>
```
flask_app/app/templates/navbar.html

As you can see, the navigation bar will render correctly and even the hamburger icon functionality will work by toggling the mobile menu on smaller devices.

This configuration can also be found on the [Flask starter project](https://github.com/themesberg/tailwind-flask-starter) from GitHub where Flask, Tailwind CSS, and Flowbite are already configured and you can start building websites right away.