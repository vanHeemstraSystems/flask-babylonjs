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
<script src="../path/to/flowbite/dist/flowbite.js"></script>
```

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


