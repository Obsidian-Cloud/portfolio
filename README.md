# Welcome
My name is Keith, and thanks for stopping by. This README should give you a clear look into why I built this application and my approach to software design. I’m a lifelong learner who loves diving into the 'how' and 'why' of code. Without further ado..


# What is it?
Two words. 'Clean Architecture'. This project is an implementation of Uncle Bob's architectural philosophy, designed to be independent. It serves as a blueprint for building scalable, testable, and maintainable software.


# Over-engineered?
Yeah, it is. But that is the point afterall. To show off what I understand and what I can do. What I have the potential to learn working for a great employer. Not just coding, but real-world systems. Here is my version of a clean system.

# What problem does it solve?
The main focus is **decoupling**. By using dependency inversion and SOLID principles, concrete classes are accessed only via 'interfaces'. Within my portfolio's structure, the database model (Entities) is completely decoupled from the database itself, allowing for the 'Entities' to be tested freely of any database calls.


# How is it structured?
Everything flows toward the center, the 'Business Layer'. Its a strictly unidirectional flow. Every module within a layer is completely unaware of the layers above it. This ensures that any changes in the 'Frameworks and Drivers Layer' doesnt affect core logic in the 'Business Layer'.


## How *Boundaries* are declared
Boundaries are what make 'Clean Architecture' tick. They enforce the unidirectional flow. I achieve this by inverting dependencies through 'interfacing'.

- **Backend:** I use **zope.interface** and **zope.component**. This allows for a clean relationship between concrete providers and their 'interfaces', making the implementation 'plug-n-play' within the calling module.

For more information on **zope interfaces** check out the documentation [here](https://zopeinterface.readthedocs.io/en/latest/).

- **Frontend:** I use 'TypeScript interfaces' to act as 'ports'. Since JavaScript is modular by nature, I wrote simple porting functions, wired them up, and compiled them. This provided 100% functional 'interfaces' to set the stage for the rest of the JavaScript development.

## The *Boundaries*
### The Business Layer (Entities - Imperatively/Classically mapped)
The innermost layer. It relies on nothing. In this portfolio, 'Entities' are completely isolated. They don't depend on specific abstractions like **SQLAlchemy** (the current ORM). 

I use **imperative mapping** here. While this allows the 'Domain Model' to remain unaware of the ORM, it does also mean that the ORM can't automatically determine mappings when pulling the object from the database. This requires handling like `assert orm_obj is not None` to access the classes attributes.

Point being, the 'Business Layer' can be tested in complete isolation because it does not rely on anything and is not tied to the ORM. While still being able to produce instances which can be saved and inserted into the database easily. 


### The Application Layer (Use Cases)
In my portfolio, the 'Application Layer' serves as an orchestrator. It is is completely unaware of the 'Entities'. Instead of importing the 'Entities' and manipulating them directly, it coordinates the flow through specialized modules:

- **API:** Receives the request via **Flask** and uses **Flask-JSON** to parse the request into a standard python dictionary object.
- **Validation:** It hands the dictionary object to **Cerberus** to ensure data integrity before any logic fires.
- **Database Abstraction:** It calls upon the **Mapper** (which acts as the Repository) to handle the heavy lifting. 
    - Note: Currently, the **Mapper** handles both CRUD and session management. In a production-scale refactor, I would split these into a dedicated Unit of Work and individual Repository modules.
- **Encapsulation:** Because the **Mapper** is the only module with a reference to the 'Entities' and the ORM, the 'Application Layer' remains focused solely on the **intent**(the 'what'), not the **structure** of the data(the 'how').

This ensures that if the 'Entities' logic or the database schema changes, the 'Application Layer'(the actual business logic)doesn't need to be touched.


### The Interface Adapter Layer (Controller/Presenter)
These act as the translators. Controllers take user input and convert it into a format the 'Application Layer' can understand. Presenters take the results from the 'Application Layer' and format them into a structure the UI can easily consume. This ensures the core business logic never has to deal with HTTP requests or view-specific logic.


### The Frameworks and Drivers Layer (SQLAlchemy/Cerberus/UI)
The outermost layer. Nothing depends on these. They are completely interchangeable tools. This means that all those cool external libraries and frameworks don't force you to cram your business logic into their restricted abstractions.

The `UI`, `SQLAlchemy`, `Cerberus`, or any other external library or framework  basically becomes 'plug-n-play' to the 'Application Layer' through the 'interfaces'. This is `True` independence.


# Clean Architecture Diagram
This is a diagram from Uncle Bob's(Robert C Martin) book titled: 'Clean Architecture - A Craftmans Guide to Software Structure and Design'(page 162)  

It should help having a visualization.

As far as the visualization of 'flow of control' in the bottom right of this diagram, my portfolio is slightly different. In my implementation, the **Controller** logic is 'plug-n-play' into the Flask API responses, directly transforming the Use Case output into JSON for the client.

![Uncle Bob's clean architecture diagram](/static/clean_diagram.png)


# Live Demo
This application is currently deployed at: [baranzini.dev](https://www.baranzini.dev)


# Local Development

To clone locally

1. **Clone and Install:**
    ```bash
    git clone https://github.com/Obsidian-Cloud/portfolio.git
    pip install -r requirements.txt
    ```
