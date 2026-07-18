#1. Check Salesforce opportunity stage and print appropriate message
opportunity_stage = "Closed Won"  
if opportunity_stage == "Closed Won":
    print("Congratulations! The opportunity is won.")
else:
    print("The opportunity is not won yet.")

#2. check user role to show setup menu
user_role = "Admin"
if user_role == "Admin":
    print("Setup menu is visible")  
else:
    print("Setup menu is not visible")

#3. check deployment status of a Salesforce change set
deployment_status = "In Progress"
if deployment_status == "In Progress":
    print("Deployment is currently in progress.")
elif deployment_status == "Completed":
    print("Deployment has been completed.")
else:
    print("Deployment status is unknown.")

#4. check testcases running browser
test_browser = "Chrome"
if test_browser == "Chrome":
    print("Running test cases on Chrome browser.")
elif test_browser == "Firefox":
    print("Running test cases on Firefox browser.")
else:
    print("Running test cases on an unsupported browser.")

#5. Check environment type and print appropriate message
environment_type = "UAT"
if environment_type == "UAT":
    print("Execute Regression suite.")
else:
    print("Execute Smoke suite.")

#6. check login is successful and user is admin
login_successful = True
user_is_admin = True
if login_successful and user_is_admin:
    print("Access granted.")
else:
    print("Access denied.") 

#7. Accept leads based on lead source and lead status
lead_source = "Website"
lead_status = "New"
if lead_source == "Website" or lead_source == "Email" and lead_status == "New":
    print("Accept the lead.")
elif lead_source == "Chat" or lead_source =="Phone" and lead_status !=  "New":
    print("Do not accept the lead.")
else:
    print("Lead status is not new.")

#8. Check zipcode is required for a specific country
country = "USA" , "Canada"
if country == "USA" or country == "Canada":
    print("Zipcode is required.")
else:   
    print("Zipcode is not required.")

#9. Check opportunity stages in salesforce
match opportunity_stage:
    case "Closed Won":
        print("Won")
    case "Closed lost":
        print("Lost")
    case "Payment pending":
        print("Payment pending")
    case "Payment received":
        print("Payment received")
        