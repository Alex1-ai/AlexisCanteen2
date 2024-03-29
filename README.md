# Alexis Canteen App

## Introduction

The Alexis Canteen App is a fullstack solution built with  Html, Css, Javascript, Boostrap, Django, Sqllite, Docker, Git. Designed to bridge the gap between hungry students and the distant campus canteen. Recognizing the inconvenience faced by students who reside far from the canteen, often having to traverse long distances or navigate through multiple building levels, this app aims to simplify access to food through a convenient, user-friendly platform.

## Problem

On our campus, the primary source of meals is the school canteen. Unfortunately, its location poses a significant challenge for many students. Positioned far from the hostels and typically on upper floors, the journey to the canteen is not only time-consuming but also physically demanding. This situation discourages students from making the trip, especially during tight schedules or after a long day of lectures.

## Solution

The Alexis Canteen App transforms this challenge into an opportunity for improvement. By developing a fullstack application, we now offer a seamless way for students to order food from anywhere around the campus - be it from the comfort of their hostel, an office, or even a classroom. The process is straightforward: select your meal, pay for it along with a nominal delivery fee (which supports site maintenance), and await your delivery. This solution not only saves time but also promotes a more enjoyable campus living experience.

## Getting Started

To run the Alexis Canteen App on your local server, follow these steps:

### Using Docker
1. **Make sure your have Docker installed**

2. **Clone the Repository**
    ```
    git clone https://github.com/Alex1-ai/AlexisCanteen2
    ```
3. **Move into the Directory**
    ```
    cd AlexisCanteen2
    ```
4. **Build the docker file**
   ``
    docker build .
   ``

5. **Run with Docker-compose**
    ``
    docker-compose up
    ``





### Running on your machine
1. **Clone the Repository**
    ```
    git clone https://github.com/Alex1-ai/AlexisCanteen2
    ```

2. **Move into the Directory**
    ```
    cd AlexisCanteen2
    ```

3. **Install Dependencies**
    ```
    pipenv install
    ```

4. **Activate the Environment**
    ```
    pipenv shell
    ```

5. **Set Up Your Environment Variables**
    - Create a `.env` file in the root directory of AlexisCanteen2.
    - Copy the contents of `env.sample` into your `.env` file.
    - Fill out the necessary data correctly in the `.env` file.

6. **Run the Server**
    ```
    python manage.py runserver
    ```

## Additional Information

- Ensure you have Python installed on your system.
- This guide assumes you have pipenv installed. If not, you can install it using pip by running `pip install pipenv`.

For any issues or questions, please open an issue on the repository, and we'll get back to you as soon as possible.
