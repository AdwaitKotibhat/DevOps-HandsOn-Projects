**Simulation:**
Blue Green Deployment and rollback is fast compared to the canary and the rolling update. Easy to rollback.

2 deployments:
* Version 1 - Blue version of the application
* Version 2 - Green version of the application

1 service: This is where we switch the application between blue and green version.

**Pods status:**
<img width="990" height="157" alt="image" src="https://github.com/user-attachments/assets/5aaa55e5-f407-412a-ac7e-1f12b24fb21d" />

Currently the application BLUE version is running
<img width="350" height="150" alt="image" src="https://github.com/user-attachments/assets/14bcb552-65db-4616-8852-112640c4f13a" />


Switch the selector label in the service to green from blue

Request will get directed to the GREEN version of the application
<img width="411" height="131" alt="image" src="https://github.com/user-attachments/assets/1737495c-cc71-4982-bcb7-f48d4e6d14e2" />


**ROLLBACK:**

Its easy if we again update the service selector parameter. 


