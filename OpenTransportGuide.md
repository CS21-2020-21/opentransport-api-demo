# Open Transport Initiative APIs - Guidance for Implementation

## Our background

From October 2020 - March 2021, we have been working with the Open Transport Initiative as part of the University of Glasgow Professional Software Development Honours project.  Our goal was to provide a proof of concept, illustrating how the Open Transport Initiative API specifications can be implemented in practice.  Our final product is located on our GitHub repository [here]().

## Our plan

At the start of the project, we decided that we would be implementing both the Operator and Customer API specifications.  We would do this by creating the centralised operator-info API, with an accompanying operator query tool to facilitate queries.  We also agreed to create two mock customer accounts which could communicate using the customer API specification.  All members of our team had experience building Django web applications, so we planned to use the [Django Rest Framework](https://www.django-rest-framework.org/).

## Our Design

Initially, reading the API specifications was rather daunting as we had not attempted any project like this before.  In order to help us understand the specifications on a deeper level, we spent some time visualising them with sequence diagrams.  This gave us a clear idea of who would be using the APIs and what was required of us. 

## Our Product

Our final product is located on our GitHub repository [here]().  We hope that this repository can act as a useful guide to any developers implementing the API spec.  It contains the centralised operator database (also hosted at https://cs21operatorapi.pythonanywhere.com) and two customer accounts which are able to communicate with each other.  We have a customer account hosted at https://psdbuses.pythonanywhere.com which can communicate with the other account running on a local machine.

## Our tips

During our time implementing the API specifications, we took note of certain issues which arose.  We have collated some general advice here to assist any developers in the future who may come across the same problems.

* There are no security protocols which must be followed when implementing the API.  We believe that it might be beneficial for the Open Transport Initiative to consider a standardised security protocol. For example, our mock customer account made use of [Django Rest Framework Authentication](https://www.django-rest-framework.org/api-guide/authentication/).  In contrast, another project team which also created a mock account used [JWT Authentication](https://jwt.io/introduction).  This meant that when we aimed to share data between them, they were incompatible.  By enforcing a standardised security protocol, all customer accounts would be able to communicate safely and securely.

* The API specification makes use of kebab-case for naming JSON keys.  While JSON does not have any strict naming convention, we believe it might be more useful for the specification to use one which is compatible with a wider array of programming languages.  For example, by using the Django Rest Framework, our API was built with the python programming language. [PEP 8](https://www.python.org/dev/peps/pep-0008/), the style guide for python, recommends that snake_case is used.  In fact, variable names must not contain hyphens as this could be confused with the subtraction operator.  On the other hand a small number of programming languages which are derivatives of LISP promote the use of kebab-case.  We were able to work our way around this issue by receiving JSON from other applications and parsing it to change all cases of hyphens to underscores.  Alternatively, a JSON serializer could be used to handle the inconsistencies between programming languages.  Overall, however, we feel it might be beneficial for the specification to support a wider array of more popular programming languages.

* PAS212

* n+1 performance issue

* If implementing a similar repository with multiple Django applications you may find creating a CI/CD pipeline problematic. However, we have very little experience with AutoDevOps therefore you may have better luck. If you do decide to go down the same route, we would highly encourage using a different repository for each Django application and implementing a seperate pipeline for each.

## Our experience

We have greatly appreciated to work with Hayden and the Open Transport who have been an excellent client.  We have gained valuable experience in the professional software development world and we hope that our project will encourage other developers to expose smart data with these innovative APIs, helping to improve the transport industry as a whole.
