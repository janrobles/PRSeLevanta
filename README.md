# PRSeLevanta
DB project for sharing resources to community

Entity-Relationship Report

Entity (attributes…)

•	Applicant (apl_ID, name, address, location, region)
  ♣	The applicant represents the person in need which request a resource of his necessity.  It includes a region attribute to help with       statistics analysis.  

•	Resource (res_ID, category, size, gender, battery_type, pack_size, res_name, qty, price, supp_ID)
  ♣	Resource is the entity that lets you know the resource that the applicant may request to reserve or purchase along with different         specifications of the product.

•	Supplier (supp_ID, name, address, location, region)
  ♣	The supplier represents the person that has one or more resources available to provide to one or more applicants. It includes a region     attribute to help with statistics analysis.  

•	Account (account_#, balance, supp_ID)
  ♣	The account entity represents the bank account where the supplier will receive the money for the transactions being processed.

•	Credit_card (card_#, exp_date, balance, apl_ID)
  ♣	This entity represents the applicants credit card information such as card number, expiration date and balance. 

Relationship

•	Reserve_purchase: relates applicant with resource 
  ♣	Resource request entity register a request of a certain resource which gives information of the amount of resource needed, date the       request was made, the person doing the request, the supplier that will provide the resource and the id of the resource being               requested.     

•	Provide: relates resource with supplier
  ♣	This relationship permits the applicant know which supplier can provide the resource being requested.

•	Transaction: relates account with credit card
  ♣	This relationship helps keep record of the payments made to the supplier bank account and stores relative information such as the date     and the total of the transaction.  Also, lets you know if the part has been dispatched. Besides it lets the supplier validate and         charge the applicants credit card by verifying if the balance is greater than the amount it will charge.

•	Who’s_account: relates supplier with account 
  ♣	Let’s you know to which supplier is the owner of each account to be deposited. 

•	Payment: relates applicant with credit card 
  ♣	This relationship keeps the information of the applicant’s credit card which he or she will be charged once finished purchasing the       necessary resources.


