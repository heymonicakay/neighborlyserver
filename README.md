## Neighborly Server

<b style="font-size: 20px;"><i>... so fetch!</i></b>

## Learning Goals

- Expand understanding of ORM, React & full-stack development
- Set up the models and ViewSets to allow users to upload images
- Implement full CRUD functionality
- Implement authentication using Django

## Features

The server utilizes unmapped properties to send useful information along with the objects stored in the database, and custom actions to either send very specific data to the client, or manipulate object properties. These features allow the client to request more precise data from the server, thereby minimizing the amount of extraneous data sent back to the client and reducing &mdash; if not eliminating &mdash; the need for client side data filtering.

## Set Up

1. Clone this repo

    ```
    git clone git@github.com:heymonicakay/neighborlyserver.git
    cd neighborlyserver
    ```

2. Activate virtual environment

    ```
    pipenv shell
    ```

3. Install dependencies

    ```
    pipenv install
    ```

4. [Install Pillow](https://pillow.readthedocs.io/en/stable/installation.html)

4. Run the server

    ```
    python manage.py runserver
    ```

5. Finish installation by following the instructions found here:
<a href="https://www.github.com/heymonicakay/neighborly" target="_blank"><img src="https://img.shields.io/badge/client_repo%20-%2375120e.svg?&style=for-the-badge&&logoColor=white" alt="Neighborly Client Repo" style="height: auto !important; width: auto !important;" /></a>

## Created by Monica Kay

<a href="https://www.github.com/heymonicakay/" target="_blank"><img src="https://img.shields.io/badge/github%20-%23121011.svg?&style=for-the-badge&logo=github&logoColor=white" alt="Monica Kay GitHub" style="height: auto !important;width: auto !important;" /></a> <a href="https://www.linkedin.com/in/heymonicakay/" target="_blank"><img src="https://img.shields.io/badge/linkedin%20-%230077B5.svg?&style=for-the-badge&logo=linkedin&logoColor=white" alt="Monica Kay LinkedIn" style="height: auto !important;width: auto !important;" /></a>
