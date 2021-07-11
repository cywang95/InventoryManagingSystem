# InventoryManagingSystem

*This is final project for my "Intro to Database" course.*


------

**Problem Statement:**

Our idea is to create an inventory management system in order to help small
business’s owner to stay on track with their current inventory of the product.

Therefore, we need database system to control the backend information

------
**Database Structure**

Our database will consist of two portions: data that represent the employees information and data that represents the product information.

The ``Store`` entity is a store, with attributes <font color=#FF6600>*store_id*, *store_phone*, *store_address*, *store_manager* and *inventory*. </font>

The ``Store`` entity contains two relationships, **Sells** and **Work For**. The relationship **Sell** will connect ``store`` entity to ``Product`` entity and **Work For** will connect ``employee`` entity. 

``Product`` entity is an entity of item information, the attributes are *item_ID* and *item_name* and it has a weak entity which is ``Customer``. In ``Customer`` entity contains three attributes: *name*, *phone* and *address*, this entity is connected to ``Product`` with a **Buy** relationship.

``Employee`` entity is an entity containing attributes of employee’s information which is, *Employee_ID*, *Name*, *SSN*, *Phone*, *Address*. ``Employee`` entity also connects to 3 other weak entities, ``Manager``, ``Accounting`` and ``Worker``, they all have the same attribute which is *Employee_ID*. There is an ``emergency contact`` entity under ``employee`` which contains 2 attributes: *phone* and *name*.


------

**User Manual**

•	Product:

	•	This category includes the information of all products in records.
	•	It is a list of all products with information about the name, store that sells them, and inventory at the store.
	•	It allows you to add product information as well as search a certain product
	•	To add, simple type in the blank the information of the product, then click edit inventory. If there exists the same product id, it will pop up a warning that there’s duplicated value. Otherwise, it will add a new product in the database.
	•	When users click the search button, it will list all the data stored in the database.




•	Inventory

	•	this category allows users to check all inventory at each store.
	•	It has a filter function which allows users to check all inventory at certain store.
	•	To use the filter function, click the down arrow and select the store you want. The result will show all the products at that store.



•	Employee:

	•	This category contains the information of all employees working in the company.
	•	It is a list that shows the information, including name, ssn, phone number, address and position, of all employees in that company.
	•	It provides search and add function.
	•	To search, click the search button. When users click the search button, it will list all the data stored in the database.
	•	To add, like for product, simple type in the blank the information of the employee, then click add new If there exists the same employee id, it will pop up a warning. Otherwise, it will add a new employee in the database.


-----


*Author: CYWang, LYZhao*

*Created Date: 2020/12/11*
