[![Build Status](https://img.shields.io/circleci/project/github/Semprini/cbe-retail.svg)](https://circleci.com/gh/Semprini/cbe-retail)  [![Docker](http://dockeri.co/image/semprini/cbe-retail)](https://hub.docker.com/r/semprini/cbe-retail/)

# cbe-retail
Extensions to the Common Business Entities framework for Retail Operations. See [Semprini/cbe](https://github.com/Semprini/cbe) for more details.

# Why?
The most common & costly architectural issues seen in enterprises is legacy replacement big bang and integration tight coupling. To address this Microservices can be used to transform legacy via specific units of business functionality. When developing a Microservices architecture data input & output needs to be thought about. CBE-Retail can be deployed as a data fabric, extending an API layer accross back offices and stores without needing an integration bus as the schema is consistent. Perfect for a hybrid or cloud deployment model.

With a common schema deployed accross the enterprise and exposed via a governed API layer many domains are simplified like integration, BI & reporting. One key to this is not to give ownership of business data to products but treat business data as it's own product which can be goverened and exposed independently. This effectively means the business is only coupled to it's own semantics.

Extensions include:
  - Sale
  - Product
  - Pricing
 
Entities inherited from CBE:
  - business_interaction
  - customer
  - location
  - party
  - trouble
  - physical_object
  - supplier_partner
  - resource

