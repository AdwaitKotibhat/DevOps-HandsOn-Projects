Output:

<img width="513" height="248" alt="image" src="https://github.com/user-attachments/assets/33c29f76-8d80-490c-b766-11abf6e48268" />


Flow:

Browser --> localhost:8000 ---> (port forward- command as below) --> K8s Service (port 80) --> K8s Deployment --> K8s pod (port 5000)

`kubectl port-forward service/python-app-service 8000:80`
